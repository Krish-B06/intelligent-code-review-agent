import os
import re
import sys
import urllib.parse
import urllib.request
import base64


def extract_requirement_link(text):
    patterns = [
        r'https?://[^\s<>"\']+',
    ]

    for pattern in patterns:
        match = re.search(pattern, text or "")
        if match:
            return match.group(0).rstrip(".,)")
    
    return None


def fetch_url(url):
    token = os.getenv("REQUIREMENTS_TOKEN")

    request = urllib.request.Request(url)

    if token:
        request.add_header("Authorization", f"Bearer {token}")

    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8", errors="replace")


def fetch_ado_work_item(url):
    match = re.search(r"/_workitems/edit/(\d+)", url)

    if not match:
        return None

    work_item_id = match.group(1)

    parsed = urllib.parse.urlparse(url)
    parts = parsed.path.strip("/").split("/")

    if len(parts) < 3:
        return None

    organization = parts[0]
    project = parts[1]

    api_url = (
        f"https://dev.azure.com/{organization}/{project}"
        f"/_apis/wit/workitems/{work_item_id}?api-version=7.1"
    )

    pat = os.getenv("AZURE_DEVOPS_PAT")

    if not pat:
        raise RuntimeError(
            "AZURE_DEVOPS_PAT is required to read Azure DevOps work items."
        )

    credentials = base64.b64encode(f":{pat}".encode()).decode()

    request = urllib.request.Request(api_url)
    request.add_header("Authorization", f"Basic {credentials}")

    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8", errors="replace")


def main():
    if len(sys.argv) != 2:
        print("Usage: fetch-requirements.py <PR_BODY_FILE>")
        sys.exit(1)

    pr_body_file = sys.argv[1]

    with open(pr_body_file, "r", encoding="utf-8") as f:
        pr_body = f.read()

    url = extract_requirement_link(pr_body)

    if not url:
        print("No external requirement link provided.")
        with open("requirements-context.md", "w", encoding="utf-8") as f:
            f.write(
                "# External Requirements\n\n"
                "No external requirement link was provided.\n"
            )
        return

    print(f"Requirement link found: {url}")

    if "/_workitems/edit/" in url:
        content = fetch_ado_work_item(url)
    else:
        content = fetch_url(url)

    with open("requirements-context.md", "w", encoding="utf-8") as f:
        f.write("# External Requirements\n\n")
        f.write(f"Source: {url}\n\n")
        f.write("## Retrieved Content\n\n")
        f.write(content)

    print("Requirement context generated successfully.")


if __name__ == "__main__":
    main()