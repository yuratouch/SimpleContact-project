class PhoneVerificationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class EmailVerificationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

