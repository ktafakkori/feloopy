# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.


from coptpy import *
import itertools as it

sets = it.product

POSITIVE = COPT.CONTINUOUS
INTEGER = COPT.INTEGER
BINARY = COPT.BINARY
FREE = COPT.CONTINUOUS
INFINITY = COPT.INFINITY

def generate_variable(model_object, variable_type, variable_name, variable_bound, variable_dim=0):

    if variable_bound[0] is None:
        variable_bound[0] = -INFINITY

    if variable_bound[1] is None:
        variable_bound[1] = +INFINITY

    def add_vars(vtype, bounds, keys):
        return model_object.addVars(
            keys,
            vtype=vtype,
            lb=bounds[0],
            ub=bounds[1],
            nameprefix=variable_name
        )

    if variable_dim == 0:
        vtypes = {
            'pvar': POSITIVE,
            'bvar': BINARY,
            'ivar': INTEGER,
            'fvar': FREE
        }

        generated_variable = model_object.addVar(
            vtype=vtypes[variable_type], lb=variable_bound[0], ub=variable_bound[1], name=variable_name)
    else:
        if isinstance(variable_dim, set):
            keys = list(variable_dim)
        elif len(variable_dim) == 1:
            keys = variable_dim[0]
        else:
            keys = list(sets(*variable_dim))

        vtypes = {
            'pvar': POSITIVE,
            'bvar': BINARY,
            'ivar': INTEGER,
            'fvar': FREE,
            'ptvar': POSITIVE,
            'ftvar': FREE,
            'btvar': BINARY,
            'itvar': INTEGER
        }

        if variable_type in ['ptvar', 'ftvar', 'btvar', 'itvar']:
            shape = tuple(len(dim) for dim in variable_dim)
            generated_variable = model_object.addMVar(
                shape, vtype=vtypes[variable_type], lb=variable_bound[0], ub=variable_bound[1], nameprefix=variable_name)
        else:
            generated_variable = add_vars(vtypes[variable_type], variable_bound, keys)

    return generated_variable