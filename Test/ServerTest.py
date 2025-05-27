testData = """
<dcrgraph title="test1" dataTypesStatus="hide" filterLevel="-1" insightFilter="false" zoomLevel="0" formGroupStyle="Normal" formLayoutStyle="Horizontal" formShowPendingCount="true" graphBG="#f1f6fe" graphType="0" exercise="false" version="1.1">
<meta>
<graph id="1992798" hash="F7E54D8487CA0367B94BC0F5BB34791E" guid="05424208-7CC7-4076-97BE-37330DEE4760" OwnerName="Emil Vedel Thage" OwnerId="174110" categoryId="10366" categoryTitle="Default"/>
<revision id="4765116" type="medium" date="2025-05-07T10:27:35.263"/>
<organization id="1024" name="KU - Academic Alliance"/>
</meta>
<specification>
<resources>
<events>
<event id="A1" type="nesting">
<precondition message=""/>
<custom>
<visualization>
<location xLoc="170" yLoc="170"/>
<colors bg="#f9f7ed" textStroke="#000000" stroke="#cccccc"/>
</visualization>
<roles>
<role/>
</roles>
<readRoles>
<readRole/>
</readRoles>
<groups>
<group/>
</groups>
<phases>
<phase/>
</phases>
<eventType/>
<eventScope>private</eventScope>
<eventTypeData/>
<eventDescription/>
<purpose/>
<guide/>
<insight use="false"/>
<level>1</level>
<sequence>1</sequence>
<costs>0</costs>
<eventData/>
<interfaces/>
</custom>
<event id="A2">
<precondition message=""/>
<custom>
<visualization>
<location xLoc="200" yLoc="220"/>
<colors bg="#f9f7ed" textStroke="#000000" stroke="#cccccc"/>
</visualization>
<roles>
<role/>
</roles>
<readRoles>
<readRole/>
</readRoles>
<groups>
<group/>
</groups>
<phases>
<phase/>
</phases>
<eventType/>
<eventScope>private</eventScope>
<eventTypeData/>
<eventDescription/>
<purpose/>
<guide/>
<insight use="false"/>
<level>1</level>
<sequence>2</sequence>
<costs>0</costs>
<eventData/>
<interfaces/>
</custom>
</event>
<event id="A4">
<precondition message=""/>
<custom>
<visualization>
<location xLoc="350" yLoc="220"/>
<colors bg="#f9f7ed" textStroke="#000000" stroke="#cccccc"/>
</visualization>
<roles>
<role/>
</roles>
<readRoles>
<readRole/>
</readRoles>
<groups>
<group/>
</groups>
<phases>
<phase/>
</phases>
<eventType/>
<eventScope>private</eventScope>
<eventTypeData/>
<eventDescription/>
<purpose/>
<guide/>
<insight use="false"/>
<level>1</level>
<sequence>4</sequence>
<costs>0</costs>
<eventData/>
<interfaces/>
</custom>
</event>
</event>
<event id="A3">
<precondition message=""/>
<custom>
<visualization>
<location xLoc="522" yLoc="331"/>
<colors bg="#f9f7ed" textStroke="#000000" stroke="#cccccc"/>
</visualization>
<roles>
<role/>
</roles>
<readRoles>
<readRole/>
</readRoles>
<groups>
<group/>
</groups>
<phases>
<phase/>
</phases>
<eventType/>
<eventScope>private</eventScope>
<eventTypeData/>
<eventDescription/>
<purpose/>
<guide/>
<insight use="false"/>
<level>1</level>
<sequence>3</sequence>
<costs>0</costs>
<eventData/>
<interfaces/>
</custom>
</event>
</events>
<subProcesses/>
<distribution/>
<labels>
<label id="A1"/>
<label id="A2"/>
<label id="A3"/>
<label id="A4"/>
</labels>
<labelMappings>
<labelMapping eventId="A1" labelId="A1"/>
<labelMapping eventId="A2" labelId="A2"/>
<labelMapping eventId="A3" labelId="A3"/>
<labelMapping eventId="A4" labelId="A4"/>
</labelMappings>
<expressions/>
<variables/>
<variableAccesses>
<writeAccesses/>
</variableAccesses>
<custom>
<keywords/>
<roles/>
<kpis/>
<groups/>
<phases/>
<eventTypes/>
<eventParameters/>
<graphDetails>DCR Process</graphDetails>
<graphDocumentation/>
<graphLanguage>en-US</graphLanguage>
<graphDomain>process</graphDomain>
<graphFilters>
<filteredGroups/>
<filteredRoles/>
<filteredPhases/>
</graphFilters>
<hightlighterMarkup id="HLM"/>
<highlighterMarkup>
<highlightLayers>
<highlightLayer default="true" name="description">
<![CDATA[ DCR Process ]]>
</highlightLayer>
</highlightLayers>
<highlights/>
</highlighterMarkup>
</custom>
</resources>
<constraints>
<conditions>
<condition sourceId="A3" targetId="A1" filterLevel="1" description="" time="" groups=""/>
</conditions>
<responses/>
<coresponses/>
<excludes>
<exclude sourceId="A2" targetId="A1" filterLevel="1" description="" time="" groups=""/>
</excludes>
<includes/>
<milestones/>
<updates/>
<spawns/>
<templateSpawns/>
</constraints>
</specification>
<runtime>
<custom>
<globalMarking/>
</custom>
<marking>
<globalStore/>
<executed/>
<included>
<event id="A1"/>
<event id="A2"/>
<event id="A3"/>
<event id="A4"/>
</included>
<pendingResponses/>
</marking>
</runtime>
</dcrgraph>"""

import unittest
import json
import flask
from server import app     

def access_setup(self, adr, method, ret = False):
        resp = self.client.request(method, 'http://127.0.0.1:5000/' + adr)
        code = resp.status_code
        msg = resp.json()
        if ret:
            return code, msg
        self.assertEqual(code, 403)
        self.assertEqual(msg['Status'], 'Access Denied')
    
def sim_setup(self):
    setup = self.client.post('http://127.0.0.1:5000/api/utility/xml2dcr', auth=('test', '123'), data=testData)
    gid = setup.json()
    setup2 = self.client.post('http://127.0.0.1:5000/api/graphs/' + f'{gid}' + '/DCRsimulator', auth=('test', '123'))
    sid = setup2.json()
    return gid, sid

class ServerTest(unittest.TestCase):
    #TODO: Make 1 unified object, rename functions and additional setup functions
    def setUp(self):
        self.client = app.test_client()  # create test client
        self.client.testing = True


    def test_LoadXML_not_logged_in(self):
        resp = self.client.post('http://127.0.0.1:5000/api/utility/xml2dcr', data=testData)
        code = resp.status_code
        msg = resp.json()
        self.assertEqual(code, 403)
        self.assertEqual(msg['Status'], 'Not Logged In/ Invalid Authorization Type')

    def test_LoadXML_misformated(self):
        test = testData + "aaaaaaaaaaaaaaaaaaaaajdisoandisadosa"
        resp = self.client.post('http://127.0.0.1:5000/api/utility/xml2dcr', auth=('test', '123'), data=test)
        code = resp.status_code
        msg = resp.json()
        self.assertEqual(code, 400)
        self.assertEqual(msg['Status'], 'Misformated request data')
    
    def test_LoadXML_success(self):
        resp = self.client.post('http://127.0.0.1:5000/api/utility/xml2dcr', auth=('test', '123'), data=testData)
        code = resp.status_code
        msg = resp.json()
        self.assertEqual(code, 201)
        self.assertIsInstance(msg, int)


    def test_getGraph_access(self):
        access_setup(self, 'api/graphs/1', 'get')

    def test_getGraph_success(self):
        setup = self.client.post('http://127.0.0.1:5000/api/utility/xml2dcr', auth=('test', '123'), data=testData)
        self.assertEqual(setup.status_code, 201)
        id = setup.json()
        resp = self.client.get('http://127.0.0.1:5000/api/graphs/' + f'{id}', auth=('test', '123'))
        code = resp.status_code
        msg = resp.json()
        self.assertEqual(code, 200) 
        self.assertTrue(key == id for key in msg.keys())


    def test_getGraphs_access(self):
        code, msg = access_setup(self, 'api/graphs', 'get', ret=True)
        self.assertEqual(code, 401)
        self.assertEqual(msg['Status'], 'Not Logged In/ Invalid Authorization Type')
    
    def test_getGraphs_failed(self):
        resp = self.client.get('http://127.0.0.1:5000/api/graphs', auth=('test', 'fail'))
        code = resp.status_code
        msg = resp.json()
        self.assertEqual(code, 404)
        self.assertEqual(msg['Status'], 'Failed')

    def test_getGraphs_success(self):
        setup = self.client.post('http://127.0.0.1:5000/api/utility/xml2dcr', auth=('test', '123'), data=testData)
        self.assertEqual(setup.status_code, 201)
        resp = self.client.get('http://127.0.0.1:5000/api/graphs', auth=('test', '123'))
        code = resp.status_code
        msg = resp.json()
        self.assertEqual(code, 200) 
        ids = msg['GIDs']
        self.assertIsInstance(ids, list)
        self.assertGreater(len(msg), 0)


    def test_deleteGraph_access(self):
        access_setup(self, 'api/graphs/0', 'delete')

    def test_deleteGraph_success(self):
        setup = self.client.post('http://127.0.0.1:5000/api/utility/xml2dcr', auth=('test', '123'), data=testData)
        self.assertEqual(setup.status_code, 201)
        id = setup.json()
        resp = self.client.delete('http://127.0.0.1:5000/api/graphs/' + f'{id}', auth=('test', '123'))
        code = resp.status_code
        msg = resp.json()
        self.assertEqual(code, 200)
        self.assertEqual(msg['Status'], 'Success')

        check = self.client.get('http://127.0.0.1:5000/api/graphs/' + f'{id}')
        check_code = check.status_code
        self.assertEqual(check_code, 403) # Check if actually deleted

        check2 = self.client.post('http://127.0.0.1:5000/api/utility/xml2dcr', auth=('test', '123'), data=testData)
        self.assertEqual(check2.status_code, 201)
        self.assertEqual(int(check2.content), id) # Check if id becomes available again


    def test_DCRsimulator_access(self):
        access_setup(self, 'api/graphs/0/DCRsimulator', 'post')
    
    def test_DCRsimulator_success(self):
        setup = self.client.post('http://127.0.0.1:5000/api/utility/xml2dcr', auth=('test', '123'), data=testData)
        gid = setup.json()
        resp = self.client.post('http://127.0.0.1:5000/api/graphs/' + f'{gid}' + '/DCRsimulator', auth=('test', '123'))
        code = resp.status_code
        sid = int(resp.json())
        self.assertEqual(code, 201)
        self.assertIsInstance(sid, int) # Accuracy of graph is tested in SimulatorTest


    def test_getSim_access(self):
        access_setup(self, 'api/graphs/0/sims/100', 'get')

    def test_getSim_success(self):
        gid, sid = sim_setup()
        resp = self.client.get(f'http://127.0.0.1:5000/api/graphs/{gid}/sims/{sid}', auth=('test', '123'))
        code = resp.status_code
        msg = resp.json()
        self.assertEqual(code, 200)
        self.assertTrue(key == sid for key in msg.keys())


    def test_getSims_access(self):
        access_setup(self, 'api/graphs/0/sims', 'get')

    def test_getSims_success(self):
        gid, sid = sim_setup()
        resp = self.client.get(f'http://127.0.0.1:5000/api/graphs/{gid}/sims', auth=('test', '123'))
        code = resp.status_code
        msg = resp.json()
        self.assertEqual(code, 200)
        self.assertIn(str(sid), msg)


    def test_deleteSim_access(self):
        access_setup(self, 'api/graphs/0/sims/100', 'delete')        

    def test_deleteSim_success(self):
        gid, sid = sim_setup()
        resp = self.client.delete('http://127.0.0.1:5000/api/graphs/' + f'{gid}' + '/sims/' + f'{sid}', auth=('test', '123'))
        code = resp.status_code
        msg = resp.json()
        self.assertEqual(code, 200)
        self.assertEqual(msg['Status'], 'Success')

        check = self.client.get('http://127.0.0.1:5000/api/graphs/' + f'{gid}' + '/sims/' + f'{sid}')
        check_code = check.status_code
        self.assertEqual(check_code, 403) # Check if actually deleted

        check2 = self.client.post('http://127.0.0.1:5000/api/graphs/' + f'{gid}' + '/DCRsimulator', auth=('test', '123'), data=testData)
        self.assertEqual(check2.status_code, 201)
        self.assertEqual(check2.json(), sid) # Check if id becomes available again


    def test_getEvents_access(self):
        access_setup(self, 'api/graphs/0/sims/100/events', 'get')     

    def test_getEvents_success(self):
        gid, sid = sim_setup()
        resp = self.client.get('http://127.0.0.1:5000/api/graphs/' + f'{gid}' + '/sims/' + f'{sid}' + '/events', auth=('test', '123'))
        code = resp.status_code
        msg = resp.json()
        self.assertEqual(code, 200)
        self.assertDictEqual(msg, {'A1' : 'A1', 'A2' : 'A2', 'A3' : 'A3', 'A4' : 'A4'})


    def test_getRelations_access(self):
        access_setup(self, 'api/graphs/0/sims/100/relations', 'get')     

    def test_getRelations_success(self):
        gid, sid = sim_setup()
        resp = self.client.get('http://127.0.0.1:5000/api/graphs/' + f'{gid}' + '/sims/' + f'{sid}' + '/relations', auth=('test', '123'))
        code = resp.status_code
        msg = resp.json()
        self.assertEqual(code, 200)
        self.assertDictEqual(msg, {'Conditions': [{'A1': "{'A3'}"}], 'Excludes': [{'A2': "{'A1'}"}], 'Includes': [], 'Milestone': [], 'Responses': []})


    def test_getIncluded_access(self):
        access_setup(self, 'api/graphs/0/sims/100/included', 'get')     

    def test_getIncluded_success(self):
        gid, sid = sim_setup()
        resp = self.client.get('http://127.0.0.1:5000/api/graphs/' + f'{gid}' + '/sims/' + f'{sid}' + '/included', auth=('test', '123'))
        code = resp.status_code
        msg = resp.json()
        self.assertEqual(code, 200)
        events = ['A1', 'A2', 'A3', 'A4']
        self.assertEqual(len(events), len(msg))
        self.assertTrue(e in msg for e in events)


    def test_getPending_access(self):
        access_setup(self, 'api/graphs/0/sims/100/pending', 'get')     

    def test_getPending_success(self):
        gid, sid = sim_setup()
        resp = self.client.get('http://127.0.0.1:5000/api/graphs/' + f'{gid}' + '/sims/' + f'{sid}' + '/pending', auth=('test', '123'))
        code = resp.status_code
        msg = resp.json()
        self.assertEqual(code, 200)
        events = []
        self.assertEqual(len(events), len(msg))
        self.assertTrue(e in msg for e in events)


    def test_getExecuted_access(self):
        access_setup(self, 'api/graphs/0/sims/100/executed', 'get')     

    def test_getExecuted_success(self):
        gid, sid = sim_setup()
        resp = self.client.get('http://127.0.0.1:5000/api/graphs/' + f'{gid}' + '/sims/' + f'{sid}' + '/executed', auth=('test', '123'))
        code = resp.status_code
        msg = resp.json()
        self.assertEqual(code, 200)
        events = []
        self.assertEqual(len(events), len(msg))
        self.assertTrue(e in msg for e in events)


    def test_executeEvent_access(self):
        access_setup(self, 'api/graphs/0/DCRsimulator/0/executeEvent/A4', 'put')     

    def test_executeEvent_unsuccessful(self):
        gid, sid = sim_setup()
        event = 'A1' #TODO: If nesting semantics implemented, change event to A2 or A4
        resp = self.client.put('http://127.0.0.1:5000/api/graphs/' + f'{gid}' + '/DCRsimulator/' + f'{sid}' + '/executeEvent/' + event, auth=('test', '123'))
        code = resp.status_code
        msg = resp.json()
        self.assertEqual(code, 409)
        self.assertEqual(msg['Status'], {"Unsuccessful": ['A1'], "Successful" : []})

    def test_executeEvent_success(self):
        gid, sid = sim_setup()
        event = 'A3'
        resp = self.client.put('http://127.0.0.1:5000/api/graphs/' + f'{gid}' + '/DCRsimulator/' + f'{sid}' + '/executeEvent/' + event, auth=('test', '123'))
        code = resp.status_code
        msg = resp.json()
        self.assertEqual(code, 200)
        self.assertEqual(msg['Status'], "Success")

        check = self.client.get('http://127.0.0.1:5000/api/graphs/' + f'{gid}' + '/sims/' + f'{sid}' + '/executed', auth=('test', '123'))
        self.assertIn(event, check.json()) # Check that the event is in the executed list


    def test_executeTrace_access(self):
        access_setup(self, 'api/graphs/0/DCRsimulator/0/executeTrace', 'put')   

    def test_executeTrace_misformated(self):
        data = testData + 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
        gid, sid = sim_setup()
        resp = self.client.put('http://127.0.0.1:5000/api/graphs/' + f'{gid}' + '/DCRsimulator/' + f'{sid}' + '/executeTrace', auth=('test', '123'), data=data)
        code = resp.status_code
        msg = resp.json()
        self.assertEqual(code, 400)
        self.assertEqual(msg['Status'], 'Misformated request data')     

    def test_executeTrace_unsuccessful(self):
        trace = '{"trace": ["A1", "A3"]}'
        #TODO: Change A1 to A2 or A4 when nesting semantics are implemented
        gid, sid = sim_setup()
        resp = self.client.put('http://127.0.0.1:5000/api/graphs/' + f'{gid}' + '/DCRsimulator/' + f'{sid}' + '/executeTrace', auth=('test', '123'), data=trace)
        code = resp.status_code
        msg = resp.json()
        self.assertEqual(code, 409)
        self.assertDictEqual(msg['Status'], {"Unsuccessful": ['A1'], "Successful" : ['A3']})

    def test_executeTrace_success(self):
        trace = '{"trace": ["A3", "A1"]}'
        gid, sid = sim_setup()
        resp = self.client.put('http://127.0.0.1:5000/api/graphs/' + f'{gid}' + '/DCRsimulator/' + f'{sid}' + '/executeTrace', auth=('test', '123'), data=trace)
        code = resp.status_code
        msg = resp.json()
        self.assertEqual(code, 200)
        self.assertEqual(msg['Status'], 'Success')

        check = self.client.get('http://127.0.0.1:5000/api/graphs/' + f'{gid}' + '/sims/' + f'{sid}' + '/executed', auth=('test', '123'))
        self.assertTrue(t in check.json() for t in json.loads(trace)['trace']) # Check that the event is in the executed list

if __name__ == '__main__':
    unittest.main()