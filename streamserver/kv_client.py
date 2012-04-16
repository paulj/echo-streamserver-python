from echo_client import EchoClient

class KVClient(EchoClient):
	def get(self, key):
		params = {'key':str(key)}
		res = self.execute_query('kvs/get', params)
		
		return res['value']
		
	def put(self, key, value, public=False):
		params = {'key':str(key), 'value':str(value)}
		if public:
			params.public = 'true'
			
		return self.execute_update('kvs/put', params)
		
	def delete(self, key):
		params = {'key':str(key)}
			
		return self.execute_update('kvs/delete', params)