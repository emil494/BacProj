testData = """
<dcrgraph title="test1" dataTypesStatus="hide" filterLevel="-1" insightFilter="false" zoomLevel="0" formGroupStyle="Normal" formLayoutStyle="Horizontal" formShowPendingCount="true" graphBG="#f1f6fe" graphType="0" exercise="false" version="1.1">
<meta>
<graph id="1992798" hash="A78AB51B9EB997210A8170FD97B7337F" guid="05424208-7CC7-4076-97BE-37330DEE4760" OwnerName="Emil Vedel Thage" OwnerId="174110" categoryId="10366" categoryTitle="Default"/>
<revision id="4765086" type="medium" date="2025-05-07T10:25:47.280"/>
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
</labels>
<labelMappings>
<labelMapping eventId="A1" labelId="A1"/>
<labelMapping eventId="A2" labelId="A2"/>
<labelMapping eventId="A3" labelId="A3"/>
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
<condition sourceId="A3" targetId="A1" filterLevel="1" description="" time="" groups="" link="A3--condition--A1"/>
</conditions>
<responses/>
<coresponses/>
<excludes>
<exclude sourceId="A2" targetId="A1" filterLevel="1" description="" time="" groups=""/>
</excludes>
<includes/>
<milestones>
<milestone sourceId="A3" targetId="A1" filterLevel="1" description="" time="" groups="" link="A3--condition--A1"/>
</milestones>
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
</included>
<pendingResponses/>
</marking>
</runtime>
</dcrgraph>"""

import unittest
import flask
import requests as r

class TestLoadXML(unittest.TestCase):

    def test_not_logged_in(self):
        resp = r.post('http://127.0.0.1:5000/api/utility/xml2dcr', data=testData)
        code = resp.status_code
        msg = resp.json()
        self.assertEqual(code, 403)
        self.assertTrue(msg['Status'] == 'Not Logged In/ Invalid Authorization Type')

    def test_misformated(self):
        test = testData + "aaaaaaaaaaaaaaaaaaaaajdisoandisadosa"
        resp = r.post('http://127.0.0.1:5000/api/utility/xml2dcr', auth=('test', '123'), data=test)
        code = resp.status_code
        msg = resp.json()
        self.assertEqual(code, 400)
        self.assertTrue(msg['Status'] == 'Misformated request data')
    
    def test_success(self):
        resp = r.post('http://127.0.0.1:5000/api/utility/xml2dcr', auth=('test', '123'), data=testData)
        code = resp.status_code
        msg = resp.json()
        self.assertEqual(code, 201)
        self.assertTrue(isinstance(msg, int))


class TestGetGraph(unittest.TestCase):

    def test_access(self):
        resp = r.get('http://127.0.0.1:5000/api/graphs/1', auth=('test', '12'))
        code = resp.status_code
        msg = resp.json()
        self.assertTrue(code == 403 and msg['Status'] == 'Access Denied')

    def test_success(self):
        setup = r.post('http://127.0.0.1:5000/api/utility/xml2dcr', auth=('test', '123'), data=testData)
        self.assertEqual(setup.status_code, 201)
        id = setup.json()
        resp = r.get('http://127.0.0.1:5000/api/graphs/' + f'{id}', auth=('test', '123'))
        code = resp.status_code
        msg = resp.json()
        self.assertEqual(code, 200) 
        self.assertTrue(isinstance(msg, dict))

if __name__ == '__main__':
    unittest.main()