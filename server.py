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
    """
    replaceAllInstances replaces all instances of "old" with "new" in the given input. 
    Instances can only be part of the items, not the keys of json.

    :param input: data structured as json
    :param old: Keyword you want replaced
    :param new: The item to want old to be replaced by
    :returns: A modified version of "input" with requested replacements
    """
    if isinstance(input, dict):
        return {k: replaceAllInstances(v, old, new) for k, v in input.items()}
    elif isinstance(input, list):
        return [replaceAllInstances(elem, old, new) for elem in input]
    elif input == old:
        return new
    return input

@app.post('/api/utility/xml2dcr')
def loadXML():
    """
    Loads XML from HTTP headers of DCR graphs of DCRgraphs.net format. Stores the graphs as json and ties it to the signed in user.

    :returns: If successful, GID and code 201, 
            if not logged in, Status and code 403, 
            if malformed request data, status and code 400
    """
    xml = request.data
    header = request.headers
    if not dm.checkLoggedIn(header):
        return jsonify({"Status":'Not Logged In/ Invalid Authorization Type'}),403
    
    try:
        dict = xmltodict.parse(xml)
    except:
        return jsonify({"Status":'Malformed request data'}),400
    
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

    return jsonify({'gid' : gid}),201

@app.get('/api/graphs/<string:GID>')
def getGraph(GID):
    """
    Fetches a specific graph based on GID

    :param GID: ID of a graph

    :returns: If successful, json representation of graph and code 200, 
            if not correct security key, Status and code 403, 
            otherwise unknown GID, status and code 404 #At the moment not reachable because of security strictness
    """
    if not dm.checkAccessGraph(request.headers, GID):
        return jsonify({"Status":'Access Denied'}),403
    
    graph = dm.findGraph(GID)
    if graph is not None:
        return jsonify(graph),200
    return jsonify({"Status":"Unknown GID"}),404

@app.get('/api/graphs')
def getGraphs():
    """
    Fetches all GIDs a user has access to

    :returns: If successful, list of GIDs and code 200, 
            if not logged in, Status and code 401, 
            otherwise failed due to unknown user, status and code 404
    """
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
    """
    Deletes a graph and all associated simulations

    :param GID: ID of graph

    :returns: if not correct security key, Status and code 403, 
            otherwise successful, status and code 200 
    """
    if not dm.checkAccessGraph(request.headers, GID):
        return jsonify({"Status":'Access Denied'}),403
    
    dm.removeGraph(GID,request.headers['Authorization'])
    return jsonify({"Status":"Success"}),200

@app.post('/api/graphs/<string:GID>/DCRsimulator')
def SimulateInit(GID):
    """
    Creates a simulation of a graph as a DCR object, that will be tied to the graph.

    :param GID: ID of graph

    :returns: if successful, SID and code 201
            if not correct security key, Status and code 403, 
            otherwise, unknown GID and code 404
    """
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
            return jsonify({'sid' : sid}),201
    return jsonify({"Status":"Unknown GID"}),404

@app.get('/api/graphs/<string:GID>/sims/<string:SID>')
def getSimulation(GID, SID):
    """
    Gets a specific simulation tied to a graph

    :param GID: ID of graph
    :param SID: ID of simulation

    :returns: if successful, string representation of simulation and code 200
            if not correct security key, Status and code 403, 
            otherwise, unknown SID and code 404
    """
    if not dm.checkAccessSim(request.headers, GID, SID):
        return jsonify({"Status":'Access Denied'}),403
    
    sim = dm.findSim(SID)
    if sim:
        return {SID: sim.__repr__()},200
    return jsonify({"Status":"Unknown SID"}),404

@app.get('/api/graphs/<string:GID>/sims')
def getSims(GID):
    """
    Fetches a list of simulations of a graph

    :param GID: ID of graph

    :returns: if not correct security key, Status and code 403, 
            otherwise, successful, string representation of simulation and code 200
    """
    if not dm.checkAccessGraph(request.headers, GID):
        return jsonify({"Status":'Access Denied'}),403
    
    sims = dm.graphIDs[GID]['SIDs']
    return jsonify(sims),200

@app.delete('/api/graphs/<string:GID>/sims/<string:SID>')
def deleteSim(GID, SID):
    """
    Deletes a specific simulation of a graph

    :param GID: ID of graph
    :param SID: ID of simulation

    :returns: if not correct security key, Status and code 403, 
            otherwise, successful, Status and code 200
    """
    if not dm.checkAccessSim(request.headers, GID, SID):
        return jsonify({"Status":'Access Denied'}),403
    
    dm.removeSim(GID, SID)
    return jsonify({"Status":"Success"}),200

@app.get('/api/graphs/<string:GID>/sims/<string:SID>/events')
def getEvents(GID, SID):
    """
    Gets the event label map of a simulation tied to a graph

    :param GID: ID of graph
    :param SID: ID of simulation

    :returns: if successful, json of label map with keys as event IDs and items as labels and code 200
            if not correct security key, Status and code 403, 
            otherwise, unknown SID and code 404
    """
    if not dm.checkAccessSim(request.headers, GID, SID):
        return jsonify({"Status":'Access Denied'}),403
    
    sim = dm.findSim(SID)
    if sim:
        return jsonify(sim.label_map),200
    
    return jsonify({"Status":'Unknown SID'}),404

@app.get('/api/graphs/<string:GID>/sims/<string:SID>/relations')
def getRelations(GID, SID):
    """
    Gets the relations between event IDs of a simulation tied to a graph

    :param GID: ID of graph
    :param SID: ID of simulation

    :returns: if successful, json of relations and code 200
            if not correct security key, Status and code 403, 
            otherwise, unknown SID and code 404
    """
    if not dm.checkAccessSim(request.headers, GID, SID):
        return jsonify({"Status":'Access Denied'}),403
    
    sim = dm.findSim(SID)
    if sim:
        return jsonify(GetAllConds(sim)),200
    
    return jsonify({"Status":'Unknown SID'}),404

@app.get('/api/graphs/<string:GID>/sims/<string:SID>/included')
def getIncluded(GID, SID):
    """
    Gets the included events of a simulation tied to a graph

    :param GID: ID of graph
    :param SID: ID of simulation

    :returns: if successful, list of included event IDs and items as labels and code 200
            if not correct security key, Status and code 403, 
            otherwise, unknown SID and code 404
    """
    if not dm.checkAccessSim(request.headers, GID, SID):
        return jsonify({"Status":'Access Denied'}),403
    
    sim = dm.findSim(SID)
    if sim:
        return jsonify(list(sim.marking.included)),200
    
    return jsonify({"Status":'Unknown SID'}),404

@app.get('/api/graphs/<string:GID>/sims/<string:SID>/pending')
def getPending(GID, SID):
    """
    Gets the pending events of a simulation tied to a graph

    :param GID: ID of graph
    :param SID: ID of simulation

    :returns: if successful, a list of pending event IDs and code 200
            if not correct security key, Status and code 403, 
            otherwise, unknown SID and code 404
    """
    if not dm.checkAccessSim(request.headers, GID, SID):
        return jsonify({"Status":'Access Denied'}),403
    
    sim = dm.findSim(SID)
    if sim:
        return jsonify(list(sim.marking.pending)),200
    
    return jsonify({"Status":'Unknown SID'}),404

@app.get('/api/graphs/<string:GID>/sims/<string:SID>/executed')
def getExecuted(GID, SID):
    """
    Gets executed events of a simulation tied to a graph

    :param GID: ID of graph
    :param SID: ID of simulation

    :returns: if successful, list of executed event IDs and code 200
            if not correct security key, Status and code 403, 
            otherwise, unknown SID and code 404
    """
    if not dm.checkAccessSim(request.headers, GID, SID):
        return jsonify({"Status":'Access Denied'}),403
    
    sim = dm.findSim(SID)
    if sim:
        return jsonify(list(sim.marking.executed))
    
    return jsonify({"Status":'Unknown SID'}),404

@app.post('/api/graphs/<string:GID>/DCRsimulator/<string:SID>/executeEvent/<string:event>')
def executeEvent(GID, SID, event):
    """
    Executes a specific event on a simulation tied to a graph

    :param GID: ID of graph
    :param SID: ID of simulation
    :param event: event ID as a string

    :returns: if successful, Status an code 200
            if not correct security key, Status and code 403, 
            if unsuccessful, json of successful and unsuccessful events and code 409
            otherwise, unknown SID and code 404
    """
    if not dm.checkAccessSim(request.headers, GID, SID):
        return jsonify({"Status":'Access Denied'}),403
    
    sim = dm.findSim(SID)
    if sim:
        res = ExecuteEventOnGraph(sim, event)
        if res is None:
            return jsonify({"Status":{"Unsuccessful": [f"{event}"], "Successful" : []}}), 409
        return jsonify({"Status":'Success'}), 200
    return jsonify({"Status":'Unknown SID'}),404

@app.post('/api/graphs/<string:GID>/DCRsimulator/<string:SID>/executeTrace')
def executeTrace(GID, SID):
    """
    Executes a trace of events on a simulation tied to a graph. The trace is taken from the HTTP headers body

    :param GID: ID of graph
    :param SID: ID of simulation

    :returns: if successful, Status an code 200
            if not correct security key, Status and code 403, 
            if an unsuccessful event, json of successful and unsuccessful events and code 409
            if malformed data, Status and code 400
            otherwise, unknown SID and code 404
    """
    if not dm.checkAccessSim(request.headers, GID, SID):
        return jsonify({"Status":'Access Denied'}),403
    
    sim = dm.findSim(SID)
    if sim:
        jsn = request.data
        failed = []
        try: 
            jsn = json.loads(jsn)
            trace = jsn['trace']
            for e in trace:
                if ExecuteEventOnGraph(sim, e) is None:
                    failed.append(e)
            if len(failed) > 0:
                return jsonify({"Status":{"Unsuccessful": failed, "Successful" : list(set(trace).difference(failed))}}), 409
            return jsonify({"Status":"Success"}), 200
        except:
            return jsonify({"Status":'Malformed request data'}),400
    return jsonify({"Status":'Unknown SID'}),404