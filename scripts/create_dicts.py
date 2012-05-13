# coding: utf-8
from csv import reader
from collections import defaultdict

data_file = 'data/country_currency.csv'
mapper_file = 'lccc_mapper/mapper.py'

with open(data_file, 'rb') as fin:
    r = reader(fin, delimiter=',', quotechar='"')
    curr_cc = defaultdict(list)
    cc_curr = defaultdict(list)
    first = True
    for country_code, currency, expiration_date in r:
        if first:
            first = False
            continue
        if currency and country_code and not expiration_date:
            cc_curr[country_code].append(currency)
            curr_cc[currency].append(country_code)

with open(mapper_file, 'w') as fout:
    fout.write('# coding: utf-8\n')
    fout.write('currency_country_code = {\n')
    for currency, countries in curr_cc.items():
        fout.write("    '%s': %s,\n" % (currency, countries))
    fout.write('}\n')
    fout.write('country_code_currency = {\n')
    for country, currencies in cc_curr.items():
        fout.write("    '%s': %s,\n" % (country, currencies))
    fout.write('}\n')

