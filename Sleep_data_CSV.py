from XML_to_CSV_Script import parse_xml_to_dataframe
import pandas as pd

#Read the XML file into a pandas DataFrame
xml_file = 'export/apple_health_export/export.xml'
df = parse_xml_to_dataframe(xml_file)
print(df.head()) # Display the first few rows of the DataFrame  

#Converting the DataFrame to CSV  
df.to_csv('sleep_data.csv', index=False)
print('XML data successfully converted to CSV.')
print(df.head())  # Display the first few rows of the DataFrame 




