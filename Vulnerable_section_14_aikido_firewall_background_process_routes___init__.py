 
     def __init__(self, max_size=1000):
         self.max_size = max_size
        self.routes = dict()
 
     def add_route(self, method, path):
         """