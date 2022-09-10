#!/usr/bin/env python3
"""
Expiration
"""

from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """ session expiration"""

    def __init__(self):
        """overload method
        """
        try:
            self.session_duration = int(getenv('SESSION_DURATION'))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """overloads auth create session method
        """
        try:
            session_id = super().create_session(user_id)
        except Exception:
            return None
        session_dictionary = {
                              'user_id': user_id,
                              'created_at': datetime.now()
                              }
        self.user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ overloads method user_id_by-session id on auth class
        """
        if session_id is None:
            return None
        session_dict = self.user_id_by_session_id.get(session_id)
        if session_dict is None or 'created_at' not in session_dict:
            return None
        if self.session_duration <= 0:
            return session_dict.get('user_id')
        created_time = session_dict.get('created_at')
        session_elapsed = timedelta(seconds=self.session_duration)
        if created_time + session_elapsed < datetime.now():
            return None
        else:
            return session_dict.get('user_id')
