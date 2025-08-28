     @staticmethod
     def start_ray_daemon(python_loc, pid_to_watch, pgid_to_kill):
         daemon_path = os.path.join(os.path.dirname(__file__), "ray_daemon.py")
         start_daemon_command = ['nohup', python_loc, daemon_path, str(pid_to_watch),
                                 str(pgid_to_kill)]
         # put ray daemon process in its children's process group to avoid being killed by spark.