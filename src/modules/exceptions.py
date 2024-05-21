class PhoneVerificationError(Exception):
    def __init__(self, phone):
        self.phone = phone
        self.message = f"Invalid phone number: {phone}"
        super().__init__(self.message)


class PhoneNotFoundError(Exception):
    def __init__(self, phone):
        self.phone = phone
        self.message = f"Phone was not found: {phone}"
        super().__init__(self.message)


class PhoneAlreadyExistsError(Exception):
    def __init__(self, phone):
        self.phone = phone
        self.message = f"Phone already exists: {phone}"
        super().__init__(self.message)