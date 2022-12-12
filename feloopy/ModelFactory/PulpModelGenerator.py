import pulp as pulp_interface

def GenerateModel():
    return pulp_interface.LpProblem('None', pulp_interface.LpMinimize)
