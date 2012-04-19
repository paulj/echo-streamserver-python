require 'bundler'
Bundler.setup
require 'sinatra'
require './lib/kvs'
require 'oauth'
require 'oauth/request_proxy/rack_request'
require 'json'

CURRENT_KVS=KVS.new

set :show_exceptions, false
# set :dump_errors, false

before do
  generate_error(401, "incorrect_appkey", "Incorrect or missing mandatory parameter appkey") unless params[:appkey]

  basic_auth = Rack::Auth::Basic::Request.new(request.env)
  if basic_auth.provided? && basic_auth.basic?
    unless basic_auth.credentials == ['test.echoenabled.com', 'secret123']
      generate_error(401, 'basic_auth_invalid_password')
    end
    
    @authenticated = basic_auth.credentials.first
  end
  
  if params[:oauth_consumer_key]
    generate_error(401, 'oauth_consumer_key_not_found') unless params[:oauth_consumer_key] == 'test.echoenabled.com'
    generate_error(401, 'oauth_mandatory_parameter_absent') unless (params[:oauth_nonce] && params[:oauth_timestamp])
    generate_error(401, 'oauth_mandatory_parameter_absent') unless (params[:oauth_version] && params[:oauth_signature_method])
    generate_error(401, 'oauth_mandatory_parameter_absent') unless (params[:oauth_signature])
    
    consumer = OAuth::Consumer.new('test.echoenabled.com', 'secret123')
    
    generate_error(401, 'oauth_signature_mismatch') unless OAuth::Signature.verify(request, :consumer => consumer)
    
    @authenticated = params[:oauth_consumer_key]
  end
end

get '/v1/search' do 
end

get '/v1/count' do
end

get '/v1/submit' do
end

get '/v1/mux' do
end

get '/v1/kvs/get' do
  require_parameter :key
  
  v = CURRENT_KVS.get(params[:appkey], params[:key])
  
  json_header
  {:value => v}.to_json
end

post '/v1/kvs/put' do
  require_parameter :key, :value
  require_auth
  
  CURRENT_KVS.put(params[:appkey], params[:key], params[:value])
  
  success_result
end

post '/v1/kvs/delete' do
  require_parameter :key
  require_auth
  
  CURRENT_KVS.delete(params[:appkey], params[:key])
  
  success_result
end

error KeyNotFoundException do
  generate_error(404, 'not_found')
end

def json_header
  headers 'Content-Type' => 'application/x-javascript; charset="utf-8"'
end

def success_result
  json_header
  {:result => 'success'}.to_json
end

def generate_error(status_code, echo_code, msg = nil)
  res = {:result => 'error', :errorCode => echo_code}
  res[:errorMessage] = msg if msg
  
  json_header
  halt status_code, res.to_json
end

def require_parameter(*required)
  required.each do |r|
    generate_error(400, "parameter_missing", "Mandatory parameter \"#{r.to_s}\" is missing") unless params[r]
  end
end

def require_auth
  generate_error(401, 'oauth_consumer_key_absent') unless @authenticated
end