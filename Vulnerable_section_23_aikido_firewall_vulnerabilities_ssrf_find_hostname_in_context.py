     if not isinstance(hostname, str) or not isinstance(port, int):
         # Validate hostname and port input
         return None
     for source in UINPUT_SOURCES:
         if not hasattr(context, source):
             continue