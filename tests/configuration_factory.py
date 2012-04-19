from streamserver import (EchoAuthConfig, EchoAuthMethod)

test_host = "http://localhost:4567/v1"

no_auth = EchoAuthConfig(appkey = "test.echoenabled.com")
basic_auth = EchoAuthConfig(appkey = "test.echoenabled.com", secret = "secret123")
oauth_auth = EchoAuthConfig(appkey = "test.echoenabled.com", secret = "secret123", method = EchoAuthMethod.OAUTH)
invalid_basic_auth = EchoAuthConfig(appkey = "test.echoenabled.com", secret = "secret1234")
invalid_oauth_auth = EchoAuthConfig(appkey = "test.echoenabled.com", secret = "secret1234", method = EchoAuthMethod.OAUTH)