from echo_client import EchoClient

class UsersClient(EchoClient):
	def get(self, identityURL):
		return self.execute_query('users/get', {'identityURL':identityURL})
	
	def update(self, identityURL, subject, content):
		return self.execute_update('users/update', {'identityURL':identityURL, 'subject':subject, 'content':str(content)})
		
	def whoami(self, sessionID):
		return self.execute_query('users/whoami', {'sessionID':sessionID})