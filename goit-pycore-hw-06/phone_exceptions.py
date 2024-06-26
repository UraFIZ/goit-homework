class PhoneExceptions:
    class PhoneValidationError(Exception):
        """Base class for phone-related validation errors."""

    class PhoneNotFound(PhoneValidationError):
        """Raised when a phone number is not found."""

    class PhoneLengthError(PhoneValidationError):
        """Raised when a phone number has an invalid length."""

    class NameError(Exception):
        """Raised when a name is invalid."""

    class PhoneAlreadyExists(PhoneValidationError):
        """Raised when a phone number already exists in the record."""