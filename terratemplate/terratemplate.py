import os
import json
import click

@click.group()
def cli():
    pass

@cli.command()
@click.option('--template-name', required=True, help='Name of the Terraform template')
def load_terraform_json(template_name: str):
    """
    Create a Terraform stack using a JSON configuration file.

    This command reads a JSON file with directory and file paths and creates them
    in the specified location. The JSON file must have the following structure:

    {
        "directories": [
            "path/to/directory1",
            "path/to/directory2",
            ...
        ],
        "files": {
            "path/to/file1.tf": "file contents",
            "path/to/file2.tf": "file contents",
            ...
        }
    }

    The JSON file should be named <template_name>.json and should be located in the same
    directory as this script.
    """
    template_json = load_terraform_stack_json(template_name=template_name)
    create_template_directories(template_details=template_json)
    create_template_files(template_details=template_json, template_name=template_name)

def add_files(files, root_directory, template_name, stack_details):
    for file in files:
        if file.endswith('.tf'):
            file_path = os.path.join(root_directory, file)
            with open(file_path, 'r') as f:
                file_contents = f.read()
                stack_details['files'][os.path.relpath(file_path, template_name)] = file_contents

def add_directories(root_directory, template_name, stack_details):
    relative_path = os.path.relpath(root_directory, template_name)
    if relative_path != "..":
        stack_details['directories'].append(os.path.relpath(root_directory))

@click.command()
@click.option('--template-name', required=True, help='Name of the Terraform template')
def generate_terraform_json(template_name: str):
    """
    Generate a Terraform stack JSON configuration file.

    This command walks the directory tree from the current working directory
    and creates a JSON file with the directory and file paths. The resulting JSON file
    can be used as input to the `create-terraform-stack` command.

    The JSON file will have the following structure:

    {
        "directories": [
            "path/to/directory1",
            "path/to/directory2",
            ...
        ],
        "files": {
            "path/to/file1.tf": "file contents",
            "path/to/file2.tf": "file contents",
            ...
        }
    }

    The JSON file will be named <template_name>.json and will be located in the same
    directory as this script.
    """
    stack_details = {}
    stack_details['directories'] = []
    stack_details['files'] = {}

    for root, dirs, files in os.walk(os.getcwd()):
        add_directories(root_directory=root, template_name=template_name, stack_details=stack_details)
        add_files(files=files, root_directory=root, template_name=template_name, stack_details=stack_details)

    with open(f"{template_name}.json", "w") as f:
        json.dump(stack_details, f)

if __name__ == '__main__':
    cli.add_command(load_terraform_json)
    cli.add_command(generate_terraform_json)
    cli()
