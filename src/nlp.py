

import re
import string

### functions used in final model

def remove_space(text):
    """
    remove extra spaces and ending space if any
    """
    # remove extra spaces
    text = re.sub('\s+', ' ', text)
    # condense empty string with spaces+ to empty string
    text = re.sub('\s+$', '', text)
    text = re.sub('\u200b', ' ', text)

    return text


regular_punct = list(string.punctuation)
extra_punct = [
        ',', '.', '"', ':', ')', '(', '!', '?', '|', ';', "'", '$', '&',
        '/', '[', ']', '>', '%', '=', '#', '*', '+', '\\', '•',  '~', '@', '£',
        '·', '_', '{', '}', '©', '^', '®', '`',  '<', '→', '°', '€', '™', '›',
        '♥', '←', '×', '§', '″', '′', 'Â', '█', '½', 'à', '…', '“', '★', '”',
        '–', '●', 'â', '►', '−', '¢', '²', '¬', '░', '¶', '↑', '±', '¿', '▾',
        '═', '¦', '║', '―', '¥', '▓', '—', '‹', '─', '▒', '：', '¼', '⊕', '▼',
        '▪', '†', '■', '’', '▀', '¨', '▄', '♫', '☆', 'é', '¯', '♦', '¤', '▲',
        'è', '¸', '¾', 'Ã', '⋅', '‘', '∞', '∙', '）', '↓', '、', '│', '（', '»',
        '，', '♪', '╩', '╚', '³', '・', '╦', '╣', '╔', '╗', '▬', '❤', 'ï', 'Ø',
        '¹', '≤', '‡', '√', '«', '»', '´', 'º', '¾', '¡', '§', '£', '₤']

all_punct = list(set(regular_punct + extra_punct))

def spacing_punctuation(text):
    """
    add space before and after punctuation and symbols
    """
    for punc in all_punct:
        if punc in text:
            text = text.replace(punc, f" {punc} ")

    return text




def clean_misspell(text):
    """
    misspell list (quora vs. glove)
    """

    mispell_dict = {'demonitisation': 'demonetization', 'demonitization': 'demonetization',
                    'demonetisation': 'demonetization',
                    'pokémon': 'pokemon',
                    'Wjy': 'Why',
                    'Whst' : 'What',
                    'BNBR': 'Be Nice, Be Respectful',
                    'Bolsonaro': 'Jair Bolsonaro',
                    'XXXTentacion': 'Tentacion',
                    'Žižek': 'Slovenian philosopher Slavoj Žižek',
                    'Adityanath': 'Indian monk Yogi Adityanath',
                    'Brexit': 'British Exit',
                    'Brexiter': 'British Exit supporter',
                    'Brexiters': 'British Exit supporters',
                    'Brexiteer': 'British Exit supporter',
                    'Brexiteers': 'British Exit supporters',
                    'Brexiting': 'British Exit',
                    'Brexitosis': 'British Exit disorder',
                    'brexit': 'British Exit',
                    'brexiters': 'British Exit supporters',
                    'cryptocurrencies': 'cryptocurrency',
                    'Cryptocurrency': 'cryptocurrency',
                    'Litecoin' : 'cryptocurrency',
                    'litecoin' : 'cryptocurrency',
                    'altcoin' : 'cryptocurrency',
                    'altcoins' : 'cryptocurrency',
                    'jallikattu': 'Jallikattu',
                    'Swachh': 'Swachh Bharat mission campaign ',
                    'SJWs': 'social justice warrior',
                    'Quorans': 'Quoran',
                    'Qoura ': 'Quora ',
                    'quoras': 'Quora',
                    'Quroa': 'Quora',
                    'QUORA': 'Quora',
                    'Qoura': 'Quora',
                    'narcissit': 'narcissist',
                    'ethereum': 'Ethereum',
                    'Blockchain': 'blockchain',
                    'UCEED': 'Undergraduate Common Entrance Examination for Design',
                    'GDPR': 'General Data Protection Regulation',
                    'Redmi' : 'Xiaomi smartphone',
                    'OnePlus': 'Android smartphone',
                    'Machedo' : 'hot guy',
                    'Coinbase':'bitcoin broker',
                    'coinbase':'bitcoin broker',
                    'DCEU' : 'American media franchise',
                    'IIEST': 'Indian Institutes of Engineering Science and Technology',
                    'Upwork' : 'global freelancing platform',
                    'upwork' : 'global freelancing platform',
                    'HackerRank' : 'technology company focuses on competitive programming challenges',
                    'pokémon': 'pokemon'}

    misspell_re = re.compile('(%s)' % '|'.join(mispell_dict.keys()))

    def _replace(match):
        """
        reference: https://www.kaggle.com/hengzheng/attention-capsule-why-not-both-lb-0-694 # noqa
        """
        try:
            word = mispell_dict.get(match.group(0))
        except KeyError:
            word = match.group(0)
            print('!!Error: Could Not Find Key: {}'.format(word))
        return word
    return misspell_re.sub(_replace, text)


### addtional functions

def decontracted(text):
    """
    de-contract the contraction
    """
    # specific
    text = re.sub(r"(W|w)on(\'|\’)t", "will not", text)
    text = re.sub(r"(C|c)an(\'|\’)t", "can not", text)
    text = re.sub(r"(Y|y)(\'|\’)all", "you all", text)
    text = re.sub(r"(Y|y)a(\'|\’)ll", "you all", text)

    # general
    text = re.sub(r"(I|i)(\'|\’)m", "i am", text)
    text = re.sub(r"(A|a)in(\'|\’)t", "is not", text)
    text = re.sub(r"n(\'|\’)t", " not", text)
    text = re.sub(r"(\'|\’)re", " are", text)
    text = re.sub(r"(\'|\’)s", " is", text)
    text = re.sub(r"(\'|\’)d", " would", text)
    text = re.sub(r"(\'|\’)ll", " will", text)
    text = re.sub(r"(\'|\’)t", " not", text)
    text = re.sub(r"(\'|\’)ve", " have", text)
    return text

def remove_newline(text):
    """
    remove \n and  \t
    """
    text = re.sub('\n', ' ', text)
    text = re.sub('\t', ' ', text)
    text = re.sub('\b', ' ', text)
    text = re.sub('\r', ' ', text)
    return text


### preprocess function

def preprocess(text):
    """
    preprocess text main steps

    NOTE:
        1. glove supports uppper case words
        2. glove supports digit
        3. glove supports punctuation
        5. glove supports domains e.g. www.apple.com
        6. glove supports misspelled words e.g. FUCKKK
    """

    """
        1. paragram does NOT support uppper case words
            (all lower case)
        2. paragram supports digit
        3. paragram supports punctuation and special punctuation
        4. paragram supports domains e.g. www.apple.com
        5. paragram supports misspelled word e.g. travelling, organisation

    """

    """

       preprocess text into clean text for tokenization
    NOTE:
        1. fasttext supports uppper case words
        2. fasttext supports digit
        3. fasttext supports ONLY some punctuation
        4. fasttext does NOT supports domains e.g. www.apple.com
        5. fasttext does NOT supports misspelled word e.g. travelling, organisation
            (unclear it supports misspelled words)
    """

    #text = normalize_unicode(text)
    text = clean_misspell(text)
    text = spacing_punctuation(text)
    text = remove_space(text)

#     if remove_num:
#         text = remove_number(text)
#     else:
#         text = spacing_digit(text)

    return text
