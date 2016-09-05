class MoneybotException(Exception):
    public = False


class NoSuchQuery(MoneybotException):
    pass


class InsufficientFunds(MoneybotException):
    public = True


class InvalidCommand(MoneybotException):
    public = True
