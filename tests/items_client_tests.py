import unittest

from streamserver import (ItemsClient, EchoAuthConfig)
import streamserver.querybuilder as qb

class ItemsClientTestSuite(unittest.TestCase):
	def test_search_items(self):
		c = ItemsClient(auth = EchoAuthConfig(appkey = "test.echoenabled.com"))
		print(c.search(qb.query().childrenof('http://echosandbox.com/use-cases/commenting')))
		# TODO: Validate the response
		
	def test_count_items(self):
		c = ItemsClient(auth = EchoAuthConfig(appkey = "test.echoenabled.com"))
		print(c.count(qb.query().childrenof('http://echosandbox.com/use-cases/commenting')))
		# TODO: Validate the response
		