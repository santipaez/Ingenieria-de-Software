import pytest
from app.repositories.user_repository import UserRepository

class TestDatabase:
    @pytest.fixture
    def setup(self):
        self.user_repository = UserRepository()

    def test_create_user(self, setup):
        user = self.user_repository.create('test', 'test@example.com')
        assert user.id is not None
        assert user.name == 'test'
        assert user.email == 'test@example.com'

    def test_get_user(self, setup):
        user = self.user_repository.get_user('test')
        assert user is not None
        assert user.name == 'test'
        assert user.email == 'test@example.com'