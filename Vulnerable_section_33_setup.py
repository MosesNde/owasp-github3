 	raise ImportError("""Not Implemented.""")
 
 
def readFile(filename="""./README.md"""):
 	theResult = None
	try:
		with open(str("""./{}""").format(str(filename))) as f:
			theResult = f.read()
	except Exception:
		theResult = str(
			"""See https://github.com/reactive-firewall/python-repo/{}"""
		).format(filename)
 	return theResult
 
 
 
 setup(
 	name="""pythonrepo""",
	version="""1.1.2""",
 	description="""Python Repo""",
 	long_description=readme,
 	install_requires=requirements,