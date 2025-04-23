import pm4py
from pm4py.objects.dcr.hierarchical.obj import HierarchicalDcrGraph

test = {'GID': 0, 'graph': {'dcrgraph': {'@title': 'Testtt', '@dataTypesStatus': 'hide', '@filterLevel': '-1', '@insightFilter': 'false', '@zoomLevel': '0', '@formGroupStyle': 'Normal', '@formLayoutStyle': 'Horizontal', '@formShowPendingCount': 'true', '@graphBG': '#f1f6fe', '@graphType': '0', '@exercise': 'false', '@version': '1.1', 'meta': {'graph': {'@id': '1992671', '@hash': '04D88AE56A9B3579B6BF0BCE1CD98D18', '@guid': 'C2BF6265-5ACA-4EB4-9059-0BEA4F0F3BCC', '@OwnerName': 'Emil Vedel Thage', '@OwnerId': '174110', '@categoryId': '10366', '@categoryTitle': 'Default'}, 'revision': {'@id': '4732320', '@type': 'medium', '@date': '2025-04-23T15:13:05.887'}, 'organization': {'@id': '1024', '@name': 'KU - Academic Alliance'}}, 'specification': {'resources': {'events': {'event': [{'@id': 'A1', 'precondition': {'@message': ''}, 'custom': {'visualization': {'location': {'@xLoc': '600', '@yLoc': '220'}, 'colors': {'@bg': '#f9f7ed', '@textStroke': '#000000', '@stroke': '#cccccc'}}, 'roles': {'role': None}, 'readRoles': {'readRole': None}, 'groups': {'group': None}, 'phases': {'phase': None}, 'eventType': None, 'eventScope': 'private', 'eventTypeData': None, 'eventDescription': None, 'purpose': None, 'guide': None, 'insight': {'@use': 'false'}, 'level': '1', 'sequence': '1', 'costs': '0', 'eventData': None, 'interfaces': None}}, {'@id': 'A2', 'precondition': {'@message': ''}, 'custom': {'visualization': {'location': {'@xLoc': '750', '@yLoc': '470'}, 'colors': {'@bg': '#f9f7ed', '@textStroke': '#000000', '@stroke': '#cccccc'}}, 'roles': {'role': None}, 'readRoles': {'readRole': None}, 'groups': {'group': None}, 'phases': {'phase': None}, 'eventType': None, 'eventScope': 'private', 'eventTypeData': None, 'eventDescription': None, 'purpose': None, 'guide': None, 'insight': {'@use': 'false'}, 'level': '1', 'sequence': '2', 'costs': '0', 'eventData': None, 'interfaces': None}}, {'@id': 'A3', 'precondition': {'@message': ''}, 'custom': {'visualization': {'location': {'@xLoc': '250', '@yLoc': '220'}, 'colors': {'@bg': '#f9f7ed', '@textStroke': '#000000', '@stroke': '#cccccc'}}, 'roles': {'role': None}, 'readRoles': {'readRole': None}, 'groups': {'group': None}, 'phases': {'phase': None}, 'eventType': None, 'eventScope': 'private', 'eventTypeData': None, 'eventDescription': None, 'purpose': None, 'guide': None, 'insight': {'@use': 'false'}, 'level': '1', 'sequence': '3', 'costs': '0', 'eventData': None, 'interfaces': None}}, {'@id': 'A4', 'precondition': {'@message': ''}, 'custom': {'visualization': {'location': {'@xLoc': '850', '@yLoc': '220'}, 'colors': {'@bg': '#f9f7ed', '@textStroke': '#000000', '@stroke': '#cccccc'}}, 'roles': {'role': None}, 'readRoles': {'readRole': None}, 'groups': {'group': None}, 'phases': {'phase': None}, 'eventType': None, 'eventScope': 'private', 'eventTypeData': None, 'eventDescription': None, 'purpose': None, 'guide': None, 'insight': {'@use': 'false'}, 'level': '1', 'sequence': '4', 'costs': '0', 'eventData': None, 'interfaces': None}}, {'@id': 'A5', 'precondition': {'@message': ''}, 'custom': {'visualization': {'location': {'@xLoc': '600', '@yLoc': '20'}, 'colors': {'@bg': '#f9f7ed', '@textStroke': '#000000', '@stroke': '#cccccc'}}, 'roles': {'role': None}, 'readRoles': {'readRole': None}, 'groups': {'group': None}, 'phases': {'phase': None}, 'eventType': None, 'eventScope': 'private', 'eventTypeData': None, 'eventDescription': None, 'purpose': None, 'guide': None, 'insight': {'@use': 'false'}, 'level': '1', 'sequence': '5', 'costs': '0', 'eventData': None, 'interfaces': None}}, {'@id': 'A6', 'precondition': {'@message': ''}, 'custom': {'visualization': {'location': {'@xLoc': '500', '@yLoc': '470'}, 'colors': {'@bg': '#f9f7ed', '@textStroke': '#000000', '@stroke': '#cccccc'}}, 'roles': {'role': None}, 'readRoles': {'readRole': None}, 'groups': {'group': None}, 'phases': {'phase': None}, 'eventType': None, 'eventScope': 'private', 'eventTypeData': None, 'eventDescription': None, 'purpose': None, 'guide': None, 'insight': {'@use': 'false'}, 'level': '1', 'sequence': '6', 'costs': '0', 'eventData': None, 'interfaces': None}}]}, 'subProcesses': None, 'distribution': None, 'labels': {'label': [{'@id': 'A1'}, {'@id': 'A2'}, {'@id': 'A3'}, {'@id': 'A4'}, {'@id': 'A5'}, {'@id': 'A6'}]}, 'labelMappings': {'labelMapping': [{'@eventId': 'A1', '@labelId': 'A1'}, {'@eventId': 'A2', '@labelId': 'A2'}, {'@eventId': 'A3', '@labelId': 'A3'}, {'@eventId': 'A4', '@labelId': 'A4'}, {'@eventId': 'A5', '@labelId': 'A5'}, {'@eventId': 'A6', '@labelId': 'A6'}]}, 'expressions': None, 'variables': None, 'variableAccesses': {'writeAccesses': None}, 'custom': {'keywords': None, 'roles': None, 'kpis': None, 'groups': None, 'phases': None, 'eventTypes': None, 'eventParameters': None, 'graphDetails': 'DCR Process', 'graphDocumentation': None, 'graphLanguage': 'en-US', 'graphDomain': 'process', 'graphFilters': {'filteredGroups': None, 'filteredRoles': None, 'filteredPhases': None}, 'hightlighterMarkup': {'@id': 'HLM'}, 'highlighterMarkup': {'highlightLayers': None, 'highlights': None}}}, 'constraints': {'conditions': {'condition': {'@sourceId': 'A3', '@targetId': 'A1', '@filterLevel': '1', '@description': '', '@time': '', '@groups': '', '@link': 'A3--condition--A1'}}, 'responses': {'response': {'@sourceId': 'A2', '@targetId': 'A1', '@filterLevel': '1', '@description': '', '@time': '', '@groups': ''}}, 'coresponses': None, 'excludes': {'exclude': {'@sourceId': 'A4', '@targetId': 'A1', '@filterLevel': '1', '@description': '', '@time': '', '@groups': ''}}, 'includes': {'include': {'@sourceId': 'A5', '@targetId': 'A1', '@filterLevel': '1', '@description': '', '@time': '', '@groups': ''}}, 'milestones': {'milestone': [{'@sourceId': 'A3', '@targetId': 'A1', '@filterLevel': '1', '@description': '', '@time': '', '@groups': '', '@link': 'A3--condition--A1'}, {'@sourceId': 'A1', '@targetId': 'A6', '@filterLevel': '1', '@description': '', '@time': '', '@groups': ''}]}, 'updates': None, 'spawns': None, 'templateSpawns': None}}, 'runtime': {'custom': {'globalMarking': None}, 'marking': {'globalStore': None, 'executed': None, 'included': {'event': [{'@id': 'A1'}, {'@id': 'A2'}, {'@id': 'A3'}, {'@id': 'A4'}, {'@id': 'A5'}, {'@id': 'A6'}]}, 'pendingResponses': None}}}}}

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

def EventinList(event,eventlist):
    if eventlist is None:
                return False
    for object in eventlist['event']:
            if event == object['@id']:
                return True
    return False


def createDCRgraph(graph):
    jsn = graph['graph']
    
    dcr = HierarchicalDcrGraph()

    rel = findKey(jsn, 'constraints')
    events = findKey(jsn, 'labelMapping')
    included = findKey(jsn, 'included')
    pending = findKey(jsn, 'pendingResponses')
#    print("\n",rel.items())

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
    print(dcr)
    return dcr

createDCRgraph(test)
