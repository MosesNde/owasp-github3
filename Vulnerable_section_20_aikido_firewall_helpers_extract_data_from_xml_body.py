 
     extracted_xml_attrs = context.xml
     for el in root_element:
        print(extracted_xml_attrs)
         for k, v in el.items():
            print("Key : %s, Value : %s", k, v)
             if not extracted_xml_attrs.get(k):
                 extracted_xml_attrs[k] = set()
             extracted_xml_attrs[k].add(v)