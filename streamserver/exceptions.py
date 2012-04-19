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
	
class InvalidSessionException(InvalidRequestException):
	"""The provided backplane session ID was not valdi"""
	
class NotFoundException(EchoException):
	"""A requested object was not found, such as a key within the KVS"""