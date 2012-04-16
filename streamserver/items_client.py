from echo_client import EchoClient

class ItemsClient(EchoClient):
	def submit(self, items, mode='update'):
		return self.execute_update('submit', {'content':str(content), 'mode':mode})
	
	def search(self, query, since=None):
		params = {'q':str(query)}
		if since != None:
			params.since = str(since)
		
		return self.execute_query('search', params)
		
	def count(self, query):
		res = self.execute_query('count', {'q':str(query)})
		return res['count']
		
	def mux(self):
		pass