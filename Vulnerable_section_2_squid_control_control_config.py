     # B1 upper left corner in mm: x = 12.13 mm - 3.3 mm/2, y = 8.99 mm + 4.5 mm - 3.3 mm/2
     # B2 upper left corner in pixel: x = 177, y = 141
 
    WELLPLATE_OFFSET_X_mm: float = 0  # x offset adjustment for using different plates
    WELLPLATE_OFFSET_Y_mm: float = 0  # y offset adjustment for using different plates
 
     # for USB spectrometer
     N_SPECTRUM_PER_POINT: int = 5
         config_path = current_dir / (
             "../configurations/configuration_" + str(config_path) + ".ini"
         )
 
     CONFIG.CACHE_CONFIG_FILE_PATH = str(config_dir / "cache_config_file_path.txt")
     CONFIG.CHANNEL_CONFIGURATIONS_PATH = str(config_dir / "uc2_fucci_illumination_configurations.xml")
     CONFIG.LAST_COORDS_PATH = str(config_dir / "last_coords.txt")
 
    if config_path and not os.path.exists(config_path):
         raise FileNotFoundError(f"Configuration file {config_path} not found.")

     cf_editor_parser = ConfigParser()
     cached_config_file_path = CONFIG.read_config(config_path)
     CONFIG.STAGE_POS_SIGN_X = CONFIG.STAGE_MOVEMENT_SIGN_X
         CONFIG.A1_X_MM = 24.55
         CONFIG.A1_Y_MM = 23.01
 
     # Write configuration to txt file after reading
     CONFIG.write_config_to_txt('config_parameters.txt')

 
     try:
        if os.path.exists(cached_config_file_path):
             cf_editor_parser.read(cached_config_file_path)
    except:
         return False
 
 
 # For flexible plate format: