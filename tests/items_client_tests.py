import unittest

from streamserver import (ItemsClient, EchoAuthConfig)
import streamserver.querybuilder as qb
import configuration_factory as cf

class ItemsClientTestSuite(unittest.TestCase):
	def setUp(self):
		self.noauth_client = ItemsClient(auth = cf.no_auth, host = cf.test_host)
	
	def test_search_items(self):
		self.noauth_client.search(qb.query().childrenof('http://echosandbox.com/use-cases/commenting'))
		# TODO: Validate the response
		
	def test_count_items(self):
		commenting_count = self.noauth_client.count(qb.query().childrenof('http://echosandbox.com/use-cases/commenting'))
		self.assertEquals(5, commenting_count)

		trending_count = self.noauth_client.count(qb.query().childrenof('http://echosandbox.com/use-cases/trending'))
		self.assertEquals(12, trending_count)
		