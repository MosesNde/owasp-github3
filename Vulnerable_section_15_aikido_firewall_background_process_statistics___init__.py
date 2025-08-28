 
     def reset(self):
         """Resets the stored data to an initial state"""
        self.stats = dict()
         self.requests = {
             "total": 0,
             "aborted": 0,