import re


def remove_emoji(string):
#essa função remove os emojis e caracteres especiais de uma string via seu codigo unicode
    emoji_pattern = re.compile("["
                            u"\U0001F600-\U0001F64F"  # emoticons
                            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                            u"\U0001F680-\U0001F6FF"  # transport & map symbols
                            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            u"\U00002500-\U00002BEF"  # chinese char
                            u"\U00002702-\U000027B0"
                            u"\U00002702-\U000027B0"
                            u"\U000024C2-\U0001F251"
                            u"\U0001f926-\U0001f937"
                            u"\U00010000-\U0010ffff"
                            u"\u2640-\u2642"
                            u"\u2600-\u2B55"
                            u"\u200d"
                            u"\u23cf"
                            u"\u23e9"
                            u"\u231a"
                            u"\ufe0f"  # dingbats
                            u"\u3030"
                            u'\u0142'
                            u'\u20e3'
                            u'\u203c'
                            u'\u02da'
                            u'\u039f'
                            u'\u21c0'
                            u'\u0336'
                            u'\u015b'
                            u'\u2192'
                            u'\u2234'
                            u'\u2070'
                            u'\u208d'
                            u'\u208e'
                            u'\u2206'
                            u'\u0302'
                            u'\u2066'
                            u'\u2077'
                            u'\u141f'
                            u'\u10e7'
                            u'\u2069'
                            u'\u203f'
                            u'\u22c6'
                            u'\u2049'
                            u'\u2139'
                            u'\u0137'
                            u'\u0113'
                            u'\u23ef'
                            u'\u23f0'
                            u'\u1dbb'
                            u'\u013a'
                            u'\u221a'
                            u'\u0a82'
                            u'\u2307'
                            u'\u2022'  
                            u'\u2212'  
                            u'\u2303'  
                            u'\u2264'
                            u'&lt;3'
                            u'&lt;/?[a-z]+&gt;'  # <tag>
                            "]+", flags=re.UNICODE)
    clean_string = emoji_pattern.sub('', string)
    cleaned_string = clean_string.replace("&lt;3", "<").replace("-&gt", ">").replace("&gt;PORRA&lt;",">PORRA<").replace("&amp","&").replace("&gt;&gt;&gt;&gt;","").replace("&gt;wandinha&lt;","")
    return cleaned_string
