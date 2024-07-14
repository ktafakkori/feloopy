# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.


import itertools as it

sets = it.product


def generate_variable(model_object, variable_type, variable_name, variable_bound, variable_dim=0):

    if isinstance(variable_dim,set):
        variable_dim=[variable_dim]

    match variable_type:

        case 'pvar':

            '''
            Positive Variable Generator
            '''

            if variable_dim == 0:
                GeneratedVariable=f"\n@variable(jlmodel, {variable_name} >= 0)"
            else:
                index_ranges = ', '.join([f'element in {str(list(dim))}' for dim in variable_dim])
                GeneratedVariable = f"\n@variable(jlmodel, {variable_name}[{index_ranges}] >= 0)"

        case 'bvar':

            '''
            Binary Variable Generator
            '''

            if variable_dim == 0:
                GeneratedVariable=f"\n@variable(jlmodel, {variable_name}, Bin)"
            else:
                index_ranges = ', '.join([f'element in {str(list(dim))}' for dim in variable_dim])
                GeneratedVariable = f"\n@variable(jlmodel, {variable_name}[{index_ranges}], Bin)"

        case 'ivar':

            '''
            Integer Variable Generator
            '''

            if variable_dim == 0:
                GeneratedVariable=f"\n@variable(jlmodel, {variable_name}, Int)"
            else:
                index_ranges = ', '.join([f'element in {str(list(dim))}' for dim in variable_dim])
                GeneratedVariable = f"\n@variable(jlmodel, {variable_name}[{index_ranges}], Int)"

        case 'fvar':

            '''
            Free Variable Generator
            '''
            if variable_dim == 0:
                GeneratedVariable=f"\n@variable(jlmodel, {variable_name})"
            else:
                index_ranges = ', '.join([f'element in {str(list(dim))}' for dim in variable_dim])
                GeneratedVariable = f"\n@variable(jlmodel, {variable_name}[{index_ranges}])"

    return GeneratedVariable
