#!/usr/bin/python
'''Basic Helper Functions
Created on 13/04/2021'''

import json
import sys
from typing import *
from pathlib import Path

import numpy as np
import pandas as pd
import sklearn as sk
import matplotlib.pyplot as plt

####################
## JSON DATA #######
####################

def store_json(data: Dict, path: Union[str, Path]) -> None:
    with open(Path(path), "w") as json_upload:
        json.dump(data, json_upload)
    
    return

def load_json(path: Union[str, Path]) -> Dict:
    with open(Path(path), "r") as json_down:
        data = json.load(json_down)
    
    return data

###################
## PROCESSING #####
###################

def prep_data(raw_df: pd.DataFrame, target_columns: List, drop_first: bool = True, make_na_col: bool = True) -> pd.DataFrame:
    """Dummify a pandas dataframe
    """
    dataframe_dummy = pd.get_dummies(raw_df, columns=target_columns, 
                                        drop_first=drop_first, 
                                        dummy_na=make_na_col)
    return (dataframe_dummy)

###################
## EVALUATION #####
###################

def threshold_accuracy(y_pred: Union[List, np.array], 
                        y_true: Union[List, np.array], 
                        threshold: float = 0.5) -> float:
    
    if len(y_pred) != len(y_true):
        raise ValueError(f"Cannot process unequal length of {len(y_pred)} against {len(y_true)}")
    
    result = 0
    
    for pred, true in zip(y_pred, y_true): 
        difference = pred - true
        if -0.5 < difference < 0.5:
            result += 1

    return round(result/len(y_true)*100, 3)

###################
## VISUALIZATION ##
###################

def plot_pred_true_correlation(y_pred: np.array,
                            y_true: np.array,
                            title: str = "",
                            figsize: Tuple[int] = (10,10)):
    """Simple Correlation Plot"""
    fig, ax = plt.subplots(figsize=figsize);

    plottable_df = pd.DataFrame(dict(y_pred=y_pred,y_true=y_true));
    plottable_df.plot.scatter(x="y_pred", y="y_true", ax=ax);

    longest_ax = max(plottable_df.max())+(0.01*max(plottable_df.max()));
    shortest_ax = min(plottable_df.min())+(0.01*min(plottable_df.min()));

    ax.set_xlim([shortest_ax, longest_ax]);
    ax.set_ylim([shortest_ax, longest_ax]);

    ax.plot(ax.get_xlim(), ax.get_ylim(), ls="--", c=".3");
    
    ax.title(title)

    return (fig, ax)

###################
####### END #######
###################