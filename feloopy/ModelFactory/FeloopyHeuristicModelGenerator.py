

def GenerateModel(TotVars, Directions, SolverName, AlgOptions):

    match SolverName:

        case 'GWO':
            from ..AlgorithmFactory.Heuristic.GWO import GWO
            ModelObject = GWO(F=TotVars, D=Directions, S=AlgOptions.get('S', 100), T=AlgOptions.get('T', 50))
        
        case 'GA':
            from ..AlgorithmFactory.Heuristic.GA import GA
            ModelObject = GA(F=TotVars, D=Directions, S=AlgOptions.get('S', 100), T=AlgOptions.get('T', 50), Mu=AlgOptions.get('Mu', 0.02), Cr=AlgOptions.get('Cr', 0.7))

        case 'DE':
            from ..AlgorithmFactory.Heuristic.DE import DE
            ModelObject = DE(F=TotVars, D=Directions, S=AlgOptions.get('S', 100), T=AlgOptions.get('T', 50), Mu=AlgOptions.get('Mu', 0.02), Cr=AlgOptions.get('Cr', 0.7))

        case 'SA':
            from ..AlgorithmFactory.Heuristic.SA import SA
            ModelObject = SA(F=TotVars, D=Directions, S=AlgOptions.get('S', 100), T=AlgOptions.get('T', 1), Cc=AlgOptions.get('Cc', 50), Mt=AlgOptions.get('Mt', 1000))

        case 'TS':
            from ..AlgorithmFactory.Heuristic.TS import TS
            ModelObject = TS(F=TotVars, D=Directions, S=AlgOptions.get('S', 100), T=AlgOptions.get('T', 1), C=AlgOptions.get('C', 10))

    return ModelObject
