from flask import render_template
from flask import Flask

from datetime import datetime
import os
import xml.etree.ElementTree as ET
import requests
from xml.etree import ElementTree as etree

app = Flask(__name__,  template_folder='templates', static_folder='static')


@app.route('/livecyclehireupdates', methods=['GET', 'POST'])
def livecyclehireupdates():
    document = requests.get("https://tfl.gov.uk/tfl/syndication/feeds/cycle-hire/livecyclehireupdates.xml")
    tree = etree.fromstring(document.content)
    stationArr = []
    for station in tree.findall('station'):
        response = {}
        response['id'] = station.find('id').text
        response['name'] = station.find('name').text
        response['terminalName'] = station.find('terminalName').text
        response['lat'] = station.find('lat').text
        response['long'] = station.find('long').text
        response['installed'] = station.find('installed').text
        response['removalDate'] = station.find('removalDate').text
        response['locked'] = station.find('locked').text
        response['installDate'] = station.find('installDate').text
        response['temporary'] = station.find('temporary').text
        response['nbBikes'] = station.find('nbBikes').text
        response['nbStandardBikes'] = station.find('nbStandardBikes').text
        response['nbEBikes'] = station.find('nbEBikes').text
        response['nbEmptyDocks'] = station.find('nbEmptyDocks').text
        response['nbDocks'] = station.find('nbDocks').text
        stationArr.append(response)
    return stationArr




if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
    

