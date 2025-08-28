 from bigdl.dllib.utils.utils import get_zoo_bigdl_classpath_on_driver
 from bigdl.dllib.utils.utils import get_bigdl_class_version
 from bigdl.dllib.utils.utils import get_bigdl_image_workdir
 from bigdl.dllib.utils.engine import get_bigdl_jars
 from bigdl.dllib.utils.log4Error import *
 
             pyspark_home = os.path.abspath(pyspark.__file__ + "/../")
             zoo_standalone_home = os.path.abspath(__file__ + "/../../../share/dllib/bin/standalone")
             node_ip = get_node_ip()
             SparkRunner.standalone_env = {
                 "SPARK_HOME": pyspark_home,
                 "ZOO_STANDALONE_HOME": zoo_standalone_home,
                 # If not set this, by default master is hostname but not ip,
                 "SPARK_MASTER_HOST": node_ip}
             if 'JAVA_HOME' in os.environ:
                 SparkRunner.standalone_env["JAVA_HOME"] = os.environ["JAVA_HOME"]
             # The scripts installed from pip don't have execution permission
             # and need to first give them permission.
             pro = subprocess.Popen(["chmod", "-R", "+x", "{}/sbin".format(zoo_standalone_home)])
             else:
                 worker_script = "start-worker.sh"
             start_worker_pro = subprocess.Popen(
                "{}/sbin/{} {}".format(zoo_standalone_home, worker_script, master),
                 shell=True, env=SparkRunner.standalone_env)
             _, status = os.waitpid(start_worker_pro.pid, 0)
             if status != 0: