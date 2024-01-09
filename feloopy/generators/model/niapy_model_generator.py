# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

def generate_model(solver_name, solver_options):

    module_mappings = {

        # Basic Heuristic Optimization Algorithms

        'base-abc': ('niapy.algorithms.basic', 'ArtificialBeeColonyAlgorithm'), #
        'base-ba': ('niapy.algorithms.basic', 'BatAlgorithm'), #
        'base-bea': ('niapy.algorithms.basic', 'BeesAlgorithm'), #
        'base-bfo': ('niapy.algorithms.basic', 'BacterialForagingOptimization'), #
        'base-ca': ('niapy.algorithms.basic', 'CamelAlgorithm'), #
        'base-clonalg': ('niapy.algorithms.basic', 'ClonalSelectionAlgorithm'), #
        'base-cro': ('niapy.algorithms.basic', 'CoralReefsOptimization'), #
        'base-cs': ('niapy.algorithms.basic', 'CuckooSearch'), #
        'base-cso': ('niapy.algorithms.basic', 'CatSwarmOptimization'), #
        'base-de': ('niapy.algorithms.basic', 'DifferentialEvolution'), #
        'base-dynnp-de' : ('niapy.algorithms.basic', 'DynNpDifferentialEvolution'), #
        'base-anp-de' : ('niapy.algorithms.basic','AgingNpDifferentialEvolution'), #
        'base-ms-de': ('niapy.algorithms.basic', 'MultiStrategyDifferentialEvolution'), #
        'base-dynnp-ms-de': ('niapy.algorithms.basic','DynNpMultiStrategyDifferentialEvolution'), #
        'base-1+1-es': ('niapy.algorithms.basic', 'EvolutionStrategy1p1'), #
        'base-m+1-es': ('niapy.algorithms.basic','EvolutionStrategyMp1'), #
        'base-m+l-es': ('niapy.algorithms.basic', 'EvolutionStrategyMpL'), #
        'base-m,l-es': ('niapy.algorithms.basic', 'EvolutionStrategyML'), #
        'base-fa': ('niapy.algorithms.basic', 'EvolutionStrategyML'), #
        'base-foa': ('niapy.algorithms.basic','ForestOptimizationAlgorithm'), #
        'base-fpa': ('niapy.algorithms.basic', 'FlowerPollinationAlgorithm'), #
        'base-fss': ('niapy.algorithms.basic', 'FishSchoolSearch'), #
        'base-bb-fwa': ('niapy.algorithms.basic', 'BareBonesFireworksAlgorithm'), #
        'base-fwa': ('niapy.algorithms.basic', 'FireworksAlgorithm'), #
        'base-e-fwa': ('niapy.algorithms.basic', 'EnhancedFireworksAlgorithm'), #
        'base-dyn-fwa-g': ('niapy.algorithms.basic','DynamicFireworksAlgorithmGauss'), #
        'base-dyn-fwa': ('niapy.algorithms.basic','DynamicFireworksAlgorithm'), #
        'base-ga': ('niapy.algorithms.basic', 'GeneticAlgorithm'), #
        'base-gsa': ('niapy.algorithms.basic', 'GravitationalSearchAlgorithm'), #
        'base-gso': ('niapy.algorithms.basic', 'GlowwormSwarmOptimization'), #
        'base-gso-v1': ('niapy.algorithms.basic', 'GlowwormSwarmOptimizationV1'), #
        'base-gso-v2': ('niapy.algorithms.basic', 'GlowwormSwarmOptimizationV2'), #
        'base-gso-v3': ('niapy.algorithms.basic', 'GlowwormSwarmOptimizationV3'), #
        'base-gwo': ('niapy.algorithms.basic', 'GreyWolfOptimizer'), #
        'base-hho': ('niapy.algorithms.basic', 'HarrisHawksOptimization'), #
        'base-hs': ('niapy.algorithms.basic', 'HarmonySearch'), #  
        'base-hs-v1': ('niapy.algorithms.basic', 'HarmonySearchV1'), #    
        'base-kh': ('niapy.algorithms.basic', 'KrillHerd'), #    
        'base-loa': ('niapy.algorithms.basic', 'LionOptimizationAlgorithm'), #
        'base-mbo': ('niapy.algorithms.basic', 'MonarchButterflyOptimization'), #
        'base-mfo': ('niapy.algorithms.basic','MothFlameOptimizer'), #
        'base-mke-v1': ('niapy.algorithms.basic','MonkeyKingEvolutionV1'), #
        'base-mke-v2': ('niapy.algorithms.basic','MonkeyKingEvolutionV2'), #
        'base-mke-v3': ('niapy.algorithms.basic','MonkeyKingEvolutionV3'), #
        'base-wvc-pso': ('niapy.algorithms.basic', 'WeightedVelocityClampingParticleSwarmAlgorithm'), #
        'base-pso': ('niapy.algorithms.basic', 'ParticleSwarmOptimization'), #
        'base-ovc-pso': ('niapy.algorithms.basic', 'OppositionVelocityClampingParticleSwarmOptimization'), #
        'base-c-pso': ('niapy.algorithms.basic', 'CenterParticleSwarmOptimization'), #
        'base-m-pso': ('niapy.algorithms.basic', 'MutatedParticleSwarmOptimization'), #
        'base-mc-pso': ('niapy.algorithms.basic', 'MutatedCenterParticleSwarmOptimization'), #
        'base-mcu-pso': ('niapy.algorithms.basic', 'MutatedCenterUnifiedParticleSwarmOptimization'), #
        'base-cl-pso': ('niapy.algorithms.basic', 'ComprehensiveLearningParticleSwarmOptimizer'), #
        'base-sca': ('niapy.algorithms.basic', 'SineCosineAlgorithm'),

        # Modified Heuristic Optimziation Algorithms

        'modi-h-ba': ('niapy.algorithms.modified', 'HybridBatAlgorithm'),
        'modi-de-mts': ('niapy.algorithms.modified', 'DifferentialEvolutionMTS'),
        'modi-de-mts-v1': ('niapy.algorithms.modified', 'DifferentialEvolutionMTSv1'),
        'modi-dynnp-de-mts': ('niapy.algorithms.modified', 'DynNpDifferentialEvolutionMTS'),
        'modi-dynnp-de-mts-v1': ('niapy.algorithms.modified', 'DynNpDifferentialEvolutionMTSv1'),
        'modi-ms-de-mts': ('niapy.algorithms.modified', 'MultiStrategyDifferentialEvolutionMTS'),
        'modi-ms-de-mts-v1': ('niapy.algorithms.modified', 'MultiStrategyDifferentialEvolutionMTSv1'),
        'modi-dynnp-ms-de-mts': ('niapy.algorithms.modified', 'DynNpMultiStrategyDifferentialEvolutionMTS'),
        'modi-dynnp-ms-de-mts-v1': ('niapy.algorithms.modified', 'DynNpMultiStrategyDifferentialEvolutionMTSv1'),
        'modi-sa-de': ('niapy.algorithms.modified', 'SelfAdaptiveDifferentialEvolution'),
        'modi-ms-sa-de': ('niapy.algorithms.modified', 'MultiStrategySelfAdaptiveDifferentialEvolution'),
        'modi-a-ba': ('niapy.algorithms.modified', 'AdaptiveBatAlgorithm'),
        'modi-sa-ba': ('niapy.algorithms.modified', 'SelfAdaptiveBatAlgorithm'),
        'modi-hsa-ba': ('niapy.algorithms.modified', 'HybridSelfAdaptiveBatAlgorithm'),
        'modi-pf-ba': ('niapy.algorithms.modified', 'ParameterFreeBatAlgorithm'),
        'modi-sh-a-de': ('niapy.algorithms.modified', 'SuccessHistoryAdaptiveDifferentialEvolution'),
        'modi-lpsr-sh-a-de': ('niapy.algorithms.modified', 'LpsrSuccessHistoryAdaptiveDifferentialEvolution'),

        # Other Heuristic Optimziation Algorithms:

        'other-nmm': ('niapy.algorithms.other', 'NelderMeadMethod'),
        'other-hc': ('niapy.algorithms.other', 'HillClimbAlgorithm'),
        'other-sa': ('niapy.algorithms.other', 'SimulatedAnnealing'),
        'other-mts': ('niapy.algorithms.other', 'MultipleTrajectorySearch'),
        'other-mts1': ('niapy.algorithms.other', 'MultipleTrajectorySearchV1'),
        'other-mts-ls1': ('niapy.algorithms.other', 'mts_ls1'),
        'other-mts-ls2': ('niapy.algorithms.other', 'mts_ls2'),
        'other-mts-ls3': ('niapy.algorithms.other', 'mts_ls3'),
        'other-mts-ls1v1': ('niapy.algorithms.other', 'mts_ls1v1'),
        'other-mts-ls3v1': ('niapy.algorithms.other', 'mts_ls3v1'),
        'other-aso': ('niapy.algorithms.other', 'AnarchicSocietyOptimization'),
        'other-rs': ('niapy.algorithms.other', 'RandomSearch')

    }

    module_name, model_class = module_mappings.get(solver_name, (None, None))


    if module_name and model_class:

        import importlib

        module = importlib.import_module(module_name)
        model_class = getattr(module, model_class)

        if solver_options.get('epoch',None) !=None or solver_options.get('max_evals',None) !=None:
            import numpy as np
            if solver_options.get('epoch',None) !=None: 
                hold = np.copy(solver_options['epoch'])
                del solver_options['epoch']
            if  solver_options.get('max_evals',None) !=None: 
                hold = np.copy(solver_options['max_evals'])
                del solver_options['max_evals']
            
        model_object = model_class(**solver_options)
        solver_options['epoch'] = np.copy(hold)

    else:
    
        raise ValueError("Invalid solver name. Please refer to https://feloopy.readthedocs.io/en/latest/heuristic.html")

    return model_object