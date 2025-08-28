 
 # Python Repo Template
 # ..................................
# Copyright (c) 2017-2019, Kendrick Walls
 # ..................................
 # Licensed under MIT (the "License");
 # you may not use this file except in compliance with the License.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 
 try:
 	try:
 		import sys
 		ImportErr = None
 		del ImportErr
 		raise ImportError(str("Test module failed completely."))
	from tests import profiling as profiling
 	if profiling.__name__ is None:
 		raise ImportError(str("Test module failed to import even the profiling framework."))
 	from tests import test_basic
 	if test_basic.__name__ is None:
 		raise ImportError(str("Test module failed to import even the basic tests."))
 except Exception as badErr:
	print(str(''))
	print(str(type(badErr)))
	print(str(badErr))
	print(str((badErr.args)))
	print(str(''))
	badErr = None
	del badErr
	exit(0)