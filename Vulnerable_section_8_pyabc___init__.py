     AdaptivePopulationSize,
     ConstantPopulationSize)
 from . import visualization
 from .version import __version__  # noqa: F401
 
 try:
     loglevel = os.environ['ABC_LOG_LEVEL'].upper()
 except KeyError:
     loglevel = 'INFO'

 logging.basicConfig(level=loglevel)
 
 if 'OMP_NUM_THREADS' not in os.environ:
     os.environ['OMP_NUM_THREADS'] = '1'