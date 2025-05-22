import pm4py
from pm4py.objects.dcr.hierarchical.obj import HierarchicalDcrGraph
from pm4py.objects.dcr.semantics import DcrSemantics
import json

test = {'GID': 0, 'graph': {"dcrgraph": {"@title": "Aflevering 3", "@dataTypesStatus": "hide", "@filterLevel": "-1", "@insightFilter": "false", "@zoomLevel": "0", "@formGroupStyle": "Normal", "@formLayoutStyle": "Horizontal", "@formShowPendingCount": "true", "@graphBG": "#f1f6fe", "@graphType": "0", "@exercise": "false", "@version": "1.1", "meta": {"graph": {"@id": "1987618", "@hash": "780FE9C6B5797EA050103B45136907EB", "@guid": "1B9E75F7-0EA3-477C-979C-662BB55D9F92", "@OwnerName": "Emil Vedel Thage", "@OwnerId": "174110", "@categoryId": "10366", "@categoryTitle": "Default"}, "revision": {"@id": "4625064", "@type": "medium", "@date": "2025-03-10T10:35:02.200"}, "organization": {"@id": "1024", "@name": "KU - Academic Alliance"}}, "specification": {"resources": {"events": {"event": [{"@id": "A5", "precondition": {"@message": ""}, "custom": {"visualization": {"location": {"@xLoc": "200", "@yLoc": "220"}, "colors": {"@bg": "#f9f7ed", "@textStroke": "#000000", "@stroke": "#cccccc"}}, "roles": {"role": "Teacher"}, "readRoles": {"readRole": ["Group 1", "Group 2"]}, "groups": {"group": None}, "phases": {"phase": None}, "eventType": None, "eventScope": "private", "eventTypeData": None, "eventDescription": None, "purpose": None, "guide": None, "insight": {"@use": "false"}, "level": "1", "sequence": "1", "costs": "0", "eventData": None, "interfaces": None}}, {"@id": "A6", "precondition": {"@message": ""}, "custom": {"visualization": {"location": {"@xLoc": "250", "@yLoc": "620"}, "colors": {"@bg": "#f9f7ed", "@textStroke": "#000000", "@stroke": "#cccccc"}}, "roles": {"role": "Teacher"}, "readRoles": {"readRole": ["Group 1", "Group 2"]}, "groups": {"group": None}, "phases": {"phase": None}, "eventType": None, "eventScope": "private", "eventTypeData": None, "eventDescription": None, "purpose": None, "guide": None, "insight": {"@use": "false"}, "level": "1", "sequence": "2", "costs": "0", "eventData": None, "interfaces": None}}, {"@id": "A7", "@type": "nesting", "precondition": {"@message": ""}, "custom": {"visualization": {"location": {"@xLoc": "450", "@yLoc": "20"}, "colors": {"@bg": "#f9f7ed", "@textStroke": "#000000", "@stroke": "#cccccc"}}, "roles": {"role": None}, "readRoles": {"readRole": None}, "groups": {"group": None}, "phases": {"phase": None}, "eventType": None, "eventScope": "private", "eventTypeData": None, "eventDescription": None, "purpose": None, "guide": None, "insight": {"@use": "false"}, "level": "1", "sequence": "3", "costs": "0", "eventData": None, "interfaces": None}, "event": [{"@id": "A16", "@type": "nesting", "precondition": {"@message": ""}, "custom": {"visualization": {"location": {"@xLoc": "650", "@yLoc": "320"}, "colors": {"@bg": "#f9f7ed", "@textStroke": "#000000", "@stroke": "#cccccc"}}, "roles": {"role": None}, "readRoles": {"readRole": None}, "groups": {"group": None}, "phases": {"phase": None}, "eventType": None, "eventScope": "private", "eventTypeData": None, "eventDescription": None, "purpose": None, "guide": None, "insight": {"@use": "false"}, "level": "1", "sequence": "11", "costs": "0", "eventData": None, "interfaces": None}, "event": [{"@id": "A9", "precondition": {"@message": ""}, "custom": {"visualization": {"location": {"@xLoc": "680", "@yLoc": "370"}, "colors": {"@bg": "#f9f7ed", "@textStroke": "#000000", "@stroke": "#cccccc"}}, "roles": {"role": "Teacher"}, "readRoles": {"readRole": ["Group 1", "Group 2"]}, "groups": {"group": None}, "phases": {"phase": None}, "eventType": None, "eventScope": "private", "eventTypeData": None, "eventDescription": None, "purpose": None, "guide": None, "insight": {"@use": "false"}, "level": "1", "sequence": "5", "costs": "0", "eventData": None, "interfaces": None}}, {"@id": "A12", "precondition": {"@message": ""}, "custom": {"visualization": {"location": {"@xLoc": "830", "@yLoc": "370"}, "colors": {"@bg": "#f9f7ed", "@textStroke": "#000000", "@stroke": "#cccccc"}}, "roles": {"role": "Teacher"}, "readRoles": {"readRole": ["Group 1", "Group 2"]}, "groups": {"group": None}, "phases": {"phase": None}, "eventType": None, "eventScope": "private", "eventTypeData": None, "eventDescription": None, "purpose": None, "guide": None, "insight": {"@use": "false"}, "level": "1", "sequence": "6", "costs": "0", "eventData": None, "interfaces": None}}, {"@id": "A13", "precondition": {"@message": ""}, "custom": {"visualization": {"location": {"@xLoc": "980", "@yLoc": "370"}, "colors": {"@bg": "#f9f7ed", "@textStroke": "#000000", "@stroke": "#cccccc"}}, "roles": {"role": "Teacher"}, "readRoles": {"readRole": ["Group 1", "Group 2"]}, "groups": {"group": None}, "phases": {"phase": None}, "eventType": None, "eventScope": "private", "eventTypeData": None, "eventDescription": None, "purpose": None, "guide": None, "insight": {"@use": "false"}, "level": "1", "sequence": "7", "costs": "0", "eventData": None, "interfaces": None}}]}, {"@id": "A17", "precondition": {"@message": ""}, "custom": {"visualization": {"location": {"@xLoc": "480", "@yLoc": "370"}, "colors": {"@bg": "#f9f7ed", "@textStroke": "#000000", "@stroke": "#cccccc"}}, "roles": {"role": "Teacher"}, "readRoles": {"readRole": ["Group 1", "Group 2"]}, "groups": {"group": None}, "phases": {"phase": None}, "eventType": None, "eventScope": "private", "eventTypeData": None, "eventDescription": None, "purpose": None, "guide": None, "insight": {"@use": "false"}, "level": "1", "sequence": "8", "costs": "0", "eventData": None, "interfaces": None}}, {"@id": "A15", "@type": "nesting", "precondition": {"@message": ""}, "custom": {"visualization": {"location": {"@xLoc": "650", "@yLoc": "70"}, "colors": {"@bg": "#f9f7ed", "@textStroke": "#000000", "@stroke": "#cccccc"}}, "roles": {"role": None}, "readRoles": {"readRole": None}, "groups": {"group": None}, "phases": {"phase": None}, "eventType": None, "eventScope": "private", "eventTypeData": None, "eventDescription": None, "purpose": None, "guide": None, "insight": {"@use": "false"}, "level": "1", "sequence": "13", "costs": "0", "eventData": None, "interfaces": None}, "event": [{"@id": "A4", "precondition": {"@message": ""}, "custom": {"visualization": {"location": {"@xLoc": "680", "@yLoc": "120"}, "colors": {"@bg": "#f9f7ed", "@textStroke": "#000000", "@stroke": "#cccccc"}}, "roles": {"role": "Group 1"}, "readRoles": {"readRole": "Teacher"}, "groups": {"group": None}, "phases": {"phase": None}, "eventType": None, "eventScope": "private", "eventTypeData": None, "eventDescription": None, "purpose": None, "guide": None, "insight": {"@use": "false"}, "level": "1", "sequence": "0", "costs": "0", "eventData": None, "interfaces": None}}, {"@id": "A4Copy", "precondition": {"@message": ""}, "custom": {"visualization": {"location": {"@xLoc": "860", "@yLoc": "120"}, "colors": {"@bg": "#f9f7ed", "@textStroke": "#000000", "@stroke": "#cccccc"}}, "roles": {"role": "Group 2"}, "readRoles": {"readRole": "Teacher"}, "groups": {"group": None}, "phases": {"phase": None}, "eventType": None, "eventScope": "private", "eventTypeData": None, "eventDescription": None, "purpose": None, "guide": None, "insight": {"@use": "false"}, "level": "1", "sequence": "4", "costs": "0", "eventData": None, "interfaces": None}}]}]}, {"@id": "A14", "@type": "nesting", "precondition": {"@message": ""}, "custom": {"visualization": {"location": {"@xLoc": "750", "@yLoc": "620"}, "colors": {"@bg": "#f9f7ed", "@textStroke": "#000000", "@stroke": "#cccccc"}}, "roles": {"role": None}, "readRoles": {"readRole": None}, "groups": {"group": None}, "phases": {"phase": None}, "eventType": None, "eventScope": "private", "eventTypeData": None, "eventDescription": None, "purpose": None, "guide": None, "insight": {"@use": "false"}, "level": "1", "sequence": "12", "costs": "0", "eventData": None, "interfaces": None}, "event": [{"@id": "A28", "precondition": {"@message": ""}, "custom": {"visualization": {"location": {"@xLoc": "780", "@yLoc": "670"}, "colors": {"@bg": "#f9f7ed", "@textStroke": "#000000", "@stroke": "#cccccc"}}, "roles": {"role": "Group 1"}, "readRoles": {"readRole": None}, "groups": {"group": None}, "phases": {"phase": None}, "eventType": None, "eventScope": "private", "eventTypeData": None, "eventDescription": None, "purpose": None, "guide": None, "insight": {"@use": "false"}, "level": "1", "sequence": "9", "costs": "0", "eventData": None, "interfaces": None}}, {"@id": "A29", "precondition": {"@message": ""}, "custom": {"visualization": {"location": {"@xLoc": "930", "@yLoc": "670"}, "colors": {"@bg": "#f9f7ed", "@textStroke": "#000000", "@stroke": "#cccccc"}}, "roles": {"role": "Group 2"}, "readRoles": {"readRole": None}, "groups": {"group": None}, "phases": {"phase": None}, "eventType": None, "eventScope": "private", "eventTypeData": None, "eventDescription": None, "purpose": None, "guide": None, "insight": {"@use": "false"}, "level": "1", "sequence": "10", "costs": "0", "eventData": None, "interfaces": None}}]}]}, "subProcesses": None, "distribution": None, "labels": {"label": [{"@id": "Open Assignment"}, {"@id": "Start Exam"}, {"@id": "Assignment"}, {"@id": "Close Assignments"}, {"@id": "Close Assignment"}, {"@id": "Close Assignment 1"}, {"@id": "Close Assignment 2"}, {"@id": "Close - No Hand-Ins"}, {"@id": "Hand-Ins"}, {"@id": "Hand-In"}, {"@id": "Hand-In"}, {"@id": "Exam Attendance"}, {"@id": "Attend Exam G1"}, {"@id": "Attend Exam G2"}]}, "labelMappings": {"labelMapping": [{"@eventId": "A5", "@labelId": "Open Assignment"}, {"@eventId": "A6", "@labelId": "Start Exam"}, {"@eventId": "A7", "@labelId": "Assignment"}, {"@eventId": "A16", "@labelId": "Close Assignments"}, {"@eventId": "A9", "@labelId": "Close Assignment"}, {"@eventId": "A12", "@labelId": "Close Assignment 1"}, {"@eventId": "A13", "@labelId": "Close Assignment 2"}, {"@eventId": "A17", "@labelId": "Close - No Hand-Ins"}, {"@eventId": "A15", "@labelId": "Hand-Ins"}, {"@eventId": "A4", "@labelId": "Hand-In"}, {"@eventId": "A4Copy", "@labelId": "Hand-In"}, {"@eventId": "A14", "@labelId": "Exam Attendance"}, {"@eventId": "A28", "@labelId": "Attend Exam G1"}, {"@eventId": "A29", "@labelId": "Attend Exam G2"}]}, "expressions": None, "variables": None, "variableAccesses": {"writeAccesses": None}, "custom": {"keywords": None, "roles": {"role": [{"@description": "d", "@specification": "df", "#text": "fg"}, {"@description": "", "@specification": "", "#text": "Not fg"}, {"@description": "", "@specification": "", "#text": "Teacher"}, {"@description": "", "@specification": "", "#text": "Group 1"}, {"@description": "", "@specification": "", "#text": "Group 2"}]}, "groups": {"group": {"@sequence": "4", "@description": "sd", "#text": "sd"}}, "phases": None, "eventTypes": None, "eventParameters": None, "graphDetails": "DCR Process", "graphDocumentation": None, "graphLanguage": "en-US", "graphDomain": "process", "graphFilters": {"filteredGroups": None, "filteredRoles": None, "filteredPhases": None}, "hightlighterMarkup": {"@id": "HLM"}, "highlighterMarkup": {"highlightLayers": {"highlightLayer": {"@default": "true", "@name": "description", "#text": "DCR Process"}}, "highlights": None}}}, "constraints": {"conditions": None, "responses": {"response": [{"@sourceId": "A5", "@targetId": "A7", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A6", "@targetId": "A14", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A16", "@targetId": "A5", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A17", "@targetId": "A5", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}]}, "coresponses": None, "excludes": {"exclude": [{"@sourceId": "A5", "@targetId": "A6", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A6", "@targetId": "A5", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A17", "@targetId": "A14", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A12", "@targetId": "A28", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A13", "@targetId": "A29", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A29", "@targetId": "A29", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A28", "@targetId": "A28", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A12", "@targetId": "A13", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A13", "@targetId": "A12", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A17", "@targetId": "A16", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A12", "@targetId": "A9", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A13", "@targetId": "A9", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A17", "@targetId": "A17", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A6", "@targetId": "A7", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A6", "@targetId": "A6", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A15", "@targetId": "A17", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A4", "@targetId": "A13", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A4Copy", "@targetId": "A12", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A12", "@targetId": "A4Copy", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A13", "@targetId": "A4", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A17", "@targetId": "A15", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}]}, "includes": {"include": [{"@sourceId": "A17", "@targetId": "A6", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A16", "@targetId": "A6", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A5", "@targetId": "A17", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A9", "@targetId": "A16", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}]}, "milestones": {"milestone": [{"@sourceId": "A5", "@targetId": "A7", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A6", "@targetId": "A14", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A7", "@targetId": "A14", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A4Copy", "@targetId": "A13", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A4", "@targetId": "A12", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}, {"@sourceId": "A15", "@targetId": "A9", "@filterLevel": "1", "@description": "", "@time": "", "@groups": ""}]}, "updates": None, "spawns": None, "templateSpawns": None}}, "runtime": {"custom": {"globalMarking": None}, "marking": {"globalStore": None, "executed": None, "included": {"event": [{"@id": "A5"}, {"@id": "A6"}, {"@id": "A16"}, {"@id": "A9"}, {"@id": "A12"}, {"@id": "A13"}, {"@id": "A17"}, {"@id": "A15"}, {"@id": "A4"}, {"@id": "A4Copy"}, {"@id": "A14"}, {"@id": "A28"}, {"@id": "A29"}]}, "pendingResponses": {"event": [{"@id": "A5"}, {"@id": "A6"}]}}}}}}

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

def isNesting(graph, nestings):
    for elm in graph:
        if '@type' in elm:
            nestings.setdefault(elm['@id'],[])
            for events in elm['event']:
                nestings[elm['@id']].append(events['@id'])
            isNesting(elm['event'],nestings)
    return nestings

def EventinList(event,eventlist):
    if eventlist is None:
                return False
    for object in eventlist['event']:
            if event == object['@id']:
                return True
    return False


def createDCRgraph(graph):
    jsn = graph['graph']
    nestings = {}

    dcr = HierarchicalDcrGraph()
    nestings = isNesting(findKey(jsn,"event"),nestings)
    rel = findKey(jsn, 'constraints')
    events = findKey(jsn, 'labelMapping')
    included = findKey(jsn, 'included')
    pending = findKey(jsn, 'pendingResponses')
    
    for (key,values) in nestings.items():
            dcr.nestedgroups[key] = {values[i] for i in range(len(values))}

    for group, NEvents in dcr.nestedgroups.items():
        for e in NEvents:
            dcr.nestedgroups_map[e] = group
    
    # TODO: Add data to DcrGraph()
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
                            dcr.responses[target['@sourceId']]={target['@targetId']}
                        if cond == 'exclude':
                            dcr.excludes[target['@sourceId']]={target['@targetId']}
                        if cond == 'include':
                            dcr.includes[target['@sourceId']]={target['@targetId']}
                        if cond == 'milestone':
                            if '@link' not in target.keys():
                                dcr.milestones[target['@sourceId']]={target['@targetId']}
                        if cond == 'condition':
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
                            dcr.milestones[targets['@sourceId']]={targets['@targetId']}
                    if cond == 'condition':
                        dcr.conditions[targets['@targetId']]={targets['@sourceId']}
                    # TODO : add spawn, ing?

    return dcr

def ExecuteEventOnGraph(dcr,event):
    semantics = DcrSemantics()
    if not event in dcr.events:
        if not event in dcr.labels:
            return "Unknown event"
        map = dcr.label_map
        #TODO: Discriminate between groups if 2+ events use the same label, else fail due to ambiguity
        for (e, alias) in map.items():
            if alias == event:
                event = e
                break

    semantics.execute(dcr,event)
    return dcr

def GetAllConds(SID):
    allConds = {}

    allConds.update({"conditions": SID.conditions})
    for key,val in allConds["conditions"].items():
        allConds["conditions"].update({key:next(iter(val))})

    allConds.update({"responses": SID.responses})
    for key,val in allConds["responses"].items():
        allConds["responses"].update({key:next(iter(val))})
    
    allConds.update({"includes": SID.includes})
    for key,val in allConds["includes"].items():
        allConds["includes"].update({key:next(iter(val))})
    
    allConds.update({"excludes": SID.excludes})
    for key,val in allConds["excludes"].items():
        allConds["excludes"].update({key:next(iter(val))})

    print(allConds)
    return allConds
