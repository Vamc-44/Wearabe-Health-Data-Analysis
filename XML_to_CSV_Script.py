import xml.etree.ElementTree as ET
import pandas as pd

def parse_xml_to_dataframe(xml_file):
    #Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    #Initialize a list to hold the data
    sleep_data = []

    #Iterate through each 'record' element in the XML
    for record in root.findall("Record"):
        row = {
            "type": record.get("type"),
            "startDate": record.get("startDate"),
            "endDate": record.get("endDate"),
            "value": record.get("value"),
        }
        sleep_data.append(row)

    #Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(sleep_data)

    return df
