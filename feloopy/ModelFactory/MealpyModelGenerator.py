
def GenerateModel(SolverName,AlgOptions):

        match SolverName:

            #Evolutionary
            case 'OriginalEP':

                from mealpy.evolutionary_based import EP
                ModelObject = EP.OriginalEP(**AlgOptions)
            
            case 'LevyEP':

                from mealpy.evolutionary_based import EP
                ModelObject = EP.LevyEP(**AlgOptions)

            case 'OriginalES':
                
                from mealpy.evolutionary_based import ES
                ModelObject = ES.OriginalES(**AlgOptions)
            
            case 'LevyES':
                from mealpy.evolutionary_based import ES
                ModelObject = ES.LevyES(**AlgOptions)
            
            case 'OriginalMA':

                from mealpy.evolutionary_based import MA
                ModelObject = MA.OriginalMA(**AlgOptions)
            
            case 'BaseGA':
                from mealpy.evolutionary_based import GA
                ModelObject = GA.BaseGA(**AlgOptions)

            case 'SingleGA':
                from mealpy.evolutionary_based import GA
                ModelObject = GA.SingleGA(**AlgOptions)
            
            case 'MultiGA':
                from mealpy.evolutionary_based import GA
                ModelObject = GA.MultiGA(**AlgOptions)

            case 'EliteSingleGA':
                from mealpy.evolutionary_based import GA
                ModelObject = GA.EliteSingleGA(**AlgOptions)

            case 'EliteMultiGA':
                from mealpy.evolutionary_based import GA
                ModelObject = GA.EliteMultiGA(**AlgOptions)

            case 'BaseDE':
                from mealpy.evolutionary_based import DE
                ModelObject = DE.BaseDE(**AlgOptions)

            case 'JADE':
                from mealpy.evolutionary_based import DE
                ModelObject = DE.JADE(**AlgOptions)

            case 'SADE':
                from mealpy.evolutionary_based import DE
                ModelObject = DE.SADE(**AlgOptions)
            
            case 'SHADE':
                from mealpy.evolutionary_based import DE
                ModelObject = DE.SHADE(**AlgOptions)

            case 'L_SHADE':
                from mealpy.evolutionary_based import DE
                ModelObject = DE.L_SHADE(**AlgOptions)

            case 'SAP_DE':
                from mealpy.evolutionary_based import DE
                ModelObject = DE.SAP_DE(**AlgOptions)

            case 'OriginalFPA':
                from mealpy.evolutionary_based import FPA
                ModelObject = FPA.OriginalFPA(**AlgOptions)

            
            case 'OriginalCRO':
                from mealpy.evolutionary_based import CRO
                ModelObject = CRO.OriginalCRO(**AlgOptions)

            case 'OCRO':
                from mealpy.evolutionary_based import CRO
                ModelObject = CRO.OCRO(**AlgOptions)

            #Swarm
            case 'OriginalPSO':
                from mealpy.swarm_based import PSO
                ModelObject = PSO.OriginalPSO(**AlgOptions)

            
            case 'PPSO':
                from mealpy.swarm_based import PSO
                ModelObject = PSO.PPSO(**AlgOptions)

            case 'HPSO_TVAC':
                from mealpy.swarm_based import PSO
                ModelObject = PSO.HPSO_TVAC(**AlgOptions)

            case 'C_PSO':
                from mealpy.swarm_based import PSO
                ModelObject = PSO.C_PSO(**AlgOptions)

            case 'CL_PSO':
                from mealpy.swarm_based import PSO
                ModelObject = PSO.CL_PSO(**AlgOptions)

            case 'OriginalBFO':
                from mealpy.swarm_based import BFO
                ModelObject = BFO.OriginalBFO(**AlgOptions)

            case 'ABFO':
                from mealpy.swarm_based import BFO
                ModelObject = BFO.OriginalBFO(**AlgOptions)

            case 'OriginalBeesA':
                from mealpy.swarm_based import BeesA
                ModelObject = BeesA.OriginalBeesA(**AlgOptions)

            case 'ProbBeesA':
                from mealpy.swarm_based import BeesA
                ModelObject = BeesA.ProbBeesA(**AlgOptions)

            case 'OriginalCSO':
                from mealpy.swarm_based import CSO
                ModelObject = CSO.OriginalCSO(**AlgOptions)
                
            case 'OriginalABC':
                from mealpy.swarm_based import ABC
                ModelObject = ABC.OriginalABC(**AlgOptions)

            case 'OriginalACOR':
                from mealpy.swarm_based import ACOR
                ModelObject = ACOR.OriginalACOR(**AlgOptions)

            case 'OriginalCSA':
                from mealpy.swarm_based import CSA
                ModelObject = CSA.OriginalCSA(**AlgOptions)

            case 'OriginalFFA':
                from mealpy.swarm_based import FFA
                ModelObject = FFA.OriginalFFA(**AlgOptions)

            case 'OriginalFA':
                from mealpy.swarm_based import FA
                ModelObject = FA.OriginalFA(**AlgOptions)

            case 'OriginalBA':
                from mealpy.swarm_based import BA
                ModelObject = BA.OriginalBA(**AlgOptions)

            case 'AdaptiveBA':
                from mealpy.swarm_based import BA
                ModelObject = BA.AdaptiveBA(**AlgOptions)

            case 'ModifiedBA':
                from mealpy.swarm_based import BA
                ModelObject = BA.ModifiedBA(**AlgOptions)

            case 'OriginalFOA':
                from mealpy.swarm_based import FOA
                ModelObject = FOA.OriginalFOA(**AlgOptions)

            case 'BaseFOA':
                from mealpy.swarm_based import FOA
                ModelObject = FOA.BaseFOA(**AlgOptions)

            case 'WhaleFOA':
                from mealpy.swarm_based import FOA
                ModelObject = FOA.WhaleFOA(**AlgOptions)

            case 'OriginalSSpiderO':
                from mealpy.swarm_based import SSpiderO
                ModelObject = SSpiderO.OriginalSSpiderO(**AlgOptions)

            case 'OriginalGWO':
                from mealpy.swarm_based import GWO
                ModelObject = GWO.OriginalGWO(**AlgOptions)

            case 'RW_GWO':
                from mealpy.swarm_based import GWO
                ModelObject = GWO.RW_GWO(**AlgOptions)

            case 'OriginalSSpiderA':
                from mealpy.swarm_based import SSpiderA
                ModelObject = SSpiderA.OriginalSSpiderA(**AlgOptions)

            case 'OriginalALO':
                from mealpy.swarm_based import ALO
                ModelObject = ALO.OriginalALO(**AlgOptions)

            case 'BaseALO':
                from mealpy.swarm_based import ALO
                ModelObject = ALO.BaseALO(**AlgOptions)

            case 'OriginalMFO':
                from mealpy.swarm_based import MFO
                ModelObject = MFO.OriginalMFO(**AlgOptions)

            case 'BaseMFO':
                from mealpy.swarm_based import MFO
                ModelObject = MFO.BaseMFO(**AlgOptions)

            case 'OriginalEHO':
                from mealpy.swarm_based import EHO
                ModelObject = EHO.OriginalEHO(**AlgOptions)

            case 'OriginalJA':
                from mealpy.swarm_based import JA
                ModelObject = JA.OriginalJA(**AlgOptions)

            case 'BaseJA':
                from mealpy.swarm_based import JA
                ModelObject = JA.BaseJA(**AlgOptions)

            case 'LevyJA':
                from mealpy.swarm_based import JA
                ModelObject = JA.LevyJA(**AlgOptions)

            case 'OriginalWOA':
                from mealpy.swarm_based import WOA
                ModelObject = WOA.OriginalWOA(**AlgOptions)

            case 'HI_WOA':
                from mealpy.swarm_based import WOA
                ModelObject = WOA.HI_WOA(**AlgOptions)

            case 'OriginalDO':
                from mealpy.swarm_based import DO
                ModelObject = DO.OriginalDO(**AlgOptions)

            case 'OriginalBSA':
                from mealpy.swarm_based import BSA
                ModelObject = BSA.OriginalBSA(**AlgOptions)

            case 'OriginalSHO':
                from mealpy.swarm_based import SHO
                ModelObject = SHO.OriginalSHO(**AlgOptions)

            case 'OriginalSSO':
                from mealpy.swarm_based import SSO
                ModelObject = SSO.OriginalSSO(**AlgOptions)

            case 'OriginalSRSR':
                from mealpy.swarm_based import SRSR
                ModelObject = SRSR.OriginalSRSR(**AlgOptions)

            case 'OriginalGOA':
                from mealpy.swarm_based import GOA
                ModelObject = GOA.OriginalGOA(**AlgOptions)

            case 'OriginalCOA':
                from mealpy.swarm_based import COA
                ModelObject = COA.OriginalCOA(**AlgOptions)

            case 'OriginalMSA':
                from mealpy.swarm_based import MSA
                ModelObject = MSA.OriginalMSA(**AlgOptions)

            case 'OriginalSLO':
                from mealpy.swarm_based import SLO
                ModelObject = SLO.OriginalSLO(**AlgOptions)

            case 'ModifiedSLO':
                from mealpy.swarm_based import SLO
                ModelObject = SLO.ModifiedSLO(**AlgOptions)

            case 'ImprovedSLO':
                from mealpy.swarm_based import SLO
                ModelObject = SLO.ImprovedSLO(**AlgOptions)

            case 'OriginalNMRA':
                from mealpy.swarm_based import NMRA
                ModelObject = NMRA.OriginalNMRA(**AlgOptions)

            case 'ImprovedNMRA':
                from mealpy.swarm_based import NMRA
                ModelObject = NMRA.ImprovedNMRA(**AlgOptions)

            case 'OriginalPFA':
                from mealpy.swarm_based import PFA
                ModelObject = PFA.OriginalPFA(**AlgOptions)

            case 'OriginalSFO':
                from mealpy.swarm_based import SFO
                ModelObject = SFO.OriginalSFO(**AlgOptions)

            case 'ImprovedSFO':
                from mealpy.swarm_based import SFO
                ModelObject = SFO.ImprovedSFO(**AlgOptions)
                
            case 'OriginalHHO':
                from mealpy.swarm_based import HHO
                ModelObject = HHO.OriginalHHO(**AlgOptions)

            case 'OriginalMRFO':
                from mealpy.swarm_based import MRFO
                ModelObject = MRFO.OriginalMRFO(**AlgOptions)

            case 'OriginalBES':
                from mealpy.swarm_based import BES
                ModelObject = BES.OriginalBES(**AlgOptions)

            case 'OriginalSSA':
                from mealpy.swarm_based import SSA
                ModelObject = SSA.OriginalSSA(**AlgOptions)

            case 'BaseSSA':
                from mealpy.swarm_based import SSA
                ModelObject = SSA.BaseSSA(**AlgOptions)

            case 'OriginalHGS':
                from mealpy.swarm_based import HGS
                ModelObject = HGS.OriginalHGS(**AlgOptions)

            case 'OriginalAO':
                from mealpy.swarm_based import AO
                ModelObject = AO.OriginalAO(**AlgOptions)

            case 'GWO_WOA':
                from mealpy.swarm_based import GWO
                ModelObject = GWO.OriginalGWO(**AlgOptions)

            case 'OriginalMPA':
                from mealpy.swarm_based import MPA
                ModelObject = MPA.OriginalMPA(**AlgOptions)

            case 'OriginalHBA':
                from mealpy.swarm_based import HBA
                ModelObject = HBA.OriginalHBA(**AlgOptions)

            case 'OriginalSCSO':
                from mealpy.swarm_based import SCSO
                ModelObject = SCSO.OriginalSCSO(**AlgOptions)

            case 'OriginalTSO':
                from mealpy.swarm_based import TSO
                ModelObject = TSO.OriginalTSO(**AlgOptions)

            case 'OriginalAVOA':
                from mealpy.swarm_based import AVOA
                ModelObject = AVOA.OriginalAVOA(**AlgOptions)

            case 'OriginalAGTO':
                from mealpy.swarm_based import AGTO
                ModelObject = AGTO.OriginalAGTO(**AlgOptions)

            case 'OriginalARO':
                from mealpy.swarm_based import ARO
                ModelObject = ARO.OriginalARO(**AlgOptions)

            #Physics
            case 'OriginalSA':
                from mealpy.physics_based import SA
                ModelObject = SA.OriginalSA(**AlgOptions)

            case 'OriginalWDO':
                from mealpy.physics_based import WDO
                ModelObject = WDO.OriginalWDO(**AlgOptions)

            case 'OriginalMVO':
                from mealpy.physics_based import MVO
                ModelObject = MVO.OriginalMVO(**AlgOptions)

            case 'BaseMVO':
                from mealpy.physics_based import MVO
                ModelObject = MVO.BaseMVO(**AlgOptions)

            case 'OriginalTWO':
                from mealpy.physics_based import TWO
                ModelObject = TWO.OriginalTWO(**AlgOptions)

            case 'OppoTWO':
                from mealpy.physics_based import TWO
                ModelObject = TWO.OppoTWO(**AlgOptions)

            case 'LevyTWO':
                from mealpy.physics_based import TWO
                ModelObject = TWO.LevyTWO(**AlgOptions)

            case 'EnhancedTWO':
                from mealpy.physics_based import TWO
                ModelObject = TWO.EnhancedTWO(**AlgOptions)

            case 'OriginalEFO':
                from mealpy.physics_based import EFO
                ModelObject = EFO.OriginalEFO(**AlgOptions)

            case 'BaseEFO':
                from mealpy.physics_based import EFO
                ModelObject = EFO.BaseEFO(**AlgOptions)

            case 'OriginalNRO':
                from mealpy.physics_based import NRO
                ModelObject = NRO.OriginalNRO(**AlgOptions)

            case 'OriginalHGSO':
                from mealpy.physics_based import HGSO
                ModelObject = HGSO.OriginalHGSO(**AlgOptions)

            case 'OriginalASO':
                from mealpy.physics_based import ASO
                ModelObject = ASO.OriginalASO(**AlgOptions)

            case 'OriginalEO':
                from mealpy.physics_based import EO
                ModelObject = EO.OriginalEO(**AlgOptions)

            case 'ModifiedEO':
                from mealpy.physics_based import EO
                ModelObject = EO.ModifiedEO(**AlgOptions)

            case 'AdaptiveEO':
                from mealpy.physics_based import EO
                ModelObject = EO.AdaptiveEO(**AlgOptions)

            case 'OriginalArchOA':
                from mealpy.physics_based import ArchOA
                ModelObject = ArchOA.OriginalArchOA(**AlgOptions)

            #Human
            case 'OriginalCA':
                from mealpy.human_based import CA
                ModelObject = CA.OriginalCA(**AlgOptions)

            case 'OriginalICA':
                from mealpy.human_based import ICA
                ModelObject = ICA.OriginalICA(**AlgOptions)

            case 'OriginalTLO':
                from mealpy.human_based import TLO
                ModelObject = TLO.OriginalTLO(**AlgOptions)
            
            case 'BaseTLO':
                from mealpy.human_based import TLO
                ModelObject = TLO.BaseTLO(**AlgOptions)

            case 'ITLO':
                from mealpy.human_based import TLO
                ModelObject = TLO.ITLO(**AlgOptions)

            case 'OriginalBSO':
                from mealpy.human_based import BSO
                ModelObject = BSO.OriginalBSO(**AlgOptions)

            case 'ImprovedBSO':
                from mealpy.human_based import BSO
                ModelObject = BSO.ImprovedBSO(**AlgOptions)

            case 'OriginalQSA':
                from mealpy.human_based import QSA
                ModelObject = QSA.OriginalQSA(**AlgOptions)

            case 'BaseQSA':
                from mealpy.human_based import QSA
                ModelObject = QSA.BaseQSA(**AlgOptions)

            case 'OppoQSA':
                from mealpy.human_based import QSA
                ModelObject = QSA.OppoQSA(**AlgOptions)

            case 'LevyQSA':
                from mealpy.human_based import QSA
                ModelObject = QSA.LevyQSA(**AlgOptions)

            case 'ImprovedQSA':
                from mealpy.human_based import QSA
                ModelObject = QSA.ImprovedQSA(**AlgOptions)

            case 'OriginalSARO':
                from mealpy.human_based import SARO
                ModelObject = SARO.OriginalSARO(**AlgOptions)

            case 'BaseSARO':
                from mealpy.human_based import SARO
                ModelObject = SARO.BaseSARO(**AlgOptions)

            case 'OriginalLCO':
                from mealpy.human_based import LCO
                ModelObject = LCO.OriginalLCO(**AlgOptions)
                
            case 'BaseLCO':
                from mealpy.human_based import LCO
                ModelObject = LCO.BaseLCO(**AlgOptions)

            case 'ImprovedLCO':
                from mealpy.human_based import LCO
                ModelObject = LCO.ImprovedLCO(**AlgOptions)

            case 'OriginalSSDO':
                from mealpy.human_based import SSDO
                ModelObject = SSDO.OriginalSSDO(**AlgOptions)

            case 'OriginalGSKA':
                from mealpy.human_based import GSKA
                ModelObject = GSKA.OriginalGSKA(**AlgOptions)

            case 'BaseGSKA':
                from mealpy.human_based import GSKA
                ModelObject = GSKA.BaseGSKA(**AlgOptions)

            case 'OriginalCHIO':
                from mealpy.human_based import CHIO
                ModelObject = CHIO.OriginalCHIO(**AlgOptions)

            case 'BaseCHIO':
                from mealpy.human_based import CHIO
                ModelObject = CHIO.BaseCHIO(**AlgOptions)

            case 'OriginalFBIO':
                from mealpy.human_based import FBIO
                ModelObject = FBIO.OriginalFBIO(**AlgOptions)

            case 'BaseFBIO':
                from mealpy.human_based import FBIO
                ModelObject = FBIO.BaseFBIO(**AlgOptions)

            case 'OriginalBRO':
                from mealpy.human_based import BRO
                ModelObject = BRO.OriginalBRO(**AlgOptions)
            
            case 'BaseBRO':
                from mealpy.human_based import BRO
                ModelObject = BRO.BaseBRO(**AlgOptions)

            case 'OriginalSPBO':
                from mealpy.human_based import SPBO
                ModelObject = SPBO.OriginalSPBO(**AlgOptions)

            case 'DevSPBO':
                from mealpy.human_based import SPBO
                ModelObject = SPBO.DevSPBO(**AlgOptions)

            case 'OriginalDMOA':
                from mealpy.human_based import DMOA
                ModelObject = DMOA.OriginalDMOA(**AlgOptions)

            case 'DevDMOA':
                from mealpy.human_based import DMOA
                ModelObject = DMOA.DevDMOA(**AlgOptions)

            #Bio
            case 'OriginalIWO':
                from mealpy.bio_based import IWO
                ModelObject = IWO.OriginalIWO(**AlgOptions)

            case 'OriginalBBO':
                from mealpy.bio_based import BBO
                ModelObject = BBO.OriginalBBO(**AlgOptions)

            case 'BaseBBO':
                from mealpy.bio_based import BBO
                ModelObject = BBO.BaseBBO(**AlgOptions)

            case 'OriginalVCS':
                from mealpy.bio_based import VCS
                ModelObject = VCS.OriginalVCS(**AlgOptions)

            case 'BaseVCS':
                from mealpy.bio_based import VCS
                ModelObject = VCS.BaseVCS(**AlgOptions)

            case 'OriginalSBO':
                from mealpy.bio_based import SBO
                ModelObject = SBO.OriginalSBO(**AlgOptions)

            case 'BaseSBO':
                from mealpy.bio_based import SBO
                ModelObject = SBO.BaseSBO(**AlgOptions)

            case 'OriginalEOA':
                from mealpy.bio_based import EOA
                ModelObject = EOA.OriginalEOA(**AlgOptions)

            case 'OriginalWHO':
                from mealpy.bio_based import WHO
                ModelObject = WHO.OriginalWHO(**AlgOptions)

            case 'OriginalSMA':
                from mealpy.bio_based import SMA
                ModelObject = SMA.OriginalSMA(**AlgOptions)

            case 'BaseSMA':
                from mealpy.bio_based import SMA
                ModelObject = SMA.BaseSMA(**AlgOptions)

            case 'OriginalBMO':
                from mealpy.bio_based import BMO
                ModelObject = BMO.OriginalBMO(**AlgOptions)

            case 'OriginalTSA':
                from mealpy.bio_based import TSA
                ModelObject = TSA.OriginalTSA(**AlgOptions)

            case 'OriginalSOS':
                from mealpy.bio_based import SOS
                ModelObject = SOS.OriginalSOS(**AlgOptions)

            case 'OriginalSOA':
                from mealpy.bio_based import SOA
                ModelObject = SOA.OriginalSOA(**AlgOptions)

            case 'DevSOA':
                from mealpy.bio_based import SOA
                ModelObject = SOA.DevSOA(**AlgOptions)

            #System
            case 'OriginalGCO':
                from mealpy.system_based import GCO
                ModelObject = GCO.OriginalGCO(**AlgOptions)

            case 'BaseGCO':
                from mealpy.system_based import GCO
                ModelObject = GCO.BaseGCO(**AlgOptions)

            case 'OriginalWCA':
                from mealpy.system_based import WCA
                ModelObject = WCA.OriginalWCA(**AlgOptions)

            case 'OriginalAEO':
                from mealpy.system_based import AEO
                ModelObject = AEO.OriginalAEO(**AlgOptions)

            case 'EnhancedAEO':
                from mealpy.system_based import AEO
                ModelObject = AEO.EnhancedAEO(**AlgOptions)

            case 'ModifiedAEO':
                from mealpy.system_based import AEO
                ModelObject = AEO.ModifiedAEO(**AlgOptions)

            case 'ImprovedAEO':
                from mealpy.system_based import AEO
                ModelObject = AEO.ImprovedAEO(**AlgOptions)

            case 'AdaptiveAEO':
                from mealpy.system_based import AEO
                ModelObject = AEO.AdaptiveAEO(**AlgOptions)

            #Math
            case 'OriginalHC':
                from mealpy.math_based import HC
                ModelObject = HC.OriginalHC(**AlgOptions)

            case 'SwarmHC':
                from mealpy.math_based import HC
                ModelObject = HC.SwarmHC(**AlgOptions)

            case 'OriginalCEM':
                from mealpy.math_based import CEM
                ModelObject = CEM.OriginalCEM(**AlgOptions)

            case 'OriginalSCA':
                from mealpy.math_based import SCA
                ModelObject = SCA.OriginalSCA(**AlgOptions)

            case 'BaseSCA':
                from mealpy.math_based import SCA
                ModelObject = SCA.BaseSCA(**AlgOptions)

            case 'OriginalGBO':
                from mealpy.math_based import GBO
                ModelObject = GBO.OriginalGBO(**AlgOptions)

            case 'OrginalAOA':
                from mealpy.math_based import AOA
                ModelObject = AOA.OriginalAOA(**AlgOptions)

            case 'OriginalCGO':
                from mealpy.math_based import CGO
                ModelObject = CGO.OriginalCGO(**AlgOptions)

            case 'OriginalPSS':
                from mealpy.math_based import PSS
                ModelObject = PSS.OriginalPSS(**AlgOptions)

            case 'OriginalINFO':
                from mealpy.math_based import INFO
                ModelObject = INFO.OriginalINFO(**AlgOptions)

            case 'OriginalRUN':
                from mealpy.math_based import RUN
                ModelObject = RUN.OriginalRUN(**AlgOptions)

            case 'OriginalCircleSA':
                from mealpy.math_based import CircleSA
                ModelObject = CircleSA.OriginalCircleSA(**AlgOptions)
            
            #Music
            case 'OriginalHS':
                from mealpy.music_based import HS
                ModelObject = HS.OriginalHS(**AlgOptions)

            case 'BaseHS':
                from mealpy.music_based import HS
                ModelObject = HS.BaseHS(**AlgOptions)
        
        return ModelObject