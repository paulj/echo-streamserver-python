import requests
import json

class EchoAuthMethod:
	BASIC='basic'
	OAUTH='oauth'
	
class EchoAuthConfig:
	def __init__(self, appkey = None, secret = None, method = EchoAuthMethod.BASIC):
		self.appkey = appkey
		self.secret = secret
		self.method = method
	
class EchoClient:
	def __init__(self, auth = EchoAuthConfig(), host = "https://api.echoenabled.com/v1"):
		self.auth = auth
		self.host = host
		
	def execute_query(self, method, params):
		full_params = params.copy()
		full_params.update({'appkey' : self.auth.appkey})
		
		res = requests.get(self.host + "/" + method, params=full_params)
		self.assert_status(res)
		
		return json.loads(res.content)

	def assert_status(self, response):
		if response.status_code == 200:
			return True
		else:
			# Attempt to decode as a JSON response
			res = json.loads(response.content)
			if res.errorCode == "incorrect_appkey":
				raise InvalidOrMissingAppKeyException()
			else:
				# TODO: More decoding!
				raise EchoException()
			
			
class EchoException(RuntimeError):
	"""An exception occurred executing an Echo request"""
	
class InvalidRequestException(EchoException):
	"""A request submitted to Echo was invalid"""

class InvalidOrMissingAppKeyException(InvalidRequestException):
	"""The appkey provided to echo was blank or invalid"""
	
	