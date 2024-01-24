# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.


from .classes import *
from .feloopy import *
from .operators import *
from .algorithms import *

try:
    from .extras import *
except ImportError:
    pass

HEURISTIC_ALGORITHMS = [
    
    ['feloopy', 'de'],
    ['feloopy', 'ga'],
    ['feloopy', 'gwo'],
    ['feloopy', 'sa'],
    ['feloopy', 'ts'],
    
    ['mealpy', 'a-bfo'], 
    ['mealpy', 'adap-ba'], 
    ['mealpy', 'adap-eo'], 
    ['mealpy', 'augm-aeo'], 
    ['mealpy', 'base-alo'], 
    ['mealpy', 'base-bbo'], 
    ['mealpy', 'base-bro'], 
    ['mealpy', 'base-chio'],
    ['mealpy', 'base-de'],
    ['mealpy', 'base-efo'],
    ['mealpy', 'base-fbio'],
    ['mealpy', 'base-foa'],

    ['mealpy', 'base-gco'], 
    ['mealpy', 'base-gska'], 
    ['mealpy', 'base-hs'],
    ['mealpy', 'base-ja'], 
    ['mealpy', 'base-lco'], 
    ['mealpy', 'base-mfo'], 
    ['mealpy', 'base-mvo'], 
    ['mealpy', 'base-qsa'], 
    ['mealpy', 'base-saro'], 
    ['mealpy', 'base-sbo'], 
    ['mealpy', 'base-sca'], 
    ['mealpy', 'base-sma'], 
    ['mealpy', 'base-ssa'], 
    ['mealpy', 'base-tlo'], 
    ['mealpy', 'base-vcs'],

    ['mealpy', 'c-pso'], 
    ['mealpy', 'cl-pso'], 
    ['mealpy', 'h-pso-tvac'],  
    ['mealpy', 'cl-pso'], 
    ['mealpy', 'h-pso-tvac'],
    ['mealpy', 'p-pso'],
    ['mealpy', 'orig-pso'],

    ['mealpy', 'base-ga'],
    ['mealpy', 'single-ga'],
    ['mealpy', 'multi-ga'], 
    ['mealpy', 'elite-multi-ga'], 
    ['mealpy', 'elite-single-ga'],

    ['mealpy', 'orig-abc'],
    
    ['mealpy', 'cma-es'], 
    ['mealpy', 'dev-dmoa'], 
    ['mealpy', 'dev-soa'], 
    ['mealpy', 'dev-spbo'],

    ['mealpy', 'enha-aeo'], 
    ['mealpy', 'enha-two'], 
    ['mealpy', 'gwo-woa'], 
    ['mealpy', 'hi-woa'], 
    ['mealpy', 'impr-aeo'], 
    ['mealpy', 'impr-bso'], 
    ['mealpy', 'impr-lco'], 
    ['mealpy', 'impr-nmra'], 
    ['mealpy', 'impr-qsa'], 
    ['mealpy', 'impr-sfo'], 
    ['mealpy', 'impr-slo'], 
    ['mealpy', 'itlo'], 
    ['mealpy', 'ja-de'], 
    ['mealpy', 'l-sha-de'], 
    ['mealpy', 'levy-aro'], 
    ['mealpy', 'levy-ep'], 
    ['mealpy', 'levy-es'], 
    ['mealpy', 'levy-ja'], 
    ['mealpy', 'levy-qsa'], 
    ['mealpy', 'levy-two'], 
    ['mealpy', 'modi-aeo'], 
    ['mealpy', 'modi-ba'], 
    ['mealpy', 'modi-eo'],
    ['mealpy', 'modi-slo'],
    ['mealpy', 'modi101-gto'],
    ['mealpy', 'modi102-gto'],
    
    ['mealpy', 'o-cro'], 
    ['mealpy', 'oppo-qsa'], 
    ['mealpy', 'oppo-two'], 
     
    ['mealpy', 'orig-acor'], 
    ['mealpy', 'orig-aeo'], 
    ['mealpy', 'orig-agto'], 
    ['mealpy', 'orig-alo'], 
    ['mealpy', 'orig-ao'], 
    ['mealpy', 'orig-archoa'], 
    ['mealpy', 'orig-aro'], 
    ['mealpy', 'orig-aso'], 
    ['mealpy', 'orig-avoa'], 
    ['mealpy', 'orig-ba'], 
    ['mealpy', 'orig-bbo'], 
    ['mealpy', 'orig-beesa'], 
    ['mealpy', 'orig-beesa'], 
    ['mealpy', 'orig-bes'], 
    ['mealpy', 'orig-bfo'], 
    ['mealpy', 'orig-bmo'], 
    ['mealpy', 'orig-bro'], 
    ['mealpy', 'orig-bsa'], 
    ['mealpy', 'orig-bso'], 
    ['mealpy', 'orig-ca'], 
    ['mealpy', 'orig-cdo'], 
    ['mealpy', 'orig-cem'], 
    ['mealpy', 'orig-cgo'], 
    ['mealpy', 'orig-chio'], 
    ['mealpy', 'orig-circle-sa'], 
    ['mealpy', 'orig-coa'], 
    ['mealpy', 'orig-cro'], 
    ['mealpy', 'orig-csa'], 
    ['mealpy', 'orig-cso'], 
    ['mealpy', 'orig-dmoa'], 
    ['mealpy', 'orig-do'], 
    ['mealpy', 'orig-efo'], 
    ['mealpy', 'orig-eho'], 
    ['mealpy', 'orig-eo'], 
    ['mealpy', 'orig-eoa'], 
    ['mealpy', 'orig-ep'], 
    ['mealpy', 'orig-es'], 
    ['mealpy', 'orig-esoa'], 
    ['mealpy', 'orig-evo'], 
    ['mealpy', 'orig-fa'], 
    ['mealpy', 'orig-fbio'], 
    ['mealpy', 'orig-ffa'], 
    ['mealpy', 'orig-fla'], 
    ['mealpy', 'orig-foa'], 
    ['mealpy', 'orig-fox'], 
    ['mealpy', 'orig-fpa'], 
    ['mealpy', 'orig-gbo'], 
    ['mealpy', 'orig-gco'], 
    ['mealpy', 'orig-gjo'], 
    ['mealpy', 'orig-goa'], 
    ['mealpy', 'orig-gska'], 
    ['mealpy', 'orig-gto'],
    ['mealpy', 'orig-gwo'], 
    ['mealpy', 'orig-hba'], 
    ['mealpy', 'orig-hbo'], 
    ['mealpy', 'orig-hc'], 
    ['mealpy', 'orig-hgs'], 
    ['mealpy', 'orig-hgso'], 
    ['mealpy', 'orig-hho'], 
    ['mealpy', 'orig-hs'], 
    ['mealpy', 'orig-huco'], 
    ['mealpy', 'orig-ica'], 
    ['mealpy', 'orig-info'], 
    ['mealpy', 'orig-iwo'], 
    ['mealpy', 'orig-ja'], 
    ['mealpy', 'orig-lco'], 
    ['mealpy', 'orig-ma'], 
    ['mealpy', 'orig-mfo'], 
    ['mealpy', 'orig-mgo'], 
    ['mealpy', 'orig-mpa'], 
    ['mealpy', 'orig-mrfo'], 
    ['mealpy', 'orig-msa'], 
    ['mealpy', 'orig-mvo'], 
    ['mealpy', 'orig-nmra'], 
    ['mealpy', 'orig-nro'], 
    ['mealpy', 'orig-pfa'], 
     
    ['mealpy', 'orig-pss'], 
    ['mealpy', 'orig-qsa'], 
    ['mealpy', 'orig-rime'], 
    ['mealpy', 'orig-run'], 
    ['mealpy', 'orig-sa'], 
    ['mealpy', 'orig-saro'],
    ['mealpy', 'orig-sbo'], 
    ['mealpy', 'orig-sca'], 
    ['mealpy', 'orig-scso'], 
    ['mealpy', 'orig-sfo'], 
    ['mealpy', 'orig-shio'], 
    ['mealpy', 'orig-sho'], 
    ['mealpy', 'orig-slo'], 
    ['mealpy', 'orig-sma'], 
    ['mealpy', 'orig-soa'], 
    ['mealpy', 'orig-sos'], 
    ['mealpy', 'orig-spbo'], 
    ['mealpy', 'orig-srsr'], 
    ['mealpy', 'orig-ssa'], 
    ['mealpy', 'orig-ssdo'], 
    ['mealpy', 'orig-sso'], 
    ['mealpy', 'orig-sspidera'], 
    ['mealpy', 'orig-sspidero'], 
    ['mealpy', 'orig-tlo'], 
    ['mealpy', 'orig-tsa'], 
    ['mealpy', 'orig-tso'], 
    ['mealpy', 'orig-two'], 
    ['mealpy', 'orig-vcs'], 
    ['mealpy', 'orig-warso'], 
    ['mealpy', 'orig-wca'], 
    ['mealpy', 'orig-wdo'], 
    ['mealpy', 'orig-who'], 
    ['mealpy', 'orig-woa'],  
    ['mealpy', 'prob-beesa'], 
    ['mealpy', 'ql-sca'], 
    ['mealpy', 'rw-gwo'], 
    ['mealpy', 'sa-de'], 
    ['mealpy', 'sap-de'], 
    ['mealpy', 'sea-ho'], 
    ['mealpy', 'selec-aro'], 
    ['mealpy', 'sha-de'], 
    ['mealpy', 'simp-cma-es'],  
    ['mealpy', 'swarm-hc'], 
    ['mealpy', 'whale-foa'], 
    ['mealpy', 'wmqi-mrfo'], 

    ['niapy', 'base-abc'],
    ['niapy', 'base-ba'],
    ['niapy', 'base-bea'],
    ['niapy', 'base-bfo'],
    ['niapy', 'base-ca'],
    ['niapy', 'base-clonalg'],
    ['niapy', 'base-cro'],
    ['niapy', 'base-cs'],
    ['niapy', 'base-cso'],
    ['niapy', 'base-de'],
    ['niapy', 'base-dynnp-de'],
    ['niapy', 'base-anp-de'],
    ['niapy', 'base-ms-de'],
    ['niapy', 'base-dynnp-ms-de'],
    ['niapy', 'base-1+1-es'],
    ['niapy', 'base-m+1-es'],
    ['niapy', 'base-m+l-es'],
    ['niapy', 'base-m,l-es'],
    ['niapy', 'base-fa'],
    ['niapy', 'base-foa'],
    ['niapy', 'base-fpa'],
    ['niapy', 'base-fss'],
    ['niapy', 'base-bb-fwa'],
    ['niapy', 'base-fwa'],
    ['niapy', 'base-e-fwa'],
    ['niapy', 'base-dyn-fwa-g'],
    ['niapy', 'base-dyn-fwa'],
    ['niapy', 'base-ga'],
    ['niapy', 'base-gsa'],
    ['niapy', 'base-gso'],
    ['niapy', 'base-gso-v1'],
    ['niapy', 'base-gso-v2'],
    ['niapy', 'base-gso-v3'],
    ['niapy', 'base-gwo'],
    ['niapy', 'base-hho'],
    ['niapy', 'base-hs'],
    ['niapy', 'base-hs-v1'],
    ['niapy', 'base-kh'],
    ['niapy', 'base-loa'],
    ['niapy', 'base-mbo'],
    ['niapy', 'base-mfo'],
    ['niapy', 'base-mke-v1'],
    ['niapy', 'base-mke-v2'],
    ['niapy', 'base-mke-v3'],
    ['niapy', 'base-wvc-pso'],
    ['niapy', 'base-pso'],
    ['niapy', 'base-ovc-pso'],
    ['niapy', 'base-c-pso'],
    ['niapy', 'base-m-pso'],
    ['niapy', 'base-mc-pso'],
    ['niapy', 'base-mcu-pso'],
    ['niapy', 'base-cl-pso'],
    ['niapy', 'base-sca'],
    
    ['niapy', 'modi-h-ba'],
    ['niapy', 'modi-de-mts'],
    ['niapy', 'modi-de-mts-v1'],
    ['niapy', 'modi-dynnp-de-mts'],
    ['niapy', 'modi-dynnp-de-mts-v1'],
    ['niapy', 'modi-ms-de-mts'],
    ['niapy', 'modi-ms-de-mts-v1'],
    ['niapy', 'modi-dynnp-ms-de-mts'],
    ['niapy', 'modi-dynnp-ms-de-mts-v1'],
    ['niapy', 'modi-sa-de'],
    ['niapy', 'modi-ms-sa-de'],
    ['niapy', 'modi-a-ba'],
    ['niapy', 'modi-sa-ba'],
    ['niapy', 'modi-hsa-ba'],
    ['niapy', 'modi-pf-ba'],
    ['niapy', 'modi-sh-a-de'],
    ['niapy', 'modi-lpsr-sh-a-de'],
  
    ['niapy', 'other-nmm'],
    ['niapy', 'other-hc'],
    ['niapy', 'other-sa'],
    ['niapy', 'other-mts'],
    ['niapy', 'other-mts1'],
    ['niapy', 'other-mts-ls1'],
    ['niapy', 'other-mts-ls2'],
    ['niapy', 'other-mts-ls3'],
    ['niapy', 'other-mts-ls1v1'],
    ['niapy', 'other-mts-ls3v1'],
    ['niapy', 'other-aso'],
    ['niapy', 'other-rs'],
  
    ]

EXACT_ALGORITHMS = [

    ['copt', 'copt'],
    ['cplex', 'cplex'],
    ['cvxpy', 'cbc'],
    ['cvxpy', 'clarabel'],
    ['cvxpy', 'copt'],
    ['cvxpy', 'cplex'],
    ['cvxpy', 'cvxopt'],
    ['cvxpy', 'ecos'],
    ['cvxpy', 'glop'],
    ['cvxpy', 'glpk-mi'],
    ['cvxpy', 'glpk'],
    ['cvxpy', 'gurobi'],
    ['cvxpy', 'mosek'],
    ['cvxpy', 'nag'],
    ['cvxpy', 'osqp'],
    ['cvxpy', 'pdlp'],
    ['cvxpy', 'proxqp'],
    ['cvxpy', 'scip'],
    ['cvxpy', 'scipy'],
    ['cvxpy', 'scs'],
    ['cvxpy', 'xpress'],
    ['cylp', 'cbc'],
    ['gekko', 'apopt'],
    ['gekko', 'bpopt'],
    ['gekko', 'ipopt'],
    ['gurobi', 'gurobi'],
    ['linopy', 'cbc'],
    ['linopy', 'cplex'],
    ['linopy', 'glpk'],
    ['linopy', 'gurobi'],
    ['linopy', 'highs'],
    ['linopy', 'xpress'],
    ['insideopt', 'seeker'],
    ['insideopt-demo', 'seeker'],
    ['mip', 'cbc'],
    ['mip', 'gurobi'],
    ['mip', 'cplex'],
    ['mip', 'glpk'],
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
    ['pymprog', 'glpk'],
    ['pyomo', 'asl'],
    ['pyomo', 'baron'],
    ['pyomo', 'cbc'],
    ['pyomo', 'conopt'],
    ['pyomo', 'cplex-direct'],
    ['pyomo', 'cplex-persistent'],
    ['pyomo', 'cplex'],
    ['pyomo', 'cyipopt'],
    ['pyomo', 'gams'],
    ['pyomo', 'gdpopt.gloa'],
    ['pyomo', 'gdpopt.lbb'],
    ['pyomo', 'gdpopt.loa'],
    ['pyomo', 'gdpopt.ric'],
    ['pyomo', 'gdpopt'],
    ['pyomo', 'glpk'],
    ['pyomo', 'gurobi-direct'],
    ['pyomo', 'gurobi-persistent'],
    ['pyomo', 'gurobi'],
    ['pyomo', 'highs'],
    ['pyomo', 'ipopt'],
    ['pyomo', 'mindtpy'],
    ['pyomo', 'mosek-direct'],
    ['pyomo', 'mosek-persistent'],
    ['pyomo', 'mosek'],
    ['pyomo', 'mpec-minlp'],
    ['pyomo', 'mpec-nlp'],
    ['pyomo', 'multistart'],
    ['pyomo', 'path'],
    ['pyomo', 'scip'],
    ['pyomo', 'trustregion'],
    ['pyomo', 'xpress-direct'],
    ['pyomo', 'xpress-persistent'],
    ['pyomo', 'xpress'],
    ['xpress', 'xpress'],
    ['gams', 'alphaecp'],
    ['gams', 'antigone'],
    ['gams', 'baron'],
    ['gams', 'cbc'],
    ['gams', 'conopt'],
    ['gams', 'convert'],
    ['gams', 'copt'],
    ['gams', 'cplex'],
    ['gams', 'de'],
    ['gams', 'decis'],
    ['gams', 'dicopt'],
    ['gams', 'examiner'],
    ['gams', 'gamschk'],
    ['gams', 'gurobi'],
    ['gams', 'guss'],
    ['gams', 'highs'],
    ['gams', 'ipopt'],
    ['gams', 'jams'],
    ['gams', 'kestrel'],
    ['gams', 'knitro'],
    ['gams', 'lindo'],
    ['gams', 'lindoglobal'],
    ['gams', 'miles'],
    ['gams', 'minos'],
    ['gams', 'mosek'],
    ['gams', 'mps2gms'],
    ['gams', 'mpsge'],
    ['gams', 'msnlp'],
    ['gams', 'nlpec'],
    ['gams', 'octeract'],
    ['gams', 'odh'],
    ['gams', 'path'],
    ['gams', 'pathnlp'],
    ['gams', 'quad'],
    ['gams', 'sbb'],
    ['gams', 'scip'],
    ['gams', 'shot'],
    ['gams', 'snopt'],
    ['gams', 'soplex'],
    ['gams', 'xpress'],
]



UNCERTAINTY_ALGORITHMS = [
    ['rsome-dro', 'copt'],
    ['rsome-dro', 'cplex'],
    ['rsome-dro', 'cvxpy'],
    ['rsome-dro', 'cylp'],
    ['rsome-dro', 'ecos'],
    ['rsome-dro', 'gurobi'],
    ['rsome-dro', 'mosek'],
    ['rsome-dro', 'ortools'],
    ['rsome-dro', 'scipy'],
    ['rsome-ro', 'copt'],
    ['rsome-ro', 'cplex'],
    ['rsome-ro', 'cvxpy'],
    ['rsome-ro', 'cylp'],
    ['rsome-ro', 'ecos'],
    ['rsome-ro', 'gurobi'],
    ['rsome-ro', 'mosek'],
    ['rsome-ro', 'ortools'],
    ['rsome-ro', 'scipy'],
]

CONSTRAINT_ALGORITHMS = [
    ['cplex-cp', 'cplex'],
    ['ortools-cp', 'ortools']
]

MOO_ALGORITHMS = [
    ['pymoo', 'age-mo-ea-ii'],
    ['pymoo', 'age-mo-ea'],
    ['pymoo', 'cta-ea'],
    ['pymoo', 'd-ns-ga-ii'],
    ['pymoo', 'mo-ea-d'],
    ['pymoo', 'ns-ga-ii'],
    ['pymoo', 'ns-ga-iii'],
    ['pymoo', 'r-ns-ga-ii'],
    ['pymoo', 'r-ns-ga-iii'],
    ['pymoo', 'rv-ea'],
    ['pymoo', 'sms-ea'],
    ['pymoo', 'sp-ea-ii'],
    ['pymoo', 'u-ns-ga-iii'],
    ['pymultiobjective', 'cta-ea'],
    ['pymultiobjective', 'ea-d'],
    ['pymultiobjective', 'ea-fc'],
    ['pymultiobjective', 'ea-hv'],
    ['pymultiobjective', 'est-hv'],
    ['pymultiobjective', 'gr-ea'],
    ['pymultiobjective', 'modi-pso'],
    ['pymultiobjective', 'na-ea'],
    ['pymultiobjective', 'ns-ga-ii'],
    ['pymultiobjective', 'ns-ga-ii'],
    ['pymultiobjective', 'ns-ga-iii'],
    ['pymultiobjective', 'pa-es'],
    ['pymultiobjective', 'rv-ea'],
    ['pymultiobjective', 'sm-pso'],
    ['pymultiobjective', 'sms-ea'],
    ['pymultiobjective', 'sp-ea-ii'],
    ['pymultiobjective', 'u-ns-ga-iii'],
]

WEIGHTING_ALGORITHMS = [
    ['ahp_method','pydecision'],
    ['fuzzy_ahp_method','pydecision'],
    ['bw_method','pydecision'],
    ['fuzzy_bw_method','pydecision'],
    ['cilos_method', 'pydecision'],
    ['critic_method', 'pydecision'],
    ['entropy_method', 'pydecision'],
    ['idocriw_method', 'pydecision'],
    ['merec_method', 'pydecision'],
    ['lp_method', 'feloopy'],
    ]

RANKING_ALGORITHMS = [
    ['aras_method', 'pydecision'],
    ['fuzzy_aras_method', 'pydecision'],
    ['borda_method', 'pydecision'],
    ['cocoso_method', 'pydecision'],
    ['codas_method', 'pydecision'],
    ['copeland_method', 'pydecision'],
    ['copras_method', 'pydecision'],
    ['fuzzy_copras_method', 'pydecision'],
    ['cradis_method', 'pydecision'],
    ['edas_method', 'pydecision'],
    ['fuzzy_edas_method', 'pydecision'],
    ['gra_method', 'pydecision'],
    ['mabac_method', 'pydecision'],
    ['macbeth_method', 'pydecision'],
    ['mairca_method', 'pydecision'],
    ['marcos_method', 'pydecision'],
    ['maut_method', 'pydecision'],
    ['moora_method', 'pydecision'],
    ['fuzzy_moora_method', 'pydecision'],
    ['moosra_method', 'pydecision'],
    ['multimoora_method', 'pydecision'],
    ['ocra_method', 'pydecision'],
    ['fuzzy_ocra_method', 'pydecision'],
    ['oreste_method', 'pydecision'],
    ['piv_method', 'pydecision'],
    ['promethee_ii', 'pydecision'],
    ['promethee_iv', 'pydecision'],
    ['promethee_vi', 'pydecision'],
    ['psi_method', 'pydecision'],
    ['regime_method', 'pydecision'],
    ['rov_method', 'pydecision'],
    ['saw_method', 'pydecision'],
    ['smart_method', 'pydecision'],
    ['spotis_method', 'pydecision'],
    ['todim_method', 'pydecision'],
    ['topsis_method', 'pydecision'],
    ['fuzzy_topsis_method', 'pydecision'],
    ['vikor_method', 'pydecision'],
    ['fuzzy_vikor_method', 'pydecision'],
    ['waspas_method', 'pydecision'],
    ['fuzzy_waspas_method', 'pydecision'],
    ['la_method', 'feloopy'],
    ]

SPECIAL_ALGORITHMS = [
    ['dematel_method', 'pydecision'],
    ['fuzzy_dematel_method', 'pydecision'],
    ['electre_i', 'pydecision'],
    ['electre_i_s', 'pydecision'],
    ['electre_i_v', 'pydecision'],
    ['electre_ii', 'pydecision'],
    ['electre_iii', 'pydecision'],
    ['electre_iv', 'pydecision'],
    ['electre_tri_b', 'pydecision'],
    ['promethee_i', 'pydecision'],
    ['promethee_iii', 'pydecision'],
    ['promethee_v', 'pydecision'],
    ['promethee_gaia', 'pydecision'],
    ['wings_method', 'pydecision'],
    ['cwdea_method', 'feloopy']
]