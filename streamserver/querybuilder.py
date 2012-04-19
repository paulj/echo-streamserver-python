import string

def query():
	return MainQueryBuilder()
	
def subquery():
	return SubQueryBuilder()
	
class QueryBuilderBase:
	def __init__(self):
		self.terms = []
		
	def add_term(self, term, value = None):
		if value == None:
			self.terms.append(term)
		else:
			self.terms.append(term + ":" + str(value))
		return self
	
	def add_terms(self, term, values):
		return self.add_term(term, ",".join(values))
	
	def __str__(self):
		return string.join(self.terms, " ")

class CommonQueryOperations:
	def state(self, *states):
		return self.add_terms("state", states)
	
	def type(self, *types):
		return self.add_terms("type", types)
	
	def source(self, *sources):
		return self.add_terms("source", sources)
	
	def provider(self, *providers):
		return self.add_terms("provider", providers)
	
	def tags(self, *tags):
		return self.add_terms("tags", tags)
	
	def markers(self, *markers):
		return self.add_terms("markers", markers)
	
	def user_id(self, userid):
		return self.add_term("user.id", userid)

	def user_markers(self, *markers):
		return self.add_terms("user.markers", markers)

	def user_roles(self, *roles):
		return self.add_terms("user.roles", roles)

	def user_state(self, *states):
		return self.add_terms("user.state", states)
	
class RootQueryBuilder(QueryBuilderBase, CommonQueryOperations):
	def __init__(self):
		QueryBuilderBase.__init__(self)
	
	def scope(self, s):
		return self.add_term("scope", s)

	def childrenof(self, s):
		return self.add_term("childrenof", s)

	def url(self, s):
		return self.add_term("url", s)
	
	def or_terms(self, *terms):
		return self.add_term(" OR ".join(map(lambda t: "(" + str(t) + ")", terms)))
	
class MainQueryBuilder(RootQueryBuilder):
	def __init__(self):
		RootQueryBuilder.__init__(self)
		
	def children(self, count=None):
		return self.add_term("children", count)
		
	def itemsPerPage(self, count):
		return self.add_term("itemsPerPage", count)

	def sortOrder(self, order):
		return self.add_term("sortOrder", order)

	def after(self, ts):
		return self.add_term("after", self.quote_term(ts))

	def before(self, ts):
		return self.add_term("before", self.quote_term(ts))

	def pageAfter(self, ts):
		return self.add_term("pageAfter", self.quote_term(ts))

	def safeHTML(self, mode):
		return self.add_term("safeHTML", mode)
		
	def quote_term(self, term):
		return '"' + term + '"'
		
class SubQueryBuilder(RootQueryBuilder):
	def __init__(self):
		RootQueryBuilder.__init__(self)
		
class ChildrenQueryBuilder(QueryBuilderBase, CommonQueryOperations):
	def __init__(self, prefix):
		QueryBuilderBase.__init__(self)
		
		self.prefix = prefix
		
	def childrenItemsPerPage(self, count):
		return self.add_term("childrenItemsPerPage", count)

	def childrenSortOrder(self, order):
		return self.add_term("childrenSortOrder", order)


		
	def __str__(self):
		return self.prefix + " " + QueryBuilderBase.__str__(self)
		