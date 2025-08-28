 
             cwd_path = os.path.split(os.path.realpath(__file__))[0]
 
             p = subprocess.Popen(["horovodrun", "-np", str(nprocs), "-H", f"localhost:{nprocs}",
                                   sys.executable, f"{cwd_path}/horovod_worker.py", temp_dir])
 