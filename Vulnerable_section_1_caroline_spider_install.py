     # then the github repositories
     for dependency in GITHUB_DEPENDENCIES.keys():
         os.system(f'''echo "{dependency}..."''')
        if os.path.exists(f"{CONFIG['CAROLINE_PLUGINS_DIRECTORIES']}/{dependency}"):
             # if the path exists, the directory has already been cloned once before. We need to sync with git pull
             # to the right branch. This is one command as we need to change directories
             os.system(
                f"cd {CONFIG['CAROLINE_PLUGINS_DIRECTORIES']}/{dependency}; git pull; "
                 f"git checkout {GITHUB_DEPENDENCIES[dependency]['branch']}; git pull"
             )
         else: