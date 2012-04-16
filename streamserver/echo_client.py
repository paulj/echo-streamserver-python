import requests
import json
from oauth_hook import OAuthHook

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
		
		if self.auth.method == EchoAuthMethod.OAUTH:
			self.oauth_hook = OAuthHook(consumer_key = self.auth.appkey, consumer_secret = self.auth.secret, header_auth = False)
			
			# Due to a bug in requests/oauth-requests, running the oauth hook in its proper form as a hook doesn't work when we need
			# parameters (and not an Authorization header). So we're creating the hook, then manually running it and copying the output
			# in the execution methods. Not ideal, and hopefully something that can be removed when oauth-requests gets fixed.
			self.client = requests
		elif self.auth.secret != None:
			self.client = requests.session(auth=(self.auth.appkey, self.auth.secret))
		else:
			self.client = requests
		
	def execute_query(self, method, params):
		full_params = self.prepare_params(params)
		
		# If we've got an oauth hook, run it against a mock request and use the parameters it generated
		if self.oauth_hook:
			req = MockRequest('GET', self.host + "/" + method, {}, full_params)
			self.oauth_hook(req)
			full_params = req.data_and_params
		
		res = self.client.get(self.host + "/" + method, params=full_params)
		return self.process_response(res)

	def execute_update(self, method, params):
		full_params = self.prepare_params(params)
		
		# If we've got an oauth hook, run it against a mock request and use the data it generated
		if self.oauth_hook:
			req = MockRequest('POST', self.host + "/" + method, {}, full_params)
			self.oauth_hook(req)
			full_params = req._enc_data
		
		res = self.client.post(self.host + "/" + method, data=full_params)
		return self.process_response(res)

	def prepare_params(self, params):
		full_params = params.copy()
		full_params.update({'appkey' : self.auth.appkey})
		
		return full_params

	def process_response(self, res):
		self.assert_status(res)
		return self.decode_response(res)

	def assert_status(self, response):
		if response.status_code == 200:
			return True
		else:
			# Attempt to decode as a JSON response
			res = self.decode_response(response)
			if res['errorCode'] == "incorrect_appkey":
				raise InvalidOrMissingAppKeyException()
			else:
				# TODO: More decoding!
				raise EchoException(res['errorCode'])
			
	def decode_response(self, res):
		if res.headers['content-type'] == 'text/xml':
			return res.content
		else:
			return json.loads(res.content)
			
class EchoException(RuntimeError):
	"""An exception occurred executing an Echo request"""
	
class InvalidRequestException(EchoException):
	"""A request submitted to Echo was invalid"""

class InvalidOrMissingAppKeyException(InvalidRequestException):
	"""The appkey provided to echo was blank or invalid"""
	
class MockRequest:
	"""A mock version of the requests.Request object that is used to drive the OAuth hook"""
	def __init__(self, method, url, params, data):
		self.method = method
		self.url = url
		self.params = params
		self.data = data
		self._enc_params = ""