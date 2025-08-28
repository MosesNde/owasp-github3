     return NULL;
   }
   if (params->debug) {
    log_message(LOG_INFO, pamh, "debug: start of google_authenticator for %s", username);
   }
   return username;
 }
         !pw->pw_dir ||
         *pw->pw_dir != '/') {
     err:
      log_message(LOG_ERR, pamh, "Failed to compute location of secret file");
       free(buf);
       free(secret_filename);
       return NULL;
       // but we remember that this was the result of a missing state file.
       params->nullok = SECRETNOTFOUND;
     } else {
      log_message(LOG_ERR, pamh, "Failed to read \"%s\"", secret_filename);
     }
  error:
     if (fd >= 0) {
       username = buf;
     }
     log_message(LOG_ERR, pamh,
                "Secret file \"%s\" must be owned by %s",
                 secret_filename, username);
     goto error;
   }
   // If necessary, notify the user of the rate limiting that is in effect.
   if (exceeded) {
     log_message(LOG_ERR, pamh,
                "Too many concurrent login attempts. Please try again.");
     return -1;
   }
 
         return -1;
       }
       log_message(LOG_ERR, pamh,
                  "Trying to reuse a previously used time-based code. "
                   "Retry again in %d seconds. "
                   "Warning! This might mean, you are currently subject to a "
                  "man-in-the-middle attack.", step);
       return -1;
     }
 
     if (rc == PAM_SUCCESS) {
       log_message(LOG_INFO , pamh, "Accepted google_authenticator for %s", username);
     } else {
      log_message(LOG_ERR, pamh, "Invalid verification code");
     }
   }
 