#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from user import Base, User
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> str:
        """ creates a user
        """
        addUser = User(email=email, hashed_password=hashed_password)
        self._session.add(addUser)
        self._session.commit()
        return addUser

    def find_user_by(self, **kwargs):
        """Find user
        """
        try:
            search_record = self._session.query(User).filter_by(**kwargs).first()
        except TypeError:
            raise InvalidRequestError
        if search_record is None:
            raise NoResultFound
        return search_record

    def update_user(self, user_id: int, **kwargs) -> None:
        """ updates a user
        """
        user_record = self.find_user_by(id=user_id)
        for i, value in kwargs.items():
            if hasattr(user_record, i):
                setattr(user_record, i, value)
            else:
                raise ValueError

        self._session.commit()
        return None
