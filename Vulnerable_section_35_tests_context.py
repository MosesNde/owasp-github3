 
 # Python Repo Template
 # ..................................
# Copyright (c) 2017-2019, Kendrick Walls
 # ..................................
 # Licensed under MIT (the "License");
 # you may not use this file except in compliance with the License.
 # limitations under the License.
 
 
 try:
 	import sys
 	import os
 	if 'pythonrepo' in __file__:
 		sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
except Exception as ImportErr:
	print(str(type(ImportErr)))
	print(str(ImportErr))
	print(str((ImportErr.args)))
	ImportErr = None
	del ImportErr
	raise ImportError("Python Repo Failed to Import")
 
 
 try:
	import pythonrepo as pythonrepo
 	if pythonrepo.__name__ is None:
 		raise ImportError("Failed to import pythonrepo.")
except Exception as importErr:
	importErr = None
	del importErr
	raise ImportError("Test module failed to load pythonrepo for test.")
	exit(0)