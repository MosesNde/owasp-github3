         ):
             op, spot, key = op_data[0], op_data[1][0], op_data[1][1]
             data = None
            print(kwargs, key)
             if kwargs.get(key, None):
                 # Keyword found, setting data
                 data = kwargs.get(key)