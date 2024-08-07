import csv
import xml.etree.ElementTree as ET
from xml.dom import minidom
import os
import codecs

def prettify(elem):
    """Return a pretty-printed XML string for the Element."""
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

# Leer el archivo CSV
csv_file_path = r'C:\Users\franciscojavier.mart\Documents\iNews_parser\libro1.csv'
csv_filename = os.path.splitext(os.path.basename(csv_file_path))[0]
csv_data = []

with codecs.open(csv_file_path, encoding='utf-8-sig') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=';')
    csv_data = list(csvreader)
    #total_lines = len(csv_data)
    for row in csvreader:
        csv_data.append(row)

# Generar un archivo XML por cada línea en el CSV
for idx, row in enumerate(csv_data):
    # Create the root element
    root = ET.Element("NewsML", Version="1.2")

    # Add comment
    root.append(ET.Comment("Documentation:\nIMPORTANT INFO:\n    - Tesauro deprecated: Use SubjetCode."))

    # Add NewsEnvelope
    news_envelope = ET.SubElement(root, "NewsEnvelope")
    ET.SubElement(news_envelope, "DateAndTime").text = "20240515T140206+0000"

    # Add another comment
    root.append(ET.Comment("** SUGGESTION FOR DEVS: Use 'Duid' attribute to help you on XPath navigation."))

    # Add NewsItem
    news_item = ET.SubElement(root, "NewsItem", Duid="text_55013577599")
    ET.SubElement(news_item, "Comment", FormalName="EfeNewsMLVersion").text = "1.0.1"

    # Add NewsManagement
    news_management = ET.SubElement(news_item, "NewsManagement")
    ET.SubElement(news_management, "NewsItemType", FormalName="News")
    ET.SubElement(news_management, "FirstCreated").text = "20240515T122125+0000"
    ET.SubElement(news_management, "ThisRevisionCreated").text = "20240515T140119+0000"
    ET.SubElement(news_management, "Status", FormalName="Usable")
    ET.SubElement(news_management, "Urgency", FormalName="5")

    # Add NewsComponent
    news_component = ET.SubElement(news_item, "NewsComponent", Duid="text_55013577599.text")
    ET.SubElement(news_component, "Role", FormalName="Main")

    # Add NewsLines
    news_lines = ET.SubElement(news_component, "NewsLines")
    ET.SubElement(news_lines, "HeadLine").text = "Alemania ve alejarse a Georgia de Europa y apoya las protestas a la \"ley rusa\""
    ET.SubElement(news_lines, "SubHeadLine").text = "GEORGIA OPOSICIÓN"
    ET.SubElement(news_lines, "RunDownLine1").text = row['Noticia']
    ET.SubElement(news_lines, "RunDownLine2").text = row['Presentador']
    ET.SubElement(news_lines, "RunDownLine3").text = row['Ubicación']
    ET.SubElement(news_lines, "RunDownLine4").text = row['camara']

    # Add AdministrativeMetadata
    admin_metadata = ET.SubElement(news_component, "AdministrativeMetadata")
    provider = ET.SubElement(admin_metadata, "Provider")
    ET.SubElement(provider, "Party", FormalName="Agencia EFE")

    # Add DescriptiveMetadata
    desc_metadata = ET.SubElement(news_component, "DescriptiveMetadata")
    ET.SubElement(desc_metadata, "Language", FormalName="es-ES")
    location = ET.SubElement(desc_metadata, "Location", HowPresent="Event")
    ET.SubElement(location, "Property", FormalName="Country", Value="DEU")
    ET.SubElement(location, "Property", FormalName="City", Value="Berlín")

    subject_code1 = ET.SubElement(desc_metadata, "SubjectCode")
    ET.SubElement(subject_code1, "Subject", FormalName="11000000", Scheme="IptcSubjectCodes")

    subject_code2 = ET.SubElement(desc_metadata, "SubjectCode")
    ET.SubElement(subject_code2, "SubjectMatter", FormalName="11002000", Scheme="IptcSubjectCodes")

    ET.SubElement(desc_metadata, "Property", FormalName="Tesauro", Value="POL:POLITICA;POL:POLITICA,EXTERIOR")
    ET.SubElement(desc_metadata, "Property", FormalName="EfePais", Value="DEU")
    ET.SubElement(desc_metadata, "Property", FormalName="EfeRegional", Value="")
    ET.SubElement(desc_metadata, "Property", FormalName="EfeComplemento", Value="")

    # Add ContentItem
    content_item = ET.SubElement(news_component, "ContentItem")
    ET.SubElement(content_item, "MediaType", FormalName="Text")
    ET.SubElement(content_item, "Format", FormalName="NITF")
    ET.SubElement(content_item, "MimeType", FormalName="text/vnd.IPTC.NITF")

    # Add DataContent
    data_content = ET.SubElement(content_item, "DataContent")
    nitf = ET.SubElement(data_content, "nitf", version="-//IPTC//DTD NITF 3.2//EN", change_date="October 10, 2003", change_time="19:30", baselang="es-ES")
    body = ET.SubElement(nitf, "body")
    body_head = ET.SubElement(body, "body.head")
    body_content = ET.SubElement(body, "body.content")

    ET.SubElement(body_content, "p").text = row["Texto"]
    #ET.SubElement(body_content, "p").text = "prueba linea de texto 2 del cuerpo noticia"

    # Generate the final XML string
    xml_str = prettify(root)

    # Save to a file
    output_file_path = r"C:\Users\franciscojavier.mart\Documents\iNews_parser\csv\prueba_" + str(idx+1) + "_" + csv_filename + ".xml"
    with open(output_file_path, "w", encoding="utf-8-sig") as f:
        f.write(xml_str)

print("XML files generated successfully.")
