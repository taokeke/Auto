class H3CSwitchError(Exception):
    def __init__(self, value, text=''):
        self.value = value
        self.text = text

    def __str__(self):
        ret = self.value

        if self.text is not None and self.text != '':
            ret += "\n从交换机中得到反馈： " + str(self.text)

        return ret


class AuthenticationError(H3CSwitchError):
    pass


class InvalidCommand(H3CSwitchError):
    def __init__(self, cmd):
        self.cmd = cmd

    def __str__(self):
        ret = "错误命令 " + str(self.cmd)
        return ret
