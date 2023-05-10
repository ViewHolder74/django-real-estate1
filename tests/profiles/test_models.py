import pytest

def test_profile_str(self):
    """Test the profile model string representation"""
    assert self.__str__() ==f"{self.user.username}'s profile"