from echo_client import EchoClient
from xml.dom.minidom import parseString

class FeedsClient(EchoClient):
	"""Client for managing the feeds polled by Echo"""
	def list(self):
		"""Lists the feeds registered for this account."""
		opml_str = self.execute_query('feeds/list', {})
		opml = parseString(opml_str)
		
		def process_outline_element(el):
			return (el.getAttribute('text'), el.getAttribute('refreshRate'))
		
		feeds = map(process_outline_element, self._find_xml_elements(opml, ["opml", "body", "outline"]))
		return feeds
	
	def register(self, url, interval):
		"""Registers the given url for polling with the specified interval (in seconds)"""
		return self.execute_query('feeds/register', {'url':url, 'interval':interval})
	
	def unregister(self, url):
		"""Unregisters the given url from polling"""
		return self.execute_query('feeds/unregister', {'url':url})
		
	def _find_xml_elements(self, el, tags):
		for child in el.childNodes:
			if child.localName==tags[0]:
				if len(tags) == 1:
					yield child
				else:
					for child_child in self._find_xml_elements(child, tags[1:]):
						yield child_child