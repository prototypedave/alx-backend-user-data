#!/usr/bin/env python3
"""
user model
"""
from models.base import Base
from typing import List


class UserSession(Base):
    """ class that inherits from base
    """
    def __init__(self, *args: list, **kwargs: dict):
        """ initializes class UserSession
        """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
