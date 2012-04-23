from echo_client import EchoClient

class ItemsClient(EchoClient):
	"""Client responsible for querying the Echo Items API"""
	
	def submit(self, items, mode='update'):
		"""Submits an activitystream to Echo for processing"""
		return self.execute_update('submit', {'content':str(content), 'mode':mode})
	
	def search(self, query, since=None):
		"""Submits a search request to echo. The query parameter can be either a string or :class:`QueryBuilder <QueryBuilder>` instance."""
		params = {'q':str(query)}
		if since != None:
			params.since = str(since)
		
		return self.execute_query('search', params)
		
	def count(self, query):
		"""Submits a count request to echo. The query parameter can be either a string or :class:`QueryBuilder <QueryBuilder>` instance."""
		res = self.execute_query('count', {'q':str(query)})
		return res['count']
		
	def mux(self):
		pass