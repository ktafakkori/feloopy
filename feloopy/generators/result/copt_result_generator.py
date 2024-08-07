# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

from coptpy import *
from ...helpers.formatter import *

copt_status_dict = {
    COPT.OPTIMAL: 'optimal',
    COPT.INFEASIBLE: 'infeasible',
    COPT.UNBOUNDED: 'unbounded',
    COPT.NODELIMIT: 'node limit',
    COPT.INTERRUPTED: 'interrupted',
}

def Get(model_object, result, input1, input2=None):

    input1 = input1[0]

    match input1:

        case 'variable':
            return input2.X

        case 'status':
            return copt_status_dict[model_object.status]

        case 'objective':
            return model_object.objval

        case 'time':
            return (result[1][1]-result[1][0])

        case 'dual':
            return model_object.getConstrByName(input2).Pi

        case 'slack':
            return model_object.getConstrByName(input2).Slack

        case 'rc':
            return input2.rc

        case 'iis':
            model_object.computeIIS()

            output = ''

            constrs = model_object.getConstrs()
            vars = model_object.getVars()


            for i, c in enumerate(constrs):
                if c.getUpperIIS() > 0 or c.getLowerIIS() > 0:
                    output += left_align(f"con: {c.getName()}", rt=True)
                    if i != len(constrs) or i == 0:
                        output += "\n"

            for i, v in enumerate(vars):
                if v.getLowerIIS() > 0 or v.getUpperIIS() > 0:
                    output += left_align(f"var: {v.getName()}", rt=True)
                    if i != len(vars) - 1 or i == 0:
                        output += "\n"

            return output