# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

def set_init_value(features, variable, value, fix):

    if fix:
        ""
    else:
        features['model_object'].setMipStart(variable, value)
