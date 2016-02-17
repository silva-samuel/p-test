
def hhmmss2sec( hours, minutes, seconds ):
	"""Given a hour value in th eformat hh:mm:ss convert it to the amount of seconds"""
	if checkHourRange( hours ) == False:
		return -1
	elif checkMinutesSecondsRange( minutes ) == False:
		return -1
	elif checkMinutesSecondsRange( seconds ) == False:
		return -1
	else:
		result = ( hours * 3600) + ( minutes * 60) + seconds
	
		return result
	
def checkHourRange( hours ):
	"""Check if hours value is between 00 and 23"""
	
	if hours >= 0 and hours <=23:
		return True
		
	return False
	
def checkMinutesSecondsRange( value ):
	"""Check if minutes/seconds value is between 00 and 59"""
	
	if value >= 0 and value <=59:
		return True
		
	return False
