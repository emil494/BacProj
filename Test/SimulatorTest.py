
from pm4py.objects.dcr.hierarchical.obj import HierarchicalDcrGraph
from pm4py.objects.dcr.extended.semantics import ExtendedSemantics
from simulatorInit import createDCRgraph, ExecuteEventOnGraph, GetAllConds
from server import replaceAllInstances
import unittest
import xmltodict, json

# To run test, simply write: python -m Test.SimulatorTest
# when in terminal at right location ofc


class SimulatorTest(unittest.TestCase):
  def setUp(self):
      with open('Test/XML/test4.xml', 'r') as f: 
          self.xml = f.read()
      self.xml2dict = xmltodict.parse(self.xml)
      self.dict = {"graph" :replaceAllInstances(self.xml2dict, 'null', None)}
      '''self.bs_data = BeautifulSoup(self.xml, "xml")'''
      self.graph = HierarchicalDcrGraph()
      self.events = ("A1","A2","A3")
      for event in self.events:
        self.graph.events.add(event)
        self.graph.labels.add(event)
        self.graph.label_map[event] = event
        self.graph.marking.included.add(event)
      self.graph.marking.pending.add("A3")
      self.graph.excludes["A3"]={"A2"}
      self.graph.excludes["A2"]={"A3","A2","A1"}
      self.graph.includes["A1"]={"A2"}
      self.graph.conditions["A1"]={"A3"}
      self.graph.milestones["A2"]={"A3"}

      self.createGraph = createDCRgraph(self.dict)
      self.semantic = ExtendedSemantics()

  def executeEvent(self,graph,event):
    self.enabled = self.semantic.enabled(graph)
    if event in self.enabled:
      return self.semantic.execute(graph,event)

    
  def test_Markings(self):
    self.assertEqual(self.createGraph.marking.included,self.graph.marking.included)
    self.assertEqual(self.createGraph.marking.pending,self.graph.marking.pending)
    
  def test_Events(self):
    self.assertEqual(self.createGraph.events,self.graph.events)

  def test_Includes(self):
    self.assertEqual(self.createGraph.includes,self.graph.includes)

  def test_Excludes(self):
    self.assertEqual(self.createGraph.excludes,self.graph.excludes)
  
  def test_Responds(self):
    self.assertEqual(self.createGraph.responses,self.graph.responses)

  def test_Conditions(self):
    self.assertEqual(self.createGraph.conditions,self.graph.conditions)
  
  def test_Label(self):
    self.assertEqual(self.createGraph.label_map,self.graph.label_map)

  def test_GettAllConds(self):
    self.assertEqual(GetAllConds(self.graph),GetAllConds(self.createGraph))
  
  def testExecuteEventNotEnabled(self):
    orginalCreateGraph = self.createGraph
    originalgraph = self.graph 
    self.executeEvent(self.graph,"A1")
    ExecuteEventOnGraph(self.createGraph,"A1")
    self.assertEqual(self.createGraph.marking.included,orginalCreateGraph.marking.included)
    self.assertEqual(self.graph.marking.included,originalgraph.marking.included)

    self.assertEqual(self.createGraph.marking.pending,orginalCreateGraph.marking.pending)
    self.assertEqual(self.graph.marking.pending,originalgraph.marking.pending)

    self.assertEqual(self.createGraph.marking.included,self.graph.marking.included)
    self.assertEqual(self.createGraph.marking.pending,self.graph.marking.pending)

  def testExecuteEventEnabled(self):
    self.executeEvent(self.graph,"A3")
    ExecuteEventOnGraph(self.createGraph,"A3")
    self.assertEqual(self.createGraph.marking.included,self.graph.marking.included)
    self.assertEqual(self.createGraph.marking.pending,self.graph.marking.pending)

  def testExecuteEventSequence(self):
    events = ["A3","A1"]
    for event in events:
      self.executeEvent(self.graph,event)
      ExecuteEventOnGraph(self.createGraph,event)
    self.assertEqual(self.createGraph.marking.included,self.graph.marking.included)
    self.assertEqual(self.createGraph.marking.pending,self.graph.marking.pending)

  def testExecuteEventSequenceNotEnabled(self):
    events = ["A3","A2"]
    for event in events:
      self.executeEvent(self.graph,event)
      ExecuteEventOnGraph(self.createGraph,event)
    self.assertEqual(self.createGraph.marking.included,self.graph.marking.included)
    self.assertEqual(self.createGraph.marking.pending,self.graph.marking.pending)

  def testExecuteEventCompleteSequence(self):
    events = ["A3","A1","A2"]
    for event in events:
      self.executeEvent(self.graph,event)
      ExecuteEventOnGraph(self.createGraph,event)
    self.assertEqual(self.createGraph.marking.included,self.graph.marking.included)
    self.assertEqual(self.createGraph.marking.pending,self.graph.marking.pending)

if __name__ == '__main__':
  unittest.main()

