#!/usr/bin/env python3
"""
Module that implements the review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel
    """
    place_id = ""
    user_id = ""
    test = ""
