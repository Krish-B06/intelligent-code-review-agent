#!/usr/bin/env python3

import os
import re
import sys
import ipaddress
import socket
import urllib.request
import urllib.error
from urllib.parse import urlparse


OUTPUT = "requirements-context.md"

# Replace these with the actual domains used by your organization.
ALLOWED_HOSTS = {
    "dev.azure.com"
}

REQUIREMENT_PATTERN = re.compile(
    r"https?://[^\s<>\"]+",
    re.IGNORECASE,
)


def extract_requirement_link(text):
    match = REQUIREMENT_PATTERN.search(text or "")
    if not match:
        return None

    return match.group(0).rstrip(".,)")


def validate_url(url):
    parsed = urlparse(url)

    if parsed.scheme != "https":
        raise ValueError("Only HTTPS requirement URLs are allowed.")

    hostname = parsed.hostname
    if not hostname:
        raise ValueError("Requirement URL has no hostname.")

    if hostname.lower() not in ALLOWED_HOSTS:
        raise ValueError(
            f"Requirement host is not allowed: {hostname}"
        )

    try:
        addresses = socket.getaddrinfo(
            hostname,
            443,
            type=socket.SOCK_STREAM,
        )
    except socket.gaierror as exc:
        raise ValueError("Unable to resolve requirement host.") from exc

    for address in addresses:
        ip = ipaddress.ip_address(address[4][0])

        if (
            ip.is_private
            or ip.is_loopback
            or ip.is_link_local
            or ip.is_reserved
            or ip.is_multicast
        ):
            raise ValueError(
                "Requirement URL resolves to a private/internal address."
            )


def fetch_url(url, token=None):
    validate_url(url)

    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "repository-code-review-agent",
        },
    )

    if token:
        request.add_header(
            "Authorization",
            f"Bearer {token}",
        )

    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            return response.read().decode("utf-8", errors="replace")

    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        raise RuntimeError(
            f"Unable to fetch requirement: {exc}"
        ) from exc


def main():
    pr_body = os.environ.get("PR_BODY", "")
    token = os.environ.get("REQUIREMENTS_TOKEN", "")

    link = extract_requirement_link(pr_body)

    if not link:
        with open(OUTPUT, "w", encoding="utf-8") as file:
            file.write(
                "# External Requirements\n\n"
                "No external requirement link was provided.\n"
            )

        print("No external requirement link provided.")
        return

    print(f"Requirement link detected: {link}")

    try:
        content = fetch_url(link, token)

        with open(OUTPUT, "w", encoding="utf-8") as file:
            file.write("# External Requirements\n\n")
            file.write(f"Source: {link}\n\n")
            file.write(content)

        print("External requirement fetched successfully.")

    except Exception as exc:
        with open(OUTPUT, "w", encoding="utf-8") as file:
            file.write("# External Requirements\n\n")
            file.write(f"Source: {link}\n\n")
            file.write(
                "The external requirement could not be retrieved.\n"
            )
            file.write(f"Reason: {exc}\n")

        print(f"Requirement fetch failed: {exc}")
        sys.exit(0)


if __name__ == "__main__":
    main()