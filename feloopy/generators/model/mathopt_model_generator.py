# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

from ortools.math_opt.python import mathopt


def generate_model(features):

    return mathopt.Model(name=features['model_name'])