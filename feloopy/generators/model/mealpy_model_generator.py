'''
 # @ Author: Keivan Tafakkori
 # @ Created: 2023-05-11
 # @ Modified: 2023-05-12
 # @ Contact: https://www.linkedin.com/in/keivan-tafakkori/
 # @ Github: https://github.com/ktafakkori
 # @ Website: https://ktafakkori.github.io/
 # @ Copyright: 2023. MIT License. All Rights Reserved.
 '''


def generate_model(solver_name, solver_options):

    match solver_name:

        # Evolution-Inspired Heuristic Optimization Algorithms

        case 'orig-ep':
            from mealpy.evolutionary_based import EP
            model_object = EP.OriginalEP(**solver_options)

        case 'levy-ep':
            from mealpy.evolutionary_based import EP
            model_object = EP.LevyEP(**solver_options)

        case 'orig-es':
            from mealpy.evolutionary_based import ES
            model_object = ES.OriginalES(**solver_options)

        case 'levy-es':
            from mealpy.evolutionary_based import ES
            model_object = ES.LevyES(**solver_options)

        case 'orig-ma':
            from mealpy.evolutionary_based import MA
            model_object = MA.OriginalMA(**solver_options)

        case 'base-ga':
            from mealpy.evolutionary_based import GA
            model_object = GA.BaseGA(**solver_options)

        case 'single-ga':
            from mealpy.evolutionary_based import GA
            model_object = GA.SingleGA(**solver_options)

        case 'multi-ga':
            from mealpy.evolutionary_based import GA
            model_object = GA.MultiGA(**solver_options)

        case 'elite-single-ga':
            from mealpy.evolutionary_based import GA
            model_object = GA.EliteSingleGA(**solver_options)

        case 'elite-multi-ga':
            from mealpy.evolutionary_based import GA
            model_object = GA.EliteMultiGA(**solver_options)

        case 'base-de':
            from mealpy.evolutionary_based import DE
            model_object = DE.BaseDE(**solver_options)

        case 'ja-de':
            from mealpy.evolutionary_based import DE
            model_object = DE.JADE(**solver_options)

        case 'sa-de':
            from mealpy.evolutionary_based import DE
            model_object = DE.SADE(**solver_options)

        case 'sha-de':
            from mealpy.evolutionary_based import DE
            model_object = DE.SHADE(**solver_options)

        case 'l-sha-de':
            from mealpy.evolutionary_based import DE
            model_object = DE.L_SHADE(**solver_options)

        case 'sap-de':
            from mealpy.evolutionary_based import DE
            model_object = DE.SAP_DE(**solver_options)

        case 'orig-fpa':
            from mealpy.evolutionary_based import FPA
            model_object = FPA.OriginalFPA(**solver_options)

        case 'orig-cro':
            from mealpy.evolutionary_based import CRO
            model_object = CRO.OriginalCRO(**solver_options)

        case 'o-cro':
            from mealpy.evolutionary_based import CRO
            model_object = CRO.OCRO(**solver_options)

        case 'cma-es':
            from mealpy.evolutionary_based import ES
            model_object = ES.CMA_ES(**solver_options)

        case 'simp-cma-es':
            from mealpy.evolutionary_based import ES
            model_object = ES.Simple_CMA_ES(**solver_options)

        # Swarm-Inspired Heuristic Optimization Algorithms

        case 'orig-pso':
            from mealpy.swarm_based import PSO
            model_object = PSO.OriginalPSO(**solver_options)

        case 'p-pso':
            from mealpy.swarm_based import PSO
            model_object = PSO.PPSO(**solver_options)

        case 'h-pso-tvac':
            from mealpy.swarm_based import PSO
            model_object = PSO.HPSO_TVAC(**solver_options)

        case 'c-pso':
            from mealpy.swarm_based import PSO
            model_object = PSO.C_PSO(**solver_options)

        case 'cl-pso':
            from mealpy.swarm_based import PSO
            model_object = PSO.CL_PSO(**solver_options)

        case 'orig-bfo':
            from mealpy.swarm_based import BFO
            model_object = BFO.OriginalBFO(**solver_options)

        case 'orig-beesa':
            from mealpy.swarm_based import BeesA
            model_object = BeesA.OriginalBeesA(**solver_options)

        case 'a-bfo':
            from mealpy.swarm_based import BFO
            model_object = BFO.OriginalBFO(**solver_options)

        case 'prob-beesa':
            from mealpy.swarm_based import BeesA
            model_object = BeesA.ProbBeesA(**solver_options)

        case 'orig-cso':
            from mealpy.swarm_based import CSO
            model_object = CSO.OriginalCSO(**solver_options)

        case 'orig-abc':
            from mealpy.swarm_based import ABC
            model_object = ABC.OriginalABC(**solver_options)

        case 'orig-acor':
            from mealpy.swarm_based import ACOR
            model_object = ACOR.orig_acor(**solver_options)

        case 'orig-csa':
            from mealpy.swarm_based import CSA
            model_object = CSA.OriginalCSA(**solver_options)

        case 'orig-ffa':
            from mealpy.swarm_based import FFA
            model_object = FFA.OriginalFFA(**solver_options)

        case 'orig-fa':
            from mealpy.swarm_based import FA
            model_object = FA.OriginalFA(**solver_options)

        case 'orig-ba':
            from mealpy.swarm_based import BA
            model_object = BA.OriginalBA(**solver_options)

        case 'adap-ba':
            from mealpy.swarm_based import BA
            model_object = BA.AdaptiveBA(**solver_options)

        case 'modi-ba':
            from mealpy.swarm_based import BA
            model_object = BA.ModifiedBA(**solver_options)

        case 'orig-foa':
            from mealpy.swarm_based import FOA
            model_object = FOA.OriginalFOA(**solver_options)

        case 'base-foa':
            from mealpy.swarm_based import FOA
            model_object = FOA.BaseFOA(**solver_options)

        case 'whale-foa':
            from mealpy.swarm_based import FOA
            model_object = FOA.WhaleFOA(**solver_options)

        case 'orig-sspidero':
            from mealpy.swarm_based import SSpiderO
            model_object = SSpiderO.OriginalSSpiderO(**solver_options)

        case 'orig-gwo':
            from mealpy.swarm_based import GWO
            model_object = GWO.OriginalGWO(**solver_options)

        case 'rw-gwo':
            from mealpy.swarm_based import GWO
            model_object = GWO.RW_GWO(**solver_options)

        case 'orig-sspidera':
            from mealpy.swarm_based import SSpiderA
            model_object = SSpiderA.OriginalSSpiderA(**solver_options)

        case 'orig-alo':
            from mealpy.swarm_based import ALO
            model_object = ALO.OriginalALO(**solver_options)

        case 'base-alo':
            from mealpy.swarm_based import ALO
            model_object = ALO.BaseALO(**solver_options)

        case 'orig-mfo':
            from mealpy.swarm_based import MFO
            model_object = MFO.OriginalMFO(**solver_options)

        case 'base-mfo':
            from mealpy.swarm_based import MFO
            model_object = MFO.BaseMFO(**solver_options)

        case 'orig-eho':
            from mealpy.swarm_based import EHO
            model_object = EHO.OriginalEHO(**solver_options)

        case 'orig-ja':
            from mealpy.swarm_based import JA
            model_object = JA.OriginalJA(**solver_options)

        case 'base-ja':
            from mealpy.swarm_based import JA
            model_object = JA.BaseJA(**solver_options)

        case 'levy-ja':
            from mealpy.swarm_based import JA
            model_object = JA.LevyJA(**solver_options)

        case 'orig-woa':
            from mealpy.swarm_based import WOA
            model_object = WOA.OriginalWOA(**solver_options)

        case 'hi-woa':
            from mealpy.swarm_based import WOA
            model_object = WOA.HI_WOA(**solver_options)

        case 'orig-do':
            from mealpy.swarm_based import DO
            model_object = DO.OriginalDO(**solver_options)

        case 'orig-bsa':
            from mealpy.swarm_based import BSA
            model_object = BSA.OriginalBSA(**solver_options)

        case 'orig-sho':
            from mealpy.swarm_based import SHO
            model_object = SHO.OriginalSHO(**solver_options)

        case 'orig-sso':
            from mealpy.swarm_based import SSO
            model_object = SSO.OriginalSSO(**solver_options)

        case 'orig-srsr':
            from mealpy.swarm_based import SRSR
            model_object = SRSR.OriginalSRSR(**solver_options)

        case 'orig-goa':
            from mealpy.swarm_based import GOA
            model_object = GOA.OriginalGOA(**solver_options)

        case 'orig-coa':
            from mealpy.swarm_based import COA
            model_object = COA.OriginalCOA(**solver_options)

        case 'orig-msa':
            from mealpy.swarm_based import MSA
            model_object = MSA.OriginalMSA(**solver_options)

        case 'orig-slo':
            from mealpy.swarm_based import SLO
            model_object = SLO.OriginalSLO(**solver_options)

        case 'modi-slo':
            from mealpy.swarm_based import SLO
            model_object = SLO.ModifiedSLO(**solver_options)

        case 'impr-slo':
            from mealpy.swarm_based import SLO
            model_object = SLO.ImprovedSLO(**solver_options)

        case 'orig-nmra':
            from mealpy.swarm_based import NMRA
            model_object = NMRA.OriginalNMRA(**solver_options)

        case 'impr-nmra':
            from mealpy.swarm_based import NMRA
            model_object = NMRA.ImprovedNMRA(**solver_options)

        case 'orig-pfa':
            from mealpy.swarm_based import PFA
            model_object = PFA.OriginalPFA(**solver_options)

        case 'orig-sfo':
            from mealpy.swarm_based import SFO
            model_object = SFO.OriginalSFO(**solver_options)

        case 'impr-sfo':
            from mealpy.swarm_based import SFO
            model_object = SFO.ImprovedSFO(**solver_options)

        case 'orig-hho':
            from mealpy.swarm_based import HHO
            model_object = HHO.OriginalHHO(**solver_options)

        case 'orig-mrfo':
            from mealpy.swarm_based import MRFO
            model_object = MRFO.OriginalMRFO(**solver_options)

        case 'orig-bes':
            from mealpy.swarm_based import BES
            model_object = BES.OriginalBES(**solver_options)

        case 'orig-ssa':
            from mealpy.swarm_based import SSA
            model_object = SSA.OriginalSSA(**solver_options)

        case 'base-ssa':
            from mealpy.swarm_based import SSA
            model_object = SSA.BaseSSA(**solver_options)

        case 'orig-hgs':
            from mealpy.swarm_based import HGS
            model_object = HGS.OriginalHGS(**solver_options)

        case 'orig-ao':
            from mealpy.swarm_based import AO
            model_object = AO.OriginalAO(**solver_options)

        case 'gwo-woa':
            from mealpy.swarm_based import GWO
            model_object = GWO.OriginalGWO(**solver_options)

        case 'orig-mpa':
            from mealpy.swarm_based import MPA
            model_object = MPA.OriginalMPA(**solver_options)

        case 'orig-hba':
            from mealpy.swarm_based import HBA
            model_object = HBA.OriginalHBA(**solver_options)

        case 'orig-scso':
            from mealpy.swarm_based import SCSO
            model_object = SCSO.OriginalSCSO(**solver_options)

        case 'orig-tso':
            from mealpy.swarm_based import TSO
            model_object = TSO.OriginalTSO(**solver_options)

        case 'orig-avoa':
            from mealpy.swarm_based import AVOA
            model_object = AVOA.OriginalAVOA(**solver_options)

        case 'orig-agto':
            from mealpy.swarm_based import AGTO
            model_object = AGTO.OriginalAGTO(**solver_options)

        case 'orig-aro':
            from mealpy.swarm_based import ARO
            model_object = ARO.OriginalARO(**solver_options)

        case 'levy-aro':
            from mealpy.swarm_based import ARO
            model_object = ARO.LARO(**solver_options)

        case 'selec-aro':
            from mealpy.swarm_based import ARO
            model_object = ARO.IARO(**solver_options)

        case 'wmqi-mrfo':
            from mealpy.swarm_based import MRFO
            model_object = MRFO.WMQIMRFO(**solver_options)

        case 'orig-esoa':
            from mealpy.swarm_based import ESOA
            model_object = ESOA.OriginalESOA(**solver_options)

        case 'sea-ho':
            from mealpy.swarm_based import SeaHO
            model_object = SeaHO.OriginalSeaHO(**solver_options)

        case 'orig-mgo':
            from mealpy.swarm_based import MGO
            model_object = MGO.OriginalMGO(**solver_options)

        case 'orig-gjo':
            from mealpy.swarm_based import GJO
            model_object = GJO.OriginalGJO(**solver_options)

        case 'orig-fox':
            from mealpy.swarm_based import FOX
            model_object = FOX.OriginalFOX(**solver_options)

        case 'orig-gto':
            from mealpy.swarm_based import GTO
            model_object = GTO.OriginalGTO(**solver_options)

        case 'modi101-gto':
            from mealpy.swarm_based import GTO
            model_object = GTO.Matlab101GTO(**solver_options)

        case 'modi102-gto':
            from mealpy.swarm_based import GTO
            model_object = GTO.Matlab102GTO(**solver_options)

        # Physics-Inspired Heuristic Optimization Algorithms

        case 'orig-sa':
            from mealpy.physics_based import SA
            model_object = SA.OriginalSA(**solver_options)

        case 'orig-wdo':
            from mealpy.physics_based import WDO
            model_object = WDO.OriginalWDO(**solver_options)

        case 'orig-mvo':
            from mealpy.physics_based import MVO
            model_object = MVO.OriginalMVO(**solver_options)

        case 'base-mvo':
            from mealpy.physics_based import MVO
            model_object = MVO.BaseMVO(**solver_options)

        case 'orig-two':
            from mealpy.physics_based import TWO
            model_object = TWO.OriginalTWO(**solver_options)

        case 'oppo-two':
            from mealpy.physics_based import TWO
            model_object = TWO.OppoTWO(**solver_options)

        case 'levy-two':
            from mealpy.physics_based import TWO
            model_object = TWO.LevyTWO(**solver_options)

        case 'enha-two':
            from mealpy.physics_based import TWO
            model_object = TWO.EnhancedTWO(**solver_options)

        case 'orig-efo':
            from mealpy.physics_based import EFO
            model_object = EFO.OriginalEFO(**solver_options)

        case 'base-efo':
            from mealpy.physics_based import EFO
            model_object = EFO.BaseEFO(**solver_options)

        case 'orig-nro':
            from mealpy.physics_based import NRO
            model_object = NRO.OriginalNRO(**solver_options)

        case 'orig-hgso':
            from mealpy.physics_based import HGSO
            model_object = HGSO.OriginalHGSO(**solver_options)

        case 'orig-aso':
            from mealpy.physics_based import ASO
            model_object = ASO.OriginalASO(**solver_options)

        case 'orig-eo':
            from mealpy.physics_based import EO
            model_object = EO.OriginalEO(**solver_options)

        case 'modi-eo':
            from mealpy.physics_based import EO
            model_object = EO.ModifiedEO(**solver_options)

        case 'adap-eo':
            from mealpy.physics_based import EO
            model_object = EO.AdaptiveEO(**solver_options)

        case 'orig-archoa':
            from mealpy.physics_based import ArchOA
            model_object = ArchOA.OriginalArchOA(**solver_options)

        case 'orig-rime':
            from mealpy.physics_based import RIME
            model_object = RIME.OriginalRIME(**solver_options)

        case 'orig-evo':
            from mealpy.physics_based import EVO
            model_object = EVO.OriginalEVO(**solver_options)

        case 'orig-cdo':
            from mealpy.physics_based import CDO
            model_object = CDO.OriginalCDO

        case 'orig-fla':
            from mealpy.physics_based import FLA
            model_object = FLA.OriginalFLA

        # Human-Inspired Heuristic Optimization Algorithms

        case 'orig-ca':
            from mealpy.human_based import CA
            model_object = CA.OriginalCA(**solver_options)

        case 'orig-ica':
            from mealpy.human_based import ICA
            model_object = ICA.OriginalICA(**solver_options)

        case 'orig-tlo':
            from mealpy.human_based import TLO
            model_object = TLO.OriginalTLO(**solver_options)

        case 'base-tlo':
            from mealpy.human_based import TLO
            model_object = TLO.BaseTLO(**solver_options)

        case 'itlo':
            from mealpy.human_based import TLO
            model_object = TLO.ImprovedTLO(**solver_options)

        case 'orig-bso':
            from mealpy.human_based import BSO
            model_object = BSO.OriginalBSO(**solver_options)

        case 'impr-bso':
            from mealpy.human_based import BSO
            model_object = BSO.ImprovedBSO(**solver_options)

        case 'orig-qsa':
            from mealpy.human_based import QSA
            model_object = QSA.OriginalQSA(**solver_options)

        case 'base-qsa':
            from mealpy.human_based import QSA
            model_object = QSA.BaseQSA(**solver_options)

        case 'oppo-qsa':
            from mealpy.human_based import QSA
            model_object = QSA.OppoQSA(**solver_options)

        case 'levy-qsa':
            from mealpy.human_based import QSA
            model_object = QSA.LevyQSA(**solver_options)

        case 'impr-qsa':
            from mealpy.human_based import QSA
            model_object = QSA.ImprovedQSA(**solver_options)

        case 'orig-saro':
            from mealpy.human_based import SARO
            model_object = SARO.OriginalSARO(**solver_options)

        case 'base-saro':
            from mealpy.human_based import SARO
            model_object = SARO.BaseSARO(**solver_options)

        case 'orig-lco':
            from mealpy.human_based import LCO
            model_object = LCO.OriginalLCO(**solver_options)

        case 'base-lco':
            from mealpy.human_based import LCO
            model_object = LCO.BaseLCO(**solver_options)

        case 'impr-lco':
            from mealpy.human_based import LCO
            model_object = LCO.ImprovedLCO(**solver_options)

        case 'orig-ssdo':
            from mealpy.human_based import SSDO
            model_object = SSDO.OriginalSSDO(**solver_options)

        case 'orig-gska':
            from mealpy.human_based import GSKA
            model_object = GSKA.OriginalGSKA(**solver_options)

        case 'base-gska':
            from mealpy.human_based import GSKA
            model_object = GSKA.BaseGSKA(**solver_options)

        case 'orig-chio':
            from mealpy.human_based import CHIO
            model_object = CHIO.OriginalCHIO(**solver_options)

        case 'base-chio':
            from mealpy.human_based import CHIO
            model_object = CHIO.BaseCHIO(**solver_options)

        case 'orig-fbio':
            from mealpy.human_based import FBIO
            model_object = FBIO.OriginalFBIO(**solver_options)

        case 'base-fbio':
            from mealpy.human_based import FBIO
            model_object = FBIO.BaseFBIO(**solver_options)

        case 'orig-bro':
            from mealpy.human_based import BRO
            model_object = BRO.OriginalBRO(**solver_options)

        case 'base-bro':
            from mealpy.human_based import BRO
            model_object = BRO.BaseBRO(**solver_options)

        case 'orig-spbo':
            from mealpy.human_based import SPBO
            model_object = SPBO.OriginalSPBO(**solver_options)

        case 'dev-spbo':
            from mealpy.human_based import SPBO
            model_object = SPBO.DevSPBO(**solver_options)

        case 'orig-dmoa':
            print('OriginalDMOA: Not supported yet. Using SPBO instead')
            # from mealpy.human_based import DMOA
            # model_object = DMOA.OriginalDMOA(**solver_options)
            from mealpy.human_based import SPBO
            model_object = SPBO.DevSPBO(**solver_options)

        case 'dev-dmoa':
            print('DevDMOA: Not supported yet. Using SPBO instead')
            # from mealpy.human_based import DMOA
            # model_object = DMOA.DevDMOA(**solver_options)
            from mealpy.human_based import SPBO
            model_object = SPBO.DevSPBO(**solver_options)

        case 'orig-huco':
            from mealpy.human_based import HCO
            model_object = HCO.OriginalHCO(**solver_options)

        case 'orig-warso':
            from mealpy.human_based import WarSO
            model_object = WarSO.OriginalWarSO(**solver_options)

        case 'orig-hbo':
            from mealpy.human_based import HBO
            model_object = HBO.OriginalHBO(**solver_options)

        # Bio-Inspired Heuristic Optimization Algorithms

        case 'orig-iwo':
            from mealpy.bio_based import IWO
            model_object = IWO.OriginalIWO(**solver_options)

        case 'orig-bboa':
            from mealpy.bio_based import BBO
            model_object = BBO.OriginalBBO(**solver_options)

        case 'base-bbo':
            from mealpy.bio_based import BBO
            model_object = BBO.BaseBBO(**solver_options)

        case 'orig-vcs':
            from mealpy.bio_based import VCS
            model_object = VCS.OriginalVCS(**solver_options)

        case 'base-vcs':
            from mealpy.bio_based import VCS
            model_object = VCS.BaseVCS(**solver_options)

        case 'orig-sbo':
            from mealpy.bio_based import SBO
            model_object = SBO.OriginalSBO(**solver_options)

        case 'base-sbo':
            from mealpy.bio_based import SBO
            model_object = SBO.BaseSBO(**solver_options)

        case 'orig-eoa':
            from mealpy.bio_based import EOA
            model_object = EOA.OriginalEOA(**solver_options)

        case 'orig-who':
            from mealpy.bio_based import WHO
            model_object = WHO.OriginalWHO(**solver_options)

        case 'orig-sma':
            from mealpy.bio_based import SMA
            model_object = SMA.OriginalSMA(**solver_options)

        case 'base-sma':
            from mealpy.bio_based import SMA
            model_object = SMA.BaseSMA(**solver_options)

        case 'orig-bmo':
            from mealpy.bio_based import BMO
            model_object = BMO.OriginalBMO(**solver_options)

        case 'orig-tsa':
            from mealpy.bio_based import TSA
            model_object = TSA.OriginalTSA(**solver_options)

        case 'orig-sos':
            from mealpy.bio_based import SOS
            model_object = SOS.OriginalSOS(**solver_options)

        case 'orig-soa':
            from mealpy.bio_based import SOA
            model_object = SOA.OriginalSOA(**solver_options)

        case 'dev-soa':
            from mealpy.bio_based import SOA
            model_object = SOA.DevSOA(**solver_options)

        # System-Inspired Heuristic Optimization Algorithms

        case 'orig-gco':
            from mealpy.system_based import GCO
            model_object = GCO.OriginalGCO(**solver_options)

        case 'base-gco':
            from mealpy.system_based import GCO
            model_object = GCO.BaseGCO(**solver_options)

        case 'orig-wca':
            from mealpy.system_based import WCA
            model_object = WCA.OriginalWCA(**solver_options)

        case 'orig-aeo':
            from mealpy.system_based import AEO
            model_object = AEO.OriginalAEO(**solver_options)

        case 'enha-aeo':
            from mealpy.system_based import AEO
            model_object = AEO.EnhancedAEO(**solver_options)

        case 'modi-aeo':
            from mealpy.system_based import AEO
            model_object = AEO.ModifiedAEO(**solver_options)

        case 'impr-aeo':
            from mealpy.system_based import AEO
            model_object = AEO.ImprovedAEO(**solver_options)

        case 'augm-aeo':
            from mealpy.system_based import AEO
            model_object = AEO.AugmentedAEO(**solver_options)

        # Math-Inspired Heuristic Optimization Algorithms

        case 'orig-hc':
            from mealpy.math_based import HC
            model_object = HC.OriginalHC(**solver_options)

        case 'swarm-hc':
            from mealpy.math_based import HC
            model_object = HC.SwarmHC(**solver_options)

        case 'orig-cem':
            from mealpy.math_based import CEM
            model_object = CEM.OriginalCEM(**solver_options)

        case 'orig-sca':
            from mealpy.math_based import SCA
            model_object = SCA.OriginalSCA(**solver_options)

        case 'base-sca':
            from mealpy.math_based import SCA
            model_object = SCA.BaseSCA(**solver_options)

        case 'orig-beesa':
            from mealpy.math_based import AOA
            model_object = AOA.OriginalAOA(**solver_options)

        case 'orig-cgo':
            from mealpy.math_based import CGO
            model_object = CGO.OriginalCGO(**solver_options)

        case 'orig-gbo':
            from mealpy.math_based import GBO
            model_object = GBO.OriginalGBO(**solver_options)

        case 'orig-info':
            from mealpy.math_based import INFO
            model_object = INFO.OriginalINFO(**solver_options)

        case 'orig-pss':
            from mealpy.math_based import PSS
            model_object = PSS.OriginalPSS(**solver_options)

        case 'orig-run':
            from mealpy.math_based import RUN
            model_object = RUN.OriginalRUN(**solver_options)

        case 'orig-circle-sa':
            from mealpy.math_based import CircleSA
            model_object = CircleSA.OriginalCircleSA(**solver_options)

        case 'ql-sca':
            from mealpy.math_based import SCA
            model_object = SCA.QleSCA(**solver_options)

        case 'orig-shio':
            from mealpy.math_based import SHIO
            model_object = SHIO.OriginalSHIO(**solver_options)

        # Music-Inspired Heuristic Optimization Algorithms

        case 'orig-hs':
            from mealpy.music_based import HS
            model_object = HS.OriginalHS(**solver_options)

        case 'base-hs':
            from mealpy.music_based import HS
            model_object = HS.BaseHS(**solver_options)

    return model_object
