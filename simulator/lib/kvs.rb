class KVS
  def initialize
    @apps = {}
  end
  
  def get(appkey, key)
    val = (@apps[appkey] || {})[key]
    
    raise KeyNotFoundException unless val
    
    val
  end
  
  def put(appkey, key, value)
    @apps[appkey] ||= {}
    @apps[appkey][key] = value
  end
  
  def delete(appkey, key)
    (@apps[appkey] || {}).delete key
  end
end

class KeyNotFoundException < Exception
end