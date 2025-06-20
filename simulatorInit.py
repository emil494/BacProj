import pm4py
from pm4py.objects.dcr.hierarchical.obj import HierarchicalDcrGraph
from pm4py.objects.dcr.extended.semantics import ExtendedSemantics
import json

test = {'GID': 0, 'graph': {"dcrgraph": {"@title": "Aflevering 3", "@dataTypesStatus": "hide", "@filterLevel": "-1", "@insightFilter": "false", "@zoomLevel": "0", "@formGroupStyle": "Normal", "@formLayoutStyle": "Horizontal", "@formShowPendingCount": "true", "@graphBG": "#f1f6fe", "@graphType": "0", "@exercise": "false", "@version": "1.1", "meta": {"graph": {"@id": "1987618", "@hash": "780FE9C6B5797EA050103B45136907EB", "@guid": "1B9E75F7-0EA3-477C-979C-662BB55D9F92", "@OwnerName": "Emil Vedel Thage", "@OwnerId": "174110", "@categoryId": "10366", "@categoryTitle": "Default"}, "revision": {"@id": "4625064", "@type": "medium", "@date": "2025-03-10T10:35:02.200"}, "organization": {"@id": "1024", "@name": "KU - Academic Alliance"}}, "specification": {"resources": {"events": {"event": [{"@id": "A5", "precondition": {"@message": ""}, "custom": {"visualization": {"location": {"@xLoc": "200", "@yLoc": "220"}, "colors": {"@bg": "#f9f7ed", "@textStroke": "#000000", "@stroke": "#cccccc"}}, "roles": {"role": "Teacher"}, "readRoles": {"readRole": ["Group 1", "Group 2"]}, "groups": {"group": None}, "phases": {"phase": None}, "eventType": None, "eventScope": "private", "eventTypeData": None, "eventDescription": None, "purpose": None, "guide": None, "insight": {"@use": "false"}, "level": "1", "sequence": "1", "costs": "0", "eventData": None, "interfaces": None}}, {"@id": "A6", "precondition": {"@message": ""}, "custom": {"visualization": {"location": {"@xLoc": "250", "@yLoc": "620"}, "colors": {"@bg": "#f9f7ed", "@textStroke": "#000000", "@stroke": "#cccccc"}}, "roles": {"role": "Teacher"}, "readRoles": {"readRole": ["Group 1", "Group 2"]}, "groups": {"group": None}, "phases": {"phase": None}, "eventType": None, "eventScope": "private", "eventTypeData": None, "eventDescription": None, "purpose": None, "guide": None, "insight": {"@use": "false"}, "level": "1", "sequence": "2", "costs": "0", "eventData": None, "interfaces": None}}, {"@id": "A7", "@type": "nesting", "precondition": {"@message": ""}, "custom": {"visualization": {"location": {"@xLoc": "450", "@yLoc": "20"}, "colors": {"@bg": "#f9f7ed", "@textStroke": "#000000", "@stroke": "#cccccc"}}, "roles": {"role": None}, "readRoles": {"readRole": None}, "groups": {"group": None}, "phases": {"phase": None}, "eventType": None, "eventScope": "private", "eventTypeData": None, "eventDescription": None, "purpose": None, "guide": None, "insight": {"@use": "false"}, "level": "1", "sequence": "3", "costs": "0", "eventData": None, "interfaces": None}, "event": [{"@id": "A16", "@type": "nesting", "precondition": {"@message": ""}, "custom": {"visualization": {"location": {"@xLoc": "650", "@yLoc": "320"}, "colors": {"@bg": "#f9f7ed", "@textStroke": "#000000", "@stroke": "#cccccc"}}, "roles": {"role": None}, "readRoles": {"readRole": None}, "groups": {"group": None}, "phases": {"phase": None}, "eventType": None, "eventScope": "private", "eventTypeData": None, "eventDescription": None, "purpose": None, "guide": None, "insight": {"@use": "false"}, "level": "1", "sequence": "11", "costs": "0", "eventData": None, "interfaces": None}, "event": [{"@id": "A9", "precondition": {"@message": ""}, "custom": {"visualization": {"location": {"@xLoc": "680", "@yLoc": "370"}, "colors": {"@bg": "#f9f7ed", "@textStroke": "#000000", "@stroke": "#cccccc"}}, "roles": {"role": "Teacher"}, "readRoles": {"readRole": ["Group 1", "Group 2"]}, "groups": {"group": None}, "phases": {"phase": None}, "eventType": None, "eventScope": "private", "eventTypeData": None, "eventDescription": None, "purpose": None, "guide": None, "insight": {"@use": "false"}, "level": "1", "sequence": "5", "costs": "0", "eventData": None, "interfaces": None}}, {"@id": "A12", "precondition": {"@message": ""}, "custom": {"visualization": {"location": {"@xLoc": "830", "@yLoc": "370"}, "colors": {"@bg": "#f9f7ed", "@textStroke": "#000000", "@stroke": "#cccccc"}}, "roles": {"role": "Teacher"}, "readRoles": {"readRole": ["Group 1", "Group 2"]}, "groups": {"group": None}, "phases": {"phase": None}, "eventType": None, "eventScope": "private", "eventTypeData": None, "eventDescription": None, "purpose": None, "guide": None, "insight": {"@use": "false"}, "level": "1", "sequence": "6", "costs": "0", "eventData": None, "interfaces": None}}, {"@id": "A13", "precondition": {"@message": ""}, "custom": {"visualization": {"location": {"@xLoc": "980", "@yLoc": "370"}, "colors": {"@bg": "#f9f7ed", "@textStroke": "#000000", "@stroke": "#cccccc"}}, "roles": {"role": "Teacher"}, "readRoles": {"readRole": ["Group 1", "Group 2"]}, "groups": {"group": None}, "phases": {"phase": None}, "eventType": None, "eventScope": "private", "eventTypeData": None, "eventDescription": None, "purpose": None, "guide": None, "insight": {"@use": "false"}, "level": "1", "sequence": "7", "costs": "0", "eventData": None, "interfaces": None}}]}, {"@id": "A17", "precondition": {"@message": ""}, "custom": {"visualization": {"location": {"@xLoc": "480", "@yLoc": "370"}, "colors": {"@bg": "#f9f7ed", "@textStroke": "#000000", "@stroke": "#cccccc"}}, "roles": {"role": "Teacher"}, "readRoles": {"readRole": ["Group 1", "Group 2"]}, "groups": {"group": None}, "phases": {"phase": None}, "eventType": None, "eventScope": "private", "eventTypeData": None, "eventDescription": None, "purpose": None, "guide": None, "insight": {"@use": "false"}, "level": "1", "sequence": "8", "costs": "0", "eventData": None, "interfaces": None}}, {"@id": "A15", "@type": "nesting", "precondition": {"@message": ""}, "custom": {"visualization": {"location": {"@xLoc": "650", "@yLoc": "70"}, "colors": {"@bg": "#f9f7ed", "@textStroke": "#000000", "@stroke": "#cccccc"}}, "roles": {"role": None}, "readRoles": {"readRole": None}, "groups": {"group": None}, "phases": {"phase": None}, "eventType": None, "eventScope": "private", "eventTypeData": None, "eventDescription": None, "purpose": None, "guide": None, "insight": {"@use": "false"}, "level": "1", "sequence": "13", "costs": "0", "eventData": None, "interfaces": None}, "event": [{"@id": "A4", "precondition": {"@message": ""}, "custom": {"visualization": {"location": {"@xLoc": "680", "@yLoc": "120"}, "colors": {"@bg": "#f9f7ed", "@textStroke": "#000000", "@stroke": "#cccccc"}}, "roles": {"role": "Group 1"}, "readRoles": {"readRole": "Teacher"}, "groups": {"group": None}, "phases": {"phase": None}, "eventType": None, "eventScope": "private", "eventTypeData": None, "eventDescription": None, "purpose": None, "guide": None, "insight": {"@use": "false"}, "level": "1", "sequence": "0", "costs": "0", "eventData": None, "interfaces": None}}, {"@id": "A4Copy", "precondition": {"@message": ""}, "custom": {"visualization": {"location": {"@xLoc": "860", "@yLoc": "120"}, "colors": {"@bg": "#f9f7ed", "@textStroke": "#000000", "@stroke": "#cccccc"}}, "roles": {"role": "Group 2"}, "readRoles": {"readRole": "Teacher"}, "groups": {"group": None}, "phases": {"phase": None}, "eventType": None, "eventScope": "private", "eventTypeData": None, "eventDescription": None, "purpose": None, "guide": None, "insight": {"@use": "false"}, "level": "1", "sequence": "4", "costs": "0", "eventData": None, "interfaces": None}}]}]}, {"@id": "A14", "@type": "nesting", "precondition": {"@message": ""}, "custom": {"visualization": {"location": {"@xLoc": "750", "@yLoc": "620"}, "colors": {"@bg": "#f9f7ed", "@textStroke": "#000000", "@stroke": "#cccccc"}}, "roles": {"role": None}, "readRoles": {"readRole": None}, "groups": {"group": None}, "phases": {"phase": None}, "eventType": None, "eventScope": "private", "eventTypeData": None, "eventDescription": None, "purpose": None, "guide": None, "insight": {"@use": "false"}, "level": "1", "sequence": "12", "costs": "0", "eventData": None, "interfaces": None}, "event": [{"@id": "A28", "precondition": {"@message": ""}, "custom": {"visualization": {"location": {"@xLoc": "780", "@yLoc": "670"}, "colors": {"@bg": "#f9f7ed", "@textStroke": "#000000", "@stroke": "#cccccc"}}, "roles": {"role": "Group 1"}, "readRoles": {"readRole": None}, "groups": {"group": None}, "phases": {"phase": None}, "eventType": None, "eventScope": "private", "eventTypeData": None, "eventDescription": None, "purpose": None, "guide": None, "insight": {"@use": "false"}, "level": "1", "sequence": "9", "costs": "0", "eventData": None, "interfaces": None}}, {"@id": "A29", "precondition": {"@message": ""}, "custom": {"visualization": {"location": {"@xLoc": "930", "@yLoc": "670"}, "colors": {"@bg": "#f9f7ed", "@textStroke": "#000000", "@stroke": "#cccccc"}}, "roles": {"role": "Group 2"}, "readRoles": {"readRole": None}, "groups": {"group": None}, "phases": {"phase": None}, "eventType": None, "eventScope": "private", "eventTypeData": None, "eventDescription": None, "purpose": None, "guide": None, "insight": {"@use": "false"}, "level": "1", "sequence": "10", "costs": "0", "eventData": None, "interfaces": None}}]}]}, "subProcesses": None, "distribution": None, "labels": {"label": [{"@id": "Open Assignment"}, {"@id": "Start Exam"}, {"@id": "Assignment"}, {"@id": "Close Assignments"}, {"@id": "Close Assignment"}, {"@id": "Close Assignment 1"}, {"@id": "Close Assignment 2"}, {"@id": "Close - No Hand-Ins"}, {"@id": "Hand-Ins"}, {"@id": "Hand-In"}, {"@id": "Hand-In"}, {"@id": "Exam Attendance"}, {"@id": "Attend Exam G1"}, {"@id": "Attend Exam G2"}]}, "labelMappings": {"labelMapping": [{"@eventId": "A5", "@labelId": "Open Assignment"}, {"@eventId": "A6", "@labelId": "Start Exam"}, {"@eventId": "A7", "@labelId": "Assignment"}, {"@eventId": "A16", "@labelId": "Close Assignments"}, {"@eventId": "A9", "@labelId": "Close Assignment"}, {"@eventId": "A12", "@labelId": "Close Assignment 1"}, {"@eventId": "A13", "@labelId": "Close Assignment 2"}, {"@eventId": "A17", "@labelId": "Close - No Hand-Ins"}, {"@eventId": "A15", "@labelId": "Hand-Ins"}, {"@eventId": "A4", "@labelId": "Hand-In"}, {"@eventId": "A4Copy", "@labelId": "Hand-In"}, {"@eventId": "A14", "@labelId": "Exam Attendance"}, {"@eventId": "A28", "@labelId": "Attend Exam G1"}, {"@eventId": "A29", "@labelId": "Attend Exam G2"}]}, "expressions": None, "variables": None, "variableAccesses": {"writeAccesses": None}, "custom": {"keywords": None, "roles": {"role": [{"@description": "d", "@specification": "df", "#text": "fg"}, {"@description": "", "@specification": "", "#text": "Not fg"}, {"@description": "", "@specification": "", "#text": "Teacher"}, {"@description": "", "@specification": "", "#text": "Group 1"}, {"@description": "", "@specification": "", "#text": "Group 2"}]}, "groups": {"group": {"@sequence": "4", "@description": "sd", "#text": "sd"}}, "phases": None, "eventTypes": None, "eventParameters": None, "graphDetails": "DCR Process", "graphDocumentation": None, "graphLanguage": "en-US", "graphDomain": "process", "graphFilters": {"filteredGroups": None, "filteredRoles": None, "filteredPhases": None}, "hightlighterMarkup": {"@id": "HLM"}, "highlighterMarkup": {"highlightLayers": {"highlightLayer": {"@default": "true", "@name": "description", "#text": "DCR Process"}}, "highlights": None}}}, "constraints": {"conditions": None, "responses": {"response": [{"@sourceId": "A5", "@targetId": "A7", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A6", "@targetId": "A14", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A16", "@targetId": "A5", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A17", "@targetId": "A5", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}]}, "coresponses": None, "excludes": {"exclude": [{"@sourceId": "A5", "@targetId": "A6", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A6", "@targetId": "A5", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A17", "@targetId": "A14", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A12", "@targetId": "A28", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A13", "@targetId": "A29", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A29", "@targetId": "A29", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A28", "@targetId": "A28", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A12", "@targetId": "A13", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A13", "@targetId": "A12", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A17", "@targetId": "A16", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A12", "@targetId": "A9", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A13", "@targetId": "A9", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A17", "@targetId": "A17", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A6", "@targetId": "A7", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A6", "@targetId": "A6", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A15", "@targetId": "A17", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A4", "@targetId": "A13", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A4Copy", "@targetId": "A12", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A12", "@targetId": "A4Copy", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A13", "@targetId": "A4", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A17", "@targetId": "A15", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}]}, "includes": {"include": [{"@sourceId": "A17", "@targetId": "A6", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A16", "@targetId": "A6", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A5", "@targetId": "A17", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A9", "@targetId": "A16", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}]}, "milestones": {"milestone": [{"@sourceId": "A5", "@targetId": "A7", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A6", "@targetId": "A14", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A7", "@targetId": "A14", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A4Copy", "@targetId": "A13", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A4", "@targetId": "A12", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A15", "@targetId": "A9", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}]}, "updates": None, "spawns": None, "templateSpawns": None}}, "runtime": {"custom": {"globalMarking": None}, "marking": {"globalStore": None, "executed": None, "included": {"event": [{"@id": "A5"}, {"@id": "A6"}, {"@id": "A16"}, {"@id": "A9"}, {"@id": "A12"}, {"@id": "A13"}, {"@id": "A17"}, {"@id": "A15"}, {"@id": "A4"}, {"@id": "A4Copy"}, {"@id": "A14"}, {"@id": "A28"}, {"@id": "A29"}]}, "pendingResponses": {"event": [{"@id": "A5"}, {"@id": "A6"}]}}}}}}

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
