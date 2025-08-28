 						amass_command += ' -config /root/.config/amass.ini'
 					# Run Amass Passive
 					logging.info(amass_command)
					os.system(amass_command)
 
 				elif tool == 'amass-active':
 					amass_command = 'amass enum -active -d {} -o {}/from_amass_active.txt'.format(
 
 					# Run Amass Active
 					logging.info(amass_command)
					os.system(amass_command)
 
 				elif tool == 'assetfinder':
 					assetfinder_command = 'assetfinder --subs-only {} > {}/from_assetfinder.txt'.format(
 						domain.name, results_dir)
 
 					# Run Assetfinder
 					logging.info(assetfinder_command)
					os.system(assetfinder_command)
 
 				elif tool == 'sublist3r':
 					sublist3r_command = 'python3 /usr/src/github/Sublist3r/sublist3r.py -d {} -t {} -o {}/from_sublister.txt'.format(
 						domain.name, threads, results_dir)
 
 					# Run sublist3r
 					logging.info(sublist3r_command)
					os.system(sublist3r_command)
 
 				elif tool == 'subfinder':
 					subfinder_command = 'subfinder -d {} -t {} -o {}/from_subfinder.txt'.format(
 
 					# Run Subfinder
 					logging.info(subfinder_command)
					os.system(subfinder_command)
 
 				elif tool == 'oneforall':
 					oneforall_command = 'python3 /usr/src/github/OneForAll/oneforall.py --target {} run'.format(
 						domain.name, results_dir)
 
 					# Run OneForAll
 					logging.info(oneforall_command)
					os.system(oneforall_command)
 
 					extract_subdomain = "cut -d',' -f6 /usr/src/github/OneForAll/results/{}.csv >> {}/from_oneforall.txt".format(
 						domain.name, results_dir)
 						execution_command = execution_command.replace('{OUTPUT}', '{}/from_{}.txt'.format(results_dir, tool))
 						execution_command = execution_command.replace('{PATH}', custom_tool.github_clone_path) if '{PATH}' in execution_command else execution_command
 						logger.info('Custom tool {} running with command {}'.format(tool, execution_command))
						os.system(execution_command)
 					else:
 						logger.error('Sorry can not run this tool! because TARGET and OUTPUT are not available!')
 	except Exception as e: