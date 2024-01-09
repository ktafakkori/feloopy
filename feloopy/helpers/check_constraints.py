# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

def check_constraint_type(constraint):
    if isinstance(constraint, list):
        if isinstance(constraint[0], list):
            return 0
        elif len(constraint) <= 4:
            return 1
        else:
            return 2
    elif not isinstance(constraint, list):
        return 3
    
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
            return lhs <= rhs        
        case '==':
            return lhs == rhs   
        case '<':
            return lhs < rhs - epsilon
        case '>':
            return lhs > rhs + epsilon
        case '!=':
            return [lhs > rhs + epsilon, lhs < rhs - epsilon]                 