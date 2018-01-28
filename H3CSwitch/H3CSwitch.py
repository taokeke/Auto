# -*- coding: utf-8 -*-
import telnetlib
import re
from H3CSwitchError import *


class H3CSwitch(object):
        def __int__(self, host=None, password=None, username=None, super_password=None, port_lists=None):
            self.host = host
            self.username = username
            self.password = password
            self.super_password = super_password
            self.port_lists = port_lists

            self.connected = False
            self._connection = None
            self.hostname = None

            if self.username == '' :
                self.username = None

        def connect(self, host=None, port=23, timeout=2):
            # 建立交换机连接
            if host is None:
                host = self.host
            # 调用私有函数
            self._connection = telnetlib.Telnet(host, port, timeout)
            self._authenticate()
            self._get_hostname()
            self._super()
            # 关闭分屏功能
            self.cmd("screen-length 0 temporary")

            self.connected = True

        def disconnect(self):
            if self._connection is not None:
                self._connection.write('quit' + '\n')
                self._connection.close()

            self._connection = None
            self.connected = False

        def _authenticate(self):
            # 忽略U和P大小写情况
            idx, match, text = self.expect(['sername:', 'assword:'], 5)

            if match is None:
                raise AuthenticationError("无法获取到username或password输入提示",
                                          text)
            # 情况1：无username
            elif match.group().count(b'assword:'):
                self.write(self.password + "\n")
                # 再次出现password说明密码错误
                idx, match, text = self.expect(['assword', '>', '#'], 5)
                if match.group() is not None and match.group().count(b'assword'):
                    raise AuthenticationError("password错误")
            elif match.group().count(b'sername') > 0:
                if self.username is None:
                    raise AuthenticationError("要求输入username，但username为空字段")
                else:
                    self.write(self.username + "\n")
                    idx, match, text = self.expect(['assword:'], 5)

                    if match is None:
                        raise AuthenticationError("未能输入password", text)
                    elif match.group().count(b'assword'):
                        self.write(self.password + "\n")

                    # Check for an valid login
                    idx, match, text = self.expect(['#', '>', "invalid", "failed"], 2)
                    if match is None:
                        raise AuthenticationError("Unexpected text post-login", text)
                    elif b"invalid" in match.group() or b"failed" in match.group():
                        raise AuthenticationError("Unable to login. Your username or password are incorrect.")
            else:
                raise AuthenticationError("Unable to get a login prompt")