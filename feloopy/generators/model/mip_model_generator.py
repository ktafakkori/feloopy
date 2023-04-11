import mip as mip_interface

def generate_model(features):
    
    return mip_interface.Model(features['model_name'],solver_name='CBC')