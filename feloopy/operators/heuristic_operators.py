# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.



from ..helpers.empty import *
from ..helpers.error import *
import numpy as np
import math as mt


class NumpyVariable(np.ndarray):
    def __new__(cls, input_array):
        obj = np.asarray(input_array).view(cls)
        return obj

    def __array_finalize__(self, obj):
        if obj is None: return

    def __le__(self, other):       
        return self - other

    def __ge__(self, other):
        return other - self

    def __sub__(self, other):
        return NumpyVariable(super().__sub__(other))
    
def generate_heuristic_variable(features, type, name, variable_dim, variable_bound, agent, no_agents):

    if no_agents==None:
        no_agents=100

    if features['agent_status'] == 'idle':

        if features['vectorized']:

            if variable_dim == 0:

                if type == 'pvar' or type == 'fvar':
                    return NumpyVariable(variable_bound[0] + np.random.rand(no_agents,1)*(variable_bound[1]-variable_bound[0]))
                if type == 'bvar' or type == 'ivar':
                    return NumpyVariable(np.round(variable_bound[0] + np.random.rand(no_agents,1)*(variable_bound[1]-variable_bound[0])).astype(int))
                if type == 'svar':
                    raise VariableDimError("Dimension is set to be 0 or not defined for a sequential variable.")
                
            else:

                if type == 'pvar' or type == 'fvar':
                    return NumpyVariable(variable_bound[0] + np.random.rand(*tuple([no_agents]+[len(dims) for dims in variable_dim]))*(variable_bound[1]-variable_bound[0]))
                if type == 'bvar' or type == 'ivar':
                    return NumpyVariable(np.round(variable_bound[0] + np.random.rand(*tuple([no_agents]+[len(dims) for dims in variable_dim]))*(variable_bound[1]-variable_bound[0])).astype(int) )
                if type == 'svar':          
                    return NumpyVariable(np.argsort(np.random.rand(*tuple([no_agents]+[len(dims) for dims in variable_dim])), axis=1))

        else:
            
           

            if variable_dim == 0:

                if type == 'pvar' or type == 'fvar':
                    return NumpyVariable(variable_bound[0] + np.random.rand()*(variable_bound[1]-variable_bound[0]))
                if type == 'bvar' or type == 'ivar':
                    return NumpyVariable(np.round(variable_bound[0] + np.random.rand()*(variable_bound[1]-variable_bound[0])).astype(int))
                if type == 'svar':
                    raise VariableDimError("Dimension is set to be 0 or not defined for a sequential variable.")
            
            else:

                if type == 'pvar' or type == 'fvar':
                    return NumpyVariable(variable_bound[0] + np.random.rand(*tuple([len(dims) for dims in variable_dim]))*(variable_bound[1]-variable_bound[0]))
                if type == 'bvar' or type == 'ivar':
                    return NumpyVariable(np.round(variable_bound[0] + np.random.rand(*tuple([len(dims) for dims in variable_dim]))*(variable_bound[1]-variable_bound[0])).astype(int) )
                if type == 'svar':          
                    return NumpyVariable(np.argsort(np.random.rand(*tuple([len(dims) for dims in variable_dim]))))
    else:

        spread = features['variable_spread'][name]

        if features['vectorized']:
            if variable_dim == 0:
                if type == 'bvar' or type == 'ivar':
                    return NumpyVariable(np.round(variable_bound[0] + agent[:, spread[0]:spread[1]] * (variable_bound[1] - variable_bound[0])).astype(int))
                
                elif type == 'pvar' or type == 'fvar':
                    return NumpyVariable(variable_bound[0] + agent[:, spread[0]:spread[1]] * (variable_bound[1] - variable_bound[0]))
                else:
                    return NumpyVariable(np.argsort(agent[:, spread[0]:spread[1]]))
            else:

                if type == 'bvar' or type == 'ivar':

                    var = NumpyVariable(np.round(variable_bound[0] + agent[:, spread[0]:spread[1]] * (variable_bound[1] - variable_bound[0])).astype(int))

                    return NumpyVariable(np.reshape(var, [var.shape[0]]+[len(dims) for dims in variable_dim]))

                elif type == 'pvar' or type == 'fvar':

                    var = variable_bound[0] + agent[:, spread[0]:spread[1]
                                                    ] * (variable_bound[1] - variable_bound[0])

                    return NumpyVariable(np.reshape(var, [var.shape[0]]+[len(dims) for dims in variable_dim]))

                else:

                    return NumpyVariable(np.argsort(agent[:, spread[0]:spread[1]]))
        else:

            if variable_dim == 0:

                if type == 'bvar' or type == 'ivar':
                    
                    

                    return NumpyVariable(np.round(variable_bound[0] + agent[spread[0]:spread[1]] * (variable_bound[1] - variable_bound[0])).astype(int))

                elif type == 'pvar' or type == 'fvar':

                    return NumpyVariable(variable_bound[0] + agent[spread[0]:spread[1]] * (variable_bound[1] - variable_bound[0]))

                else:

                    return NumpyVariable(np.argsort(agent[spread[0]:spread[1]]))

            else:

                if type == 'bvar' or type == 'ivar':
                    
       
                    return NumpyVariable(np.reshape(np.round(variable_bound[0] + agent[spread[0]:spread[1]] * (variable_bound[1] - variable_bound[0])), [len(dims) for dims in variable_dim]).astype(int))

                elif type == 'pvar' or type == 'fvar':

                    return NumpyVariable(np.reshape(variable_bound[0] + agent[spread[0]:spread[1]] * (variable_bound[1] - variable_bound[0]), [len(dims) for dims in variable_dim]))

                else:

                    return NumpyVariable(np.argsort(agent[spread[0]:spread[1]]))