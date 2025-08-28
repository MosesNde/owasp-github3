     former_getresponse = copy.deepcopy(http.HTTPConnection.getresponse)
 
     def aik_new_putrequest(_self, method, path, *args, **kwargs):
        #  Aikido putrequest, gets called before the request went through
        try:
            # Set path for aik_new_getresponse :
            _self.aikido_attr_path = path

            # Create a URL Object :
            assembled_url = f"http://{_self.host}:{_self.port}{path}"
            url_object = try_parse_url(assembled_url)

            run_vulnerability_scan(
                kind="ssrf", op="http.client.putrequest", args=(url_object, _self.port)
            )
        except AikidoException as e:
            raise e
        except Exception as e:
            logger.debug("Exception occured in custom putrequest function : %s", e)
         return former_putrequest(_self, method, path, *args, **kwargs)
 
     def aik_new_getresponse(_self):