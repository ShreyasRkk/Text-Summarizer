import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import Logger #the custom logger we created
from ensure import ensure_annotations #so that we are alerted when wrong datatype is encountered
from box import ConfigBox #makes the interaction with tuples from yaml files easier
from pathlib import Path 
from typing import Any 



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose= True):
    for directory in path_to_directories:
        os.makedirs(directory, exist_ok=True)
        if verbose:
            logger.info(f"creating directory: {directory}")
        
@ensure_annotations
def get_size(path: Path) -> str: 

    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb}kb"


