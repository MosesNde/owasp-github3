 
     def load_xml_config_file(self, config_file):
         import xml.etree.ElementTree as ET
 
         with open(config_file, 'r') as file:
            config = ET.parse(file).getroot()
 
         self.handle_config(config)
 