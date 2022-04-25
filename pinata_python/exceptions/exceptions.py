class AuthenticationError(Exception):
    """Authentication exception.
    """

    def __init__(self, msg='Authentication is not provided.'):
        self.msg = msg
        super().__init__(self.msg)


class SetAuthenticationError(Exception):
    """Set authentication exception.
    """

    def __init__(self, msg=''):
        self.msg = msg
        super().__init__(self.msg)
        