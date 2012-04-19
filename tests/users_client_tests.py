import unittest

from streamserver import *
import configuration_factory as cf

class UsersClientTestSuite(unittest.TestCase):
	def setUp(self):
		self.noauth_client = UsersClient(auth = cf.no_auth, host = cf.test_host)
		self.basic_client = UsersClient(auth = cf.basic_auth, host = cf.test_host)
		self.oauth_client = UsersClient(auth = cf.oauth_auth, host = cf.test_host)
	
	def test_get_basic(self):
		user = self.basic_client.get('http://example.com/users/john')
		self.verify_user(user)

	def test_get_oauth(self):
		user = self.oauth_client.get('http://example.com/users/john')
		self.verify_user(user)
		
	def test_get_missing(self):
		with self.assertRaises(NotFoundException):
			self.oauth_client.get('http://example.com/users/john2')
			
	def test_whoami(self):
		user = self.noauth_client.whoami('abc123')
		self.verify_user(user)

	def test_whoami_bad_session(self):
		with self.assertRaises(InvalidSessionException):
			self.noauth_client.whoami('missing-session')

	def test_update(self):
		self.oauth_client.update('http://example.com/users/john', 'state', 'ModeratorApproved')
		
	def test_update_missing(self):
		with self.assertRaises(NotFoundException):
			self.oauth_client.update('http://example.com/users/john2', 'state', 'ModeratorApproved')

	def verify_user(self, user):
		self.assertEquals("ModeratorBanned", user['echo']['state'])
		self.assertEquals(["administrator", "moderator"], user['echo']['roles'])
		self.assertEquals(0, user['poco']['startIndex'])