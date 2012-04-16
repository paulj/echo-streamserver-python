from echo_client import EchoClient

class FeedsClient(EchoClient):
	def list(self):
		return self.execute_query('feeds/list', {})
	
	def register(self):
		pass
	
	def unregister(self):
		pass