import cylp as cylp_interface
from cylp.cy import CyClpSimplex

def GenerateModel():
    return cylp_interface.py.modeling.CyLPModel()
