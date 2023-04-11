import pyomo.environ as pyomo_interface

def generate_model(features):
    
    return pyomo_interface.ConcreteModel(name=features['model_name'])