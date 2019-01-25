from urllib.request import urlopen
import re

domains = []

for line in urlopen("https://raw.githubusercontent.com/zapret-info/z-i/master/nxdomain.txt"):
    domain = line.decode()
    domains.append(domain)

for domain in domains:
    re.search("[\w\d]+.([\w\d]+.[\w\d])", domain)
