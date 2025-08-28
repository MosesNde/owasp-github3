 '''
 
 TEMP_PATH = "bigdl/share/dllib"
 dllib_src_path = os.path.abspath(__file__ + "/..")
 
try:
    exec(open(dllib_src_path + "/bigdl/dllib/version.py").read())
except IOError:
    print("Failed to load bigdl-dllib version file for packaging. "
          "You need to run the release script instead.")
    sys.exit(-1)
 
VERSION = __version__  # noqa
 PYSPARK_VERSION = '2.4.6'
 
 building_error_msg = """