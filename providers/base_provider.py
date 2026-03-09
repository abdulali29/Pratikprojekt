from abc import ABC, abstractmethod


class BaseProvider(ABC):
    """
    Abstract base class for all cloud providers.
    Ensures all providers return standardized data format.
    """

    @abstractmethod
    def fetch(self):
        """
        Must return list of standardized records:
        {
            "date": "YYYY-MM-DD",
            "service": "...",
            "category": "...",
            "cost": float
        }
        """
        pass