import pulp as pulp_interface

def generate_model(features):
    
    return pulp_interface.LpProblem(features['model_name'], pulp_interface.LpMinimize)