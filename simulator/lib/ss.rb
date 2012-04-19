class SS
  def search(appkey, query, since)
    if query == 'childrenof:http://echosandbox.com/use-cases/commenting itemsPerPage:2'
      return JSON.parse File.read(File.expand_path('../responses/search-commenting.json', __FILE__))
    elsif query == 'bad'
      raise InvalidQueryException.new('Undefined predicate: bad')
    elsif query == 'scope:http://example.com/waiting'
      raise WaitingException
    elsif query == 'scope:http://example.com/timeout'
      raise EchoTimeoutException
    end
  end
  
  def count(appkey, query)
    return 5 if query == 'childrenof:http://echosandbox.com/use-cases/commenting'
    return 12 if query == 'childrenof:http://echosandbox.com/use-cases/trending'
    
    0
  end
  
  def submit(appkey, content)
  end
  
  def mux(appkey)
  end
end

class InvalidQueryException < Exception; end
class WaitingException < Exception; end
class EchoTimeoutException < Exception; end