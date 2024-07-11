# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

def generate_model(features):
    model_object = ""
    model_object += "\nusing JuMP"
    model_object += "\njlmodel = Model()"
    return model_object