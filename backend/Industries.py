""" Role Industries"""
from enum import Enum

class RoleCategory(str,Enum):
    """ Different industries members can register their co-ops as """
    TECHNOLOGY = "Technology"
    HEALTHCARE = "Healthcare"
    BUSINESS = "Business"
    ENGINEERING = "Engineering"
    SCIENCE = "Science & Research"
    ARTS_MEDIA = "Arts,Media & Design"
    GOVERNMENT ="Government & Nonprofit"
    LAW = "Law"
    OTHER = "Other"
    
    
class Seasons(str,Enum):
    "Different Seasons for dictating terms of Co-Op's"
    FALL = "Fall"
    SPRING = "Spring"


