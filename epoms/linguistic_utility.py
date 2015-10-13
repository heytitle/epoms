import unicodedata

NON_DECOMPOSABLE_CHARACTERS = {
        u'\N{Latin capital letter AE}': 'AE',
        u'\N{Latin small letter ae}': 'ae',
        u'\N{Latin capital letter Eth}': 'D', #
        u'\N{Latin small letter eth}': 'd', #
        u'\N{Latin capital letter O with stroke}': 'O', #
        u'\N{Latin small letter o with stroke}': 'o',  #
        u'\N{Latin capital letter Thorn}': 'Th',
        u'\N{Latin small letter thorn}': 'th',
        u'\N{Latin small letter sharp s}': 's',#
        u'\N{Latin capital letter D with stroke}': 'D',#
        u'\N{Latin small letter d with stroke}': 'd',#
        u'\N{Latin capital letter H with stroke}': 'H',
        u'\N{Latin small letter h with stroke}': 'h',
        u'\N{Latin small letter dotless i}': 'i',
        u'\N{Latin small letter kra}': 'k',#
        u'\N{Latin capital letter L with stroke}': 'L',
        u'\N{Latin small letter l with stroke}': 'l',
        u'\N{Latin capital letter Eng}': 'N', #
        u'\N{Latin small letter eng}': 'n', #
        u'\N{Latin capital ligature OE}': 'Oe',
        u'\N{Latin small ligature oe}': 'oe',
        u'\N{Latin capital letter T with stroke}': 'T', #
        u'\N{Latin small letter t with stroke}': 't',#
}

class LinguisticUtility():
    def remove_diacritics( self, text ):
        if not text:
            return text
        uni = None
        if isinstance(text, unicode):
            uni = text
        else :
            encoding=sys.getfilesystemencoding()
            uni =unicode(text, encoding, 'ignore')
        s = unicodedata.normalize('NFKD', uni)
        b=[]
        for ch in s:
            if  unicodedata.category(ch)!= 'Mn':
                if NON_DECOMPOSABLE_CHARACTERS.has_key(ch):
                    b.append(NON_DECOMPOSABLE_CHARACTERS[ch])
                elif ord(ch)<128:
                    b.append(ch)
                else:
                    b.append(' ')
        return ''.join(b)

