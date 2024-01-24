# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

def generate_model(solver_name, solver_options):

    module_mappings = {

        # Evolution-Inspired Heuristic Optimization Algorithms
        'orig-ep': ('mealpy.evolutionary_based', 'EP', 'OriginalEP'),
        'levy-ep': ('mealpy.evolutionary_based', 'EP', 'LevyEP'),
        'orig-es': ('mealpy.evolutionary_based', 'ES', 'OriginalES'),
        'levy-es': ('mealpy.evolutionary_based', 'ES', 'LevyES'),
        'orig-ma': ('mealpy.evolutionary_based', 'MA', 'OriginalMA'),

        # Evolutionary MealPy GA
        'base-ga': ('mealpy.evolutionary_based', 'GA', 'BaseGA'),
        'single-ga': ('mealpy.evolutionary_based', 'GA', 'SingleGA'),
        'multi-ga': ('mealpy.evolutionary_based', 'GA', 'MultiGA'),
        'elite-single-ga': ('mealpy.evolutionary_based', 'GA', 'EliteSingleGA'),
        'elite-multi-ga': ('mealpy.evolutionary_based', 'GA', 'EliteMultiGA'),

        'base-de': ('mealpy.evolutionary_based', 'DE', 'BaseDE'),
        'ja-de': ('mealpy.evolutionary_based', 'DE', 'JADE'),
        'sa-de': ('mealpy.evolutionary_based', 'DE', 'SADE'),
        'sha-de': ('mealpy.evolutionary_based', 'DE', 'SHADE'),
        'l-sha-de': ('mealpy.evolutionary_based', 'DE', 'L_SHADE'),
        'sap-de': ('mealpy.evolutionary_based', 'DE', 'SAP_DE'),
        'orig-fpa': ('mealpy.evolutionary_based', 'FPA', 'OriginalFPA'),
        'orig-cro': ('mealpy.evolutionary_based', 'CRO', 'OriginalCRO'),
        'o-cro': ('mealpy.evolutionary_based', 'CRO', 'OCRO'),
        'cma-es': ('mealpy.evolutionary_based', 'ES', 'CMA_ES'),
        'simp-cma-es': ('mealpy.evolutionary_based', 'ES', 'Simple_CMA_ES'),

        # Swarm-Inspired Heuristic Optimization Algorithms

        # Swarm MealPy PSO
        'orig-pso': ('mealpy.swarm_based', 'PSO', 'OriginalPSO'),
        'ldw-pso': ('mealpy.swarm_based', 'PSO', 'LDW_PSO'),
        'aiw-pso': ('mealpy.swarm_based', 'PSO', 'AIW_PSO'),
        'p-pso': ('mealpy.swarm_based', 'PSO', 'P_PSO'),
        'h-pso-tvac': ('mealpy.swarm_based', 'PSO', 'HPSO_TVAC'),
        'c-pso': ('mealpy.swarm_based', 'PSO', 'C_PSO'),
        'cl-pso': ('mealpy.swarm_based', 'PSO', 'CL_PSO'),


        'orig-bfo': ('mealpy.swarm_based', 'BFO', 'OriginalBFO'),
        'orig-beesa': ('mealpy.swarm_based', 'BeesA', 'OriginalBeesA'),
        'a-bfo': ('mealpy.swarm_based', 'BFO', 'OriginalBFO'),
        'prob-beesa': ('mealpy.swarm_based', 'BeesA', 'ProbBeesA'),
        'orig-cso': ('mealpy.swarm_based', 'CSO', 'OriginalCSO'),

        # Swarm MealPy ABC
        'orig-abc': ('mealpy.swarm_based', 'ABC', 'OriginalABC'),

        'orig-acor': ('mealpy.swarm_based', 'ACOR', 'OriginalACOR'),
        'orig-csa': ('mealpy.swarm_based', 'CSA', 'OriginalCSA'),
        'orig-ffa': ('mealpy.swarm_based', 'FFA', 'OriginalFFA'),
        'orig-fa': ('mealpy.swarm_based', 'FA', 'OriginalFA'),
        'orig-ba': ('mealpy.swarm_based', 'BA', 'OriginalBA'),
        'adap-ba': ('mealpy.swarm_based', 'BA', 'AdaptiveBA'),
        'modi-ba': ('mealpy.swarm_based', 'BA', 'ModifiedBA'),
        'orig-foa': ('mealpy.swarm_based', 'FOA', 'OriginalFOA'),
        'base-foa': ('mealpy.swarm_based', 'FOA', 'BaseFOA'),
        'whale-foa': ('mealpy.swarm_based', 'FOA', 'WhaleFOA'),
        'orig-sspidero': ('mealpy.swarm_based', 'SSpiderO', 'OriginalSSpiderO'),
        'orig-gwo': ('mealpy.swarm_based', 'GWO', 'OriginalGWO'),
        'impr-gwo': ('mealpy.swarm_based', 'GWO', 'IGWO'),
        'rw-gwo': ('mealpy.swarm_based', 'GWO', 'RW_GWO'),
        'orig-sspidera': ('mealpy.swarm_based', 'SSpiderA', 'OriginalSSpiderA'),
        'orig-alo': ('mealpy.swarm_based', 'ALO', 'OriginalALO'),
        'dev-alo': ('mealpy.swarm_based', 'ALO', 'DevALO'),
        'base-alo': ('mealpy.swarm_based', 'ALO', 'BaseALO'),
        'orig-mfo': ('mealpy.swarm_based', 'MFO', 'OriginalMFO'),
        'base-mfo': ('mealpy.swarm_based', 'MFO', 'BaseMFO'),
        'orig-eho': ('mealpy.swarm_based', 'EHO', 'OriginalEHO'),
        'orig-ja': ('mealpy.swarm_based', 'JA', 'OriginalJA'),
        'base-ja': ('mealpy.swarm_based', 'JA', 'BaseJA'),
        'levy-ja': ('mealpy.swarm_based', 'JA', 'LevyJA'),
        'orig-woa': ('mealpy.swarm_based', 'WOA', 'OriginalWOA'),
        'hi-woa': ('mealpy.swarm_based', 'WOA', 'HI_WOA'),
        'orig-do': ('mealpy.swarm_based', 'DO', 'OriginalDO'),
        'orig-bsa': ('mealpy.swarm_based', 'BSA', 'OriginalBSA'),
        'orig-sho': ('mealpy.swarm_based', 'SHO', 'OriginalSHO'),
        'orig-sso': ('mealpy.swarm_based', 'SSO', 'OriginalSSO'),
        'orig-srsr': ('mealpy.swarm_based', 'SRSR', 'OriginalSRSR'),
        'orig-goa': ('mealpy.swarm_based', 'GOA', 'OriginalGOA'),
        'orig-coa': ('mealpy.swarm_based', 'COA', 'OriginalCOA'),
        'orig-msa': ('mealpy.swarm_based', 'MSA', 'OriginalMSA'),
        'orig-slo': ('mealpy.swarm_based', 'SLO', 'OriginalSLO'),
        'modi-slo': ('mealpy.swarm_based', 'SLO', 'ModifiedSLO'),
        'impr-slo': ('mealpy.swarm_based', 'SLO', 'ImprovedSLO'),
        'orig-nmra': ('mealpy.swarm_based', 'NMRA', 'OriginalNMRA'),
        'impr-nmra': ('mealpy.swarm_based', 'NMRA', 'ImprovedNMRA'),
        'orig-pfa': ('mealpy.swarm_based', 'PFA', 'OriginalPFA'),
        'orig-sfo': ('mealpy.swarm_based', 'SFO', 'OriginalSFO'),
        'impr-sfo': ('mealpy.swarm_based', 'SFO', 'ImprovedSFO'),
        'orig-hho': ('mealpy.swarm_based', 'HHO', 'OriginalHHO'),
        'orig-mrfo': ('mealpy.swarm_based', 'MRFO', 'OriginalMRFO'),
        'orig-bes': ('mealpy.swarm_based', 'BES', 'OriginalBES'),
        'orig-ssa': ('mealpy.swarm_based', 'SSA', 'OriginalSSA'),
        'base-ssa': ('mealpy.swarm_based', 'SSA', 'BaseSSA'),
        'orig-hgs': ('mealpy.swarm_based', 'HGS', 'OriginalHGS'),
        'orig-ao': ('mealpy.swarm_based', 'AO', 'OriginalAO'),
        'gwo-woa': ('mealpy.swarm_based', 'GWO', 'GWO_WOA'),
        'orig-mpa': ('mealpy.swarm_based', 'MPA', 'OriginalMPA'),
        'orig-hba': ('mealpy.swarm_based', 'HBA', 'OriginalHBA'),
        'orig-scso': ('mealpy.swarm_based', 'SCSO', 'OriginalSCSO'),
        'orig-tso': ('mealpy.swarm_based', 'TSO', 'OriginalTSO'),
        'orig-avoa': ('mealpy.swarm_based', 'AVOA', 'OriginalAVOA'),


        'orig-agto': ('mealpy.swarm_based', 'AGTO', 'OriginalAGTO'),
        'mgto': ('mealpy.swarm_based', 'AGTO', 'MGTO'),

        'orig-aro': ('mealpy.swarm_based', 'ARO', 'OriginalARO'),
        'levy-aro': ('mealpy.swarm_based', 'ARO', 'LARO'),
        'selec-aro': ('mealpy.swarm_based', 'ARO', 'IARO'),
        'wmqi-mrfo': ('mealpy.swarm_based', 'MRFO', 'WMQIMRFO'),
        'orig-esoa': ('mealpy.swarm_based', 'ESOA', 'OriginalESOA'),
        'sea-ho': ('mealpy.swarm_based', 'SeaHO', 'OriginalSeaHO'),
        'orig-mgo': ('mealpy.swarm_based', 'MGO', 'OriginalMGO'),
        'orig-gjo': ('mealpy.swarm_based', 'GJO', 'OriginalGJO'),
        'orig-fox': ('mealpy.swarm_based', 'FOX', 'OriginalFOX'),
        'orig-gto': ('mealpy.swarm_based', 'GTO', 'OriginalGTO'),
        'modi101-gto': ('mealpy.swarm_based', 'GTO', 'Matlab101GTO'),
        'modi102-gto': ('mealpy.swarm_based', 'GTO', 'Matlab102GTO'),

        # Physics-Inspired Heuristic Optimization Algorithms
        
        'orig-sa': ('mealpy.physics_based', 'SA', 'OriginalSA'),
        'orig-wdo': ('mealpy.physics_based', 'WDO', 'OriginalWDO'),
        'orig-mvo': ('mealpy.physics_based', 'MVO', 'OriginalMVO'),
        'base-mvo': ('mealpy.physics_based', 'MVO', 'BaseMVO'),
        'orig-two': ('mealpy.physics_based', 'TWO', 'OriginalTWO'),
        'oppo-two': ('mealpy.physics_based', 'TWO', 'OppoTWO'),
        'levy-two': ('mealpy.physics_based', 'TWO', 'LevyTWO'),
        'enha-two': ('mealpy.physics_based', 'TWO', 'EnhancedTWO'),
        'orig-efo': ('mealpy.physics_based', 'EFO', 'OriginalEFO'),
        'base-efo': ('mealpy.physics_based', 'EFO', 'BaseEFO'),
        'orig-nro': ('mealpy.physics_based', 'NRO', 'OriginalNRO'),
        'orig-hgso': ('mealpy.physics_based', 'HGSO', 'OriginalHGSO'),
        'orig-aso': ('mealpy.physics_based', 'ASO', 'OriginalASO'),
        'orig-eo': ('mealpy.physics_based', 'EO', 'OriginalEO'),
        'modi-eo': ('mealpy.physics_based', 'EO', 'ModifiedEO'),
        'adap-eo': ('mealpy.physics_based', 'EO', 'AdaptiveEO'),
        'orig-archoa': ('mealpy.physics_based', 'ArchOA', 'OriginalArchOA'),
        'orig-rime': ('mealpy.physics_based', 'RIME', 'OriginalRIME'),
        'orig-evo': ('mealpy.physics_based', 'EVO', 'OriginalEVO'),
        'orig-cdo': ('mealpy.physics_based', 'CDO', 'OriginalCDO'),
        'orig-fla': ('mealpy.physics_based', 'FLA', 'OriginalFLA'),

        # Human-Inspired Heuristic Optimization Algorithms

        'orig-ca': ('mealpy.human_based', 'CA', 'OriginalCA'),
        'orig-ica': ('mealpy.human_based', 'ICA', 'OriginalICA'),
        'orig-tlo': ('mealpy.human_based', 'TLO', 'OriginalTLO'),
        'base-tlo': ('mealpy.human_based', 'TLO', 'BaseTLO'),
        'itlo': ('mealpy.human_based', 'TLO', 'ImprovedTLO'),
        'orig-bso': ('mealpy.human_based', 'BSO', 'OriginalBSO'),
        'impr-bso': ('mealpy.human_based', 'BSO', 'ImprovedBSO'),
        'orig-qsa': ('mealpy.human_based', 'QSA', 'OriginalQSA'),
        'base-qsa': ('mealpy.human_based', 'QSA', 'BaseQSA'),
        'oppo-qsa': ('mealpy.human_based', 'QSA', 'OppoQSA'),
        'levy-qsa': ('mealpy.human_based', 'QSA', 'LevyQSA'),
        'impr-qsa': ('mealpy.human_based', 'QSA', 'ImprovedQSA'),
        'orig-saro': ('mealpy.human_based', 'SARO', 'OriginalSARO'),
        'base-saro': ('mealpy.human_based', 'SARO', 'BaseSARO'),
        'orig-lco': ('mealpy.human_based', 'LCO', 'OriginalLCO'),
        'base-lco': ('mealpy.human_based', 'LCO', 'BaseLCO'),
        'impr-lco': ('mealpy.human_based', 'LCO', 'ImprovedLCO'),
        'orig-ssdo': ('mealpy.human_based', 'SSDO', 'OriginalSSDO'),
        'orig-gska': ('mealpy.human_based', 'GSKA', 'OriginalGSKA'),
        'base-gska': ('mealpy.human_based', 'GSKA', 'BaseGSKA'),
        'orig-chio': ('mealpy.human_based', 'CHIO', 'OriginalCHIO'),
        'base-chio': ('mealpy.human_based', 'CHIO', 'BaseCHIO'),
        'orig-fbio': ('mealpy.human_based', 'FBIO', 'OriginalFBIO'),
        'base-fbio': ('mealpy.human_based', 'FBIO', 'BaseFBIO'),
        'orig-bro': ('mealpy.human_based', 'BRO', 'OriginalBRO'),
        'base-bro': ('mealpy.human_based', 'BRO', 'BaseBRO'),
        'orig-spbo': ('mealpy.human_based', 'SPBO', 'OriginalSPBO'),
        'dev-spbo': ('mealpy.human_based', 'SPBO', 'DevSPBO'),
        'orig-dmoa': ('mealpy.human_based', 'SPBO', 'DevSPBO'),
        'dev-dmoa': ('mealpy.human_based', 'SPBO', 'DevSPBO'),
        'orig-huco': ('mealpy.human_based', 'HCO', 'OriginalHCO'),
        'orig-warso': ('mealpy.human_based', 'WarSO', 'OriginalWarSO'),
        'orig-hbo': ('mealpy.human_based', 'HBO', 'OriginalHBO'),

        # Bio-Inspired Heuristic Optimization Algorithms

        'orig-iwo': ('mealpy.bio_based', 'IWO', 'OriginalIWO'),
        'orig-bbo': ('mealpy.bio_based', 'BBO', 'OriginalBBO'),
        'base-bbo': ('mealpy.bio_based', 'BBO', 'BaseBBO'),
        'orig-vcs': ('mealpy.bio_based', 'VCS', 'OriginalVCS'),
        'base-vcs': ('mealpy.bio_based', 'VCS', 'BaseVCS'),
        'orig-sbo': ('mealpy.bio_based', 'SBO', 'OriginalSBO'),
        'base-sbo': ('mealpy.bio_based', 'SBO', 'BaseSBO'),
        'orig-eoa': ('mealpy.bio_based', 'EOA', 'OriginalEOA'),
        'orig-who': ('mealpy.bio_based', 'WHO', 'OriginalWHO'),
        'orig-sma': ('mealpy.bio_based', 'SMA', 'OriginalSMA'),
        'base-sma': ('mealpy.bio_based', 'SMA', 'BaseSMA'),
        'orig-bmo': ('mealpy.bio_based', 'BMO', 'OriginalBMO'),
        'orig-tsa': ('mealpy.bio_based', 'TSA', 'OriginalTSA'),
        'orig-sos': ('mealpy.bio_based', 'SOS', 'OriginalSOS'),
        'orig-soa': ('mealpy.bio_based', 'SOA', 'OriginalSOA'),
        'dev-soa': ('mealpy.bio_based', 'SOA', 'DevSOA'),

        # System-Inspired Heuristic Optimization Algorithms

        'orig-gco': ('mealpy.system_based', 'GCO', 'OriginalGCO'),
        'base-gco': ('mealpy.system_based', 'GCO', 'BaseGCO'),
        'orig-wca': ('mealpy.system_based', 'WCA', 'OriginalWCA'),
        'orig-aeo': ('mealpy.system_based', 'AEO', 'OriginalAEO'),
        'enha-aeo': ('mealpy.system_based', 'AEO', 'EnhancedAEO'),
        'modi-aeo': ('mealpy.system_based', 'AEO', 'ModifiedAEO'),
        'impr-aeo': ('mealpy.system_based', 'AEO', 'ImprovedAEO'),
        'augm-aeo': ('mealpy.system_based', 'AEO', 'AugmentedAEO'),

        # Math-Inspired Heuristic Optimization Algorithms

        'orig-ts': ('mealpy.math_based', 'TS', 'OriginalTS'),
        'orig-hc': ('mealpy.math_based', 'HC', 'OriginalHC'),
        'swarm-hc': ('mealpy.math_based', 'HC', 'SwarmHC'),
        'orig-cem': ('mealpy.math_based', 'CEM', 'OriginalCEM'),
        'orig-sca': ('mealpy.math_based', 'SCA', 'OriginalSCA'),
        'base-sca': ('mealpy.math_based', 'SCA', 'BaseSCA'),
        'orig-beesa': ('mealpy.math_based', 'AOA', 'OriginalAOA'),
        'orig-cgo': ('mealpy.math_based', 'CGO', 'OriginalCGO'),
        'orig-gbo': ('mealpy.math_based', 'GBO', 'OriginalGBO'),
        'orig-info': ('mealpy.math_based', 'INFO', 'OriginalINFO'),
        'orig-pss': ('mealpy.math_based', 'PSS', 'OriginalPSS'),
        'orig-run': ('mealpy.math_based', 'RUN', 'OriginalRUN'),
        'orig-circle-sa': ('mealpy.math_based', 'CircleSA', 'OriginalCircleSA'),
        'ql-sca': ('mealpy.math_based', 'SCA', 'QleSCA'),
        'orig-shio': ('mealpy.math_based', 'SHIO', 'OriginalSHIO'),

        # Music-Inspired Heuristic Optimization Algorithms
        
        'orig-hs': ('mealpy.music_based', 'HS', 'OriginalHS'),
        'base-hs': ('mealpy.music_based', 'HS', 'BaseHS'),
    }

    module_name, class_name, model_name = module_mappings.get(solver_name, (None, None, None))

    if module_name and class_name and model_name:
    
        module = __import__(module_name, fromlist=[class_name])
        model_class = getattr(module, class_name)
        model_object = getattr(model_class, model_name)(**solver_options)

    else:
    
        raise ValueError("Invalid solver name. Please refer to https://feloopy.readthedocs.io/en/latest/heuristic.html")

    return model_object