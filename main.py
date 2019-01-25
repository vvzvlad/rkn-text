from urllib.request import urlopen

def unique(data):
    n = []
    for i in data:
        if i not in n:
            n.append(i)
    return n

def get_list(url):
  domains_raw = []
  for line in urlopen(url):
      domain = line.decode()
      domains_raw.append(domain)
  return domains_raw


def remove_sundomains(list_domains):
  domains = []
  for domain in list_domains:
      chanks = domain.split(".")
      domain = chanks[-2] + "." + chanks[-1]
      domains.append(domain)
  return domains


list_domains = get_list("https://raw.githubusercontent.com/zapret-info/z-i/master/nxdomain.txt")
print("Load {} strings".format(len(list_domains)))
list_domains_without_sb = remove_sundomains(list_domains)
print("Parsed {} domains".format(len(list_domains_without_sb)))
list_domains_without_sb_unique = unique(list_domains_without_sb)
print("Uniqued {} domains".format(len(list_domains_without_sb_unique)))
