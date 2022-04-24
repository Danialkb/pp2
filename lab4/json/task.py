import json

with open('sample.json', 'r', encoding='utf8') as f:
    x = f.read()

d = json.loads(x)

print('Interface status', '='*80, sep='\n')

print('DN', ' '*40, 'Description', ' '*4, 'Speed', ' '*4, 'MTU')

print('-'*80, )

for j in range(len(d['imdata'])):
    for i  in d['imdata'][j].values():
        if len(i['attributes']['dn'])  == 41:
            print(i['attributes']['dn'], ' '*17, i['attributes']['speed'], ' '*3, i['attributes']['mtu'])


        else:
            print(i['attributes']['dn'], ' '*16, i['attributes']['speed'], ' '*3, i['attributes']['mtu'])