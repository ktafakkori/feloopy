import cplex
from docplex.cp.model import CpoModel as CPLEXMODEL

def generate_model(features):



    return CPLEXMODEL(name=features['model_name'])