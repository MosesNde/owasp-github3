             def feed(data):
                 former_feed_result = self._feed_func_copy(data)
 
                # Fetch the data, this should just return an internal attribute and not close a stream
                # Or something that is noticable by the end-user
                 parsed_xml = self.target.close()
                 extract_data_from_xml_body(user_input=data, root_element=parsed_xml)
 