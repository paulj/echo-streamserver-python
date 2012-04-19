import unittest

import streamserver.querybuilder as qb

class QueryBuilderTestSuite(unittest.TestCase):
	def test_scope_only(self):
		q = qb.query().scope('http://example.com/m')
		self.assertEqual(str(q), "scope:http://example.com/m")
		
	def test_url(self):
		q = qb.query().url('http://example.com/u')
		self.assertEqual(str(q), "url:http://example.com/u")
		
	def test_childrenof(self):
		q = qb.query().childrenof('http://example.com/u')
		self.assertEqual(str(q), "childrenof:http://example.com/u")
		
	def test_scope_and_children(self):
		q = qb.query().scope('http://example.com/m').children(2).itemsPerPage(5)
		self.assertEqual(str(q), "scope:http://example.com/m children:2 itemsPerPage:5")
	
	def test_scope_and_unnumbered_children(self):	
		q = qb.query().scope('http://example.com/m').children().itemsPerPage(5)
		self.assertEqual(str(q), "scope:http://example.com/m children itemsPerPage:5")
	
	def test_multiple_or_terms(self):
		q = qb.query().or_terms(qb.subquery().scope('http://example.com/m'), qb.subquery().scope('http://example.com/n'))
		self.assertEqual(str(q), "(scope:http://example.com/m) OR (scope:http://example.com/n)")
		
	def testSearchOperators(self):
		q = qb.query().scope('http://example.com').state('ModeratorApproved', 'Untouched').type('article', 'comment').source('App1', 'App2')
		self.assertEqual(str(q), "scope:http://example.com state:ModeratorApproved,Untouched type:article,comment source:App1,App2")
		
		q = qb.query().scope('http://example.com').tags('t1', 't2').markers('m1', 'm2')
		self.assertEqual(str(q), "scope:http://example.com tags:t1,t2 markers:m1,m2")
				
		q = qb.query().scope('http://example.com').user_id('http://twitter.com/123').user_markers('m1', 'm2').user_roles('r1', 'r2').user_state('s1', 's2')
		self.assertEqual(str(q), "scope:http://example.com user.id:http://twitter.com/123 user.markers:m1,m2 user.roles:r1,r2 user.state:s1,s2")
		
	def testPackagingOperators(self):
		q = qb.query().scope('http://example.com').sortOrder('repliesDescending').after('1 hour ago').before('3 hours ago').pageAfter('123.123')
		self.assertEqual(str(q), "scope:http://example.com sortOrder:repliesDescending after:\"1 hour ago\" before:\"3 hours ago\" pageAfter:\"123.123\"")		
		
	def testRepresentationOperators(self):
		q = qb.query().scope('http://example.com').safeHTML('aggressive')
		self.assertEqual(str(q), "scope:http://example.com safeHTML:aggressive")