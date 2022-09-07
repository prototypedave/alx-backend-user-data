#!/usr/bin/env python3
"""
Auth class
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ creates a class auth
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Defines which routes don't need authentication
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != '/':
            path += '/'
        for i in excluded_paths:
            if i.endswith('*'):
                if path.startswith(i[:1]):
                    return False
        if path in excluded_paths:
            return False
        else:
            return True
    

    def authorization_header(self, request=None) -> str:
        """ Request validation!
        """
        if request is None or not request.headers.get('Authorization'):
            return None
        else:
            return request.headers.get('Authorization')


    def current_user(self, request=None) -> TypeVar('User'):
        """ request object
        """
        return None
