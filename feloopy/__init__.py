'''
 # @ Author: Keivan
 # @ Created: 2023-05-11
 # @ Modified: 2023-05-11
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''


from .feloopy import *
from .operators import *

heuristic_algorithms = ['orig-ep',
                        'levy-ep',
                        'orig-es',
                        'levy-es',
                        'orig-ma',
                        'base-ga',
                        'single-ga',
                        'multi-ga',
                        'elite-single-ga',
                        'elite-multi-ga',
                        'base-de',
                        'ja-de',
                        'sa-de',
                        'sha-de',
                        'l-sha-de',
                        'sap-de',
                        'orig-fpa',
                        'orig-cro',
                        'o-cro',
                        'orig-pso',
                        'p-pso',
                        'h-pso-tvac',
                        'c-pso',
                        'cl-pso',
                        'orig-bfo',
                        'a-bfo',
                        'orig-beesa',
                        'prob-beesa',
                        'orig-cso',
                        'orig-abc',
                        'orig-acor',
                        'orig-csa',
                        'orig-ffa',
                        'orig-fa',
                        'orig-ba',
                        'adap-ba',
                        'modi-ba',
                        'orig-foa',
                        'base-foa',
                        'whale-foa',
                        'orig-sspidero',
                        'orig-gwo',
                        'rw-gwo',
                        'orig-sspidera',
                        'orig-alo',
                        'base-alo',
                        'orig-mfo',
                        'base-mfo',
                        'orig-eho',
                        'orig-ja',
                        'base-ja',
                        'levy-ja',
                        'orig-woa',
                        'hi-woa',
                        'orig-do',
                        'orig-bsa',
                        'orig-sho',
                        'orig-sso',
                        'orig-srsr',
                        'orig-goa',
                        'orig-coa',
                        'orig-msa',
                        'orig-slo',
                        'modi-slo',
                        'impr-slo',
                        'orig-nmra',
                        'impr-nmra',
                        'orig-pfa',
                        'orig-sfo',
                        'impr-sfo',
                        'orig-hho',
                        'orig-mrfo',
                        'orig-bes',
                        'orig-ssa',
                        'base-ssa',
                        'orig-hgs',
                        'orig-ao',
                        'gwo-woa',
                        'orig-mpa',
                        'orig-hba',
                        'orig-scso',
                        'orig-tso',
                        'orig-avoa',
                        'orig-agto',
                        'orig-aro',
                        'orig-sa',
                        'orig-wdo',
                        'orig-mvo',
                        'base-mvo',
                        'orig-two',
                        'oppo-two',
                        'levy-two',
                        'enha-two',
                        'orig-efo',
                        'base-efo',
                        'orig-nro',
                        'orig-hgso',
                        'orig-aso',
                        'orig-eo',
                        'modi-eo',
                        'adap-eo',
                        'orig-archoa',
                        'orig-ca',
                        'orig-ica',
                        'orig-tlo',
                        'base-tlo',
                        'i-tlo',
                        'orig-bso',
                        'impr-bso',
                        'orig-qsa',
                        'base-qsa',
                        'oppo-qsa',
                        'levy-qsa',
                        'impr-qsa',
                        'orig-saro',
                        'base-saro',
                        'orig-lco',
                        'base-lco',
                        'impr-lco',
                        'orig-ssdo',
                        'orig-gska',
                        'base-gska',
                        'orig-chio',
                        'base-chio',
                        'orig-fbio',
                        'base-fbio',
                        'orig-bro',
                        'base-bro',
                        'orig-spbo',
                        'dev-spbo',
                        'orig-dmoa',
                        'dev-dmoa',
                        'orig-iwo',
                        'orig-bbo',
                        'base-bbo',
                        'orig-vcs',
                        'base-vcs',
                        'orig-sbo',
                        'base-sbo',
                        'orig-eoa',
                        'orig-who',
                        'orig-sma',
                        'base-sma',
                        'orig-bmo',
                        'orig-tsa',
                        'orig-sos',
                        'orig-soa',
                        'dev-soa',
                        'orig-gco',
                        'base-gco',
                        'orig-wca',
                        'orig-aeo',
                        'enha-aeo',
                        'modi-aeo',
                        'impr-aeo',
                        'adap-aeo',
                        'orig-hc',
                        'swarm-hc',
                        'orig-cem',
                        'orig-sca',
                        'base-sca',
                        'orig-gbo',
                        'orig-aoa',
                        'orig-cgo',
                        'orig-pss',
                        'orig-info',
                        'orig-run',
                        'orig-circ-sa',
                        'orig-hs',
                        'base-hs'
                        ]

exact_algorithms = [

    # gekko
    ['gekko', 'apopt'],
    ['gekko', 'bpopt'],
    ['gekko', 'ipopt'],

    # ortools
    ['ortools', 'bop'],
    ['ortools', 'cbc'],
    ['ortools', 'clp'],
    ['ortools', 'cplex-'],
    ['ortools', 'cplex'],
    ['ortools', 'glop'],
    ['ortools', 'glpk-'],
    ['ortools', 'glpk'],
    ['ortools', 'gurobi-'],
    ['ortools', 'gurobi'],
    ['ortools', 'sat'],
    ['ortools', 'scip'],
    ['ortools', 'xpress-'],
    ['ortools', 'xpress'],

    # pulp
    ['pulp', 'cbc'],
    ['pulp', 'choco'],
    ['pulp', 'coin'],
    ['pulp', 'coinmp-dll'],
    ['pulp', 'cplex-py'],
    ['pulp', 'cplex'],
    ['pulp', 'glpk'],
    ['pulp', 'gurobi-cmd'],
    ['pulp', 'gurobi'],
    ['pulp', 'highs'],
    ['pulp', 'mipcl'],
    ['pulp', 'mosek'],
    ['pulp', 'pyglpk'],
    ['pulp', 'scip'],
    ['pulp', 'xpress-py'],
    ['pulp', 'xpress'],

    # cvxpy
    ['cvxpy', 'osqp'],
    ['cvxpy', 'ecos'],
    ['cvxpy', 'cvxopt'],
    ['cvxpy', 'scs'],
    ['cvxpy', 'scipy'],
    ['cvxpy', 'glop'],
    ['cvxpy', 'glpk'],
    ['cvxpy', 'glpk-mi'],
    ['cvxpy', 'gurobi'],
    ['cvxpy', 'mosek'],
    ['cvxpy', 'cbc'],
    ['cvxpy', 'cplex'],
    ['cvxpy', 'nag'],
    ['cvxpy', 'pdlp'],
    ['cvxpy', 'scip'],
    ['cvxpy', 'xpress'],
    ['cvxpy', 'copt'],
    ['cvxpy', 'clarabel'],
    ['cvxpy', 'proxqp'],

    # cylp
    ['cylp', 'cbc'],

    # gurobi
    ['gurobi', 'gurobi'],

    # cplex
    ['cplex', 'cplex'],

    # linopy
    ['linopy', 'cbc'],
    ['linopy', 'glpk'],
    ['linopy', 'highs'],
    ['linopy', 'gurobi'],
    ['linopy', 'xpress'],
    ['linopy', 'cplex'],

    # mip
    ['mip', 'cbc'],

    # picos
    ['picos', 'cplex'],
    ['picos', 'cvxopt'],
    ['picos', 'ecos'],
    ['picos', 'glpk'],
    ['picos', 'gurobi'],
    ['picos', 'mosek'],
    ['picos', 'mskfn'],
    ['picos', 'osqp'],
    ['picos', 'scip'],
    ['picos', 'smcp'],

    # pymprog
    ['pymprog', 'glpk'],

    # pyomo
    ['pyomo', 'baron'],
    ['pyomo', 'cbc'],
    ['pyomo', 'conopt'],
    ['pyomo', 'cplex'],
    ['pyomo', 'cplex-direct'],
    ['pyomo', 'cplex-persistent'],
    ['pyomo', 'cyipopt'],
    ['pyomo', 'gams'],
    ['pyomo', 'highs'],
    ['pyomo', 'asl'],
    ['pyomo', 'gdpopt'],
    ['pyomo', 'gdpopt.gloa'],
    ['pyomo', 'gdpopt.lbb'],
    ['pyomo', 'gdpopt.loa'],
    ['pyomo', 'gdpopt.ric'],
    ['pyomo', 'glpk'],
    ['pyomo', 'gurobi'],
    ['pyomo', 'gurobi-direct'],
    ['pyomo', 'gurobi-persistent'],
    ['pyomo', 'ipopt'],
    ['pyomo', 'mindtpy'],
    ['pyomo', 'mosek'],
    ['pyomo', 'mosek-direct'],
    ['pyomo', 'mosek-persistent'],
    ['pyomo', 'mpec-minlp'],
    ['pyomo', 'mpec-nlp'],
    ['pyomo', 'multistart'],
    ['pyomo', 'path'],
    ['pyomo', 'scip'],
    ['pyomo', 'trustregion'],
    ['pyomo', 'xpress'],
    ['pyomo', 'xpress-direct'],
    ['pyomo', 'xpress-persistent'],

    # xpress
    ['xpress', 'xpress'],
]

constraint_algorithms = [

    ['cplex-cp', 'cplex'],
    ['ortools-cp', 'ortools']

]

feloopy_heuristic_algorithms = [
    'ga',
    'sa',
    'ts',
    'de',
    'gwo'
]
