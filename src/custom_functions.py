import json
from typing import (
    Union,
    Dict,
    List,
)

def store_json(data, file_loc:str) -> None:
    with open(file_loc, "w") as json_file:
        json_file.write(json.dumps(data))
    print(f"Stored file at {file_loc}")

def load_json(file_loc:str) -> Union[Dict, List]:
    with open(file_loc, "r") as json_read:
        content = json.loads(json_read.read())
    return content