import unittest

from streamserver import *
import configuration_factory as cf

class ItemsClientTestSuite(unittest.TestCase):
	def setUp(self):
		self.noauth_client = KVClient(auth = cf.no_auth, host = cf.test_host)
		self.basic_client = KVClient(auth = cf.basic_auth, host = cf.test_host)
		self.oauth_client = KVClient(auth = cf.oauth_auth, host = cf.test_host)
		self.invalid_basic_client = KVClient(auth = cf.invalid_basic_auth, host = cf.test_host)
		self.invalid_oauth_client = KVClient(auth = cf.invalid_oauth_auth, host = cf.test_host)
		self.invalid_oauth_key_client = KVClient(auth = cf.invalid_oauth_key_auth, host = cf.test_host)
	
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

	def test_put_invalid_oauth_key(self):
		with self.assertRaises(InvalidKeyException):
			self.invalid_oauth_key_client.put('abc', '123')

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