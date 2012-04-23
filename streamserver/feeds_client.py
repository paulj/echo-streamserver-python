from echo_client import EchoClient

class FeedsClient(EchoClient):
	"""Client for managing the feeds polled by Echo"""
	def list(self):
		"""Lists the feeds registered for this account."""
		return self.execute_query('feeds/list', {})
	
	def register(self, url, interval):
		"""Registers the given url for polling with the specified interval (in seconds)"""
		pass
	
	def unregister(self, url):
		"""Unregisters the given url from polling"""
		pass