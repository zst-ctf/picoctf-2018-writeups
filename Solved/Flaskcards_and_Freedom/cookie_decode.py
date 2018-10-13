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

	secret = "c76db0dbbe5a58ad1a322d3b49923a96"
	cookie = ".eJwlj0mKA0EMBP9SZx-01SJ_pimpJMYYZqDbPhn_3W3mGhBB5qtsucfxU66P_RmXst1WuZYA7IIJhs6uOSaEV0hs3tYkn-iYS5oMEuPprXuAsw6pijM5qvVcNIewY5udVHutzhJs9XRImVsahCUpUT3ruNK7DABEMi-X4see2-PvHr_nnmyqaM4z10ojY1lcG8EUoEqpDIEn-XrPI_b_E9jK-wP8lD8c.DptLWQ.MW5jOpHaZnd1EnUJJu_rPN7PcsQ"
	session = decodeFlaskCookie(secret, cookie)
	print 'Decoded cookie:', session

	session['user_id'] = u'1'
	cookie = encodeFlaskCookie(secret, session)
	print 'New cookie:', cookie



