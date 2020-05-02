import os
import pathlib
from sys import argv


server_path = os.environ.get("server") or "server"
website_path = os.environ.get("website") or "website"

cwd = os.getcwd()
server = pathlib.Path(server_path)
website = pathlib.Path(website_path)
_, path = argv

print(f"Running new api script in {cwd}")
print(f"ServerFolder: {server}")
print(f"WebsiteFolder: {website}")
print(f"ArgumentVector: {argv}")
print(f"API will be created at: ")
print(f"    Server: {server}/api/{path}")
print(f"    Client: {website}/src/api/{path}")


def tsxTemplate(path: str) -> str:
    # Will crash in linux/develop logic later
    name = path.split('/')[-1]
    Name = name.capitalize()
    Request = f"{Name}Request"
    Response = f"{Name}Response"

    return f"""
export interface {Request} {{
    
}}
export interface {Response} {{
    
}}

export default function {name}API(
    request: {Request}
): Promise<{Response}> {{
    return fetch(`/api/{path}`)
        .then(response => response.json())
}}
"""
