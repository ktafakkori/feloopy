# Exact Solvers

| solver                                                                                              | interface                                           | Embedded      |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------- | ------------- |
| [apopt](https://apopt.com/download.php)                                                             | gekko                                               | gekko         |
| [asl](https://github.com/ampl/asl)                                                                  | pyomo                                               | -             |
| [baron](https://minlp.com/baron-downloads)                                                          | pyomo                                               | -             |
| [cbc](https://www.coin-or.org/download/binary/Cbc/)                                                 | cvxpy, cylp, linopy, mip, ortools, pulp, pyomo      | pulp          |
| [choco](https://github.com/chocoteam/choco-solver#dow)                                              | pulp                                                | -             |
| [clp](https://www.coin-or.org/download/binary/Clp/)                                                 | ortools                                             | -             |
| [coin](https://www.coin-or.org/download/binary/CoinAll/)                                            | pulp                                                | -             |
| [conopt](http://www.conopt.com/)                                                                    | pyomo                                               | -             |
| [cplex](https://www.ibm.com/products/ilog-cplex-optimization-studio/cplex-optimizer)                | cplex, cvxpy, linopy, ortools, picos, pulp, pyomo   | -             |
| [ecos](https://github.com/embotech/ecos)                                                            | cvxpy, picos                                        | -             |
| [glpk](https://www.gnu.org/software/glpk/)                                                          | cvxpy, linopy, ortools, picos, pulp, pymprog, pyomo | pymprog       |
| [gurobi](https://www.gurobi.com/downloads/)                                                         | cvxpy, gurobi, linopy, ortools, picos, pulp, pyomo  | -             |
| [highs](https://ergo-code.github.io/HiGHS/get-started#Precompiled-executables)                      | cvxpy, linopy, pyomo , pulp                         | -             |
| [ipopt](https://www.coin-or.org/download/binary/Ipopt/)                                             | gekko, pyomo                                        | gekko         |
| [mindtpy](https://github.com/Pyomo/pyomo/blob/main/doc/OnlineDocs/contributed_packages/mindtpy.rst) | pyomo                                               | -             |
| [mipcl](https://doaj.org/article/8eaf186ae79f4ccfb8b6a9548ba350fa)                                  | pulp                                                | -             |
| [mosek](https://www.mosek.com/downloads/)                                                           | cvxpy, picos, pulp, pyomo                           | -             |
| [nag](https://www.nag.com/content/software-downloads)                                               | cvxpy                                               | -             |
| [osqp](https://github.com/osqp/osqp)                                                                | cvxpy                                               | -             |
| [osqp](https://osqp.org/docs/get_started/)                                                          | picos                                               | -             |
| [path](https://pages.cs.wisc.edu/~ferris/path.html)                                                 | pyomo                                               | -             |
| [scip](https://scipopt.org/download.php?fname=scip-2.1.1.win.x86_64.vc10.opt.spx.lib)               | cvxpy, ortools, picos, pulp, pyomo                  | ortools       |
| [scs](https://github.com/cvxgrp/scs)                                                                | cvxpy                                               | -             |
| [smcp](https://smcp.readthedocs.io/en/latest/)                                                      | picos                                               | -             |
| [trustregion](https://optimization.mccormick.northwestern.edu/index.php/Trust-region_methods)       | pyomo                                               | -             |
| [xpress](https://www.fico.com/en/products/fico-xpress-solver)                                       | cvxpy, linopy, xpress                               | -             |
| bonmin_online                                                                                       | pyomo                                               | neos(online)  |
| bop                                                                                                 | ortools                                             | ortools       |
| bpopt                                                                                               | gekko                                               | gekko         |
| cbc_online                                                                                          | pyomo                                               | neos(online)  |
| clarabel                                                                                            | cvxpy                                               | -             |
| coinmp_dll                                                                                          | pulp                                                | -             |
| conopt_online                                                                                       | pyomo                                               | neos(online)  |
| copt                                                                                                | cvxpy                                               | -             |
| couenne_online                                                                                      | pyomo                                               | neos(online)  |
| cplex_direct                                                                                        | pyomo                                               | pyomo(online) |
| cplex_online                                                                                        | pyomo                                               | neos(online)  |
| cplex_persistent                                                                                    | pyomo                                               | -             |
| cplex_py                                                                                            | pulp                                                | -             |
| cplex\_                                                                                             | ortools                                             | -             |
| cvxopt                                                                                              | cvxpy, picos                                        | -             |
| cyipop                                                                                              | pyomo                                               | -             |
| filmint_online                                                                                      | pyomo                                               | neos(online)  |
| filter_online                                                                                       | pyomo                                               | neos(online)  |
| gams                                                                                                | pyomo                                               | -             |
| gdopt                                                                                               | pyomo                                               | -             |
| gdopt.gloa                                                                                          | pyomo                                               | -             |
| gdopt.lbb                                                                                           | pyomo                                               | -             |
| gdpopt.loa                                                                                          | pyomo                                               | -             |
| gdpopt.ric                                                                                          | pyomo                                               | -             |
| glop                                                                                                | cvxpy, ortools                                      | ortools       |
| glpk_mi                                                                                             | cvxpy                                               | -             |
| glpk\_                                                                                              | ortools                                             | -             |
| gurobi_cmd                                                                                          | pulp                                                | -             |
| gurobi_direct                                                                                       | pyomo                                               | pyomo(online) |
| gurobi_persistent                                                                                   | pyomo                                               | -             |
| gurobi\_                                                                                            | ortools                                             | -             |
| ipopt_online                                                                                        | pyomo                                               | neos(online)  |
| knitro_online                                                                                       | pyomo                                               | neos(online)  |
| l-bfgs-b_online                                                                                     | pyomo                                               | neos(online)  |
| lancelot_online                                                                                     | pyomo                                               | neos(online)  |
| lgo_online                                                                                          | pyomo                                               | neos(online)  |
| loqo_online                                                                                         | pyomo                                               | neos(online)  |
| minlp_online                                                                                        | pyomo                                               | neos(online)  |
| minos_online                                                                                        | pyomo                                               | neos(online)  |
| minto_online                                                                                        | pyomo                                               | neos(online)  |
| mosek_direct                                                                                        | pyomo                                               | pyomo(online) |
| mosek_online                                                                                        | pyomo                                               | neos(online)  |
| mosek_persistent                                                                                    | pyomo                                               | -             |
| mpec_minlp                                                                                          | pyomo                                               | -             |
| mpec_nlp                                                                                            | pyomo                                               | -             |
| mskfsn                                                                                              | picos                                               | -             |
| multistart                                                                                          | pyomo                                               | -             |
| octeract_online                                                                                     | pyomo                                               | neos(online)  |
| ooqp_online                                                                                         | pyomo                                               | neos(online)  |
| path_online                                                                                         | pyomo                                               | neos(online)  |
| pdlp                                                                                                | cvxpy                                               | -             |
| proxqp                                                                                              | cvxpy                                               | -             |
| pyglpk                                                                                              | pulp                                                | -             |
| raposa_online                                                                                       | pyomo                                               | neos(online)  |
| sat                                                                                                 | ortools                                             | ortools       |
| scipy                                                                                               | cvxpy                                               | -             |
| snopt_online                                                                                        | pyomo                                               | neos(online)  |
| xpress_direct                                                                                       | pyomo                                               | pyomo(online) |
| xpress_persistent                                                                                   | pyomo                                               | -             |
| xpress\_                                                                                            | ortools, pulp                                       | -             |


Source: The author.

# Heuristic Solvers

| FelooPy Algorithms     | Class | Solver |
| ---------------------- | ----- | ------ |
| Genetic Algorithm      | GA    | GA     |
| Simulated Annealing    | SA    | SA     |
| Tabu Search            | TS    | TS     |
| Differential Evolution | DE    | DE     |
| Grey Wolf Optimizer    | GWO   | GWO    |

Source: The author.

| MealPy Algorithms                               | Class    | Solver           |
| ----------------------------------------------- | -------- | ---------------- |
| Evolutionary Programming                        | EP       | OriginalEP       |
| \-                                              | \-       | LevyEP           |
| Evolution Strategies                            | ES       | OriginalES       |
| \-                                              | \-       | LevyES           |
| Memetic Algorithm                               | MA       | OriginalMA       |
| Genetic Algorithm                               | GA       | BaseGA           |
| \-                                              | \-       | SingleGA         |
| \-                                              | \-       | MultiGA          |
| \-                                              | \-       | EliteSingleGA    |
| \-                                              | \-       | EliteMultiGA     |
| Differential Evolution                          | DE       | BaseDE           |
| \-                                              | \-       | JADE             |
| \-                                              | \-       | SADE             |
| \-                                              | \-       | SHADE            |
| \-                                              | \-       | L_SHADE          |
| \-                                              | \-       | SAP_DE           |
| Flower Pollination Algorithm                    | FPA      | OriginalFPA      |
| Coral Reefs Optimization                        | CRO      | OriginalCRO      |
| \-                                              | \-       | OCRO             |
| Particle Swarm Optimization                     | PSO      | OriginalPSO      |
| \-                                              | \-       | PPSO             |
| \-                                              | \-       | HPSO_TVAC        |
| \-                                              | \-       | C_PSO            |
| \-                                              | \-       | CL_PSO           |
| Bacterial Foraging Optimization                 | BFO      | OriginalBFO      |
| \-                                              | \-       | ABFO             |
| Bees Algorithm                                  | BeesA    | OriginalBeesA    |
| \-                                              | \-       | ProbBeesA        |
| Cat Swarm Optimization                          | CSO      | OriginalCSO      |
| Artificial Bee Colony                           | ABC      | OriginalABC      |
| Ant Colony Optimization                         | ACO-R    | OriginalACOR     |
| Cuckoo Search Algorithm                         | CSA      | OriginalCSA      |
| Firefly Algorithm                               | FFA      | OriginalFFA      |
| Fireworks Algorithm                             | FA       | OriginalFA       |
| Bat Algorithm                                   | BA       | OriginalBA       |
| \-                                              | \-       | AdaptiveBA       |
| \-                                              | \-       | ModifiedBA       |
| Fruit-fly Optimization Algorithm                | FOA      | OriginalFOA      |
| \-                                              | \-       | BaseFOA          |
| \-                                              | \-       | WhaleFOA         |
| Social Spider Optimization                      | SSpiderO | OriginalSSpiderO |
| Grey Wolf Optimizer                             | GWO      | OriginalGWO      |
| \-                                              | \-       | RW_GWO           |
| Social Spider Algorithm                         | SSpiderA | OriginalSSpiderA |
| Ant Lion Optimizer                              | ALO      | OriginalALO      |
| \-                                              | \-       | BaseALO          |
| Moth Flame Optimization                         | MFO      | OriginalMFO      |
| \-                                              | \-       | BaseMFO          |
| Elephant Herding Optimization                   | EHO      | OriginalEHO      |
| Jaya Algorithm                                  | JA       | OriginalJA       |
| \-                                              | \-       | BaseJA           |
| \-                                              | \-       | LevyJA           |
| Whale Optimization Algorithm                    | WOA      | OriginalWOA      |
| \-                                              | \-       | HI_WOA           |
| Dragonfly Optimization                          | DO       | OriginalDO       |
| Bird Swarm Algorithm                            | BSA      | OriginalBSA      |
| Spotted Hyena Optimizer                         | SHO      | OriginalSHO      |
| Salp Swarm Optimization                         | SSO      | OriginalSSO      |
| Swarm Robotics Search And Rescue                | SRSR     | OriginalSRSR     |
| Grasshopper Optimisation Algorithm              | GOA      | OriginalGOA      |
| Coyote Optimization Algorithm                   | COA      | OriginalCOA      |
| Moth Search Algorithm                           | MSA      | OriginalMSA      |
| Sea Lion Optimization                           | SLO      | OriginalSLO      |
| \-                                              | \-       | ModifiedSLO      |
| \-                                              | \-       | ImprovedSLO      |
| Nake Mole-Rat Algorithm                         | NMRA     | OriginalNMRA     |
| \-                                              | \-       | ImprovedNMRA     |
| Pathfinder Algorithm                            | PFA      | OriginalPFA      |
| Sailfish Optimizer                              | SFO      | OriginalSFO      |
| \-                                              | \-       | ImprovedSFO      |
| Harris Hawks Optimization                       | HHO      | OriginalHHO      |
| Manta Ray Foraging Optimization                 | MRFO     | OriginalMRFO     |
| Bald Eagle Search                               | BES      | OriginalBES      |
| Sparrow Search Algorithm                        | SSA      | OriginalSSA      |
| \-                                              | \-       | BaseSSA          |
| Hunger Games Search                             | HGS      | OriginalHGS      |
| Aquila Optimizer                                | AO       | OriginalAO       |
| Hybrid Grey Wolf - Whale Optimization Algorithm | GWO      | GWO_WOA          |
| Marine Predators Algorithm                      | MPA      | OriginalMPA      |
| Honey Badger Algorithm                          | HBA      | OriginalHBA      |
| Sand Cat Swarm Optimization                     | SCSO     | OriginalSCSO     |
| Tuna Swarm Optimization                         | TSO      | OriginalTSO      |
| African Vultures Optimization Algorithm         | AVOA     | OriginalAVOA     |
| Artificial Gorilla Troops Optimization          | AGTO     | OriginalAGTO     |
| Artificial Rabbits Optimization                 | ARO      | OriginalARO      |
| Simulated Annealling                            | SA       | OriginalSA       |
| Wind Driven Optimization                        | WDO      | OriginalWDO      |
| Multi-Verse Optimizer                           | MVO      | OriginalMVO      |
| \-                                              | \-       | BaseMVO          |
| Tug of War Optimization                         | TWO      | OriginalTWO      |
| \-                                              | \-       | OppoTWO          |
| \-                                              | \-       | LevyTWO          |
| \-                                              | \-       | EnhancedTWO      |
| Electromagnetic Field Optimization              | EFO      | OriginalEFO      |
| \-                                              | \-       | BaseEFO          |
| Nuclear Reaction Optimization                   | NRO      | OriginalNRO      |
| Henry Gas Solubility Optimization               | HGSO     | OriginalHGSO     |
| Atom Search Optimization                        | ASO      | OriginalASO      |
| Equilibrium Optimizer                           | EO       | OriginalEO       |
| \-                                              | \-       | ModifiedEO       |
| \-                                              | \-       | AdaptiveEO       |
| Archimedes Optimization Algorithm               | ArchOA   | OriginalArchOA   |
| Culture Algorithm                               | CA       | OriginalCA       |
| Imperialist Competitive Algorithm               | ICA      | OriginalICA      |
| Teaching Learning-based Optimization            | TLO      | OriginalTLO      |
| \-                                              | \-       | BaseTLO          |
| \-                                              | \-       | ITLO             |
| Brain Storm Optimization                        | BSO      | OriginalBSO      |
| \-                                              | \-       | ImprovedBSO      |
| Queuing Search Algorithm                        | QSA      | OriginalQSA      |
| \-                                              | \-       | BaseQSA          |
| \-                                              | \-       | OppoQSA          |
| \-                                              | \-       | LevyQSA          |
| \-                                              | \-       | ImprovedQSA      |
| Search And Rescue Optimization                  | SARO     | OriginalSARO     |
| \-                                              | \-       | BaseSARO         |
| Life Choice-Based Optimization                  | LCO      | OriginalLCO      |
| \-                                              | \-       | BaseLCO          |
| \-                                              | \-       | ImprovedLCO      |
| Social Ski-Driver Optimization                  | SSDO     | OriginalSSDO     |
| Gaining Sharing Knowledge-based Algorithm       | GSKA     | OriginalGSKA     |
| \-                                              | \-       | BaseGSKA         |
| Coronavirus Herd Immunity Optimization          | CHIO     | OriginalCHIO     |
| \-                                              | \-       | BaseCHIO         |
| Forensic-Based Investigation Optimization       | FBIO     | OriginalFBIO     |
| \-                                              | \-       | BaseFBIO         |
| Battle Royale Optimization                      | BRO      | OriginalBRO      |
| \-                                              | \-       | BaseBRO          |
| Student Psychology Based Optimization           | SPBO     | OriginalSPBO     |
| \-                                              | \-       | DevSPBO          |
| Dwarf Mongoose Optimization Algorithm           | DMOA     | OriginalDMOA     |
| \-                                              | \-       | DevDMOA          |
| Invasive Weed Optimization                      | IWO      | OriginalIWO      |
| Biogeography-Based Optimization                 | BBO      | OriginalBBO      |
| \-                                              | \-       | BaseBBO          |
| Virus Colony Search                             | VCS      | OriginalVCS      |
| \-                                              | \-       | BaseVCS          |
| Satin Bowerbird Optimizer                       | SBO      | OriginalSBO      |
| \-                                              | \-       | BaseSBO          |
| Earthworm Optimisation Algorithm                | EOA      | OriginalEOA      |
| Wildebeest Herd Optimization                    | WHO      | OriginalWHO      |
| Slime Mould Algorithm                           | SMA      | OriginalSMA      |
| \-                                              | \-       | BaseSMA          |
| Barnacles Mating Optimizer                      | BMO      | OriginalBMO      |
| Tunicate Swarm Algorithm                        | TSA      | OriginalTSA      |
| Symbiotic Organisms Search                      | SOS      | OriginalSOS      |
| Seagull Optimization Algorithm                  | SOA      | OriginalSOA      |
| \-                                              | \-       | DevSOA           |
| Germinal Center Optimization                    | GCO      | OriginalGCO      |
| \-                                              | \-       | BaseGCO          |
| Water Cycle Algorithm                           | WCA      | OriginalWCA      |
| Artificial Ecosystem-based Optimization         | AEO      | OriginalAEO      |
| \-                                              | \-       | EnhancedAEO      |
| \-                                              | \-       | ModifiedAEO      |
| \-                                              | \-       | ImprovedAEO      |
| \-                                              | \-       | AdaptiveAEO      |
| Hill Climbing                                   | HC       | OriginalHC       |
| \-                                              | \-       | SwarmHC          |
| Cross-Entropy Method                            | CEM      | OriginalCEM      |
| Sine Cosine Algorithm                           | SCA      | OriginalSCA      |
| \-                                              | \-       | BaseSCA          |
| Gradient-Based Optimizer                        | GBO      | OriginalGBO      |
| Arithmetic Optimization Algorithm               | AOA      | OrginalAOA       |
| Chaos Game Optimization                         | CGO      | OriginalCGO      |
| Pareto-like Sequential Sampling                 | PSS      | OriginalPSS      |
| weIghted meaN oF vectOrs                        | INFO     | OriginalINFO     |
| RUNge Kutta optimizer                           | RUN      | OriginalRUN      |
| Circle Search Algorithm                         | CircleSA | OriginalCircleSA |
| Harmony Search                                  | HS       | OriginalHS       |
| \-                                              | \-       | BaseHS           |

Source: <https://github.com/thieu1995/mealpy>
