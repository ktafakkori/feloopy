'''
+---------------------------------------------------------+
|  Project: FelooPy (0.2.8)                               |
|  Modified: Wednesday, 27th September 2023 11:30:33 pm   |
|  Modified By: Keivan Tafakkori                          |
|  Project: https://github.com/ktafakkori/feloopy         |
|  Contact: https://www.linkedin.com/in/keivan-tafakkori/ |
|  Copyright 2022 - 2023 Keivan Tafakkori, FELOOP         |
+---------------------------------------------------------+
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
