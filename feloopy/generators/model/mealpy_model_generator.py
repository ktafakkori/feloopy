
def generate_model(solver_name,solver_options):

        match solver_name:

            # Evolution-Inspired Heuristic Optimization Algorithms

            case 'orig_ep':
                from mealpy.evolutionary_based import EP
                model_object = EP.OriginalEP(**solver_options)
            
            case 'levy_ep':
                from mealpy.evolutionary_based import EP
                model_object = EP.LevyEP(**solver_options)

            case 'orig_es':
                from mealpy.evolutionary_based import ES
                model_object = ES.OriginalES(**solver_options)
            
            case 'levy_es':
                from mealpy.evolutionary_based import ES
                model_object = ES.LevyES(**solver_options)
            
            case 'orig_ma':
                from mealpy.evolutionary_based import MA
                model_object = MA.OriginalMA(**solver_options)
            
            case 'base_ga':
                from mealpy.evolutionary_based import GA
                model_object = GA.BaseGA(**solver_options)

            case 'single_ga':
                from mealpy.evolutionary_based import GA
                model_object = GA.SingleGA(**solver_options)
            
            case 'multi_ga':
                from mealpy.evolutionary_based import GA
                model_object = GA.MultiGA(**solver_options)

            case 'elite_single_ga':
                from mealpy.evolutionary_based import GA
                model_object = GA.EliteSingleGA(**solver_options)

            case 'elite_multi_ga':
                from mealpy.evolutionary_based import GA
                model_object = GA.EliteMultiGA(**solver_options)

            case 'base_de':
                from mealpy.evolutionary_based import DE
                model_object = DE.BaseDE(**solver_options)

            case 'ja_de':
                from mealpy.evolutionary_based import DE
                model_object = DE.JADE(**solver_options)

            case 'sa_de':
                from mealpy.evolutionary_based import DE
                model_object = DE.SADE(**solver_options)
            
            case 'sha_de':
                from mealpy.evolutionary_based import DE
                model_object = DE.SHADE(**solver_options)

            case 'l_sha_de':
                from mealpy.evolutionary_based import DE
                model_object = DE.L_SHADE(**solver_options)

            case 'sap_de':
                from mealpy.evolutionary_based import DE
                model_object = DE.SAP_DE(**solver_options)

            case 'orig_fpa':
                from mealpy.evolutionary_based import FPA
                model_object = FPA.OriginalFPA(**solver_options)

            case 'orig_cro':
                from mealpy.evolutionary_based import CRO
                model_object = CRO.OriginalCRO(**solver_options)

            case 'o_cro':
                from mealpy.evolutionary_based import CRO
                model_object = CRO.OCRO(**solver_options)

            # Swarm-Inspired Heuristic Optimization Algorithms

            case 'orig_pso':
                from mealpy.swarm_based import PSO
                model_object = PSO.OriginalPSO(**solver_options)

            case 'p_pso':
                from mealpy.swarm_based import PSO
                model_object = PSO.PPSO(**solver_options)

            case 'h_pso_tvac':
                from mealpy.swarm_based import PSO
                model_object = PSO.HPSO_TVAC(**solver_options)

            case 'c_pso':
                from mealpy.swarm_based import PSO
                model_object = PSO.C_PSO(**solver_options)

            case 'cl_pso':
                from mealpy.swarm_based import PSO
                model_object = PSO.CL_PSO(**solver_options)

            case 'orig_bfo':
                from mealpy.swarm_based import BFO
                model_object = BFO.OriginalBFO(**solver_options)

            case 'orig_beesa':
                from mealpy.swarm_based import BeesA
                model_object = BeesA.OriginalBeesA(**solver_options)

            case 'a_bfo':
                from mealpy.swarm_based import BFO
                model_object = BFO.OriginalBFO(**solver_options)

            case 'prob_beesa':
                from mealpy.swarm_based import BeesA
                model_object = BeesA.ProbBeesA(**solver_options)

            case 'orig_cso':
                from mealpy.swarm_based import CSO
                model_object = CSO.OriginalCSO(**solver_options)

            case 'orig_abc':
                from mealpy.swarm_based import ABC
                model_object = ABC.OriginalABC(**solver_options)

            case 'orig_acor':
                from mealpy.swarm_based import ACOR
                model_object = ACOR.orig_acor(**solver_options)

            case 'orig_csa':
                from mealpy.swarm_based import CSA
                model_object = CSA.OriginalCSA(**solver_options)

            case 'orig_ffa':
                from mealpy.swarm_based import FFA
                model_object = FFA.OriginalFFA(**solver_options)

            case 'orig_fa':
                from mealpy.swarm_based import FA
                model_object = FA.OriginalFA(**solver_options)

            case 'orig_ba':
                from mealpy.swarm_based import BA
                model_object = BA.OriginalBA(**solver_options)

            case 'adap_ba':
                from mealpy.swarm_based import BA
                model_object = BA.AdaptiveBA(**solver_options)

            case 'modi_ba':
                from mealpy.swarm_based import BA
                model_object = BA.ModifiedBA(**solver_options)

            case 'orig_foa':
                from mealpy.swarm_based import FOA
                model_object = FOA.OriginalFOA(**solver_options)

            case 'base_foa':
                from mealpy.swarm_based import FOA
                model_object = FOA.BaseFOA(**solver_options)

            case 'whale_foa':
                from mealpy.swarm_based import FOA
                model_object = FOA.WhaleFOA(**solver_options)

            case 'orig_sspidero':
                from mealpy.swarm_based import SSpiderO
                model_object = SSpiderO.OriginalSSpiderO(**solver_options)

            case 'orig_gwo':
                from mealpy.swarm_based import GWO
                model_object = GWO.OriginalGWO(**solver_options)

            case 'rw_gwo':
                from mealpy.swarm_based import GWO
                model_object = GWO.RW_GWO(**solver_options)

            case 'orig_sspidera':
                from mealpy.swarm_based import SSpiderA
                model_object = SSpiderA.OriginalSSpiderA(**solver_options)

            case 'orig_alo':
                from mealpy.swarm_based import ALO
                model_object = ALO.OriginalALO(**solver_options)

            case 'base_alo':
                from mealpy.swarm_based import ALO
                model_object = ALO.BaseALO(**solver_options)

            case 'orig_mfo':
                from mealpy.swarm_based import MFO
                model_object = MFO.OriginalMFO(**solver_options)

            case 'base_mfo':
                from mealpy.swarm_based import MFO
                model_object = MFO.BaseMFO(**solver_options)

            case 'orig_eho':
                from mealpy.swarm_based import EHO
                model_object = EHO.OriginalEHO(**solver_options)

            case 'orig_ja':
                from mealpy.swarm_based import JA
                model_object = JA.OriginalJA(**solver_options)

            case 'base_ja':
                from mealpy.swarm_based import JA
                model_object = JA.BaseJA(**solver_options)

            case 'levy_ja':
                from mealpy.swarm_based import JA
                model_object = JA.LevyJA(**solver_options)

            case 'orig_woa':
                from mealpy.swarm_based import WOA
                model_object = WOA.OriginalWOA(**solver_options)

            case 'hi_woa':
                from mealpy.swarm_based import WOA
                model_object = WOA.HI_WOA(**solver_options)

            case 'orig_do':
                from mealpy.swarm_based import DO
                model_object = DO.OriginalDO(**solver_options)

            case 'orig_bsa':
                from mealpy.swarm_based import BSA
                model_object = BSA.OriginalBSA(**solver_options)

            case 'orig_sho':
                from mealpy.swarm_based import SHO
                model_object = SHO.OriginalSHO(**solver_options)

            case 'orig_sso':
                from mealpy.swarm_based import SSO
                model_object = SSO.OriginalSSO(**solver_options)

            case 'orig_srsr':
                from mealpy.swarm_based import SRSR
                model_object = SRSR.OriginalSRSR(**solver_options)

            case 'orig_goa':
                from mealpy.swarm_based import GOA
                model_object = GOA.OriginalGOA(**solver_options)

            case 'orig_coa':
                from mealpy.swarm_based import COA
                model_object = COA.OriginalCOA(**solver_options)

            case 'orig_msa':
                from mealpy.swarm_based import MSA
                model_object = MSA.OriginalMSA(**solver_options)

            case 'orig_slo':
                from mealpy.swarm_based import SLO
                model_object = SLO.OriginalSLO(**solver_options)

            case 'modi_slo':
                from mealpy.swarm_based import SLO
                model_object = SLO.ModifiedSLO(**solver_options)

            case 'impr_slo':
                from mealpy.swarm_based import SLO
                model_object = SLO.ImprovedSLO(**solver_options)

            case 'orig_nmra':
                from mealpy.swarm_based import NMRA
                model_object = NMRA.OriginalNMRA(**solver_options)

            case 'impr_nmra':
                from mealpy.swarm_based import NMRA
                model_object = NMRA.ImprovedNMRA(**solver_options)

            case 'orig_pfa':
                from mealpy.swarm_based import PFA
                model_object = PFA.OriginalPFA(**solver_options)

            case 'orig_sfo':
                from mealpy.swarm_based import SFO
                model_object = SFO.OriginalSFO(**solver_options)

            case 'impr_sfo':
                from mealpy.swarm_based import SFO
                model_object = SFO.ImprovedSFO(**solver_options)
            
            case 'orig_hho':
                from mealpy.swarm_based import HHO
                model_object = HHO.OriginalHHO(**solver_options)
            
            case 'orig_mrfo':
                from mealpy.swarm_based import MRFO
                model_object = MRFO.OriginalMRFO(**solver_options)
            
            case 'orig_bes':
                from mealpy.swarm_based import BES
                model_object = BES.OriginalBES(**solver_options)
            
            case 'orig_ssa':
                from mealpy.swarm_based import SSA
                model_object = SSA.OriginalSSA(**solver_options)
            
            case 'base_ssa':
                from mealpy.swarm_based import SSA
                model_object = SSA.BaseSSA(**solver_options)

            case 'orig_hgs':
                from mealpy.swarm_based import HGS
                model_object = HGS.OriginalHGS(**solver_options)
        
            case 'orig_ao':
                from mealpy.swarm_based import AO
                model_object = AO.OriginalAO(**solver_options)

            case 'gwo_woa':
                from mealpy.swarm_based import GWO
                model_object = GWO.OriginalGWO(**solver_options)

            case 'orig_mpa':
                from mealpy.swarm_based import MPA
                model_object = MPA.OriginalMPA(**solver_options)

            case 'orig_hba':
                from mealpy.swarm_based import HBA
                model_object = HBA.OriginalHBA(**solver_options)

            case 'orig_scso':
                from mealpy.swarm_based import SCSO
                model_object = SCSO.OriginalSCSO(**solver_options)

            case 'orig_tso':
                from mealpy.swarm_based import TSO
                model_object = TSO.OriginalTSO(**solver_options)

            case 'orig_avoa':
                from mealpy.swarm_based import AVOA
                model_object = AVOA.OriginalAVOA(**solver_options)

            case 'orig_agto':
                from mealpy.swarm_based import AGTO
                model_object = AGTO.OriginalAGTO(**solver_options)

            case 'orig_aro':
                from mealpy.swarm_based import ARO
                model_object = ARO.OriginalARO(**solver_options)

            # Physics-Inspired Heuristic Optimization Algorithms

            case 'orig_sa':
                from mealpy.physics_based import SA
                model_object = SA.OriginalSA(**solver_options)

            case 'orig_wdo':
                from mealpy.physics_based import WDO
                model_object = WDO.OriginalWDO(**solver_options)

            case 'orig_mvo':
                from mealpy.physics_based import MVO
                model_object = MVO.OriginalMVO(**solver_options)

            case 'base_mvo':
                from mealpy.physics_based import MVO
                model_object = MVO.BaseMVO(**solver_options)

            case 'orig_two':
                from mealpy.physics_based import TWO
                model_object = TWO.OriginalTWO(**solver_options)

            case 'oppo_two':
                from mealpy.physics_based import TWO
                model_object = TWO.OppoTWO(**solver_options)

            case 'levy_two':
                from mealpy.physics_based import TWO
                model_object = TWO.LevyTWO(**solver_options)

            case 'enha_two':
                from mealpy.physics_based import TWO
                model_object = TWO.EnhancedTWO(**solver_options)

            case 'orig_efo':
                from mealpy.physics_based import EFO
                model_object = EFO.OriginalEFO(**solver_options)

            case 'base_efo':
                from mealpy.physics_based import EFO
                model_object = EFO.BaseEFO(**solver_options)

            case 'orig_nro':
                from mealpy.physics_based import NRO
                model_object = NRO.OriginalNRO(**solver_options)

            case 'orig_hgso':
                from mealpy.physics_based import HGSO
                model_object = HGSO.OriginalHGSO(**solver_options)

            case 'orig_aso':
                from mealpy.physics_based import ASO
                model_object = ASO.OriginalASO(**solver_options)

            case 'orig_eo':
                from mealpy.physics_based import EO
                model_object = EO.OriginalEO(**solver_options)

            case 'modi_eo':
                from mealpy.physics_based import EO
                model_object = EO.ModifiedEO(**solver_options)

            case 'adap_eo':
                from mealpy.physics_based import EO
                model_object = EO.AdaptiveEO(**solver_options)

            case 'orig_archoa':
                from mealpy.physics_based import ArchOA
                model_object = ArchOA.OriginalArchOA(**solver_options)

            # Human-Inspired Heuristic Optimization Algorithms

            case 'orig_ca':
                from mealpy.human_based import CA
                model_object = CA.OriginalCA(**solver_options)

            case 'orig_ica':
                from mealpy.human_based import ICA
                model_object = ICA.OriginalICA(**solver_options)

            case 'orig_tlo':
                from mealpy.human_based import TLO
                model_object = TLO.OriginalTLO(**solver_options)
            
            case 'base_tlo':
                from mealpy.human_based import TLO
                model_object = TLO.BaseTLO(**solver_options)

            case 'itlo':
                from mealpy.human_based import TLO
                model_object = TLO.ImprovedTLO(**solver_options)

            case 'orig_bso':
                from mealpy.human_based import BSO
                model_object = BSO.OriginalBSO(**solver_options)

            case 'impr_bso':
                from mealpy.human_based import BSO
                model_object = BSO.ImprovedBSO(**solver_options)

            case 'orig_qsa':
                from mealpy.human_based import QSA
                model_object = QSA.OriginalQSA(**solver_options)

            case 'base_qsa':
                from mealpy.human_based import QSA
                model_object = QSA.BaseQSA(**solver_options)

            case 'oppo_qsa':
                from mealpy.human_based import QSA
                model_object = QSA.OppoQSA(**solver_options)

            case 'levy_qsa':
                from mealpy.human_based import QSA
                model_object = QSA.LevyQSA(**solver_options)

            case 'impr_qsa':
                from mealpy.human_based import QSA
                model_object = QSA.ImprovedQSA(**solver_options)

            case 'orig_saro':
                from mealpy.human_based import SARO
                model_object = SARO.OriginalSARO(**solver_options)

            case 'base_saro':
                from mealpy.human_based import SARO
                model_object = SARO.BaseSARO(**solver_options)

            case 'orig_lco':
                from mealpy.human_based import LCO
                model_object = LCO.OriginalLCO(**solver_options)
                
            case 'base_lco':
                from mealpy.human_based import LCO
                model_object = LCO.BaseLCO(**solver_options)

            case 'impr_lco':
                from mealpy.human_based import LCO
                model_object = LCO.ImprovedLCO(**solver_options)

            case 'orig_ssdo':
                from mealpy.human_based import SSDO
                model_object = SSDO.OriginalSSDO(**solver_options)

            case 'orig_gska':
                from mealpy.human_based import GSKA
                model_object = GSKA.OriginalGSKA(**solver_options)

            case 'base_gska':
                from mealpy.human_based import GSKA
                model_object = GSKA.BaseGSKA(**solver_options)

            case 'orig_chio':
                from mealpy.human_based import CHIO
                model_object = CHIO.OriginalCHIO(**solver_options)

            case 'base_chio':
                from mealpy.human_based import CHIO
                model_object = CHIO.BaseCHIO(**solver_options)

            case 'orig_fbio':
                from mealpy.human_based import FBIO
                model_object = FBIO.OriginalFBIO(**solver_options)

            case 'base_fbio':
                from mealpy.human_based import FBIO
                model_object = FBIO.BaseFBIO(**solver_options)

            case 'orig_bro':
                from mealpy.human_based import BRO
                model_object = BRO.OriginalBRO(**solver_options)
            
            case 'base_bro':
                from mealpy.human_based import BRO
                model_object = BRO.BaseBRO(**solver_options)

            case 'orig_spbo':
                from mealpy.human_based import SPBO
                model_object = SPBO.OriginalSPBO(**solver_options)

            case 'dev_spbo':
                from mealpy.human_based import SPBO
                model_object = SPBO.DevSPBO(**solver_options)

            case 'orig_dmoa':
                print('OriginalDMOA: Not supported yet. Using SPBO instead')
                # from mealpy.human_based import DMOA
                # model_object = DMOA.OriginalDMOA(**solver_options)
                from mealpy.human_based import SPBO
                model_object = SPBO.DevSPBO(**solver_options)

            case 'dev_dmoa':
                print('DevDMOA: Not supported yet. Using SPBO instead')
                #from mealpy.human_based import DMOA
                #model_object = DMOA.DevDMOA(**solver_options)
                from mealpy.human_based import SPBO
                model_object = SPBO.DevSPBO(**solver_options)

            # Bio-Inspired Heuristic Optimization Algorithms

            case 'orig_iwo':
                from mealpy.bio_based import IWO
                model_object = IWO.OriginalIWO(**solver_options)

            case 'orig_bboa':
                from mealpy.bio_based import BBO
                model_object = BBO.OriginalBBO(**solver_options)

            case 'base_bbo':
                from mealpy.bio_based import BBO
                model_object = BBO.BaseBBO(**solver_options)

            case 'orig_vcs':
                from mealpy.bio_based import VCS
                model_object = VCS.OriginalVCS(**solver_options)

            case 'base_vcs':
                from mealpy.bio_based import VCS
                model_object = VCS.BaseVCS(**solver_options)

            case 'orig_sbo':
                from mealpy.bio_based import SBO
                model_object = SBO.OriginalSBO(**solver_options)

            case 'base_sbo':
                from mealpy.bio_based import SBO
                model_object = SBO.BaseSBO(**solver_options)

            case 'orig_eoa':
                from mealpy.bio_based import EOA
                model_object = EOA.OriginalEOA(**solver_options)

            case 'orig_who':
                from mealpy.bio_based import WHO
                model_object = WHO.OriginalWHO(**solver_options)

            case 'orig_sma':
                from mealpy.bio_based import SMA
                model_object = SMA.OriginalSMA(**solver_options)

            case 'base_sma':
                from mealpy.bio_based import SMA
                model_object = SMA.BaseSMA(**solver_options)

            case 'orig_bmo':
                from mealpy.bio_based import BMO
                model_object = BMO.OriginalBMO(**solver_options)

            case 'orig_tsa':
                from mealpy.bio_based import TSA
                model_object = TSA.OriginalTSA(**solver_options)

            case 'orig_sos':
                from mealpy.bio_based import SOS
                model_object = SOS.OriginalSOS(**solver_options)

            case 'orig_soa':
                from mealpy.bio_based import SOA
                model_object = SOA.OriginalSOA(**solver_options)

            case 'dev_soa':
                from mealpy.bio_based import SOA
                model_object = SOA.DevSOA(**solver_options)

            # System-Inspired Heuristic Optimization Algorithms

            case 'orig_gco':
                from mealpy.system_based import GCO
                model_object = GCO.OriginalGCO(**solver_options)

            case 'base_gco':
                from mealpy.system_based import GCO
                model_object = GCO.BaseGCO(**solver_options)

            case 'orig_wca':
                from mealpy.system_based import WCA
                model_object = WCA.OriginalWCA(**solver_options)

            case 'orig_aeo':
                from mealpy.system_based import AEO
                model_object = AEO.OriginalAEO(**solver_options)

            case 'enha_aeo':
                from mealpy.system_based import AEO
                model_object = AEO.EnhancedAEO(**solver_options)

            case 'modi_aeo':
                from mealpy.system_based import AEO
                model_object = AEO.ModifiedAEO(**solver_options)

            case 'impr_aeo':
                from mealpy.system_based import AEO
                model_object = AEO.ImprovedAEO(**solver_options)

            case 'adap_aeo':
                from mealpy.system_based import AEO
                model_object = AEO.AdaptiveAEO(**solver_options)

            # Math-Inspired Heuristic Optimization Algorithms

            case 'orig_hc':
                from mealpy.math_based import HC
                model_object = HC.OriginalHC(**solver_options)

            case 'swarm_hc':
                from mealpy.math_based import HC
                model_object = HC.SwarmHC(**solver_options)

            case 'orig_cem':
                from mealpy.math_based import CEM
                model_object = CEM.OriginalCEM(**solver_options)

            case 'orig_sca':
                from mealpy.math_based import SCA
                model_object = SCA.OriginalSCA(**solver_options)

            case 'base_sca':
                from mealpy.math_based import SCA
                model_object = SCA.BaseSCA(**solver_options)

            case 'orig_beesa':
                from mealpy.math_based import AOA
                model_object = AOA.OriginalAOA(**solver_options)

            case 'orig_cgo':
                from mealpy.math_based import CGO
                model_object = CGO.OriginalCGO(**solver_options)

            case 'orig_gbo':
                from mealpy.math_based import GBO
                model_object = GBO.OriginalGBO(**solver_options)

            case 'orig_info':
                from mealpy.math_based import INFO
                model_object = INFO.OriginalINFO(**solver_options)

            case 'orig_pss':
                from mealpy.math_based import PSS
                model_object = PSS.OriginalPSS(**solver_options)

            case 'orig_run':
                from mealpy.math_based import RUN
                model_object = RUN.OriginalRUN(**solver_options)

            case 'orig_circle_sa':
                from mealpy.math_based import CircleSA
                model_object = CircleSA.OriginalCircleSA(**solver_options)
            
            # Music-Inspired Heuristic Optimization Algorithms
            
            case 'orig_hs':
                from mealpy.music_based import HS
                model_object = HS.OriginalHS(**solver_options)

            case 'base_hs':
                from mealpy.music_based import HS
                model_object = HS.BaseHS(**solver_options)

        
        return model_object