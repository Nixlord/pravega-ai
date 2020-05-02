import os
import pathlib
from sys import argv

server_path = os.environ.get("server") or "server"
website_path = os.environ.get("website") or "website"

cwd = os.getcwd()
server = pathlib.Path(server_path)
website = pathlib.Path(website_path)

print(f"Running new api script in {cwd}")
print(f"ServerFolder: {server}")
print(f"WebsiteFolder: {website}")
print(f"ArgumentVector: {argv}")

