 def readFile(filename):
 	"""Helper Function to read files"""
 	theResult = None
	try:
		with open(str("""./{}""").format(str(filename))) as f:
			theResult = f.read()
	except Exception:
		theResult = str(
			"""See https://github.com/reactive-firewall/python-repo/{}"""
		).format(filename)
 	return theResult
 
 