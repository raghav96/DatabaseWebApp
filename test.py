from app import app
import unittest

class FlaskTestCase(unittest.TestCase):

	# Ensure index page loads to login page
	def test_index(self):
		tester = app.test_client(self)
		response = tester.get('/login',content_type='html/text')
		self.assertEqual(response.status_code, 200)

	# Ensure login page loads properly
	def test_login_page(self):
		tester = app.test_client(self)
		response = tester.get('/login',content_type='html/text')
		self.assertTrue(b'Please Login' in response.data)

	# Ensure login works properly
	def test_correct_login(self):
		tester = app.test_client(self)
		response = tester.post(
			'/login',
			data=dict(username="admin", password="admin"),
			follow_redirects=True
			)
		self.assertTrue(b'You were just logged in' in response.data)

	# Ensure invalid credentials kick in
	def test_invalid_cred(self):
		tester = app.test_client(self)
		response = tester.post(
			'/login',
			data=dict(username="wrong", password="wrong"),
			follow_redirects=True
			)
		self.assertTrue(b'Invalid credentials. Try again' in response.data)

	# Ensure logout works
	def test_logout(self):
		tester = app.test_client(self)
		response = tester.post(
			'/login',
			data=dict(username="admin", password="admin"),
			follow_redirects=True
			)
		response = tester.get('/logout', follow_redirects= True)
		self.assertTrue(b'You were just logged out' in response.data)

	# Ensure main page requires login
	def test_login_required(self):
		tester = app.test_client(self)
		response = tester.get('/', follow_redirects= True)
		self.assertTrue(b'You need to login first' in response.data)

	# Ensure logout page requires a login page
	def test_logout_required(self):
		tester = app.test_client(self)
		response = tester.post(
			'/login',
			data=dict(username="wrong", password="wrong"),
			follow_redirects=True
			)
		response = tester.post(
			'/logout',
			data=dict(username="admin", password="admin"),
			follow_redirects=True
			)
		self.assertTrue(b'You need to login first' in response.data)



if __name__ == "__main__":
	unittest.main()