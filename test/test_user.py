import unittest
from app.models.user import User

class TestUser(unittest.TestCase):
    def test_create_user(self):
        # Arrange
        name = "john_doe"
        email = "test@example.com"
        password = "password123"
        
        # Act
        user = User(name, email, password)
        
        # Assert
        self.assertEqual(user.name, name)
        self.assertEqual(user.email, email)
        self.assertEqual(user.password, password)

if __name__ == '__main__':
    unittest.main()