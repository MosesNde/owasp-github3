 
 # Start camera
 picam = Picamera2()
picam.configure(picam.preview_configuration(main={"format": "RGB888", "size": (640, 480)}))
 picam.start()
 
 while True: