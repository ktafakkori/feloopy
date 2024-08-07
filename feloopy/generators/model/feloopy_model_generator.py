# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

def generate_model(total_variables, directions, solver_name, solver_options):
    match solver_name:
        case 'hco':
            try:
                from ...extras.algorithms.heuristic.HCO import HCO
            except ImportError:
                from ...algorithms.heuristic.HCO import HCO
            model_object = HCO(f=total_variables, d=directions, s=solver_options.get('epoch', 100), t=solver_options.get('pop_size', 50), e=solver_options.get('elitism_number', 3), ac=solver_options.get('archive_cap', 100), rep=solver_options.get('episode', 1), ben=solver_options.get('benchmark', False))

        case 'gwo':
            try:
                from ...extras.algorithms.heuristic.GWO import GWO
            except ImportError:
                from ...algorithms.heuristic.GWO import GWO
            model_object = GWO(f=total_variables, d=directions, s=solver_options.get('epoch', 100), t=solver_options.get(
                'pop_size', 50), ac=solver_options.get('archive_cap', 50), rep=solver_options.get('episode', 1), ben=solver_options.get('benchmark', False))

        case 'ga':
            try:
                from ...extras.algorithms.heuristic.GA import GA
            except ImportError:
                from ...algorithms.heuristic.GA import GA
            model_object = GA(f=total_variables, d=directions, s=solver_options.get('epoch', 100), t=solver_options.get('pop_size', 50), sc=solver_options.get('selection', 1), mu=solver_options.get('mutation_rate', 0.02), cr=solver_options.get('crossover_rate', 0.7), sfl=solver_options.get('survival_lb', 0.4), sfu=solver_options.get('survival_ub', 0.6), ac=solver_options.get('archive_cap', 50), rep=solver_options.get('episode', 1), ben=solver_options.get('benchmark', False))

        case 'de':
            try:
                from ...extras.algorithms.heuristic.DE import DE
            except ImportError:
                from ...algorithms.heuristic.DE import DE
            model_object = DE(f=total_variables, d=directions, s=solver_options.get('epoch', 100), t=solver_options.get('pop_size', 50), mu=solver_options.get('mutation_rate', 0.02),
                              cr=solver_options.get('crossover_rate', 0.7), ac=solver_options.get('archive_cap', 50), rep=solver_options.get('episode', 1), ben=solver_options.get('benchmark', False))

        case 'sa':
            try:
                from ...extras.algorithms.heuristic.SA import SA
            except ImportError:
                from ...algorithms.heuristic.SA import SA
            model_object = SA(f=total_variables, d=directions, s=solver_options.get('epoch', 100), t=1, cc=solver_options.get('cooling_cycles', 10), mt=solver_options.get(
                'maximum_temperature', 1000),  ac=solver_options.get('archive_cap', 50), rep=solver_options.get('episode', 1), ben=solver_options.get('benchmark', False))

        case 'bo':
            try:
                from ...extras.algorithms.heuristic.BO import BO
            except ImportError:
                from ...algorithms.heuristic.BO import BO
            model_object = BO(f=total_variables, d=directions, s=solver_options.get(
                'epoch', 100), t=10, rep=solver_options.get('episode', 1), ben=solver_options.get('benchmark', False))

        case 'ts':
            try:
                from ...extras.algorithms.heuristic.TS import TS
            except ImportError:
                from ...algorithms.heuristic.TS import TS
            model_object = TS(f=total_variables, d=directions, s=solver_options.get('epoch', 100), t=1, c=solver_options.get(
                'tabu_list_size', 10), ac=solver_options.get('archive_cap', 50), rep=solver_options.get('episode', 1), ben=solver_options.get('benchmark', False))

        case 'pso':
            try:
                from ...extras.algorithms.heuristic.PSO import PSO
            except ImportError:
                from ...algorithms.heuristic.PSO import PSO
            model_object = PSO(f=total_variables, d=directions, s=solver_options.get('epoch', 100), t=solver_options.get('pop_size', 50), w=solver_options.get('velocity_weight', 0.8), c1=solver_options.get(
                'p_best_weight', 0.1), c2=solver_options.get('g_best_weight', 0.1), ac=solver_options.get('archive_cap', 50), rep=solver_options.get('episode', 1), ben=solver_options.get('benchmark', False))

    return model_object