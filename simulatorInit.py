import pm4py
from pm4py.objects.dcr.hierarchical.obj import HierarchicalDcrGraph
from pm4py.objects.dcr.extended.semantics import ExtendedSemantics
import json

def findKey(jsn : dict, key : str):
    """
    Searches through the DCRgraph.net graph converted to json and returns the key of a nested dict corresponding to given search word

    Parameters
    ----------
    :jsn: Json converted DCRgraph.net graph
    :key: Keyword of a potiential nested dict which value contains the sought out information 
    
    Returns
    -------
    :res: The value of the dict, containing the sought out information
    """

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

def isNesting(graph, nestings):
    """
    Takes the dictionary containing all the events as a dict and searches through the events and marks which ones are nested, and what lies inside a potential nesting. 

    Parameters
    ----------
    :graph: The dict with all the events
    :nestings: and empty dict where all the nestings will be located in at the end
    
    Returns
    -------
    :nestings: A full dict with nestings and the markings included in them
    """


    for elm in graph:
        if '@type' in elm:
            nestings.setdefault(elm['@id'],[])
            for events in elm['event']:
                nestings[elm['@id']].append(events['@id'])
            isNesting(elm['event'],nestings)
    return nestings

def EventinList(event,eventlist):
    """
    Checks for an event inside a list of events

    Parameters
    ----------
    :event: The event to be checked for
    :eventlist: Dict of events in the graph

    Returns
    -------
    :True: If the event is in the list
    :False: If the event isn't in the list
    """
    if eventlist is None:
                return False
    if len(eventlist['event']) > 1:
        for object in eventlist['event']:
            if event == object['@id']:
                return True
    if {"@id":event} == eventlist['event']:
        return True
    return False


def createDCRgraph(graph):
    """
    Reads through the entire json converted DCRgraph.net graph and creates a DCR4PY graph object with the correct corresponding markings, relations, mappings etc. Uses both EventInList(), isNestings() as well as the findKey() functions.

    Paramters
    ---------
    :graph: The json converted DCRgraph.net graph

    Returns
    -------
    :dcr: A DCR4PY graph object corresponding to the given input graph

    """


    jsn = graph['graph']
    nestings = {}

    dcr = HierarchicalDcrGraph()
    nestings = isNesting(findKey(jsn,"events"),nestings)
    rel = findKey(jsn, 'constraints')
    events = findKey(jsn, 'labelMapping')
    included = findKey(jsn, 'included')
    pending = findKey(jsn, 'pendingResponses')
    
    for (key,values) in nestings.items():
            dcr.nestedgroups[key] = {values[i] for i in range(len(values))}

    for group, NEvents in dcr.nestedgroups.items():
        for e in NEvents:
            dcr.nestedgroups_map[e] = group
    
    for event in events:
        dcr.events.add(event['@eventId'])
        dcr.labels.add(event['@labelId'])
        dcr.label_map[event['@eventId']] = event['@labelId']
        if EventinList(event['@eventId'],included):
            dcr.marking.included.add(event['@eventId'])
        if EventinList(event['@eventId'],pending):
            dcr.marking.pending.add(event['@eventId'])

    for value in rel.values():
        if value is not None:
            for (cond, targets) in value.items():
                if isinstance(targets, list):
                    for target in targets:
                        if cond == 'response':
                            if target['@sourceId'] in dcr.responses:
                                dcr.responses[target['@sourceId']].add(target['@targetId'])
                            else:
                                dcr.responses[target['@sourceId']]={target['@targetId']}
                        if cond == 'exclude':
                            if target['@sourceId'] in dcr.excludes:
                                dcr.excludes[target['@sourceId']].add(target['@targetId'])
                            else:
                                dcr.excludes[target['@sourceId']]={target['@targetId']}
                        if cond == 'include':
                            if target['@sourceId'] in dcr.includes:
                                dcr.includes[target['@sourceId']].add(target['@targetId'])
                            else:
                                dcr.includes[target['@sourceId']]={target['@targetId']}
                        if cond == 'milestone':
                            if '@link' not in target.keys():
                                if target['@sourceId'] in dcr.milestones:
                                    dcr.milestones[target['@sourceId']].add(target['@targetId'])
                                else:
                                    dcr.milestones[target['@sourceId']]={target['@targetId']}
                        if cond == 'condition':
                            if target['@targetId'] in dcr.conditions:
                                dcr.conditions[target['@targetId']].add(target['@sourceId'])
                            else:
                                dcr.conditions[target['@targetId']]={target['@sourceId']}
                if isinstance(targets, dict):
                    if cond == 'response':
                        dcr.responses[targets['@sourceId']]={targets['@targetId']}
                    if cond == 'exclude':
                        dcr.excludes[targets['@sourceId']]={targets['@targetId']}
                    if cond == 'include':
                        dcr.includes[targets['@sourceId']]={targets['@targetId']}
                    if cond == 'milestone':
                        if '@link' not in target.keys():
                            dcr.milestones[targets['@targetId']]={targets['@sourceId']}
                    if cond == 'condition':
                        dcr.conditions[targets['@targetId']]={targets['@sourceId']}


    return dcr

def ExecuteEventOnGraph(dcr,event):
    """
    Uses the semantics from DCR4PY to check if an event is enabled and executes set event, depending on it being enabled or not

    Parameters
    ----------
    :dcr: The graph object
    :event: The event which should be executed (if eligible)

    Returns
    -------
    :semantics.execute(dcr,event): The changed graph after execution of the event
    :None: Nothing if the event wasn't eligible for execution
    """


    semantics = ExtendedSemantics()
    if event in semantics.enabled(dcr):
        return semantics.execute(dcr,event)
    return None

def GetAllConds(SID):
    """
    Searches the graph object and finds which relations there are on the graph

    Parameters
    ----------
    :SID: The graph to be checked

    Returns
    -------
    :allconds: A dict with all the relationship types as keys and values containing all the events with the relations and whom they 'relate' to

    """
    allConds = {"Conditions": SID.conditions,
                "Responses" : SID.responses,
                "Includes": SID.includes,
                "Excludes": SID.excludes,
                "Milestone": SID.milestones}
    for key,val in allConds.items():
        allConds[key] = {}
        for cKey,cVal in val.items():
            allConds[key].update({cKey:list(cVal)})
    return allConds
