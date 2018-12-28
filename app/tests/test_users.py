import unittest
from app import create_app
from flask import jsonify, json
import pytest

class TestAuthEndpoint(unittest.TestCase):

	def setUp(self):
		self.app = create_app()
		self.app.testing = True
		self.client = self.app.test_client()
		
		self.test_1 = {
			"username": "Charles",
			"password": "Pas!",
			"email": "charles@demo.com"
		}
	def test_signup(self):
		""" test for successful registration """
		response = self.client.post('/api/v1/auth/signup', 
								data = json.dumps(self.test_1), 
								content_type="application/json")
		result = json.loads(response.data)
		self.assertEqual(result["message"], "password does not meet requirements")
		# self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
	unittest.main()
