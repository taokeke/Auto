from H3CSwitch.H3CSwitch import *


host = "11.1.7.240"
username = "bosbranch"
password = "branchlyq2014"
enable = "maipulyq2014"
tn = telnetlib.Telnet(host)
tn.read_until("name:", 5)
tn.write(username.encode('ascii')+"\n")
tn.read_until("word:", 5)
tn.write(password.encode('ascii')+"\n")
tn.read_until(">", 5)
print 'success '
test = H3CSwitch()
test.host = '198.21.220.251'
test.password = 'bosbranch'
test.username = 'branchjhj2014'
test.super_password = 'h3cjhj2014'
test.connect()
portlists = test.get_portlists()
print 'portlists = '
print portlists
port_info = test.get_port_info(portlists)
print 'port_info = '
print port_info
test.disconnect()
