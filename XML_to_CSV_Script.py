# Import necessary libraries
import xml.etree.ElementTree as ET
import pandas as pd

# Load and parse the XML file
def parse_sleep_data(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    sleep_data = []

    for record in root.findall("Record"):
        if record.get("type") == "HKCategoryTypeIdentifierSleepAnalysis":
            start_time = record.get("startDate")
            end_time = record.get("endDate")
            value = record.get("value")  # Can be "Asleep", "Awake", etc.

            sleep_data.append({"Start Time": start_time, "End Time": end_time, "Sleep Type": value})

    # Convert to Pandas DataFrame
    df = pd.DataFrame(sleep_data)
    return df

