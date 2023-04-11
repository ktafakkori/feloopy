import cplex
from docplex.mp.model import Model as CPLEXMODEL


def generate_model(features):

    return CPLEXMODEL(name=features['model_name'])
