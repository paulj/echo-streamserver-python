require 'json'

class UserStore
  def get(identityURL)
    if identityURL == 'http://example.com/users/john'
      return JSON.parse File.read(File.expand_path('../responses/user-get.json', __FILE__))
    else
      raise UnknownUserException
    end
  end
  
  def whoami(sessionID)
    if sessionID == 'abc123'
      return JSON.parse File.read(File.expand_path('../responses/user-get.json', __FILE__))
    else
      raise UnknownSessionException
    end
  end
  
  def update(identityURL, subject, content)
    unless identityURL == 'http://example.com/users/john'
      raise UnknownUserException
    end
  end
end

class UnknownUserException < Exception; end
class UnknownSessionException < Exception; end