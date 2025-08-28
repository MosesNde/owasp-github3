                                     source_type_hash]['ranges']:
                                 the_second_stack = stack
                                 break
            if not the_second_stack:
                return
             self.vul_source_signature = None
             self.vul_stack = []
             self.pool_value = set(the_second_stack.get('sourceHash'))
             for ind, method in enumerate(self.method_pool):
                 if method['invokeId'] == the_second_stack['invokeId']: