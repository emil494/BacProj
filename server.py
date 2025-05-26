import sys
import os


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))  # Set PROJECT_ROOT to the current directory (BacProj)
sys.path.insert(0, PROJECT_ROOT)

import xmltodict, json
from flask import Flask, request, jsonify
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
        return jsonify({"Status":'Not Logged In/ Invalid Authorization Type'}),403
    
    try:
        dict = xmltodict.parse(xml)
    except:
        return jsonify({"Status":'Misformated request data'}),400
    
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

    return gid,201

@app.get('/api/graphs/<string:GID>')
def getGraph(GID):
    if not dm.checkAccessGraph(request.headers, GID):
        return jsonify({"Status":'Access Denied'}),403
    
    graph = dm.findGraph(GID)
    if graph is not None:
        return jsonify(graph),200
    return jsonify({"Status":"Unknown GID"}),404

@app.get('/api/graphs')
def getGraphs():
    header = request.headers
    if not dm.checkLoggedIn(header):
        return jsonify({"Status":'Not Logged In/ Invalid Authorization Type'}),401
    auth = header['Authorization']
    try:
        graphs = dm.access[auth]
        return jsonify({"GIDs": graphs}),200
    except:
        return jsonify({"Status":'Failed'}),404

@app.delete('/api/graphs/<string:GID>')
def deleteGraph(GID):
    if not dm.checkAccessGraph(request.headers, GID):
        return jsonify({"Status":'Access Denied'}),403
    
    dm.removeGraph(GID,request.headers['Authorization'])
    return jsonify({"Status":"Success"}),200

# Creates a DCRGraph object of GID
@app.post('/api/graphs/<string:GID>/DCRsimulator')
def SimulateInit(GID):
    if not dm.checkAccessGraph(request.headers, GID):
        return jsonify({"Status":'Access Denied'}),403
    
    graph = dm.findGraph(GID)
    if graph:
            dcr = createDCRgraph(graph)
            sid = dm.assignSid()
            graph['SIDs'].append(sid)
            dm.graphIDs[GID] = graph
            jsn = {sid: dcr}
            dm.simIDs.update(jsn)
            return sid,201
    return jsonify({"Status":"Unknown GID"}),404

@app.get('/api/graphs/<string:GID>/sims/<string:SID>')
def getSimulation(GID, SID):
    if not dm.checkAccessSim(request.headers, GID, SID):
        return jsonify({"Status":'Access Denied'}),403
    
    sim = dm.findSim(SID)
    if sim:
        return {SID: sim.__repr__()},200
    return jsonify({"Status":"Unknown SID"}),404

@app.get('/api/graphs/<string:GID>/sims')
def getSims(GID):
    if not dm.checkAccessGraph(request.headers, GID):
        return jsonify({"Status":'Access Denied'}),403
    
    sims = dm.graphIDs[GID]['SIDs']
    return jsonify(sims),200

@app.delete('/api/graphs/<string:GID>/sims/<string:SID>')
def deleteSim(GID, SID):
    if not dm.checkAccessSim(request.headers, GID, SID):
        return jsonify({"Status":'Access Denied'}),403
    
    dm.removeSim(GID, SID)
    return jsonify({"Status":"Success"}),200

@app.get('/api/graphs/<string:GID>/sims/<string:SID>/events')
def getEvents(GID, SID):
    if not dm.checkAccessSim(request.headers, GID, SID):
        return jsonify({"Status":'Access Denied'}),403
    
    sim = dm.findSim(SID)
    if sim:
        return jsonify(sim.label_map),200
    
    return jsonify({"Status":'Unknown SID'}),404

@app.get('/api/graphs/<string:GID>/sims/<string:SID>/relations')
def getRelations(GID, SID):
    if not dm.checkAccessSim(request.headers, GID, SID):
        return jsonify({"Status":'Access Denied'}),403
    
    sim = dm.findSim(SID)
    '''print(sim)'''
    if sim:
        return jsonify(GetAllConds(sim)),200
    
    return jsonify({"Status":'Unknown SID'}),404

@app.get('/api/graphs/<string:GID>/sims/<string:SID>/included')
def getIncluded(GID, SID):
    if not dm.checkAccessSim(request.headers, GID, SID):
        return jsonify({"Status":'Access Denied'}),403
    
    sim = dm.findSim(SID)
    if sim:
        return jsonify(list(sim.marking.included)),200
    
    return jsonify({"Status":'Unknown SID'}),404

@app.get('/api/graphs/<string:GID>/sims/<string:SID>/pending')
def getPending(GID, SID):
    if not dm.checkAccessSim(request.headers, GID, SID):
        return jsonify({"Status":'Access Denied'}),403
    
    sim = dm.findSim(SID)
    if sim:
        return jsonify(list(sim.marking.pending)),200
    
    return jsonify({"Status":'Unknown SID'}),404

@app.get('/api/graphs/<string:GID>/sims/<string:SID>/executed')
def getExecuted(GID, SID):
    if not dm.checkAccessSim(request.headers, GID, SID):
        return jsonify({"Status":'Access Denied'}),403
    
    sim = dm.findSim(SID)
    if sim:
        return jsonify(list(sim.marking.executed))
    
    return jsonify({"Status":'Unknown SID'}),404

@app.put('/api/graphs/<string:GID>/DCRsimulator/<string:SID>/executeEvent/<string:event>')
def executeEvent(GID, SID, event):
    if not dm.checkAccessSim(request.headers, GID, SID):
        return jsonify({"Status":'Access Denied'}),403
    
    sim = dm.findSim(SID)
    if sim:
        res = ExecuteEventOnGraph(sim, event)
        if res is None:
            return jsonify({"Status":{"Unsuccessful": [f"{event}"], "Successful" : []}}), 409
        return jsonify({"Status":'Success'}), 200
    return jsonify({"Status":'Unknown SID'}),404

@app.put('/api/graphs/<string:GID>/DCRsimulator/<string:SID>/executeTrace')
def executeTrace(GID, SID):
    if not dm.checkAccessSim(request.headers, GID, SID):
        return jsonify({"Status":'Access Denied'}),403
    
    sim = dm.findSim(SID)
    if sim:
        jsn = request.data
        failed = []
        try: 
            print('will it?')
            jsn = json.loads(jsn)
            trace = jsn['trace']
            for e in trace:
                if ExecuteEventOnGraph(sim, e) is None:
                    failed.append(e)
                print('yay')
            if len(failed) > 0:
                return jsonify({"Status":{"Unsuccessful": failed, "Successful" : list(set(trace).difference(failed))}}), 409
            return jsonify({"Status":"Success"}), 200
        except:
            return jsonify({"Status":'Misformated request data'}),400
    return jsonify({"Status":'Unknown SID'}),404