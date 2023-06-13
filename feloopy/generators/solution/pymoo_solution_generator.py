'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-06-13
 # @ Modified: 2023-06-13
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''

import numpy as np
import timeit

def generate_solution(solver_name, AlgOptions, Fitness, ToTalVariableCounter, ObjectivesDirections, ObjectiveBeingOptimized, number_of_times, show_plots, save_plots):

    from pymoo.core.problem import Problem
    from pymoo.optimize import minimize
    import numpy as np

    ObjectivesDirections = [-1 if direction =='max' else 1 for direction in ObjectivesDirections]

    class MyProblem(Problem):
        def __init__(self):
            super().__init__(n_var=ToTalVariableCounter[1], n_obj=len(ObjectivesDirections), xl=np.array([0,]*ToTalVariableCounter[1]), xu=np.array([1,]*ToTalVariableCounter[1]))
        def _evaluate(self, x, out, *args, **kwargs):
            f = Fitness(np.array(x))
            out["F"] = np.column_stack([ObjectivesDirections[i]*f[i] for i in range(len(ObjectivesDirections))])
    
    problem = MyProblem()

    match solver_name:

        case "ns-ga-ii":

            from pymoo.algorithms.moo.nsga2 import NSGA2
            algorithm = NSGA2()

            time_solve_begin = timeit.default_timer()
            res = minimize(problem, algorithm, termination=("n_gen", 100), verbose=False)
            time_solve_end = timeit.default_timer()
        
            pareto_front = ObjectivesDirections*res.F
            pareto_solutions = res.X
            
            return pareto_solutions, pareto_front, time_solve_begin, time_solve_end
    



