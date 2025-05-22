
import xmltodict, json
from flask import Flask, request
import xml.etree.ElementTree as ET
from pm4py.objects.dcr.hierarchical.obj import HierarchicalDcrGraph
from simulatorInit import createDCRgraph, ExecuteEventOnGraph, GetAllConds
from dataManager import dataManager

app = Flask(__name__)
dm = dataManager()

def replaceAllInstances(input, old, new):
    if isinstance(input, dict):
        return {k: replaceAllInstances(v, old, new) for k, v in input.items()}
    elif isinstance(input, list):
        return [replaceAllInstances(elem, old, new) for elem in input]
    elif input == old:
        return new
    return input


@app.post('/api/utility/xml2dcr')
def loadXML():
    xml = request.data
    header = request.headers
    if not dm.checkLoggedIn(header):
        return 'Not Logged In/ Invalid Authorization Type'
    
    try:
        dict = xmltodict.parse(xml)
    except:
        return 'Misformated request data'
    
    dict = replaceAllInstances(dict, 'null', None) # For easier python handling
    gid = dm.assignGid()
    jsn = {gid: {'SIDs': [], 'graph': dict}}
    dm.graphIDs.update(jsn)

    auth = header['Authorization']

    if (gidList := dm.findAccess(auth)) is None:
        jsn = {f'{auth}': [gid]}
        dm.access.update(jsn)
    else:
        gidList.append(gid)
        dm.access[f'{auth}'] = gidList
    print(dm.access)

    return gid

@app.get('/api/graphs/<string:GID>')
def getGraph(GID):
    if not dm.checkAccessGraph(request.headers, GID):
        return 'Access Denied'
    
    graph = dm.findGraph(GID)
    if graph is not None:
        return graph
    return "Unknown GID"

@app.get('/api/graphs')
def getGraphs():
    header = request.headers
    if not dm.checkLoggedIn(header):
        return 'Not Logged In/ Invalid Authorization Type'
    auth = header['Authorization']
    try:
        graphs = dm.access[auth]
        return graphs
    except:
        return 'Failed'

@app.delete('/api/graphs/<string:GID>')
def deleteGraph(GID):
    if not dm.checkAccessGraph(request.headers, GID):
        return 'Access Denied'
    
    dm.removeGraph(GID,request.headers['Authorization'])
    return "Sucess"

# Creates a DCRGraph object of GID
@app.post('/api/graphs/<string:GID>/DCRsimulator')
def SimulateInit(GID):
    if not dm.checkAccessGraph(request.headers, GID):
        return 'Access Denied'
    
    graph = dm.findGraph(GID)
    if graph:
            dcr = createDCRgraph(graph)
            sid = dm.assignSid()
            graph['SIDs'].append(sid)
            dm.graphIDs[GID] = graph
            jsn = {sid: dcr}
            dm.simIDs.update(jsn)
            return {sid: dcr.__repr__()}
    return "Unknown GID"

@app.get('/api/graphs/<string:GID>/sims/<string:SID>')
def getSimulation(GID, SID):
    if not dm.checkAccessSim(request.headers, GID, SID):
        return 'Access Denied'
    
    sim = dm.findSim(SID)
    if sim:
        return {SID: sim.__repr__()}
    return "Unknown SID"

@app.get('/api/graphs/<string:GID>/sims')
def getSims(GID):
    if not dm.checkAccessGraph(request.headers, GID):
        return 'Access Denied'
    
    sims = dm.graphIDs[GID]['SIDs']
    return sims

@app.delete('/api/graphs/<string:GID>/sims/<string:SID>')
def deleteSim(GID, SID):
    if not dm.checkAccessSim(request.headers, GID, SID):
        return 'Access Denied'
    
    dm.removeSim(GID, SID)
    return "Sucess"

@app.get('/api/graphs/<string:GID>/sims/<string:SID>/events')
def getEvents(GID, SID):
    if not dm.checkAccessSim(request.headers, GID, SID):
        return 'Access Denied'
    
    sim = dm.findSim(SID)
    if sim:
        return sim.label_map
    
    return 'Unknown SID'

@app.get('/api/graphs/<string:GID>/sims/<string:SID>/relations')
def getRelations(GID, SID):
    if not dm.checkAccessSim(request.headers, GID, SID):
        return 'Access Denied'
    
    sim = dm.findSim(SID)
    print(sim)
    if sim:
        return GetAllConds(sim)
    
    return 'Unknown SID'

@app.get('/api/graphs/<string:GID>/sims/<string:SID>/included')
def getIncluded(GID, SID):
    if not dm.checkAccessSim(request.headers, GID, SID):
        return 'Access Denied'
    
    sim = dm.findSim(SID)
    if sim:
        return list(sim.marking.included)
    
    return 'Unknown SID'

@app.get('/api/graphs/<string:GID>/sims/<string:SID>/pending')
def getPending(GID, SID):
    if not dm.checkAccessSim(request.headers, GID, SID):
        return 'Access Denied'
    
    sim = dm.findSim(SID)
    if sim:
        return list(sim.marking.pending)
    
    return 'Unknown SID'

@app.get('/api/graphs/<string:GID>/sims/<string:SID>/executed')
def getExecuted(GID, SID):
    if not dm.checkAccessSim(request.headers, GID, SID):
        return 'Access Denied'
    
    sim = dm.findSim(SID)
    if sim:
        return list(sim.marking.executed)
    
    return 'Unknown SID'

@app.put('/api/graphs/<string:GID>/DCRsimulator/<string:SID>/executeEvent/<string:event>')
def executeEvent(GID, SID, event):
    if not dm.checkAccessSim(request.headers, GID, SID):
        return 'Access Denied'
    
    sim = dm.findSim(SID)
    if sim:
        res = ExecuteEventOnGraph(sim, event)
        if not ("Unknown event" in res):
            return "Success"
        return res # Unknown event
    return 'Unknown SID'

@app.put('/api/graphs/<string:GID>/DCRsimulator/<string:SID>/executeTrace')
def executeTrace(GID, SID):
    if not dm.checkAccessSim(request.headers, GID, SID):
        return 'Access Denied'
    
    sim = dm.findSim(SID)
    if sim:
        jsn = request.data

        try: 
            jsn = json.loads(jsn)
            trace = jsn['trace']
            for e in trace:
                res = ExecuteEventOnGraph(sim, e)
                if "Unknown event" in res:
                    return res
            return "Success"
        except:
            return 'Misformated request data'
    return 'Unknown SID'





# TODO: Structured tests