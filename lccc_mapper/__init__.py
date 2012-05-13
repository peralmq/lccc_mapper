# coding: utf-8
import mapper

def locale_to_country_code(locale):
    return locale[locale.rfind('_')+1:] if '_' in locale else locale

def locale_to_currencies(locale):
    cc = locale_to_country_code(locale)
    return country_code_to_currencies(cc)

def country_code_to_currencies(cc):
    try:
        return mapper.country_code_currency[cc.upper()]
    except:
        print 'Failed to get currencies for country code=%s' % cc
        raise

def currency_to_country_codes(currency):
    try:
        return mapper.currency_country_code[currency.upper()]
    except:
        print 'Failed to get country codes for currency=%s' % currency
        raise

