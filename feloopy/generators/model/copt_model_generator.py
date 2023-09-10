from coptpy import *

def generate_model(features):
    env = Envr()
    return env.createModel(features['model_name'])