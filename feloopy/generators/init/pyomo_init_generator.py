# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

def set_init_value(features, variable, value, fix):
    if fix:
        variable.fix(value)
    else:
        variable.set_value(value)
