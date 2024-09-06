#!/usr/bin/env python3
import requests
import json

org = "soku-launcher-modpacks"
s = requests.Session()
repos = [
    repo["name"] for repo in s.get(f"https://api.github.com/users/{org}/repos").json()
]
download_count = {
    repo: {
        release["tag_name"]: sum(a["download_count"] for a in release["assets"])
        for release in s.get(
            f"https://api.github.com/repos/{org}/{repo}/releases"
        ).json()
    }
    for repo in repos
}
print(json.dumps(download_count, indent=2))
