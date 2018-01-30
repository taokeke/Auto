from H3CSwitch.H3CSwitch import *


test = H3CSwitch()
test.host = '161.1.1.221'
test.password = 'branchjhj2014'
test.username = 'bosbranch'
test.super_password = 'h3cjhj2014'
test.connect()
portlists = test.get_portlists()
print 'portlists = '
print portlists
port_info = test.get_port_info(portlists)
print 'port_info = '
print port_info
test.disconnect()
