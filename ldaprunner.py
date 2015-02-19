import sys
from ldap3 import Server, Connection
from ldap3 import IP_V6_PREFERRED

HOST      = "ldap.hawaii.edu"
PORT      = 636
LDAP_USER = 'cn=filedrop,ou=Specials,dc=hawaii,dc=edu'
LDAP_PASS = '' # <-- Your password goes here.

s = Server(HOST, port=PORT, use_ssl=True)
s.mode = IP_V6_PREFERRED

c = Connection(s, user=LDAP_USER, password=LDAP_PASS)
c.open()
c.bind()

uid = str(sys.argv[1])
base = 'dc=hawaii,dc=edu'
filter = '(uid=' + uid + ')'
attributes = ['cn', 'uid', 'uhUuid', 'mail']
c.search(search_base=base, search_filter=filter, attributes=attributes)

for entry in c.response:
    print(entry['attributes'])

c.unbind()
