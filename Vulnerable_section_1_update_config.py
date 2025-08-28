         # Save the updated config
         if updated:
             with open("config.json", "w") as config_file:
                json.dump(current_config, json.dumps(current_config, indent=4))
             print("Configuration updated successfully!")
         else:
             print("Configuration is already up to date!")