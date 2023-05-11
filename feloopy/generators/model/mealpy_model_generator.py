
def generate_model(solver_name,solver_options):

        match solver_name:

            # Evolutionary Heuristic Optimization Algorithms

            case 'original_ep':
                from mealpy.evolutionary_based import EP
                model_object = EP.OriginalEP(**solver_options)
            
            case 'levy_ep':
                from mealpy.evolutionary_based import EP
                model_object = EP.LevyEP(**solver_options)

            case 'original_es':
                from mealpy.evolutionary_based import ES
                model_object = ES.OriginalES(**solver_options)
            
            case 'levy_es':
                from mealpy.evolutionary_based import ES
                model_object = ES.LevyES(**solver_options)
            
            case 'original_ma':
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

            case 'original_fpa':
                from mealpy.evolutionary_based import FPA
                model_object = FPA.OriginalFPA(**solver_options)

            case 'original_cro':
                from mealpy.evolutionary_based import CRO
                model_object = CRO.OriginalCRO(**solver_options)

            case 'o_cro':
                from mealpy.evolutionary_based import CRO
                model_object = CRO.OCRO(**solver_options)

            # Swarm Heuristic Optimization Algorithms

            case 'original_pso':
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

            case 'original_bfo':
                from mealpy.swarm_based import BFO
                model_object = BFO.OriginalBFO(**solver_options)

            case 'original_beesa':
                from mealpy.swarm_based import BeesA
                model_object = BeesA.OriginalBeesA(**solver_options)

            case 'a_bfo':
                from mealpy.swarm_based import BFO
                model_object = BFO.OriginalBFO(**solver_options)

            case 'prob_beesa':
                from mealpy.swarm_based import BeesA
                model_object = BeesA.ProbBeesA(**solver_options)

            case 'original_cso':
                from mealpy.swarm_based import CSO
                model_object = CSO.OriginalCSO(**solver_options)

            case 'original_abc':
                from mealpy.swarm_based import ABC
                model_object = ABC.OriginalABC(**solver_options)

            case 'original_acor':
                from mealpy.swarm_based import ACOR
                model_object = ACOR.original_acor(**solver_options)

            case 'original_csa':
                from mealpy.swarm_based import CSA
                model_object = CSA.original_csa(**solver_options)

            case 'original_ffa':
                from mealpy.swarm_based import FFA
                model_object = FFA.original_ffa(**solver_options)

            case 'original_fa':
                from mealpy.swarm_based import FA
                model_object = FA.original_fa(**solver_options)

            case 'original_ba':
                from mealpy.swarm_based import BA
                model_object = BA.original_ba(**solver_options)

            case 'adaptive_ba':
                from mealpy.swarm_based import BA
                model_object = BA.adaptive_ba(**solver_options)

            case 'modified_ba':
                from mealpy.swarm_based import BA
                model_object = BA.modified_ba(**solver_options)

            case 'original_foa':
                from mealpy.swarm_based import FOA
                model_object = FOA.original_foa(**solver_options)

            case 'base_foa':
                from mealpy.swarm_based import FOA
                model_object = FOA.base_foa(**solver_options)

            case 'whale_foa':
                from mealpy.swarm_based import FOA
                model_object = FOA.whale_foa(**solver_options)

            case 'original_sspidero':
                from mealpy.swarm_based import SSpiderO
                model_object = SSpiderO.original_sspidero(**solver_options)

            case 'original_gwo':
                from mealpy.swarm_based import GWO
                model_object = GWO.original_gwo(**solver_options)

            case 'rw_gwo':
                from mealpy.swarm_based import GWO
                model_object = GWO.rw_gwo(**solver_options)

            case 'original_sspidera':
                from mealpy.swarm_based import SSpiderA
                model_object = SSpiderA.original_sspidera(**solver_options)

            case 'original_alo':
                from mealpy.swarm_based import ALO
                model_object = ALO.original_alo(**solver_options)

            case 'base_alo':
                from mealpy.swarm_based import ALO
                model_object = ALO.base_alo(**solver_options)

            case 'original_mfo':
                from mealpy.swarm_based import MFO
                model_object = MFO.original_mfo(**solver_options)

            case 'base_mfo':
                from mealpy.swarm_based import MFO
                model_object = MFO.BaseMFO(**solver_options)

            case 'original_eho':
                from mealpy.swarm_based import EHO
                model_object = EHO.OriginalEHO(**solver_options)

            case 'original_ja':
                from mealpy.swarm_based import JA
                model_object = JA.OriginalJA(**solver_options)

            case 'base_ja':
                from mealpy.swarm_based import JA
                model_object = JA.BaseJA(**solver_options)

            case 'levy_ja':
                from mealpy.swarm_based import JA
                model_object = JA.LevyJA(**solver_options)

            case 'original_woa':
                from mealpy.swarm_based import WOA
                model_object = WOA.OriginalWOA(**solver_options)

            case 'hi_woa':
                from mealpy.swarm_based import WOA
                model_object = WOA.HI_WOA(**solver_options)

            case 'original_do':
                from mealpy.swarm_based import DO
                model_object = DO.OriginalDO(**solver_options)

            case 'original_bsa':
                from mealpy.swarm_based import BSA
                model_object = BSA.OriginalBSA(**solver_options)

            case 'original_sho':
                from mealpy.swarm_based import SHO
                model_object = SHO.OriginalSHO(**solver_options)

            case 'original_sso':
                from mealpy.swarm_based import SSO
                model_object = SSO.OriginalSSO(**solver_options)

            case 'original_srsr':
                from mealpy.swarm_based import SRSR
                model_object = SRSR.OriginalSRSR(**solver_options)

            case 'original_goa':
                from mealpy.swarm_based import GOA
                model_object = GOA.OriginalGOA(**solver_options)

            case 'original_coa':
                from mealpy.swarm_based import COA
                model_object = COA.OriginalCOA(**solver_options)

            case 'original_msa':
                from mealpy.swarm_based import MSA
                model_object = MSA.OriginalMSA(**solver_options)

            case 'original_slo':
                from mealpy.swarm_based import SLO
                model_object = SLO.OriginalSLO(**solver_options)

            case 'modified_slo':
                from mealpy.swarm_based import SLO
                model_object = SLO.ModifiedSLO(**solver_options)

            case 'improved_slo':
                from mealpy.swarm_based import SLO
                model_object = SLO.ImprovedSLO(**solver_options)

            case 'original_nmra':
                from mealpy.swarm_based import NMRA
                model_object = NMRA.OriginalNMRA(**solver_options)

            case 'improved_nmra':
                from mealpy.swarm_based import NMRA
                model_object = NMRA.ImprovedNMRA(**solver_options)

            case 'original_pfa':
                from mealpy.swarm_based import PFA
                model_object = PFA.OriginalPFA(**solver_options)

            case 'original_sfo':
                from mealpy.swarm_based import SFO
                model_object = SFO.OriginalSFO(**solver_options)

            case 'improved_sfo':
                from mealpy.swarm_based import SFO
                model_object = SFO.ImprovedSFO(**solver_options)
            
            case 'original_hho':
                from mealpy.swarm_based import HHO
                model_object = HHO.OriginalHHO(**solver_options)
            
            case 'original_mrfo':
                from mealpy.swarm_based import MRFO
                model_object = MRFO.OriginalMRFO(**solver_options)
            
            case 'original_bes':
                from mealpy.swarm_based import BES
                model_object = BES.OriginalBES(**solver_options)
            
            case 'original_ssa':
                from mealpy.swarm_based import SSA
                model_object = SSA.OriginalSSA(**solver_options)
            
            case 'base_ssa':
                from mealpy.swarm_based import SSA
                model_object = SSA.BaseSSA(**solver_options)

            case 'original_hgs':
                from mealpy.swarm_based import HGS
                model_object = HGS.OriginalHGS(**solver_options)
        
            case 'original_ao':
                from mealpy.swarm_based import AO
                model_object = AO.OriginalAO(**solver_options)

            case 'gwo_woa':
                from mealpy.swarm_based import GWO
                model_object = GWO.OriginalGWO(**solver_options)

            case 'original_mpa':
                from mealpy.swarm_based import MPA
                model_object = MPA.OriginalMPA(**solver_options)

            case 'original_hba':
                from mealpy.swarm_based import HBA
                model_object = HBA.OriginalHBA(**solver_options)

            case 'original_scso':
                from mealpy.swarm_based import SCSO
                model_object = SCSO.OriginalSCSO(**solver_options)

            case 'original_tso':
                from mealpy.swarm_based import TSO
                model_object = TSO.OriginalTSO(**solver_options)

            case 'original_avoa':
                from mealpy.swarm_based import AVOA
                model_object = AVOA.OriginalAVOA(**solver_options)

            case 'original_agto':
                from mealpy.swarm_based import AGTO
                model_object = AGTO.OriginalAGTO(**solver_options)

            case 'original_aro':
                from mealpy.swarm_based import ARO
                model_object = ARO.OriginalARO(**solver_options)

            #============ Physics

            case 'original_sa':
                from mealpy.physics_based import SA
                model_object = SA.OriginalSA(**solver_options)

            case 'original_wdo':
                from mealpy.physics_based import WDO
                model_object = WDO.OriginalWDO(**solver_options)

            case 'original_mvo':
                from mealpy.physics_based import MVO
                model_object = MVO.OriginalMVO(**solver_options)

            case 'base_mvo':
                from mealpy.physics_based import MVO
                model_object = MVO.BaseMVO(**solver_options)

            case 'original_two':
                from mealpy.physics_based import TWO
                model_object = TWO.OriginalTWO(**solver_options)

            case 'oppo_two':
                from mealpy.physics_based import TWO
                model_object = TWO.OppoTWO(**solver_options)

            case 'levy_two':
                from mealpy.physics_based import TWO
                model_object = TWO.LevyTWO(**solver_options)

            case 'enhanced_two':
                from mealpy.physics_based import TWO
                model_object = TWO.EnhancedTWO(**solver_options)

            case 'original_efo':
                from mealpy.physics_based import EFO
                model_object = EFO.OriginalEFO(**solver_options)

            case 'base_efo':
                from mealpy.physics_based import EFO
                model_object = EFO.BaseEFO(**solver_options)

            case 'original_nro':
                from mealpy.physics_based import NRO
                model_object = NRO.OriginalNRO(**solver_options)

            case 'original_hgso':
                from mealpy.physics_based import HGSO
                model_object = HGSO.OriginalHGSO(**solver_options)

            case 'original_aso':
                from mealpy.physics_based import ASO
                model_object = ASO.OriginalASO(**solver_options)

            case 'original_eo':
                from mealpy.physics_based import EO
                model_object = EO.OriginalEO(**solver_options)

            case 'modified_eo':
                from mealpy.physics_based import EO
                model_object = EO.ModifiedEO(**solver_options)

            case 'adaptive_eo':
                from mealpy.physics_based import EO
                model_object = EO.AdaptiveEO(**solver_options)

            case 'original_archoa':
                from mealpy.physics_based import ArchOA
                model_object = ArchOA.OriginalArchOA(**solver_options)

            #============ Human

            case 'original_ca':
                from mealpy.human_based import CA
                model_object = CA.OriginalCA(**solver_options)

            case 'original_ica':
                from mealpy.human_based import ICA
                model_object = ICA.OriginalICA(**solver_options)

            case 'original_tlo':
                from mealpy.human_based import TLO
                model_object = TLO.OriginalTLO(**solver_options)
            
            case 'base_tlo':
                from mealpy.human_based import TLO
                model_object = TLO.BaseTLO(**solver_options)

            case 'itlo':
                from mealpy.human_based import TLO
                model_object = TLO.ImprovedTLO(**solver_options)

            case 'original_bso':
                from mealpy.human_based import BSO
                model_object = BSO.OriginalBSO(**solver_options)

            case 'improved_bso':
                from mealpy.human_based import BSO
                model_object = BSO.ImprovedBSO(**solver_options)

            case 'original_qsa':
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

            case 'improved_qsa':
                from mealpy.human_based import QSA
                model_object = QSA.ImprovedQSA(**solver_options)

            case 'original_saro':
                from mealpy.human_based import SARO
                model_object = SARO.OriginalSARO(**solver_options)

            case 'base_saro':
                from mealpy.human_based import SARO
                model_object = SARO.BaseSARO(**solver_options)

            case 'original_lco':
                from mealpy.human_based import LCO
                model_object = LCO.OriginalLCO(**solver_options)
                
            case 'base_lco':
                from mealpy.human_based import LCO
                model_object = LCO.BaseLCO(**solver_options)

            case 'improved_lco':
                from mealpy.human_based import LCO
                model_object = LCO.ImprovedLCO(**solver_options)

            case 'original_ssdo':
                from mealpy.human_based import SSDO
                model_object = SSDO.OriginalSSDO(**solver_options)

            case 'original_gska':
                from mealpy.human_based import GSKA
                model_object = GSKA.OriginalGSKA(**solver_options)

            case 'base_gska':
                from mealpy.human_based import GSKA
                model_object = GSKA.BaseGSKA(**solver_options)

            case 'original_chio':
                from mealpy.human_based import CHIO
                model_object = CHIO.OriginalCHIO(**solver_options)

            case 'base_chio':
                from mealpy.human_based import CHIO
                model_object = CHIO.BaseCHIO(**solver_options)

            case 'original_fbio':
                from mealpy.human_based import FBIO
                model_object = FBIO.OriginalFBIO(**solver_options)

            case 'base_fbio':
                from mealpy.human_based import FBIO
                model_object = FBIO.BaseFBIO(**solver_options)

            case 'original_bro':
                from mealpy.human_based import BRO
                model_object = BRO.OriginalBRO(**solver_options)
            
            case 'base_bro':
                from mealpy.human_based import BRO
                model_object = BRO.BaseBRO(**solver_options)

            case 'original_spbo':
                from mealpy.human_based import SPBO
                model_object = SPBO.OriginalSPBO(**solver_options)

            case 'dev_spbo':
                from mealpy.human_based import SPBO
                model_object = SPBO.DevSPBO(**solver_options)

            case 'original_dmoa':
                print('OriginalDMOA: Not supported yet. Using SPBO instead')
                # from mealpy.human_based import DMOA
                # model_object = DMOA.OriginalDMOA(**solver_options)
                from mealpy.human_based import SPBO
                model_object = SPBO.DevSPBO(**solver_options)

            case 'dev_dmoa':
                print('DevDMOA: Not supported yet. Using SPBO instead')
                # from mealpy.human_based import DMOA
                # model_object = DMOA.DevDMOA(**solver_options)
                from mealpy.human_based import SPBO
                model_object = SPBO.DevSPBO(**solver_options)

            #============ Bio

            case 'original_iwo':
                from mealpy.bio_based import IWO
                model_object = IWO.OriginalIWO(**solver_options)

            case 'original_bboa':
                from mealpy.bio_based import BBO
                model_object = BBO.OriginalBBO(**solver_options)

            case 'base_bbo':
                from mealpy.bio_based import BBO
                model_object = BBO.BaseBBO(**solver_options)

            case 'original_vcs':
                from mealpy.bio_based import VCS
                model_object = VCS.OriginalVCS(**solver_options)

            case 'base_vcs':
                from mealpy.bio_based import VCS
                model_object = VCS.BaseVCS(**solver_options)

            case 'original_sbo':
                from mealpy.bio_based import SBO
                model_object = SBO.OriginalSBO(**solver_options)

            case 'base_sbo':
                from mealpy.bio_based import SBO
                model_object = SBO.BaseSBO(**solver_options)

            case 'original_eoa':
                from mealpy.bio_based import EOA
                model_object = EOA.OriginalEOA(**solver_options)

            case 'original_who':
                from mealpy.bio_based import WHO
                model_object = WHO.OriginalWHO(**solver_options)

            case 'original_sma':
                from mealpy.bio_based import SMA
                model_object = SMA.OriginalSMA(**solver_options)

            case 'base_sma':
                from mealpy.bio_based import SMA
                model_object = SMA.BaseSMA(**solver_options)

            case 'original_bmo':
                from mealpy.bio_based import BMO
                model_object = BMO.OriginalBMO(**solver_options)

            case 'original_tsa':
                from mealpy.bio_based import TSA
                model_object = TSA.OriginalTSA(**solver_options)

            case 'original_sos':
                from mealpy.bio_based import SOS
                model_object = SOS.OriginalSOS(**solver_options)

            case 'original_soa':
                from mealpy.bio_based import SOA
                model_object = SOA.OriginalSOA(**solver_options)

            case 'dev_soa':
                from mealpy.bio_based import SOA
                model_object = SOA.DevSOA(**solver_options)

            #============ System

            case 'original_gco':
                from mealpy.system_based import GCO
                model_object = GCO.OriginalGCO(**solver_options)

            case 'base_gco':
                from mealpy.system_based import GCO
                model_object = GCO.BaseGCO(**solver_options)

            case 'original_wca':
                from mealpy.system_based import WCA
                model_object = WCA.OriginalWCA(**solver_options)

            case 'original_aeo':
                from mealpy.system_based import AEO
                model_object = AEO.OriginalAEO(**solver_options)

            case 'enhanced_aeo':
                from mealpy.system_based import AEO
                model_object = AEO.EnhancedAEO(**solver_options)

            case 'modified_aeo':
                from mealpy.system_based import AEO
                model_object = AEO.ModifiedAEO(**solver_options)

            case 'improved_aeo':
                from mealpy.system_based import AEO
                model_object = AEO.ImprovedAEO(**solver_options)

            case 'adaptive_aeo':
                from mealpy.system_based import AEO
                model_object = AEO.AdaptiveAEO(**solver_options)

            #============ Math

            case 'original_hc':
                from mealpy.math_based import HC
                model_object = HC.OriginalHC(**solver_options)

            case 'swarm_hc':
                from mealpy.math_based import HC
                model_object = HC.SwarmHC(**solver_options)

            case 'original_cem':
                from mealpy.math_based import CEM
                model_object = CEM.OriginalCEM(**solver_options)

            case 'original_sca':
                from mealpy.math_based import SCA
                model_object = SCA.OriginalSCA(**solver_options)

            case 'base_sca':
                from mealpy.math_based import SCA
                model_object = SCA.BaseSCA(**solver_options)

            case 'original_aoa':
                from mealpy.math_based import AOA
                model_object = AOA.OriginalAOA(**solver_options)

            case 'original_cgo':
                from mealpy.math_based import CGO
                model_object = CGO.OriginalCGO(**solver_options)

            case 'original_gbo':
                from mealpy.math_based import GBO
                model_object = GBO.OriginalGBO(**solver_options)

            case 'original_info':
                from mealpy.math_based import INFO
                model_object = INFO.OriginalINFO(**solver_options)

            case 'original_pss':
                from mealpy.math_based import PSS
                model_object = PSS.OriginalPSS(**solver_options)

            case 'original_run':
                from mealpy.math_based import RUN
                model_object = RUN.OriginalRUN(**solver_options)

            case 'original_circle_sa':
                from mealpy.math_based import CircleSA
                model_object = CircleSA.OriginalCircleSA(**solver_options)
            
            #============ Music
            
            case 'original_hs':
                from mealpy.music_based import HS
                model_object = HS.OriginalHS(**solver_options)

            case 'base_hs':
                from mealpy.music_based import HS
                model_object = HS.BaseHS(**solver_options)

        
        return model_object