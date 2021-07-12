import re

raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'


def web_parse(raw_string):
    parsed_raw = re.split('\s+', raw_string)

    print(parsed_raw[0], parsed_raw[3], parsed_raw[4], parsed_raw[5][1:], parsed_raw[6], parsed_raw[7][:-1],
          parsed_raw[8], parsed_raw[9])

    return


web_parse(raw)
