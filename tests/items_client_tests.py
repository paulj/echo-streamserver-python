import unittest

from streamserver import *
import streamserver.querybuilder as qb
import configuration_factory as cf

class ItemsClientTestSuite(unittest.TestCase):
	def setUp(self):
		self.noauth_client = ItemsClient(auth = cf.no_auth, host = cf.test_host)
	
	def test_search(self):
		res = self.noauth_client.search(qb.query().childrenof('http://echosandbox.com/use-cases/commenting').itemsPerPage(2))
		self.assertEquals(2, len(res['entries']))
		
	def test_search_invalid_query(self):
		with self.assertRaises(InvalidQueryException) as cm:
			self.noauth_client.search('bad')
		self.assertEquals("Undefined predicate: bad", cm.exception.message)
		
	def test_search_waiting(self):
		with self.assertRaises(EchoWaitingException):
			self.noauth_client.search(qb.query().scope('http://example.com/waiting'))
		
	def test_search_timeout(self):
		with self.assertRaises(EchoTimeoutException):
			self.noauth_client.search(qb.query().scope('http://example.com/timeout'))
		
	def test_count(self):
		commenting_count = self.noauth_client.count(qb.query().childrenof('http://echosandbox.com/use-cases/commenting'))
		self.assertEquals(5, commenting_count)

		trending_count = self.noauth_client.count(qb.query().childrenof('http://echosandbox.com/use-cases/trending'))
		self.assertEquals(12, trending_count)
		