     logger.info("Successfully wrapped package `%s` version (%s)", pkg_name, pkg_version)
     attempts = 0
     while attempts < MAX_REPORT_TRIES:
         res = comms.get_comms().send_data_to_bg_process(
             "WRAPPED_PACKAGE",
             {