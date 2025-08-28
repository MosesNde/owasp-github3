 import logging
 
 from .cmd import (N_EVAL, N_ACC, N_REQ, N_FAIL, ALL_ACCEPTED,
                  N_WORKER, SSA, QUEUE,
                   BATCH_SIZE, IS_LOOK_AHEAD, ANALYSIS_ID,
                   idfy)
 from ..util import any_particle_preliminary
 
         # increase global evaluation counter (before simulation!)
         particle_max_id = redis.incr(idfy(N_EVAL, ana_id, t), batch_size)
 
         # timer for current simulation until batch_size acceptances
         this_sim_start = time()