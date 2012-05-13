lccc_mapper
===========

Locale, currency, and country code mapper

Python library for looking up locale, currency, or country code based on one of the other.

URLs
----------------
https://github.com/peal/lccc_mapper

http://pypi.python.org/pypi/lccc_mapper


Example
----------------

    >>> import lccc_mapper
    >>> lccc_mapper.currency_to_country_codes('USD')
    ['AS', 'BQ', 'IO', 'EC', 'SV', 'GU', 'HT', 'MH', 'FM', 'MP', 'PW', 'PA', 'PR', 'TL', 'TC', 'US', 'UM', 'VG', 'VI']
    >>> lccc_mapper.country_code_to_currencies('CH')
    ['CHF', 'CHE', 'CHW']
    >>> lccc_mapper.locale_to_currencies('en_GB')[0]
    'GBP'