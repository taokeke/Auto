# -*- coding: utf-8 -*-
import telnetlib
import re
from H3CSwitchError import *


class H3CSwitch(object):
    def __init__(self, host=None, password=None, username=None, super_password=None, port_lists=None):
            self.host = host
            self.username = username
            self.password = password
            self.super_password = super_password
            self.port_lists = port_lists
            self.connected = False
            self._connection = None
            self.hostname = None

            if self.username == '':
                self.username = None

    def connect(self, host=None, port=23, timeout=2):
            # 建立交换机连接
            if host is None:
                host = self.host
            # 调用私有方法
            self._connection = telnetlib.Telnet(host, port, timeout)
            self._authenticate()
            self._get_hostname()
            self._super()
            # 关闭交换机分屏显示功能
            self.cmd("screen-length disable")
            # self.cmd("screen-length 0 temporary")
            self.connected = True
            print 'success'

    def connectx(self):
        self.cmd('telnet 198.21.220.251')
        self._authenticate()
        self._get_hostname()
        self._super()
        # 关闭交换机分屏显示功能
        # self.cmd("screen-length disable")
        self.cmd("screen-length 0 temporary")
        self.connected = True
        print 'success'

    def disconnect(self):
            if self._connection is not None:
                self._connection.write('quit' + '\n')
                self._connection.close()

            self._connection = None
            self.connected = False
            print("success")

    def _authenticate(self):
            # 忽略U和P大小写情况
            idx, match, text = self.expect(['sername:', 'assword:'], 5)

            if match is None:
                raise AuthenticationError("无法获取到username或password输入提示",
                                          text)
            # 情况1：无username
            elif match.group().count('assword:'):
                self.write(self.password + "\n")
                # 再次出现password说明密码错误
                idx, match, text = self.expect(['assword', '>', '#'], 5)
                if match.group() is not None and match.group().count('assword'):
                    raise AuthenticationError("password错误")
            elif match.group().count('sername') > 0:
                if self.username is None:
                    raise AuthenticationError("要求输入username，但username为空字段")
                else:
                    self.write(self.username + "\n")
                    idx, match, text = self.expect(['assword:'], 5)

                    if match is None:
                        raise AuthenticationError("未能输入password", text)
                    elif match.group().count('assword'):
                        self.write(self.password + "\n")
                    # Check for an valid login
                    idx, match, text = self.expect(['#', '>', "invalid", "failed"], 2)
                    if match is None:
                        raise AuthenticationError("未能得到反馈", text)
                    elif "invalid" in match.group() or "failed" in match.group():
                        raise AuthenticationError("无法登陆，username或password错误")
            else:
                raise AuthenticationError("无法获得登陆提示")

    def _get_hostname(self):
        self.write("\n")

        idx, match, text = self.expect(['>'], 2)
        # 获取<设备名称>，并将"<"及">"替换为空格
        if match is not None:
            tmp = text.replace('<','').strip()
            # strip（）方法用于移除空格
            self.hostname = tmp.replace('>', '').strip()
        else:
            raise H3CSwitchError("无法获取设备名")

    def _super(self, password=None):
        if password is not None:
            self.super_password = password
        self.write('\n')
        self.read_until_prompt()

        self.write("super"+'\n')

        idx, match, text = self.expect(['>', 'assword:'], 1)

        if match is None:
            raise H3CSwitchError("无法进入特权模式")
        else:
            # 无super密码情况
            if 'privilege is 3' in text:
                return
            # 需要super密码，输入密码
            elif 'assword' in text:
                self.write(self.super_password + "\n")

        idx, match, text = self.expect([">", 'assword:'], 1)
        # 打印所有匹配到的对象
        print match.group()
        if match is None:
            raise H3CSwitchError("尝试super模式时，无法获得反馈", text=None)
        elif match.group().count('assword') > 0:
            self.write("\n\n\n")
            raise H3CSwitchError("password错误")
        elif 'privilege is 3' in text:
            return

    def expect(self, asearch, timeout=2):
        # 对需要进行read until 操作的字符进行ascii格式转换
        idx, match, result = self._connection.expect([needle.encode('ascii') for needle in asearch], timeout)
        return idx, match, result

    def write(self, text):
        """ 将输入指令转换成设备可读的ascii格式 """

        if self._connection is None:
            self.connect()
            raise H3CSwitchError("未连接设备")

        self._connection.write(text.encode('ascii'))

    def read_until_prompt(self, prompt=None, timeout=5):
        thost = self.hostname

        if thost is None:
            raise H3CSwitchError("设备未命名", text=None)

        if prompt is None:
            expect = [thost + ">"]
        else:
            expect = [thost + prompt]

        idx, match, ret_text = self.expect(expect, timeout)

        return ret_text

    def cmd(self, cmd_text):
        """ 向设备输入命令并得到反馈结果"""

        self.write(cmd_text + "\n")
        text = self.read_until_prompt()

        # 去除设备名称字符后的无关信息
        ret_text = ""
        for a in text.split('\n')[:-1]:
            ret_text += a + "\n"

        # 获取当前设备名称
        if 'hostname' in cmd_text:
            self._get_hostname()

        if "Error" in ret_text:
            raise InvalidCommand(cmd_text)

        return ret_text

    def get_portlists(self):
        portlists = []

        result = self.cmd('display current-configuration | include ^interface.+Ethernet')
        print result
        for a in result.split('\n')[1:-1]:
            b = a.strip('interface ')
            c = b.strip('\r')
            portlists.append(c)
        return portlists

    def get_port_info(self, port_lists):
        port_info_lists = []
        num = len(port_lists)

        for b in port_lists:
            info = self.cmd('display current-configuration interface ' + b + ' | exclude ' + b)
            infe = info.replace('\n', '')
            print infe
            re_text = '#.*#'
            result = re.findall(re_text, infe)
            print(result)
            port_info_lists.append({
                "portlist": b,
                "info": result
            })

        return port_info_lists

    def get_port_status(self, port_info_lists):
        port_status_lists = []

        for a in port_info_lists:
            info = str(a.get('info'))
            portlist = a.get('portlist')
            # 关闭
            if info.count('shutdown') > 0:
                port_status_lists.append({
                    "portlist": portlist,
                    "status": 0
                })
            # trunk口
            elif info.count('trunk') > 0:
                port_status_lists.append({
                    "portlist": portlist,
                    "status": 1
                })
            # 准入口
            elif info.count('dot1x') > 6:
                port_status_lists.append({
                    "portlist": portlist,
                    "status": 2
                })
            # 例外口
            elif info.count('mac-address') > 0:
                port_status_lists.append({
                    "portlist": portlist,
                    "status": 3
                })
            # 问题口
            else:
                port_status_lists.append({
                    "portlist": portlist,
                    "status": 4
                })

        return port_status_lists

    def get_port_mac(self, port_status_lists):
        port_mac_lists = []

        for a in port_status_lists:
            status = int(a.get('status'))
            portlist = a.get('portlist')
            if status < 2:
                port_mac_lists.append({
                    "portlist": portlist,
                    "mac": []
                })

            else:
                info = self.cmd('display mac-address interface ' + portlist)
                re_text = '((?:\d|\w){4}\-(?:\d|\w){4}\-(?:\d|\w){4})'
                result = re.findall(re_text, info)
                port_mac_lists.append({
                    "portlist": portlist,
                    "mac": result
                })
        return port_mac_lists
