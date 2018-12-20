import json
import unittest
from app import create_app

class TestAuthEndpoint(unittest.TestCase):

	def setUp(self):
		app.testing = True
		self.app = create_app.test_client()
		self.test_data = {
			"username": "Charles",
			"password": "password"
		}
	def test_signup(self):
		""" test for successful registration """
		response = self.app.post('/api/v1/auth/signup', 
								data = json.dumps(self.test_data), 
								content_type="application/json")
		result = json.loads(response.data)

		self.assertEqual(result["username"], "Charles")
		self.assertEqual(result["password"], "password")
		self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
	unittest.main()
