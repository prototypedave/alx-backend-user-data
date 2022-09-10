#!/usr/bin/env python3
"""
Sessions in database
"""
from api.v1.auth.session_exp_auth import SessionExpAuth


class SessionDBAuth(SessionExoAuth):
    """ inherits from SessionExpAuth
    """
    def create_session(self, user_id=None):
        """ overloads create session method of SessionExp Auth
        """
        pass

    def user_id_for_session_id(self, session_id=None):
        """ overloads this method of SessionExpAuth
        """
        if session_id is None:
            return None
        pass

    def destroy_session(self, request=None):
        """ destroys active sessions
        """
        pass
