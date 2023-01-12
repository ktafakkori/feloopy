import gekko as gekko_interface

def GenerateModel():
    return gekko_interface.GEKKO(remote=False)