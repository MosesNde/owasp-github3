     DOMAIN,
     CONF_LOCATION_ID,
     CONF_LOCATION,
     DEFAULT_NAME,
     RADIATION_STATIONS,
     UV_LOCATIONS,
 CONFIG_SCHEMA = vol.Schema({
     DOMAIN: vol.Schema({
         vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
        vol.Required(CONF_LOCATION_ID): cv.string,
        vol.Required(CONF_LOCATION): cv.string,
     }),
 }, extra=vol.ALLOW_EXTRA)
 