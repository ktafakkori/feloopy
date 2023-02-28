import pulp as pulp_interface

def generate_model():
    return pulp_interface.LpProblem('None', pulp_interface.LpMinimize)