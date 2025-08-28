         return self.run_subprocess(target, args=args, nprocs=nprocs, envs=envs)
 
     def run_subprocess(self, target, args=..., nprocs=1, envs=None) -> Any:
        import pickle
         import subprocess
         import sys
 
         with TemporaryDirectory() as temp_dir:
             with open(os.path.join(temp_dir, "args.pkl"), 'wb') as f:
                pickle.dump((envs,) + args, f)
             with open(os.path.join(temp_dir, "target.pkl"), 'wb') as f:
                pickle.dump(target, f)
 
             cwd_path = os.path.split(os.path.realpath(__file__))[0]
 
             results = []
             for i in range(nprocs):
                 with open(os.path.join(temp_dir, f"history_{i}"), "rb") as f:
                    results.append(pickle.load(f))
         return results