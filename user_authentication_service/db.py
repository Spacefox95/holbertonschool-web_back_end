#!/usr/bin/env python3

"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.exc import NoResultFound, InvalidRequestError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
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

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Add a user to the DB"""
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        self._session.refresh(new_user)
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """
        Finds the first user that matches the given filters.

        Args:
            **kwargs: arbitrary keyword arguments to filter the query.

        Returns:
            User: the first matching user.

        Raises:
            NoResultFound: if no user matches the query.
            InvalidRequestError: if an invalid field is passed.
        """

        session = self._session

        # Validate provided column names.
        valid_columns = User.__table__.columns.keys()

        for key in kwargs.keys():
            if key not in valid_columns:
                raise InvalidRequestError(f"Invalid column name: {key}")

        # Execute query with dynamic filters.
        user = session.query(User).filter_by(**kwargs).first()

        if user is None:
            raise NoResultFound("No user found matching the criteria.")

        return user


    def update_user(self, user_id: int, **kwargs) -> None:
        """ Update user parameters"""
        try:
            user = self.find_user_by(id=user_id)

            for key, value in kwargs.items():
                if not hasattr(user, key):
                    raise ValueError(f"Invalide attribute: {key}")
                setattr(user, key, value)

            self._session.commit()

        except NoResultFound:
            raise NoResultFound(f"User with id {user_id} not found")
