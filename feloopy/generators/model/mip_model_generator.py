# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

import mip as mip_interface

def generate_model(features):
    return mip_interface.Model(features['model_name'], solver_name='CBC')
