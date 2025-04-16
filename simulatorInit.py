from pm4py_dcr_feature_dcr_in_pm4py_revised.pm4py.objects.dcr.obj import DcrGraph

def findKey(jsn : dict, key : str):
    if key in jsn.keys():
        return jsn[key]
    
    for i in jsn.values():
        if isinstance(i, dict):
            res = findKey(i, key)
            if res is not None:
                return res
        elif isinstance(i, list):
            for j in i:
                if isinstance(j, dict):
                    res = findKey(j, key)
                    if res is not None:
                        return res
        
    return None

def createDCRgraph(graph):
    jsn = graph['graph']
    
    dcr = DcrGraph()

    rel = findKey(jsn, 'constraints')
    events = findKey(jsn, 'labelMapping')
    included = findKey(jsn, 'included')
    pending = findKey(jsn, 'pendingResponse')

    # TODO: Add data to DcrGraph()
    return events
