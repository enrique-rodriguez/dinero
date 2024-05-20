class Result:

    def __init__(self, msg="ok", code="ok", is_error=False):
        self.msg = msg
        self.code = code
        self.is_error = is_error
    
    @classmethod
    def error(cls, msg, code="generic-error"):
        return Result(is_error=True, msg=msg, code=code)
    
    @classmethod
    def success(cls):
        return Result(is_error=False)