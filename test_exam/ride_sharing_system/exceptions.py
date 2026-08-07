class InvalidRatingError(Exception):
    """Raised when rating is not between 1 and 5"""
    pass

class NegativeDistanceError(Exception):
    """Raised when distance is negative"""
    pass

class RideHistoryError(Exception):
    """Raised when ride history file operation fails"""
    pass