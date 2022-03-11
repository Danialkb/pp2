import re

a, t = input(), ''
a = a.split('_')
for i in a:
    t += i.capitalize()
print(t)

# ssl_spep ----- SslSpep