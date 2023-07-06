'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-07-06
 # @ Modified: 2023-07-06
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''

def Get(model_object, result, input1, input2=None):

    input1 = input1[0]

    match input1:

        case 'variable':
           
            return input2.value

        case 'status':
            
            return model_object.get_state()

        case 'objective':
            
            return model_object.get_objective(0)

        case 'time':
            
            return model_object.get_time()

        case 'dual':
           
            raise NotImplementedError("LocalSolver does not support dual values")

        case 'slack':
            
            raise NotImplementedError("LocalSolver does not support slack values")
