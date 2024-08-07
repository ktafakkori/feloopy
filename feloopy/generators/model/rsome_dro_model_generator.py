# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

import rsome as rso
from rsome import dro

def generate_model(features):

    return dro.Model(name=features['model_name'],scens=features['scens'])


