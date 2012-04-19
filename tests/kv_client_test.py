import unittest

from streamserver import *

class ItemsClientTestSuite(unittest.TestCase):
	def setUp(self):
		self.test_host = "http://localhost:4567/v1"
		
		self.no_auth = EchoAuthConfig(appkey = "test.echoenabled.com")
		self.basic_auth = EchoAuthConfig(appkey = "test.echoenabled.com", secret = "secret123")
		self.oauth_auth = EchoAuthConfig(appkey = "test.echoenabled.com", secret = "secret123", method = EchoAuthMethod.OAUTH)
		self.invalid_basic_auth = EchoAuthConfig(appkey = "test.echoenabled.com", secret = "secret1234")
		self.invalid_oauth_auth = EchoAuthConfig(appkey = "test.echoenabled.com", secret = "secret1234", method = EchoAuthMethod.OAUTH)
		
		self.noauth_client = KVClient(auth = self.no_auth, host = self.test_host)
		self.basic_client = KVClient(auth = self.basic_auth, host = self.test_host)
		self.oauth_client = KVClient(auth = self.oauth_auth, host = self.test_host)
		self.invalid_basic_client = KVClient(auth = self.invalid_basic_auth, host = self.test_host)
		self.invalid_oauth_client = KVClient(auth = self.invalid_oauth_auth, host = self.test_host)
	
	def test_put_get_basic(self):
		self.basic_client.put('abc', '123')
		self.assertEquals('123', self.noauth_client.get('abc'))

	def test_put_get_oauth(self):
		self.oauth_client.put('abc', '123')
		self.assertEquals('123', self.noauth_client.get('abc'))

	def test_put_noauth(self):
		with self.assertRaises(AuthorisationRequiredException):
			self.noauth_client.put('abc', '123')
			
	def test_put_invalid_oauth(self):
		with self.assertRaises(InvalidSecretException):
			self.invalid_oauth_client.put('abc', '123')

	def test_put_invalid_basic(self):
		with self.assertRaises(InvalidSecretException):
			self.invalid_basic_client.put('abc', '123')

	def test_get_missing(self):
		with self.assertRaises(NotFoundException):
			self.noauth_client.get('missing')
			
	def test_delete_get(self):
		self.basic_client.put('abc', '123')
		self.basic_client.delete('abc')
		with self.assertRaises(NotFoundException):
			self.noauth_client.get('abc')