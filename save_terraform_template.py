import os
import json

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

def generate_terraform_stack_json(template_name):
    stack_details = {}
    stack_details['directories'] = []
    stack_details['files'] = {}

    for root, dirs, files in os.walk(os.getcwd()):
        add_directories(root_directory=root, template_name=template_name, stack_details=stack_details)
        add_files(files=files, root_directory=root, template_name=template_name, stack_details=stack_details)

    with open(f"{template_name}.json", "w") as f:
        json.dump(stack_details, f)

generate_terraform_stack_json(template_name="terratemplate")
