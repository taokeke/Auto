from H3CSwitch.H3CSwitch import *

test = H3CSwitch()
test.host = '11.1.7.54'
test.username = 'bosbranch'
test.password = 'branchjhj2014'
test.super_password = 'h3cjhj2014'
test.connect()
portlists = test.get_portlists()
print 'portlists = '
print portlists
port_info = test.get_port_info(portlists)
print 'port_info = '
print port_info
port_status_lists = test.get_port_status(port_info)
print port_status_lists
test.disconnect()
