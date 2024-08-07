# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

import importlib

def generate_model(features):
    module = importlib.import_module(features["interface_name"])
    Model = getattr(module, 'Model')
    return Model()
