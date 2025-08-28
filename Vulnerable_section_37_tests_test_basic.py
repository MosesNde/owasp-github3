 	def test_absolute_truth_and_meaning(self):
 		"""Insanitty Test. Because it only matters if we're not mad as hatters."""
 		assert True
 
 	def test_meta_test(self):
 		"""Insanity Test for unittests assertion."""
		self.assertTrue(True)
		self.assertFalse(False)
 		self.assertIsNone(None)
 
 	def test_syntax(self):
 			print(str(type(impErr)))
 			print(str(impErr))
 			theResult = False
		assert theResult
 
 	def test_the_help_command(self):
 		"""Test case for backend library."""
 			theResult = True
 		except Exception:
 			theResult = False
		assert theResult
 
 	def test_corner_case_example(self):
 		"""Example Test case for bad input directly into function."""
		theResult = False
 		try:
 			from .context import pythonrepo
 			if pythonrepo.__name__ is None:
 				theResult = False
			from pythonrepo import pythonrepo as pythonrepo
			self.assertIsNone(pythonrepo.useTool(None))
			self.assertIsNone(pythonrepo.useTool("JunkInput"))
			theResult = True
 		except Exception:
 			theResult = False
		assert theResult
 
 	def test_new_tests(self):
 		"""Try adding new tests."""