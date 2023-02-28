
def generate_model(solver_name,solver_options):

        match solver_name:

            #============ Evolutionary

            case 'OriginalEP':
                from mealpy.evolutionary_based import EP
                model_object = EP.OriginalEP(**solver_options)
            
            case 'LevyEP':
                from mealpy.evolutionary_based import EP
                model_object = EP.LevyEP(**solver_options)

            case 'OriginalES':
                from mealpy.evolutionary_based import ES
                model_object = ES.OriginalES(**solver_options)
            
            case 'LevyES':
                from mealpy.evolutionary_based import ES
                model_object = ES.LevyES(**solver_options)
            
            case 'OriginalMA':
                from mealpy.evolutionary_based import MA
                model_object = MA.OriginalMA(**solver_options)
            
            case 'BaseGA':
                from mealpy.evolutionary_based import GA
                model_object = GA.BaseGA(**solver_options)

            case 'SingleGA':
                from mealpy.evolutionary_based import GA
                model_object = GA.SingleGA(**solver_options)
            
            case 'MultiGA':
                from mealpy.evolutionary_based import GA
                model_object = GA.MultiGA(**solver_options)

            case 'EliteSingleGA':
                from mealpy.evolutionary_based import GA
                model_object = GA.EliteSingleGA(**solver_options)

            case 'EliteMultiGA':
                from mealpy.evolutionary_based import GA
                model_object = GA.EliteMultiGA(**solver_options)

            case 'BaseDE':
                from mealpy.evolutionary_based import DE
                model_object = DE.BaseDE(**solver_options)

            case 'JADE':
                from mealpy.evolutionary_based import DE
                model_object = DE.JADE(**solver_options)

            case 'SADE':
                from mealpy.evolutionary_based import DE
                model_object = DE.SADE(**solver_options)
            
            case 'SHADE':
                from mealpy.evolutionary_based import DE
                model_object = DE.SHADE(**solver_options)

            case 'L_SHADE':
                from mealpy.evolutionary_based import DE
                model_object = DE.L_SHADE(**solver_options)

            case 'SAP_DE':
                from mealpy.evolutionary_based import DE
                model_object = DE.SAP_DE(**solver_options)

            case 'OriginalFPA':
                from mealpy.evolutionary_based import FPA
                model_object = FPA.OriginalFPA(**solver_options)

            case 'OriginalCRO':
                from mealpy.evolutionary_based import CRO
                model_object = CRO.OriginalCRO(**solver_options)

            case 'OCRO':
                from mealpy.evolutionary_based import CRO
                model_object = CRO.OCRO(**solver_options)

            #============ Swarm

            case 'OriginalPSO':
                from mealpy.swarm_based import PSO
                model_object = PSO.OriginalPSO(**solver_options)

            case 'PPSO':
                from mealpy.swarm_based import PSO
                model_object = PSO.PPSO(**solver_options)

            case 'HPSO_TVAC':
                from mealpy.swarm_based import PSO
                model_object = PSO.HPSO_TVAC(**solver_options)

            case 'C_PSO':
                from mealpy.swarm_based import PSO
                model_object = PSO.C_PSO(**solver_options)

            case 'CL_PSO':
                from mealpy.swarm_based import PSO
                model_object = PSO.CL_PSO(**solver_options)

            case 'OriginalBFO':
                from mealpy.swarm_based import BFO
                model_object = BFO.OriginalBFO(**solver_options)

            case 'ABFO':
                from mealpy.swarm_based import BFO
                model_object = BFO.OriginalBFO(**solver_options)

            case 'OriginalBeesA':
                from mealpy.swarm_based import BeesA
                model_object = BeesA.OriginalBeesA(**solver_options)

            case 'ProbBeesA':
                from mealpy.swarm_based import BeesA
                model_object = BeesA.ProbBeesA(**solver_options)

            case 'OriginalCSO':
                from mealpy.swarm_based import CSO
                model_object = CSO.OriginalCSO(**solver_options)
                
            case 'OriginalABC':
                from mealpy.swarm_based import ABC
                model_object = ABC.OriginalABC(**solver_options)

            case 'OriginalACOR':
                from mealpy.swarm_based import ACOR
                model_object = ACOR.OriginalACOR(**solver_options)

            case 'OriginalCSA':
                from mealpy.swarm_based import CSA
                model_object = CSA.OriginalCSA(**solver_options)

            case 'OriginalFFA':
                from mealpy.swarm_based import FFA
                model_object = FFA.OriginalFFA(**solver_options)

            case 'OriginalFA':
                from mealpy.swarm_based import FA
                model_object = FA.OriginalFA(**solver_options)

            case 'OriginalBA':
                from mealpy.swarm_based import BA
                model_object = BA.OriginalBA(**solver_options)

            case 'AdaptiveBA':
                from mealpy.swarm_based import BA
                model_object = BA.AdaptiveBA(**solver_options)

            case 'ModifiedBA':
                from mealpy.swarm_based import BA
                model_object = BA.ModifiedBA(**solver_options)

            case 'OriginalFOA':
                from mealpy.swarm_based import FOA
                model_object = FOA.OriginalFOA(**solver_options)

            case 'BaseFOA':
                from mealpy.swarm_based import FOA
                model_object = FOA.BaseFOA(**solver_options)

            case 'WhaleFOA':
                from mealpy.swarm_based import FOA
                model_object = FOA.WhaleFOA(**solver_options)

            case 'OriginalSSpiderO':
                from mealpy.swarm_based import SSpiderO
                model_object = SSpiderO.OriginalSSpiderO(**solver_options)

            case 'OriginalGWO':
                from mealpy.swarm_based import GWO
                model_object = GWO.OriginalGWO(**solver_options)

            case 'RW_GWO':
                from mealpy.swarm_based import GWO
                model_object = GWO.RW_GWO(**solver_options)

            case 'OriginalSSpiderA':
                from mealpy.swarm_based import SSpiderA
                model_object = SSpiderA.OriginalSSpiderA(**solver_options)

            case 'OriginalALO':
                from mealpy.swarm_based import ALO
                model_object = ALO.OriginalALO(**solver_options)

            case 'BaseALO':
                from mealpy.swarm_based import ALO
                model_object = ALO.BaseALO(**solver_options)

            case 'OriginalMFO':
                from mealpy.swarm_based import MFO
                model_object = MFO.OriginalMFO(**solver_options)

            case 'BaseMFO':
                from mealpy.swarm_based import MFO
                model_object = MFO.BaseMFO(**solver_options)

            case 'OriginalEHO':
                from mealpy.swarm_based import EHO
                model_object = EHO.OriginalEHO(**solver_options)

            case 'OriginalJA':
                from mealpy.swarm_based import JA
                model_object = JA.OriginalJA(**solver_options)

            case 'BaseJA':
                from mealpy.swarm_based import JA
                model_object = JA.BaseJA(**solver_options)

            case 'LevyJA':
                from mealpy.swarm_based import JA
                model_object = JA.LevyJA(**solver_options)

            case 'OriginalWOA':
                from mealpy.swarm_based import WOA
                model_object = WOA.OriginalWOA(**solver_options)

            case 'HI_WOA':
                from mealpy.swarm_based import WOA
                model_object = WOA.HI_WOA(**solver_options)

            case 'OriginalDO':
                from mealpy.swarm_based import DO
                model_object = DO.OriginalDO(**solver_options)

            case 'OriginalBSA':
                from mealpy.swarm_based import BSA
                model_object = BSA.OriginalBSA(**solver_options)

            case 'OriginalSHO':
                from mealpy.swarm_based import SHO
                model_object = SHO.OriginalSHO(**solver_options)

            case 'OriginalSSO':
                from mealpy.swarm_based import SSO
                model_object = SSO.OriginalSSO(**solver_options)

            case 'OriginalSRSR':
                from mealpy.swarm_based import SRSR
                model_object = SRSR.OriginalSRSR(**solver_options)

            case 'OriginalGOA':
                from mealpy.swarm_based import GOA
                model_object = GOA.OriginalGOA(**solver_options)

            case 'OriginalCOA':
                from mealpy.swarm_based import COA
                model_object = COA.OriginalCOA(**solver_options)

            case 'OriginalMSA':
                from mealpy.swarm_based import MSA
                model_object = MSA.OriginalMSA(**solver_options)

            case 'OriginalSLO':
                from mealpy.swarm_based import SLO
                model_object = SLO.OriginalSLO(**solver_options)

            case 'ModifiedSLO':
                from mealpy.swarm_based import SLO
                model_object = SLO.ModifiedSLO(**solver_options)

            case 'ImprovedSLO':
                from mealpy.swarm_based import SLO
                model_object = SLO.ImprovedSLO(**solver_options)

            case 'OriginalNMRA':
                from mealpy.swarm_based import NMRA
                model_object = NMRA.OriginalNMRA(**solver_options)

            case 'ImprovedNMRA':
                from mealpy.swarm_based import NMRA
                model_object = NMRA.ImprovedNMRA(**solver_options)

            case 'OriginalPFA':
                from mealpy.swarm_based import PFA
                model_object = PFA.OriginalPFA(**solver_options)

            case 'OriginalSFO':
                from mealpy.swarm_based import SFO
                model_object = SFO.OriginalSFO(**solver_options)

            case 'ImprovedSFO':
                from mealpy.swarm_based import SFO
                model_object = SFO.ImprovedSFO(**solver_options)
                
            case 'OriginalHHO':
                from mealpy.swarm_based import HHO
                model_object = HHO.OriginalHHO(**solver_options)

            case 'OriginalMRFO':
                from mealpy.swarm_based import MRFO
                model_object = MRFO.OriginalMRFO(**solver_options)

            case 'OriginalBES':
                from mealpy.swarm_based import BES
                model_object = BES.OriginalBES(**solver_options)

            case 'OriginalSSA':
                from mealpy.swarm_based import SSA
                model_object = SSA.OriginalSSA(**solver_options)

            case 'BaseSSA':
                from mealpy.swarm_based import SSA
                model_object = SSA.BaseSSA(**solver_options)

            case 'OriginalHGS':
                from mealpy.swarm_based import HGS
                model_object = HGS.OriginalHGS(**solver_options)

            case 'OriginalAO':
                from mealpy.swarm_based import AO
                model_object = AO.OriginalAO(**solver_options)

            case 'GWO_WOA':
                from mealpy.swarm_based import GWO
                model_object = GWO.OriginalGWO(**solver_options)

            case 'OriginalMPA':
                from mealpy.swarm_based import MPA
                model_object = MPA.OriginalMPA(**solver_options)

            case 'OriginalHBA':
                from mealpy.swarm_based import HBA
                model_object = HBA.OriginalHBA(**solver_options)

            case 'OriginalSCSO':
                from mealpy.swarm_based import SCSO
                model_object = SCSO.OriginalSCSO(**solver_options)

            case 'OriginalTSO':
                from mealpy.swarm_based import TSO
                model_object = TSO.OriginalTSO(**solver_options)

            case 'OriginalAVOA':
                from mealpy.swarm_based import AVOA
                model_object = AVOA.OriginalAVOA(**solver_options)

            case 'OriginalAGTO':
                from mealpy.swarm_based import AGTO
                model_object = AGTO.OriginalAGTO(**solver_options)

            case 'OriginalARO':
                from mealpy.swarm_based import ARO
                model_object = ARO.OriginalARO(**solver_options)

            #============ Physics

            case 'OriginalSA':
                from mealpy.physics_based import SA
                model_object = SA.OriginalSA(**solver_options)

            case 'OriginalWDO':
                from mealpy.physics_based import WDO
                model_object = WDO.OriginalWDO(**solver_options)

            case 'OriginalMVO':
                from mealpy.physics_based import MVO
                model_object = MVO.OriginalMVO(**solver_options)

            case 'BaseMVO':
                from mealpy.physics_based import MVO
                model_object = MVO.BaseMVO(**solver_options)

            case 'OriginalTWO':
                from mealpy.physics_based import TWO
                model_object = TWO.OriginalTWO(**solver_options)

            case 'OppoTWO':
                from mealpy.physics_based import TWO
                model_object = TWO.OppoTWO(**solver_options)

            case 'LevyTWO':
                from mealpy.physics_based import TWO
                model_object = TWO.LevyTWO(**solver_options)

            case 'EnhancedTWO':
                from mealpy.physics_based import TWO
                model_object = TWO.EnhancedTWO(**solver_options)

            case 'OriginalEFO':
                from mealpy.physics_based import EFO
                model_object = EFO.OriginalEFO(**solver_options)

            case 'BaseEFO':
                from mealpy.physics_based import EFO
                model_object = EFO.BaseEFO(**solver_options)

            case 'OriginalNRO':
                from mealpy.physics_based import NRO
                model_object = NRO.OriginalNRO(**solver_options)

            case 'OriginalHGSO':
                from mealpy.physics_based import HGSO
                model_object = HGSO.OriginalHGSO(**solver_options)

            case 'OriginalASO':
                from mealpy.physics_based import ASO
                model_object = ASO.OriginalASO(**solver_options)

            case 'OriginalEO':
                from mealpy.physics_based import EO
                model_object = EO.OriginalEO(**solver_options)

            case 'ModifiedEO':
                from mealpy.physics_based import EO
                model_object = EO.ModifiedEO(**solver_options)

            case 'AdaptiveEO':
                from mealpy.physics_based import EO
                model_object = EO.AdaptiveEO(**solver_options)

            case 'OriginalArchOA':
                from mealpy.physics_based import ArchOA
                model_object = ArchOA.OriginalArchOA(**solver_options)

            #============ Human

            case 'OriginalCA':
                from mealpy.human_based import CA
                model_object = CA.OriginalCA(**solver_options)

            case 'OriginalICA':
                from mealpy.human_based import ICA
                model_object = ICA.OriginalICA(**solver_options)

            case 'OriginalTLO':
                from mealpy.human_based import TLO
                model_object = TLO.OriginalTLO(**solver_options)
            
            case 'BaseTLO':
                from mealpy.human_based import TLO
                model_object = TLO.BaseTLO(**solver_options)

            case 'ITLO':
                from mealpy.human_based import TLO
                model_object = TLO.ImprovedTLO(**solver_options)

            case 'OriginalBSO':
                from mealpy.human_based import BSO
                model_object = BSO.OriginalBSO(**solver_options)

            case 'ImprovedBSO':
                from mealpy.human_based import BSO
                model_object = BSO.ImprovedBSO(**solver_options)

            case 'OriginalQSA':
                from mealpy.human_based import QSA
                model_object = QSA.OriginalQSA(**solver_options)

            case 'BaseQSA':
                from mealpy.human_based import QSA
                model_object = QSA.BaseQSA(**solver_options)

            case 'OppoQSA':
                from mealpy.human_based import QSA
                model_object = QSA.OppoQSA(**solver_options)

            case 'LevyQSA':
                from mealpy.human_based import QSA
                model_object = QSA.LevyQSA(**solver_options)

            case 'ImprovedQSA':
                from mealpy.human_based import QSA
                model_object = QSA.ImprovedQSA(**solver_options)

            case 'OriginalSARO':
                from mealpy.human_based import SARO
                model_object = SARO.OriginalSARO(**solver_options)

            case 'BaseSARO':
                from mealpy.human_based import SARO
                model_object = SARO.BaseSARO(**solver_options)

            case 'OriginalLCO':
                from mealpy.human_based import LCO
                model_object = LCO.OriginalLCO(**solver_options)
                
            case 'BaseLCO':
                from mealpy.human_based import LCO
                model_object = LCO.BaseLCO(**solver_options)

            case 'ImprovedLCO':
                from mealpy.human_based import LCO
                model_object = LCO.ImprovedLCO(**solver_options)

            case 'OriginalSSDO':
                from mealpy.human_based import SSDO
                model_object = SSDO.OriginalSSDO(**solver_options)

            case 'OriginalGSKA':
                from mealpy.human_based import GSKA
                model_object = GSKA.OriginalGSKA(**solver_options)

            case 'BaseGSKA':
                from mealpy.human_based import GSKA
                model_object = GSKA.BaseGSKA(**solver_options)

            case 'OriginalCHIO':
                from mealpy.human_based import CHIO
                model_object = CHIO.OriginalCHIO(**solver_options)

            case 'BaseCHIO':
                from mealpy.human_based import CHIO
                model_object = CHIO.BaseCHIO(**solver_options)

            case 'OriginalFBIO':
                from mealpy.human_based import FBIO
                model_object = FBIO.OriginalFBIO(**solver_options)

            case 'BaseFBIO':
                from mealpy.human_based import FBIO
                model_object = FBIO.BaseFBIO(**solver_options)

            case 'OriginalBRO':
                from mealpy.human_based import BRO
                model_object = BRO.OriginalBRO(**solver_options)
            
            case 'BaseBRO':
                from mealpy.human_based import BRO
                model_object = BRO.BaseBRO(**solver_options)

            case 'OriginalSPBO':
                from mealpy.human_based import SPBO
                model_object = SPBO.OriginalSPBO(**solver_options)

            case 'DevSPBO':
                from mealpy.human_based import SPBO
                model_object = SPBO.DevSPBO(**solver_options)

            case 'OriginalDMOA':
                print('OriginalDMOA: Not supported yet. Using SPBO instead')
                # from mealpy.human_based import DMOA
                # model_object = DMOA.OriginalDMOA(**solver_options)
                from mealpy.human_based import SPBO
                model_object = SPBO.DevSPBO(**solver_options)

            case 'DevDMOA':
                print('DevDMOA: Not supported yet. Using SPBO instead')
                # from mealpy.human_based import DMOA
                # model_object = DMOA.DevDMOA(**solver_options)
                from mealpy.human_based import SPBO
                model_object = SPBO.DevSPBO(**solver_options)

            #============ Bio

            case 'OriginalIWO':
                from mealpy.bio_based import IWO
                model_object = IWO.OriginalIWO(**solver_options)

            case 'OriginalBBO':
                from mealpy.bio_based import BBO
                model_object = BBO.OriginalBBO(**solver_options)

            case 'BaseBBO':
                from mealpy.bio_based import BBO
                model_object = BBO.BaseBBO(**solver_options)

            case 'OriginalVCS':
                from mealpy.bio_based import VCS
                model_object = VCS.OriginalVCS(**solver_options)

            case 'BaseVCS':
                from mealpy.bio_based import VCS
                model_object = VCS.BaseVCS(**solver_options)

            case 'OriginalSBO':
                from mealpy.bio_based import SBO
                model_object = SBO.OriginalSBO(**solver_options)

            case 'BaseSBO':
                from mealpy.bio_based import SBO
                model_object = SBO.BaseSBO(**solver_options)

            case 'OriginalEOA':
                from mealpy.bio_based import EOA
                model_object = EOA.OriginalEOA(**solver_options)

            case 'OriginalWHO':
                from mealpy.bio_based import WHO
                model_object = WHO.OriginalWHO(**solver_options)

            case 'OriginalSMA':
                from mealpy.bio_based import SMA
                model_object = SMA.OriginalSMA(**solver_options)

            case 'BaseSMA':
                from mealpy.bio_based import SMA
                model_object = SMA.BaseSMA(**solver_options)

            case 'OriginalBMO':
                from mealpy.bio_based import BMO
                model_object = BMO.OriginalBMO(**solver_options)

            case 'OriginalTSA':
                from mealpy.bio_based import TSA
                model_object = TSA.OriginalTSA(**solver_options)

            case 'OriginalSOS':
                from mealpy.bio_based import SOS
                model_object = SOS.OriginalSOS(**solver_options)

            case 'OriginalSOA':
                from mealpy.bio_based import SOA
                model_object = SOA.OriginalSOA(**solver_options)

            case 'DevSOA':
                from mealpy.bio_based import SOA
                model_object = SOA.DevSOA(**solver_options)

            #============ System

            case 'OriginalGCO':
                from mealpy.system_based import GCO
                model_object = GCO.OriginalGCO(**solver_options)

            case 'BaseGCO':
                from mealpy.system_based import GCO
                model_object = GCO.BaseGCO(**solver_options)

            case 'OriginalWCA':
                from mealpy.system_based import WCA
                model_object = WCA.OriginalWCA(**solver_options)

            case 'OriginalAEO':
                from mealpy.system_based import AEO
                model_object = AEO.OriginalAEO(**solver_options)

            case 'EnhancedAEO':
                from mealpy.system_based import AEO
                model_object = AEO.EnhancedAEO(**solver_options)

            case 'ModifiedAEO':
                from mealpy.system_based import AEO
                model_object = AEO.ModifiedAEO(**solver_options)

            case 'ImprovedAEO':
                from mealpy.system_based import AEO
                model_object = AEO.ImprovedAEO(**solver_options)

            case 'AdaptiveAEO':
                from mealpy.system_based import AEO
                model_object = AEO.AdaptiveAEO(**solver_options)

            #============ Math

            case 'OriginalHC':
                from mealpy.math_based import HC
                model_object = HC.OriginalHC(**solver_options)

            case 'SwarmHC':
                from mealpy.math_based import HC
                model_object = HC.SwarmHC(**solver_options)

            case 'OriginalCEM':
                from mealpy.math_based import CEM
                model_object = CEM.OriginalCEM(**solver_options)

            case 'OriginalSCA':
                from mealpy.math_based import SCA
                model_object = SCA.OriginalSCA(**solver_options)

            case 'BaseSCA':
                from mealpy.math_based import SCA
                model_object = SCA.BaseSCA(**solver_options)

            case 'OriginalGBO':
                from mealpy.math_based import GBO
                model_object = GBO.OriginalGBO(**solver_options)

            case 'OrginalAOA':
                from mealpy.math_based import AOA
                model_object = AOA.OriginalAOA(**solver_options)

            case 'OriginalCGO':
                from mealpy.math_based import CGO
                model_object = CGO.OriginalCGO(**solver_options)

            case 'OriginalPSS':
                from mealpy.math_based import PSS
                model_object = PSS.OriginalPSS(**solver_options)

            case 'OriginalINFO':
                from mealpy.math_based import INFO
                model_object = INFO.OriginalINFO(**solver_options)

            case 'OriginalRUN':
                from mealpy.math_based import RUN
                model_object = RUN.OriginalRUN(**solver_options)

            case 'OriginalCircleSA':
                from mealpy.math_based import CircleSA
                model_object = CircleSA.OriginalCircleSA(**solver_options)
            
            #============ Music
            
            case 'OriginalHS':
                from mealpy.music_based import HS
                model_object = HS.OriginalHS(**solver_options)

            case 'BaseHS':
                from mealpy.music_based import HS
                model_object = HS.BaseHS(**solver_options)
        
        return model_object