 from ...epsilon import Epsilon
 from ...acceptor import Acceptor
 from ...sampler import Sampler, Sample
from .cmd import (SSA, N_EVAL, N_ACC, N_REQ, N_FAIL, ALL_ACCEPTED,
                  N_WORKER, QUEUE, MSG, START, MODE, DYNAMIC,
                  SLEEP_TIME, BATCH_SIZE, IS_LOOK_AHEAD, ANALYSIS_ID,
                  GENERATION, idfy)
 from .redis_logging import RedisSamplerLogger
 
 logger = logging.getLogger("Redis-Sampler")
         # set total number of evaluations
         self.nr_evaluations_ = int(
             self.redis.get(idfy(N_EVAL, ana_id, t)).decode())
 
         # remove all time-specific variables
         self.clear_generation_t(t)
         # logging
         self.logger.add_row(
             t=t, n_evaluated=self.nr_evaluations_,
            n_accepted=sample.n_accepted)
         self.logger.write()
 
         return sample
          .set(idfy(N_ACC, ana_id, t), 0)
          .set(idfy(N_REQ, ana_id, t), n)
          .set(idfy(N_FAIL, ana_id, t), 0)
          # encode as int
          .set(idfy(ALL_ACCEPTED, ana_id, t), int(all_accepted))
          .set(idfy(N_WORKER, ana_id, t), 0)
          .delete(idfy(N_ACC, ana_id, t))
          .delete(idfy(N_REQ, ana_id, t))
          .delete(idfy(N_FAIL, ana_id, t))
          .delete(idfy(ALL_ACCEPTED, ana_id, t))
          .delete(idfy(N_WORKER, ana_id, t))
          .delete(idfy(BATCH_SIZE, ana_id, t))
     # 0 is relative start time, 1 is the actual sample
     sample = sample_with_id[1]
 
    # check whether the sample was generated in look-ahead mode
    if sample.is_look_ahead:
        logger.n_lookahead += 1

     # check whether there are preliminary particles
     if not any(particle.preliminary for particle in sample.particles):
         n_accepted = sum(particle.accepted for particle in sample.particles)
         if n_accepted != 1:
             # this should never happen
             raise AssertionError(
                 "Expected exactly one accepted particle in sample.")
         # increase accepted counter if in look-ahead mode
         if sample.is_look_ahead:
            logger.n_lookahead_accepted += n_accepted
         # nothing else to be done
         return sample_with_id, True
 
         sample.particles[i_particle] = \
             evaluate_preliminary_particle(particle, t, ana_vars)
 
        # update the redis shared counter
         if sample.particles[i_particle].accepted:
             redis.incr(idfy(N_ACC, ana_id, t), 1)
             logger.n_lookahead_accepted += 1
 
     return (sample_with_id,