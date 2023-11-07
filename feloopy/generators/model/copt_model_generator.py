'''
+---------------------------------------------------------+
|  Project: FelooPy (0.2.8)                               |
|  Modified: Wednesday, 27th September 2023 09:02:20 pm   |
|  Modified By: Keivan Tafakkori                          |
|  Project: https://github.com/ktafakkori/feloopy         |
|  Contact: https://www.linkedin.com/in/keivan-tafakkori/ |
|  Copyright 2022 - 2023 Keivan Tafakkori, FELOOP         |
+---------------------------------------------------------+
'''

import coptpy as copt

envconfig = copt.EnvrConfig()
envconfig.set('nobanner', '1')
env = copt.Envr(envconfig)

def generate_model(features):
    return env.createModel(features['model_name'])