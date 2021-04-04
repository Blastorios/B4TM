import json
from typing import (
    Union,
    Dict,
    List,
    Any,
)

import pandas as pd

############################

def store_json(data, file_loc:str) -> None:
    """As the name suggests:
    Only parse JSON compatible data svp
    """

    with open(file_loc, "w") as json_file:
        json_file.write(json.dumps(data))
    print(f"Stored file at {file_loc}")

def load_json(file_loc:str) -> Union[Dict, List]:
    """As the name suggests
    """

    with open(file_loc, "r") as json_read:
        content = json.loads(json_read.read())
    return content

############################
##### Work in Progress #####
############################

def interchange(value: Any, elements: Dict):
    """Simple Parser
    """
    
    return elements[value]

def process_df(df_vals: pd.DataFrame, 
               df_target: Union[pd.DataFrame, str],
               target_name: str = "", 
               remove:List = [], num_target: bool = False) -> pd.DataFrame:
    """An effective function to create a quick-n-dirty df"""
    
    df = df_vals.T

    if isinstance(df_target, str) and num_target:
        elements = {val:ii for ii, val in enumerate(df[df_target].unique())}
        df[df_target] = df[df_target].apply(lambda x: interchange(x, elements))
    
    elif isinstance(df_target, pd.DataFrame):
        if target_name:
            df[target_name] = None if type(df_target[target_name].values[0]) != int or type(df_target[target_name].values[0]) != float else 0

            for instance in df_target.index:
                df.at[instance, target_name] =\
                df_target[df_target.index == instance][target_name].values[0]
        else:
            raise ValueError("Missing target name for the ")
