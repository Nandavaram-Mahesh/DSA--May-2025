class StackException(Exception):
    pass

class StackOverFlow(StackException):
    def __init__(self,message):
        super().__init__(message)

class StackUnderFlow(StackException):
    def __init__(self,message):
        super().__init__(message)
