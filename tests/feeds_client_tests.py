import unittest

from streamserver import *
import configuration_factory as cf

class FeedsClientTestSuite(unittest.TestCase):
	def setUp(self):
		self.noauth_client = FeedsClient(auth = cf.no_auth, host = cf.test_host)
		self.basic_client = FeedsClient(auth = cf.basic_auth, host = cf.test_host)
		self.oauth_client = FeedsClient(auth = cf.oauth_auth, host = cf.test_host)

	def test_list_basic(self):
		feeds = self.basic_client.list()
		self.assertEquals([(u'http://example.com/feed/1', u'300'), (u'http://example.com/feed/2', u'50')], feeds)

	def test_register_basic(self):
		self.basic_client.register('http://www.example.com/feed.xml', 5)

	def test_register_oauth(self):
		self.oauth_client.register('http://www.example.com/feed.xml', 15)
		
	def test_unregister_basic(self):
		self.basic_client.unregister('http://www.example.com/feed.xml')

	def test_unregister_bad_url(self):
		with self.assertRaises(IncorrectURLException):
			self.basic_client.unregister('foo')

	def test_unregister_oauth(self):
		self.oauth_client.unregister('http://www.example.com/feed.xml')