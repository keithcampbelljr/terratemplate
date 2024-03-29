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
- The ability to create a Terraform stack from a JSON file (`load`)
- The ability to save a JSON file from a pre-existing Terraform stack (`save`)

## Prerequisites

- Python 3.6 or later
- `click` Python package
- A Terraform environment already setup (if you want to save a JSON file)

## Installation

You can download the Python script directly or clone the whole repository.

```bash
git clone https://github.com/keithcampbelljr/terratemplate.git
```

Install required packages
```bash
make install
```

After cloning the repository, you can run the script.

```bash
tftmpl -v
```

## Usage

The tool provides two commands, `load` and `save`.

### `load`

To create a Terraform stack using a JSON configuration file, you can use the `load` command:

```bash
tftmpl load --template-name=your_template_name
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

### `save`

To save a Terraform stack JSON configuration file from your existing Terraform setup, you can use the `save` command:

```bash
tftmpl save --template-name=your_template_name
```

The saved JSON file will be named your_template_name.json and will be located in the same directory as this script.

