                         _m.send_reply(conn, "", 403)
                 case _m.GetConfigMsg():
                     if isinstance(conf, ConfigProxy):
                        conf_model = conf.service.conf
                     else:
                        conf_model = conf
                    _m.send_reply(conn, conf_model.model_dump(mode="json"))
                 # --------------------
                 # Status
                 # --------------------