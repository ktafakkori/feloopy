# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

import xpress as xpress_interface

def generate_model(features):
    return xpress_interface.problem(features['model_name'])