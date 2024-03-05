"""
Normal constraint module

Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
See the file LICENSE file for licensing details.
"""

from typing import List, Optional, Any
from numpy import reshape, shape

def check_constraint_type(constraint):

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
        
class Expression:
    pass

class NormalConstraintClass:
    
    def enforce_gt(self, lhs, rhs, epsilon=1e-6, name=None):
        self.con([lhs, '>', rhs, epsilon], name)
 
    def enforce_lt(self, lhs, rhs, epsilon=1e-6, name=None):
        self.con([lhs, '<', rhs, epsilon], name)

    def enforce_geq(self, lhs, rhs, name=None):
        self.con([lhs, '>=', rhs], name)
        
    def enforce_leq(self, lhs, rhs, epsilon=1e-6, name=None):
        self.con([lhs, '<=', rhs], name)

    def enforce_eq(self, lhs, rhs, epsilon=1e-6, name=None):
        self.con([lhs, '==', rhs], name)

    def enforce_neq(self, lhs, rhs, epsilon=1e-6, name=None):
        self.con([lhs, '!=', rhs, epsilon], name)
                             
    def con(self, expression, name=None):
        """
        Constraint Definition
        ~~~~~~~~~~~~~~~~~~~~~
        To define a constraint.

        Args:
            expression (formula): what are the terms of this constraint?
            name (str, optional): what is the name of this constraint?. Defaults to None.
        """
                    
        def add_special_constraint(element):
            relation, lower_bound, upper_bound = element[1], element[0], element[2]

            
            epsilon = element[3] if len(element) == 4 else 0.000001

            const = generate_constraint(lower_bound,relation,upper_bound,epsilon)
            if not isinstance(const, list):
                const = [const]
            return const
          
        match self.features['solution_method']:

            case 'exact':
                
                match check_constraint_type(expression):
                
                    case 'list with sense':
                        const_list = []
                        for element in expression:
                            const = add_special_constraint(element)
                            const_list+=const
                        if isinstance(name, list): self.features['constraint_labels'] += name
                        else: self.features['constraint_labels'] += [str(name)+str(i) if name else None for i in range(len(expression))]
                        self.features['constraint_counter'][0] = len(set(self.features['constraint_labels']))
                        self.features['constraints'] += const_list
                        self.features['constraint_counter'][1] = len(self.features['constraints'])
                
                    case 'single list with sense': 
               
                        if len(expression)==3: name = [name]
                        const = add_special_constraint(expression)
                        if isinstance(name, list): self.features['constraint_labels'] += name
                        else: self.features['constraint_labels'] += [str(name)+str(i) if name else None for i in range(len(const))]
                        self.features['constraint_counter'][0] = len(set(self.features['constraint_labels']))
                        self.features['constraints'] += const
                        self.features['constraint_counter'][1] = len(self.features['constraints'])

                    case 'list without sense':

                        if isinstance(name, list): self.features['constraint_labels'] += name
                        else: self.features['constraint_labels'] += [str(name)+str(i) if name else None for i in range(len(expression))]
                        self.features['constraint_counter'][0] = len(set(self.features['constraint_labels']))
                        self.features['constraints'] += list(expression)
                        self.features['constraint_counter'][1] = len(self.features['constraints'])

                    case 'dict with sense':

                        for key, value in expression.items():
    
                            const = add_special_constraint(value)
                            self.features['constraint_labels'].append(key)
                            self.features['constraint_counter'][0] = len(set(self.features['constraint_labels']))
                            self.features['constraints']+=const
                            self.features['constraint_counter'][1] = len(self.features['constraints'])

                    case 'single dict with sense':
                
                        for key, value in expression.items():
                            const = add_special_constraint(value)
                            self.features['constraint_labels'].append(key)
                            self.features['constraint_counter'][0] = len(set(self.features['constraint_labels']))
                            self.features['constraints']+=const
                            self.features['constraint_counter'][1] = len(self.features['constraints'])

                    case 'dict without sense':

                        self.features['constraint_labels']+=list(expression.keys())
                        self.features['constraint_counter'][0] = len(set(self.features['constraint_labels']))
                        self.features['constraints']+=list(expression.values())
                        self.features['constraint_counter'][1] = len(self.features['constraints'])
                       
                    case 'classic':
                    
                        self.features['constraint_labels'].append(name)
                        self.features['constraint_counter'][0] = len(set(self.features['constraint_labels']))
                        self.features['constraints'].append(expression)
                        self.features['constraint_counter'][1] = len(self.features['constraints'])

            case 'heuristic':

                if self.features['agent_status'] == 'idle':
                    self.features['constraint_labels'].append(name)
                    self.features['constraint_counter'][0] = len(set(self.features['constraint_labels']))
                    self.features['constraints'].append(expression)
                    self.features['constraint_counter'][1] = len(self.features['constraints'])
                else:
                    if self.features['vectorized']:
                        self.features['constraints'].append(reshape(expression, [shape(self.agent)[0], 1]))
                    else:
                        self.features['constraints'].append(expression)