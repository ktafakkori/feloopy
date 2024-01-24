# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

import coptpy as copt

envconfig = copt.EnvrConfig()
envconfig.set('nobanner', '1')
env = copt.Envr(envconfig)

def generate_model(features):
    return env.createModel(features['model_name'])