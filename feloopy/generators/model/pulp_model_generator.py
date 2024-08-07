# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

import pulp as pulp_interface

def generate_model(features):

    return pulp_interface.LpProblem(features['model_name'], pulp_interface.LpMinimize)
