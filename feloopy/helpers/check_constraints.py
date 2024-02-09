# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

import types

def check_constraint_type(constraint):

    print(type(constraint))
    
    if isinstance(constraint, list):
        if isinstance(constraint[0], list) and isinstance(constraint[0][1], str):
            return 'list with sense'
        elif isinstance(constraint[1], str):
            return 'single list with sense'
        else:
            return 'list without sense'

    elif type(constraint)== dict:
        if isinstance(list(constraint.values())[0], list):
            return 'single dict with sense'
        else:
            
            return 'dict without sense'
    else:
        return 'classic'

def check_sense(sense):
    if sense in ['<=', 'le', 'leq', '=l=']:
        return '<='
    elif sense in ['>=', 'ge', 'geq', '=g=']:
        return '>='
    elif sense in ['==', 'eq', '=e=']:
        return '=='
    elif sense in ['<', 'lt']:
        return '<'
    elif sense in ['>', 'gt']:
        return '>'
    elif sense in ['!=', 'neq']:
        return '!='
    
def generate_constraint(lhs, sense, rhs, epsilon):
    
    match sense:
        case '<=':
            return lhs <= rhs
        case '>=':
            return lhs >= rhs        
        case '==':
            return lhs == rhs   
        case '<':
            return lhs < rhs - epsilon
        case '>':
            return lhs > rhs + epsilon
        case '!=':
            return [lhs > rhs + epsilon, lhs < rhs - epsilon]                 