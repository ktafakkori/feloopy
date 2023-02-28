import cylp as cylp_interface
from cylp.cy import CyClpSimplex

def generate_model():
    return cylp_interface.py.modeling.CyLPModel()
