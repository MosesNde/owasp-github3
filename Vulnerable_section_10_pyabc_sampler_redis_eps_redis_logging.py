         self.data = []
 
         # internal counters
        self.n_lookahead: int = 0
         self.n_lookahead_accepted: int = 0
         self.n_preliminary: int = 0
 
     def reset_counters(self):
         """Reset counters. Typically at the start of a generation."""
        self.n_lookahead = 0
         self.n_lookahead_accepted = 0
         self.n_preliminary = 0
 
    def add_row(self, t: int, n_evaluated: int, n_accepted: int,
                n_lookahead: int = None, n_lookahead_accepted: int = None,
                n_preliminary: int = None):
         """Add row for time `t`."""
         # apply defaults
        if n_lookahead is None:
            n_lookahead = self.n_lookahead
        if n_lookahead_accepted is None:
            n_lookahead_accepted = self.n_lookahead_accepted
        if n_preliminary is None:
            n_preliminary = self.n_preliminary
 
         # append a row
         self.data.append({
            't': t, 'n_evaluated': n_evaluated, 'n_accepted': n_accepted,
             'n_lookahead': n_lookahead,
            'n_lookahead_accepted': n_lookahead_accepted,
            'n_preliminary': n_preliminary})
 
     def write(self):
         """Write data to output."""