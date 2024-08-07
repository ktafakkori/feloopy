# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

import gekko as gekko_interface

def generate_model(features):

    return gekko_interface.GEKKO(remote=False, name=features['model_name'])
