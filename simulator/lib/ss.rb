class SS
  def search(appkey, query, since)
    
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