#!/usr/bin/env python3
"""
BasicAuth
"""
from flask import request
from api.v1.auth.auth import Auth
from base64 import b64decode
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """Basic auth
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """ Basic - Base64 part
        """
        if authorization_header is None:
            return None
        elif not isinstance(authorization_header, str) or not authorization_header.startswith("Basic "):
            return None
        else:
            """ split the header to have a list from the string """
            splitAuth = authorization_header.split(" ")
            return splitAuth[1]


    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """ Basic - Base64 decode
        """
        if base64_authorization_header is None or not isinstance(base64_authorization_header, str):
            return None
        try:
            baseEncode = base64_authorization_header.encode('utf-8')
            baseDecode = b64decode(baseEncode)
            decodedValue = baseDecode.decode('utf-8')
            return decodedValue
        except Exception:
            return None


    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        """ Basic - User credentials
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        user_credentials = decoded_base64_authorization_header.split(':', 1)
        return (user_credentials[0], user_credentials[1])


    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ Basic - User object
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({'email': user_email})
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
        except Exception:
            return None


    def current_user(self, request=None) -> TypeVar('User'):
        """  Basic - Overload current_user - and BOOM!
        """
        try:
            header = self.authorization_header(request)
            base64Header = self.extract_base64_authorization_header(header)
            decodeValue = self.decode_base64_authorization_header(base64Header)
            user_credentials = self.extract_user_credentials(decodeValue)
            user = self.user_object_from_credentials(credentials[0], credentials[1])
            return user
        except Exception:
            return None
