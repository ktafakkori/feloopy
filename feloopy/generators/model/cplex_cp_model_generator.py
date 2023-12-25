# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

from docplex.cp.model import CpoModel as CPLEXMODEL

def generate_model(features):

    return CPLEXMODEL(name=features['model_name'])
