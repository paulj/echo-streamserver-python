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
	
	def __str__(self):
		return string.join(self.terms, " ")
	
class MainQueryBuilder(QueryBuilderBase):
	def __init__(self):
		QueryBuilderBase.__init__(self)
		
	def scope(self, s):
		self.add_term("scope", s)
		return self
		
	def childrenof(self, s):
		self.add_term("childrenof", s)
		return self
		
	def children(self, count=None):
		self.add_term("children", count)
		return ChildrenQueryBuilder(str(self))
		
	def or_terms(self, *terms):
		self.add_term(" OR ".join(map(lambda t: "(" + str(t) + ")", terms)))
		return self

class SubQueryBuilder(QueryBuilderBase):
	def __init__(self):
		QueryBuilderBase.__init__(self)
		
	def scope(self, s):
		self.add_term("scope", s)
		return self
		
class ChildrenQueryBuilder(QueryBuilderBase):
	def __init__(self, prefix):
		QueryBuilderBase.__init__(self)
		
		self.prefix = prefix
		
	def itemsPerPage(self, count):
		self.add_term("itemsPerPage", count)
		return self
		
	def __str__(self):
		return self.prefix + " " + QueryBuilderBase.__str__(self)
		
