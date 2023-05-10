# terratemplate
```txt
                  ___                     ___           ___                 
      ___        /  /\        ___        /__/\         /  /\                
     /  /\      /  /:/_      /  /\      |  |::\       /  /::\               
    /  /:/     /  /:/ /\    /  /:/      |  |:|:\     /  /:/\:\  ___     ___ 
   /  /:/     /  /:/ /:/   /  /:/     __|__|:|\:\   /  /:/~/:/ /__/\   /  /\
  /  /::\    /__/:/ /:/   /  /::\    /__/::::| \:\ /__/:/ /:/  \  \:\ /  /:/
 /__/:/\:\   \  \:\/:/   /__/:/\:\   \  \:\~~\__\/ \  \:\/:/    \  \:\  /:/ 
 \__\/  \:\   \  \::/    \__\/  \:\   \  \:\        \  \::/      \  \:\/:/  
      \  \:\   \  \:\         \  \:\   \  \:\        \  \:\       \  \::/   
       \__\/    \  \:\         \__\/    \  \:\        \  \:\       \__\/    
                 \__\/                   \__\/         \__\/                
```

This Python tool is designed to assist with the creation and loading of Terraform templates using a JSON configuration file. It offers two primary functionalities:
- The ability to create a Terraform stack from a JSON file (`load-terraform-json`)
- The ability to generate a JSON file from a pre-existing Terraform stack (`generate-terraform-json`)

## Prerequisites

- Python 3.6 or later
- `click` Python package
- A Terraform environment already setup (if you want to generate a JSON file)

## Installation

You can download the Python script directly or clone the whole repository.

```bash
git clone https://github.com/keithcampbelljr/terratemplate.git
```

After cloning the repository, you can run the script with Python.

```bash
python terraform_json_tool.py
```

## Usage

The tool provides two commands, `load-terraform-json` and `generate-terraform-json`.

### `load-terraform-json`

To create a Terraform stack using a JSON configuration file, you can use the `load-terraform-json` command:

```bash
python terraform_json_tool.py load-terraform-json --template-name=your_template_name
```

The JSON file should be named `your_template_name.json` and should be located in the same directory as this script. It should follow this structure:

```yaml
{
    "directories": [
        "path/to/directory1",
        "path/to/directory2",
        # ...
    ],
    "files": {
        "path/to/file1.tf": "file contents",
        "path/to/file2.tf": "file contents",
        # ...
    }
}
```

### `generate-terraform-json`

To generate a Terraform stack JSON configuration file from your existing Terraform setup, you can use the `generate-terraform-json` command:

```bash
python terraform_json_tool.py generate-terraform-json --template-name=your_template_name
```

The generated JSON file will be named your_template_name.json and will be located in the same directory as this script.

