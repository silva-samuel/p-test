
def hhmmss2sec( hours, minutes, seconds ):
	"""Given a hour value in th eformat hh:mm:ss convert it to the amount of seconds"""
	
	result = ( hours * 3600) + ( minutes * 60) + seconds
	
	return result
	