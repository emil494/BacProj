import xmltodict
from flask import Flask, request
import xml.etree.ElementTree as ET
import xmltodict

app = Flask(__name__)
graphIDs = {}
simIDs = {}

@app.post('/api/graphs/loadXML')
def loadXML():
    xml = request.data
    tree = ET.parse(xml)
    root = tree.getroot()

    subroot = root.find('events')

    for e in subroot.findall('event'):
        print(e.attrib)