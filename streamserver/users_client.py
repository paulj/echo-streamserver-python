from echo_client import EchoClient

class UsersClient(EchoClient):
	"""Interface to the Echo User information store."""
	def get(self, identityURL):
		"""Retrieves the details of a user by their identity url"""
		return self.execute_query('users/get', {'identityURL':identityURL})
	
	def update(self, identityURL, subject, content):
		"""Updates an attribute of a user by their identity url"""
		return self.execute_update('users/update', {'identityURL':identityURL, 'subject':subject, 'content':str(content)})
		
	def whoami(self, sessionID):
		"""Retrieves the details of the user logged in with the given sessionID"""
		return self.execute_query('users/whoami', {'sessionID':sessionID})