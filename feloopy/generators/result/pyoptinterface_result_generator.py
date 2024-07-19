# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

import pyoptinterface as poi

def Get(model_object, result, input1, input2=None):

    input1 = input1[0]

    match input1:

        case 'variable':

            return model_object.get_value(input2)

        case 'status':

            return model_object.get_model_attribute(poi.ModelAttribute.TerminationStatus)

        case 'objective':

            return model_object.get_model_attribute(poi.ModelAttribute.ObjectiveValue)

        case 'time':

            return (result[1][1]-result[1][0])
        
        case 'dual':

            return model_object.dual[model_object.c[input2]]

        case 'slack':

            upper_slack = model_object.c[input2].uslack()
            lower_slack = model_object.c[input2].lslack()

            return min(upper_slack, lower_slack)
        
        case 'rc':
            ""
    