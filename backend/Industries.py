""" Role Industries"""
from enum import Enum

class RoleCategory(str,Enum):
    """ Different industries members can register their co-ops as """
    TECHNOLOGY = "Technology"
    HEALTHCARE = "Healthcare"
    BUSINESS = "Business"
    ENGINEERING = "Engineering"
