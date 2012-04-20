class EchoException(RuntimeError):
	"""An exception occurred executing an Echo request"""
	
class InvalidRequestException(EchoException):
	"""A request submitted to Echo was invalid"""

class InvalidOrMissingAppKeyException(InvalidRequestException):
	"""The appkey provided to echo was blank or invalid"""
	
class AuthorisationRequiredException(EchoException):
	"""Valid Authorisation (OAuth or Basic) is required to perform this operation"""

class InvalidSecretException(EchoException):
	"""The provided Echo secret is invalid, and led to either a password rejection or invalid signature being generated"""
	
class InvalidKeyException(EchoException):
	"""The provided Echo appkey is invalid"""
	
class InvalidSessionException(InvalidRequestException):
	"""The provided backplane session ID was not valdi"""
	
class NotFoundException(EchoException):
	"""A requested object was not found, such as a key within the KVS"""
	
class EchoWaitingException(EchoException):
	"""Echo was not able to return a response within 15 seconds of request starting time. Request should be re-run at 1 minute intervals."""

class EchoTimeoutException(EchoException):
	"""Echo failed to process the query within a reasonable amount of time"""
	
class InvalidQueryException(EchoException):
	"""The provided echo query was not valid"""
