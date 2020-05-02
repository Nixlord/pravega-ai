# USAGE
# npm run new:api -- <route>
import os
import pathlib
from sys import argv

# Supply environment variables
server = os.environ.get("server") or "server"
website = os.environ.get("website") or "website"

# Pass arguments
_, path = argv
folder, file = path.rsplit('/', 1)
cwd = os.getcwd()


def tsx_template(path: str) -> str:
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
    return fetch(`/api{path}`)
        .then(response => response.json())
}}

"""


api_folder = f"{server}/api/{folder}"
api_path = f"{api_folder}/{file}.py"

client_folder = f"{website}/src/api/{folder}"
client_path = f"{client_folder}/{file}API.ts"

print(f"Running new api script in {cwd}")
print(f"ServerFolder: {server}")
print(f"WebsiteFolder: {website}")
print(f"ArgumentVector: {argv}")
print(f"API will be created at: ")
print(f"    Server: {api_path}")
print(f"    Client: {client_path}")


def create_files(path: str) -> None:
    create_client(path)


def create_client(path) -> None:
    client_text = tsx_template(path)
    if not os.path.exists(client_folder):
        os.makedirs(client_folder)
    print(client_text, file=open(client_path, 'w'))
    print("\nGenerated Client", end="")
    print(tsx_template(path))


create_files(path)

