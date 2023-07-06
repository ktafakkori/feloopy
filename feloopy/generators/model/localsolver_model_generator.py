'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-07-06
 # @ Modified: 2023-07-06
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''

import sys
import warnings

warnings.filterwarnings("ignore")

import localsolver as ls

def generate_model(features):

    ls_env = ls.LocalSolver()

    model = ls_env.model

    return model
