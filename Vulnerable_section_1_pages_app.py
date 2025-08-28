               "astro_colibri_api_key": colibri_api_key,
               }
     name = st.session_state.get("username", "user")
    config_filename = f"{username}_config.json"
     config_path = os.path.join(
         st.session_state.get("output_dir", "rpp_results"), config_filename
     )