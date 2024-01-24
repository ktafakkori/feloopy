# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.


def generate_solution(solver_name, AlgOptions, Fitness, ToTalVariableCounter, ObjectivesDirections, ObjectiveBeingOptimized, number_of_times, show_plots, save_plots, show_log):

    import timeit
    from pymoo.core.problem import Problem
    from pymoo.optimize import minimize
    from pymoo.termination import get_termination
    from pymoo.util.ref_dirs import get_reference_directions

    import numpy as np

    if show_log:
        verbose=True
    
    else:
        verbose=False

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

        case "d-ns-ga-ii":

            from pymoo.algorithms.moo.dnsga2 import DNSGA2
            algorithm = DNSGA2(**AlgOptions)

        case "ns-ga-iii":

            from pymoo.algorithms.moo.nsga3 import NSGA3
            algorithm = NSGA3(**AlgOptions)

        case "mo-ea-d":

            from pymoo.algorithms.moo.moead import MOEAD
            algorithm = MOEAD(**AlgOptions)

        case "cta-ea":

            from pymoo.algorithms.moo.ctaea import CTAEA
            algorithm = CTAEA(**AlgOptions)

        case "r-ns-ga-ii":

            from pymoo.algorithms.moo.rnsga2 import RNSGA2
            algorithm = RNSGA2(**AlgOptions)

        case "r-ns-ga-iii":

            from pymoo.algorithms.moo.rnsga3 import RNSGA3
            algorithm = RNSGA3(**AlgOptions)

        case "u-ns-ga-iii":
    
            from pymoo.algorithms.moo.unsga3 import UNSGA3
            algorithm = UNSGA3(**AlgOptions)

        case "sp-ea-ii":

            from pymoo.algorithms.moo.spea2 import SPEA2
            algorithm = SPEA2(**AlgOptions)
        
        case "sms-ea":

            from pymoo.algorithms.moo.sms import SMSEMOA
            algorithm = SMSEMOA(**AlgOptions)
        
        case "rv-ea":

            from pymoo.algorithms.moo.rvea import RVEA
            algorithm = RVEA(**AlgOptions)

        case "age-mo-ea":

            from pymoo.algorithms.moo.age import AGEMOEA
            algorithm = AGEMOEA(**AlgOptions)

        case "age-mo-ea-ii":

            from pymoo.algorithms.moo.age2 import AGEMOEA2
            algorithm = AGEMOEA2(**AlgOptions)

    from pymoo.termination.default import DefaultMultiObjectiveTermination

    termination = DefaultMultiObjectiveTermination(
        xtol=1e-8,
        cvtol=1e-6,
        ftol=0.0025,
        period=30,
        n_max_gen=1000,
        n_max_evals=100000
    )

    if AlgOptions.get('n_gen', None)!=None:
        termination = get_termination("n_gen", AlgOptions['n_gen'])

    if AlgOptions.get('n_eval', None)!=None:
        termination = get_termination("n_gen", AlgOptions['n_eval'])

    if AlgOptions.get('time', None)!=None:
        termination = get_termination("time", AlgOptions['time'])

    if AlgOptions.get('design_space_tolerance_period', None)!=None:

        from pymoo.termination.xtol import DesignSpaceTermination
        from pymoo.termination.robust import RobustTermination
        termination = RobustTermination(DesignSpaceTermination(**AlgOptions['design_space_tolerance_period'][0]), period=AlgOptions['design_space_tolerance_period'][1])

    if AlgOptions.get('objective_space_tolerance_period', None): 

        from pymoo.termination.ftol import MultiObjectiveSpaceTermination
        from pymoo.termination.robust import RobustTermination
        termination = RobustTermination(MultiObjectiveSpaceTermination(**AlgOptions['objective_space_tolerance_period'][0]), period=AlgOptions['objective_space_tolerance_period'][1])

    time_solve_begin = timeit.default_timer()
    res = minimize(problem, algorithm, termination=termination, verbose=verbose)
    time_solve_end = timeit.default_timer()
    pareto_front = ObjectivesDirections*res.F
    pareto_solutions = res.X
    
    return pareto_solutions, pareto_front, time_solve_begin, time_solve_end

