 
 @Client.command()
 async def dirsearch(ctx , *, argument):
     Path = TOOLS['dirsearch']; MainPath = getcwd(); chdir(Path)
     await ctx.send(f"**Running Your Dirsearch Scan, We Will Send The Results When It's Done**")
     Process = subprocess.Popen(f'python3 dirsearch.py -u {argument} -e * -b' , shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
 
 @Client.command()
 async def arjun(ctx , *, argument):
     Path = TOOLS['arjun']; MainPath = getcwd(); chdir(Path)
     await ctx.send(f"**Running Your Arjun Scan, We Will Send The Results When It's Done**")
     await ctx.send(f"**Note: The Bot Won't Respond Until The Scan is Done. All Of Your Commands Now Will Be Executed After This Process is Done.")