# Auto
a test
C:\Python27\python.exe D:/Auto/main.py
>
success
display current-configuration | include ^interface.+Ethernet
interface Ethernet1/0/1
interface Ethernet1/0/2
interface Ethernet1/0/3
interface Ethernet1/0/4
interface Ethernet1/0/5
interface Ethernet1/0/6
interface Ethernet1/0/7
interface Ethernet1/0/8
interface Ethernet1/0/9
interface Ethernet1/0/10
interface Ethernet1/0/11
interface Ethernet1/0/12
interface Ethernet1/0/13
interface Ethernet1/0/14
interface Ethernet1/0/15
interface Ethernet1/0/16
interface Ethernet1/0/17
interface Ethernet1/0/18
interface Ethernet1/0/19
interface Ethernet1/0/20
interface Ethernet1/0/21
interface Ethernet1/0/22
interface Ethernet1/0/23
interface Ethernet1/0/24
interface Ethernet1/0/25
interface Ethernet1/0/26
interface Ethernet1/0/27
interface Ethernet1/0/28
interface Ethernet1/0/29
interface Ethernet1/0/30
interface Ethernet1/0/31
interface Ethernet1/0/32
interface Ethernet1/0/33
interface Ethernet1/0/34
interface Ethernet1/0/35
interface Ethernet1/0/36
interface Ethernet1/0/37
interface Ethernet1/0/38
interface Ethernet1/0/39
interface Ethernet1/0/40
interface Ethernet1/0/41
interface Ethernet1/0/42
interface Ethernet1/0/43
interface Ethernet1/0/44
interface Ethernet1/0/45
interface Ethernet1/0/46
interface Ethernet1/0/47
interface Ethernet1/0/48
interface GigabitEthernet1/0/49
interface GigabitEthernet1/0/50
interface GigabitEthernet1/0/51
interface GigabitEthernet1/0/52

portlists = 
['Ethernet1/0/1', 'Ethernet1/0/2', 'Ethernet1/0/3', 'Ethernet1/0/4', 'Ethernet1/0/5', 'Ethernet1/0/6', 'Ethernet1/0/7', 'Ethernet1/0/8', 'Ethernet1/0/9', 'Ethernet1/0/10', 'Ethernet1/0/11', 'Ethernet1/0/12', 'Ethernet1/0/13', 'Ethernet1/0/14', 'Ethernet1/0/15', 'Ethernet1/0/16', 'Ethernet1/0/17', 'Ethernet1/0/18', 'Ethernet1/0/19', 'Ethernet1/0/20', 'Ethernet1/0/21', 'Ethernet1/0/22', 'Ethernet1/0/23', 'Ethernet1/0/24', 'Ethernet1/0/25', 'Ethernet1/0/26', 'Ethernet1/0/27', 'Ethernet1/0/28', 'Ethernet1/0/29', 'Ethernet1/0/30', 'Ethernet1/0/31', 'Ethernet1/0/32', 'Ethernet1/0/33', 'Ethernet1/0/34', 'Ethernet1/0/35', 'Ethernet1/0/36', 'Ethernet1/0/37', 'Ethernet1/0/38', 'Ethernet1/0/39', 'Ethernet1/0/40', 'Ethernet1/0/41', 'Ethernet1/0/42', 'Ethernet1/0/43', 'Ethernet1/0/44', 'Ethernet1/0/45', 'Ethernet1/0/46', 'Ethernet1/0/47', 'Ethernet1/0/48', 'GigabitEthernet1/0/49', 'GigabitEthernet1/0/50', 'GigabitEthernet1/0/51', 'GigabitEthernet1/0/52']
return
['#\r description To_WD-XXXX-R2900-01_F0/0\r port link-type trunk\r port trunk permit vlan 1 198 to 199\r#']
return
['#\r description Backup\r port link-type trunk\r port trunk permit vlan 1 198 to 199\r#']
return
['#\r port link-type hybrid\r port hybrid vlan 1 198 to 199 untagged\r port hybrid pvid vlan 198\r stp edged-port enable\r stp port bpdu-protection enable\r dot1x max-user 1\r dot1x guest-vlan 199\r undo dot1x handshake\r dot1x port-method portbased\r dot1x\r#']
return
['#\r port access vlan 198\r mac-address max-mac-count 0\r mac-address static 9cb6-54f4-b351 vlan 198\r#']
return
['#\r port access vlan 198\r#']
return
['#\r shutdown\r#']
return
['#\r shutdown\r#']
return
['#\r shutdown\r#']
return
['#\r port link-type hybrid\r port hybrid vlan 1 198 to 199 untagged\r port hybrid pvid vlan 198\r stp edged-port enable\r stp port bpdu-protection enable\r dot1x max-user 1\r dot1x guest-vlan 199\r undo dot1x handshake\r dot1x port-method portbased\r dot1x\r#']
return
['#\r port link-type hybrid\r port hybrid vlan 1 198 to 199 untagged\r port hybrid pvid vlan 198\r stp edged-port enable\r stp port bpdu-protection enable\r dot1x max-user 1\r dot1x guest-vlan 199\r undo dot1x handshake\r dot1x port-method portbased\r dot1x\r#']
return
['#\r port link-type hybrid\r port hybrid vlan 1 198 to 199 untagged\r port hybrid pvid vlan 198\r stp edged-port enable\r stp port bpdu-protection enable\r dot1x max-user 1\r dot1x guest-vlan 199\r undo dot1x handshake\r dot1x port-method portbased\r dot1x\r#']
return
['#\r shutdown\r#']
return
['#\r shutdown\r#']
return
['#\r shutdown\r#']
return
['#\r shutdown\r#']
return
['#\r shutdown\r#']
return
['#\r shutdown\r#']
return
['#\r shutdown\r#']
return
['#\r shutdown\r#']
return
['#\r shutdown\r#']
return
['#\r shutdown\r#']
return
['#\r shutdown\r#']
return
['#\r shutdown\r#']
return
['#\r port access vlan 198\r mac-address max-mac-count 0\r mac-address static 1243-1234-1234 vlan 198\r#']
return
['#\r shutdown\r#']
return
['#\r shutdown\r#']
return
['#\r shutdown\r#']
return
['#\r shutdown\r#']
return
['#\r shutdown\r#']
return
['#\r shutdown\r#']
return
['#\r shutdown\r#']
return
['#\r port link-type hybrid\r port hybrid vlan 1 198 to 199 untagged\r port hybrid pvid vlan 198\r stp edged-port enable\r stp port bpdu-protection enable\r dot1x max-user 1\r dot1x guest-vlan 199\r undo dot1x handshake\r dot1x port-method portbased\r dot1x\r#']
return
['#\r shutdown\r#']
return
['#\r shutdown\r#']
return
['#\r shutdown\r#']
return
['#\r shutdown\r#']
return
['#\r shutdown\r#']
return
['#\r shutdown\r#']
return
['#\r port link-type hybrid\r port hybrid vlan 1 198 to 199 untagged\r port hybrid pvid vlan 198\r stp edged-port enable\r stp port bpdu-protection enable\r dot1x max-user 1\r dot1x guest-vlan 199\r undo dot1x handshake\r dot1x port-method portbased\r dot1x\r#']
return
['#\r shutdown\r#']
return
['#\r shutdown\r#']
return
['#\r shutdown\r#']
return
['#\r shutdown\r#']
return
['#\r shutdown\r#']
return
['#\r shutdown\r#']
return
['#\r shutdown\r#']
return
['#\r shutdown\r#']
return
['#\r shutdown\r#']
return
['#\r#']
return
['#\r#']
return
['#\r#']
return
['#\r#']
port_info = 
[{'info': ['#\r description To_WD-XXXX-R2900-01_F0/0\r port link-type trunk\r port trunk permit vlan 1 198 to 199\r#'], 'portlist': 'Ethernet1/0/1'}, {'info': ['#\r description Backup\r port link-type trunk\r port trunk permit vlan 1 198 to 199\r#'], 'portlist': 'Ethernet1/0/2'}, {'info': ['#\r port link-type hybrid\r port hybrid vlan 1 198 to 199 untagged\r port hybrid pvid vlan 198\r stp edged-port enable\r stp port bpdu-protection enable\r dot1x max-user 1\r dot1x guest-vlan 199\r undo dot1x handshake\r dot1x port-method portbased\r dot1x\r#'], 'portlist': 'Ethernet1/0/3'}, {'info': ['#\r port access vlan 198\r mac-address max-mac-count 0\r mac-address static 9cb6-54f4-b351 vlan 198\r#'], 'portlist': 'Ethernet1/0/4'}, {'info': ['#\r port access vlan 198\r#'], 'portlist': 'Ethernet1/0/5'}, {'info': ['#\r shutdown\r#'], 'portlist': 'Ethernet1/0/6'}, {'info': ['#\r shutdown\r#'], 'portlist': 'Ethernet1/0/7'}, {'info': ['#\r shutdown\r#'], 'portlist': 'Ethernet1/0/8'}, {'info': ['#\r port link-type hybrid\r port hybrid vlan 1 198 to 199 untagged\r port hybrid pvid vlan 198\r stp edged-port enable\r stp port bpdu-protection enable\r dot1x max-user 1\r dot1x guest-vlan 199\r undo dot1x handshake\r dot1x port-method portbased\r dot1x\r#'], 'portlist': 'Ethernet1/0/9'}, {'info': ['#\r port link-type hybrid\r port hybrid vlan 1 198 to 199 untagged\r port hybrid pvid vlan 198\r stp edged-port enable\r stp port bpdu-protection enable\r dot1x max-user 1\r dot1x guest-vlan 199\r undo dot1x handshake\r dot1x port-method portbased\r dot1x\r#'], 'portlist': 'Ethernet1/0/10'}, {'info': ['#\r port link-type hybrid\r port hybrid vlan 1 198 to 199 untagged\r port hybrid pvid vlan 198\r stp edged-port enable\r stp port bpdu-protection enable\r dot1x max-user 1\r dot1x guest-vlan 199\r undo dot1x handshake\r dot1x port-method portbased\r dot1x\r#'], 'portlist': 'Ethernet1/0/11'}, {'info': ['#\r shutdown\r#'], 'portlist': 'Ethernet1/0/12'}, {'info': ['#\r shutdown\r#'], 'portlist': 'Ethernet1/0/13'}, {'info': ['#\r shutdown\r#'], 'portlist': 'Ethernet1/0/14'}, {'info': ['#\r shutdown\r#'], 'portlist': 'Ethernet1/0/15'}, {'info': ['#\r shutdown\r#'], 'portlist': 'Ethernet1/0/16'}, {'info': ['#\r shutdown\r#'], 'portlist': 'Ethernet1/0/17'}, {'info': ['#\r shutdown\r#'], 'portlist': 'Ethernet1/0/18'}, {'info': ['#\r shutdown\r#'], 'portlist': 'Ethernet1/0/19'}, {'info': ['#\r shutdown\r#'], 'portlist': 'Ethernet1/0/20'}, {'info': ['#\r shutdown\r#'], 'portlist': 'Ethernet1/0/21'}, {'info': ['#\r shutdown\r#'], 'portlist': 'Ethernet1/0/22'}, {'info': ['#\r shutdown\r#'], 'portlist': 'Ethernet1/0/23'}, {'info': ['#\r port access vlan 198\r mac-address max-mac-count 0\r mac-address static 1243-1234-1234 vlan 198\r#'], 'portlist': 'Ethernet1/0/24'}, {'info': ['#\r shutdown\r#'], 'portlist': 'Ethernet1/0/25'}, {'info': ['#\r shutdown\r#'], 'portlist': 'Ethernet1/0/26'}, {'info': ['#\r shutdown\r#'], 'portlist': 'Ethernet1/0/27'}, {'info': ['#\r shutdown\r#'], 'portlist': 'Ethernet1/0/28'}, {'info': ['#\r shutdown\r#'], 'portlist': 'Ethernet1/0/29'}, {'info': ['#\r shutdown\r#'], 'portlist': 'Ethernet1/0/30'}, {'info': ['#\r shutdown\r#'], 'portlist': 'Ethernet1/0/31'}, {'info': ['#\r port link-type hybrid\r port hybrid vlan 1 198 to 199 untagged\r port hybrid pvid vlan 198\r stp edged-port enable\r stp port bpdu-protection enable\r dot1x max-user 1\r dot1x guest-vlan 199\r undo dot1x handshake\r dot1x port-method portbased\r dot1x\r#'], 'portlist': 'Ethernet1/0/32'}, {'info': ['#\r shutdown\r#'], 'portlist': 'Ethernet1/0/33'}, {'info': ['#\r shutdown\r#'], 'portlist': 'Ethernet1/0/34'}, {'info': ['#\r shutdown\r#'], 'portlist': 'Ethernet1/0/35'}, {'info': ['#\r shutdown\r#'], 'portlist': 'Ethernet1/0/36'}, {'info': ['#\r shutdown\r#'], 'portlist': 'Ethernet1/0/37'}, {'info': ['#\r shutdown\r#'], 'portlist': 'Ethernet1/0/38'}, {'info': ['#\r port link-type hybrid\r port hybrid vlan 1 198 to 199 untagged\r port hybrid pvid vlan 198\r stp edged-port enable\r stp port bpdu-protection enable\r dot1x max-user 1\r dot1x guest-vlan 199\r undo dot1x handshake\r dot1x port-method portbased\r dot1x\r#'], 'portlist': 'Ethernet1/0/39'}, {'info': ['#\r shutdown\r#'], 'portlist': 'Ethernet1/0/40'}, {'info': ['#\r shutdown\r#'], 'portlist': 'Ethernet1/0/41'}, {'info': ['#\r shutdown\r#'], 'portlist': 'Ethernet1/0/42'}, {'info': ['#\r shutdown\r#'], 'portlist': 'Ethernet1/0/43'}, {'info': ['#\r shutdown\r#'], 'portlist': 'Ethernet1/0/44'}, {'info': ['#\r shutdown\r#'], 'portlist': 'Ethernet1/0/45'}, {'info': ['#\r shutdown\r#'], 'portlist': 'Ethernet1/0/46'}, {'info': ['#\r shutdown\r#'], 'portlist': 'Ethernet1/0/47'}, {'info': ['#\r shutdown\r#'], 'portlist': 'Ethernet1/0/48'}, {'info': ['#\r#'], 'portlist': 'GigabitEthernet1/0/49'}, {'info': ['#\r#'], 'portlist': 'GigabitEthernet1/0/50'}, {'info': ['#\r#'], 'portlist': 'GigabitEthernet1/0/51'}, {'info': ['#\r#'], 'portlist': 'GigabitEthernet1/0/52'}]

Process finished with exit code 0
