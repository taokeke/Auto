import re
# re_text = '((?:\d|\w){4}\-(?:\d|\w){4}\-(?:\d|\w){4})\s+(\d+/-)\s+(.+?)\s+(dynamic|sticky)\s+.+\r?\n?'
# re_text = '(?P<ip>\d+\.\d+\.\d+\.\d+)\s+((?:\d|\w){4}\-(?:\d|\w){4}\-(?:\d|\w){4}|Incomplete)\s+.+\r?\n?'
# result = '   \r\nInternet  11.1.7.1            0000.5e00.0107  ARPA    gigabitethernet0   N/A  \r\n '
result = 'asdasd#akjshdkjhasdjkhjas#asdasdasd'
# re_text = '(?P<ip>\d+\.\d+\.\d+\.\d+)\s+((?:\d|\w){4}\.(?:\d|\w){4}\.(?:\d|\w){4})\s+.+\r?\n?'
re_text = '#.*#'
items = re.findall(re_text, result)
print(items)
