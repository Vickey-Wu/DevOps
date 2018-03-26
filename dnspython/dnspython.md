dnspython: dns query

#### query A dns records
```angular2html
import dns
domain = "www.google.com.hk"
A = dns.resolver.query(domain, "A")
for i in A.response.answer:
    for j in i.items:
        print(j)
#         print(j.to_text())
```