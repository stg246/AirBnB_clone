#!/usr/bin/python3
""" User module """


from models.base_model import BaseModel


class User(BaseModel):
    """ User class """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *prmargs, **kwargs):
        """
            Constructor
        """
        super().__init__(*prmargs, **kwargs)
