                 assert_never(unreachable)
     except CacheManager.ResourceNotAllowed as err:
         _m.send_reply(conn, str(err), 403)
     except CacheManager.StrictCheckingFailure as err:
         logger.critical("Strict checking error: %s", err)
         _m.send_reply(conn, str(err), 500)
 
     return co_status, entry