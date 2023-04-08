import os
import json

def load_terraform_stack_json(template_name: str):

    with open(f"{template_name}.json", "r") as f:
        template_details = json.load(f)
        return template_details
    
def create_template_directories(template_details: str):

  for directory in template_details['directories']:
      if directory != "":
        os.makedirs(directory)

def create_template_files(template_details: str, template_name: str):
   for file, contents in template_details['files'].items():
    file_path = os.path.join(template_name, file)
    with open(file_path, 'w') as f:
        f.write(contents)

def create_terraform_stack(template_name: str):
  template_json = load_terraform_stack_json(template_name=template_name)
  create_template_directories(template_details=template_json)
  create_template_files(template_details=template_json, template_name=template_name)

create_terraform_stack(template_name="terratemplate")

