import gekko as gekko_interface

def generate_model(features):
    
    return gekko_interface.GEKKO(remote=False,name=features['model_name'])