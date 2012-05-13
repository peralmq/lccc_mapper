# coding: utf-8
import nose.tools as nt
import lccc_mapper

class TestLocaleToCurrency(object):

    def test_sv_SE_to_SEK(self):
        expected = 'SEK'
        actual = lccc_mapper.locale_to_currencies('sv_SE')[0]
        nt.assert_equals(expected, actual)

    def test_en_GB_to_GBP(self):
        expected = 'GBP'
        actual = lccc_mapper.locale_to_currencies('en_GB')[0]
        nt.assert_equals(expected, actual)

    def test_en_US_to_USD(self):
        expected = 'USD'
        actual = lccc_mapper.locale_to_currencies('en_US')[0]
        nt.assert_equals(expected, actual)

    def test_nb_NO_to_NOK(self):
        expected = 'NOK'
        actual = lccc_mapper.locale_to_currencies('nb_NO')[0]
        nt.assert_equals(expected, actual)

    def test_de_DE_to_EUR(self):
        expected = 'EUR'
        actual = lccc_mapper.locale_to_currencies('de_DE')[0]
        nt.assert_equals(expected, actual)

    def test_fr_FR_to_EUR(self):
        expected = 'EUR'
        actual = lccc_mapper.locale_to_currencies('fr_FR')[0]
        nt.assert_equals(expected, actual)

    def test_raises_KeyError_for_bad_input(self):
        with nt.assert_raises(KeyError):
            lccc_mapper.locale_to_currencies('xx_XX')

class TestCurencyToCountryCode(object):

    def test_SEK_to_SE(self):
        expected = 'SE'
        actual = lccc_mapper.currency_to_country_codes('SEK')[0]
        nt.assert_equals(expected, actual)

    def test_USD_to_US(self):
        expected = 'US'
        actual = lccc_mapper.currency_to_country_codes('USD')
        nt.assert_in(expected, actual)

    def test_raises_KeyError_for_bad_input(self):
        with nt.assert_raises(KeyError):
            lccc_mapper.currency_to_country_codes('XXX')

