#!/usr/bin/env python3
import requests
import passwords  # Import credentials

url = "https://api.github.com/user"
response = requests.get(url, auth=(passwords.GITHUB_USERNAME, passwords.GITHUB_TOKEN))

print(response.json())  # Should print GitHub user details

