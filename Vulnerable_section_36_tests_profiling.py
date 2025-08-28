 #! /usr/bin/env python
 # -*- coding: utf-8 -*-
 
# Python Repo Template
 # ..................................
# Copyright (c) 2017-2019, Kendrick Walls
 # ..................................
 # Licensed under MIT (the "License");
 # you may not use this file except in compliance with the License.
 # limitations under the License.
 
 
# Third-party Acknowlegement:
 # ..........................................
 # Some code (namely: class timewith, @do_cprofile, @do_line_profile) was modified/derived from:
 # https://github.com/zapier/profiling-python-like-a-boss/tree/1ab93a1154
 # NO ASSOCIATION
 
 
 try:
	import os
 	import sys
 	import time
	import cProfile
	for keyModule in [os, sys, time, cProfile]:
		if keyModule.__name__ is None:
			raise NotImplementedError(
				str("OMG! We could not import the {}!").format(
					str(keyModule)
				)
			)
except Exception as err:
	raise ImportError(err)
 
 
 try:
 	try:
 		sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), str('..'))))
 		sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), str('.'))))
	except Exception as ImportErr:
		print(str(''))
		print(str(type(ImportErr)))
		print(str(ImportErr))
		print(str((ImportErr.args)))
		print(str(''))
		ImportErr = None
		del ImportErr
		raise ImportError(str("Profile module failed completely."))
except Exception:
	raise ImportError("Failed to import test profiling")
 
 
 class timewith():
 	"""Basic timer for do_time_profile."""
 	def __init__(self, name=''):
 		self.name = name
 		self.start = time.time()
 	def __enter__(self):
 		return self
 
	def __exit__(self, type, value, traceback):
 		self.checkpoint(str("finished"))
 
 
 def do_time_profile(func, timer_name="time_profile"):
	"""Runs a function with a timer"""
	import functools
 
 	@functools.wraps(func)
 	def timer_profile_func(*args, **kwargs):
		"""Wraps a function in timewith()"""
 		theOutput = None
 		with timewith(timer_name) as timer:
 			timer.checkpoint(str("Start Timer"))
 
 
 def do_cprofile(func):
	"""use built-in profiler to profile."""
 	def profiled_func(*args, **kwargs):
 		profile = cProfile.Profile()
 		try:
 			profile.enable()
 try:  # noqa
 	from line_profiler import LineProfiler
 
	def do_profile(follow=None):
 		if follow is None:
 			follow = []
 
 			return profiled_func
 		return inner
 
except ImportError:
 	def do_profile(follow=None):
		"Helpful if you accidentally leave in production!"
 		if follow is None:
 			follow = []
 
 		return inner
 
 
def main(argv=None):
	"""The Main Event makes no sense to remediation."""
 	raise NotImplementedError("CRITICAL - test profiling main() not implemented. yet?")
 
 
if __name__ in '__main__':
 	exitcode = 3
 	try:
 		exitcode = main(sys.argv[1:])
 	finally:
		exit(exitcode)

 