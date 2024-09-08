#!/usr/bin/env python3
import requests
import json
import os

ORG = "soku-launcher-modpacks"
s = requests.Session()
if "TOKEN" in os.environ:
    s.headers["authorization"] = "Bearer " + os.environ["TOKEN"]
repos = [
    (ORG, repo["name"])
    for repo in s.get(f"https://api.github.com/users/{ORG}/repos?per_page=100").json()
]
repos.append(("0miles", "soku-launcher"))
download_count = {
    repo: {
        release["tag_name"]: sum(a["download_count"] for a in release["assets"])
        for release in s.get(
            f"https://api.github.com/repos/{org}/{repo}/releases"
        ).json()
    }
    for org, repo in repos
}
print(json.dumps(download_count, indent=2))
