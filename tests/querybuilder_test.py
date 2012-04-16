import unittest

import streamserver.querybuilder as qb

class QueryBuilderTestSuite(unittest.TestCase):
	def test_scope_only(self):
		q = qb.query().scope('http://example.com/m')
		self.assertEqual(str(q), "scope:http://example.com/m")
		
	def test_scope_and_children(self):
		q = qb.query().scope('http://example.com/m').children(2).itemsPerPage(5)
		self.assertEqual(str(q), "scope:http://example.com/m children:2 itemsPerPage:5")
	
	def test_scope_and_unnumbered_children(self):	
		q = qb.query().scope('http://example.com/m').children().itemsPerPage(5)
		self.assertEqual(str(q), "scope:http://example.com/m children itemsPerPage:5")
	
	def test_multiple_or_terms(self):
		q = qb.query().or_terms(qb.subquery().scope('http://example.com/m'), qb.subquery().scope('http://example.com/n'))
		self.assertEqual(str(q), "(scope:http://example.com/m) OR (scope:http://example.com/n)")