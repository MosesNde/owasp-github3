 #using os to set current working directory
 #find the current path
 path=os.path.abspath(__file__)
#find the .ini file in the directory
path_ini=os.path.join(os.path.dirname(path),'configuration_HCS_v2.ini')
path_ini=Path(path_ini)



load_config(path_ini, False)
 class SquidController:
     fps_software_trigger= 10
 