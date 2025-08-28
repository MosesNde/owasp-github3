                 self.remote_hosts.append(host)
         print("Remote hosts: ", self.remote_hosts)
         print("Hosts: ", self.hosts)
         self.processes_per_node = processes_per_node
         self.env = env if env else {}
 
         cmd = ["mpiexec.hydra"]
         # -l would label the output with process rank. -l/-ppn not available for openmpi.
         # mpi_config = "-np {} ".format(
        mpi_config = "-np {} -ppn {} -l ".format(
            self.processes_per_node * len(self.hosts),
            self.processes_per_node)
         mpi_env = os.environ.copy()
         mpi_env.update(self.env)
         if "I_MPI_PIN_DOMAIN" in mpi_env:
            mpi_config += "-genv I_MPI_PIN_DOMAIN={} ".format(mpi_env["I_MPI_PIN_DOMAIN"])
         if "OMP_NUM_THREADS" in mpi_env:
            mpi_config += "-genv OMP_NUM_THREADS={} ".format(mpi_env["OMP_NUM_THREADS"])
         if len(self.remote_hosts) > 0:
            mpi_config += "-hosts {}".format(",".join(self.hosts))
        cmd.extend(mpi_config.split())
         # cmd.append("ls")
         cmd.append(sys.executable)
         cmd.append("-u")  # This can print as the program runs