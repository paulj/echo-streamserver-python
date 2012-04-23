from echo_client import EchoClient

class KVClient(EchoClient):
	"""Interface to the Echo Key/Value store."""
	def get(self, key):
		"""Retrieve a value by key from the KV store."""
		params = {'key':str(key)}
		res = self.execute_query('kvs/get', params)
		
		return res['value']
		
	def put(self, key, value, public=False):
		"""Adds a key/value pair to the KV store, optionally make it public."""
		params = {'key':str(key), 'value':str(value)}
		if public:
			params.public = 'true'
			
		return self.execute_update('kvs/put', params)
		
	def delete(self, key):
		"""Removes a value from the KV store by key."""
		params = {'key':str(key)}
			
		return self.execute_update('kvs/delete', params)