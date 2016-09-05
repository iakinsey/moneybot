class MoneybotException(Exception):
    public = False


class NoSuchQuery(MoneybotException):
    pass
