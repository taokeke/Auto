from H3CSwitch.H3CSwitch import *
import re

test = H3CSwitch()
test.host = '161.1.1.221'
test.password = 'branchjhj2014'
test.username = 'bosbranch'
test.super_password = 'h3cjhj2014'
test.connect()
portlists = test.get_portlists()
print portlists
test.disconnect()
# re_text = '((?:\d|\w){4}\-(?:\d|\w){4}\-(?:\d|\w){4})\s+(\d+/-)\s+(.+?)\s+(dynamic|sticky)\s+.+\r?\n?'
# re_text = '(?P<ip>\d+\.\d+\.\d+\.\d+)\s+((?:\d|\w){4}\-(?:\d|\w){4}\-(?:\d|\w){4}|Incomplete)\s+.+\r?\n?'
result = '   \r\nInternet  11.1.7.1            0000.5e00.0107  ARPA    gigabitethernet0   N/A  \r\n '
re_text = '(?P<ip>\d+\.\d+\.\d+\.\d+)\s+((?:\d|\w){4}\.(?:\d|\w){4}\.(?:\d|\w){4})\s+.+\r?\n?'
items = re.findall(re_text, result)
print(items)
