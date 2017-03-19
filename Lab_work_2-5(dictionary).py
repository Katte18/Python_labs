#Lab. work 2-5 (dictionary)

#create dict with 5 items, where keys will be country name and value - domain name, i.e. {Ukraine:UA}
countries = {'Ukraine': 'UA',
             'Poland': 'PL',
             'Mexico': 'MX',
             'Germany': 'DE',
             'Spain': 'ES'
}
#create another dict with 5 items, where values of countries will be keys, and values will be the capitals i.e. {'UA': 'Kiev'}
capitals = {
    'UA': 'Kyiv',
    'PL': 'Warshaw',
    'MX': 'MX',
    'DE': 'Berlin',
    'ES': 'Madrid'
}
#add one more element to each dict above
countries.update({'Austria': 'AT'})
capitals.update({'AT': 'Vienna'})

#print sentence "Domain for COUNTRY is DOMAIN." for each record in countries with the replace from dicts
for key, value in countries.items():
    print("Domain for {} is {}".format(key, value))

#print sentence "The capital of COUNTRY is CAPITAL" for each record in capitals with the replace from dicts
for key, value in capitals.items():
    print("The capital of {} is {}".format(key, value))

#Merge sentences above together with one cycle
for key, value in countries.items():
    print("Domain for {} is {}. The capital is {}".
          format(key, value, capitals[value]))

#Add to each value of first dict another two domains: COM and GOV
for key, value in countries.items():
    countries[key] = [value, 'COM', 'GOV']

for key, value in countries.items():
    print("Domnain for{} is {}. The capital is {}".
          format(key, value, capitals[value[0]]))