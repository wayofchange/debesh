'''Created in 2022 by Édrihan and Debesh'''

import eng_to_ipa as ipa # pip install eng_to_ipa
from epitran.backoff import Backoff # pip install epitran
'''and then see https://pypi.org/project/epitran/
$ tar xjf flite-2.0.5-current.tar.bz2
$ cd flite-2.0.5-current

or

$ git clone git@github.com:festvox/flite.git
$ cd flite/

then

$ ./configure && make
$ sudo make install
$ cd testsuite
$ make lex_lookup
$ sudo cp lex_lookup /usr/local/bin
'''

#TODO: finish shit. figure out how consonants without vowels work
# Use the same vowel again
# taken from https://en.wikipedia.org/wiki/Vai_syllabary
inputStr = ''' 	e	i	a	o	u	ɔ	ɛ
‑	ꔀ	ꔤ	ꕉ	ꕱ	ꖕ	ꖺ	ꗡ
‑̃	ꔁ	ꔥ	ꕊ	ꕲ	ꖖ	ꖻ	ꗢ
ŋ‑̃	 	ꕋ	 	ꖼ	ꗣ
h‑	ꔂ	ꔦ	ꕌ	ꕳ	ꖗ	ꖽ	ꗤ
h‑̃	 	ꔧ	ꕍ	 	ꖘ	ꖾ	ꗥ
w‑	ꔃ	ꔨ	ꕎ	ꕴ	ꖙ	ꖿ	ꗦ
w‑̃	ꔄ	ꔩ	ꕏ	ꕵ	ꖚ	ꗀ	ꗧ
p‑	ꔅ	ꔪ	ꕐ	ꕶ	ꖛ	ꗁ	ꗨ
b‑	ꔆ	ꔫ	ꕑ	ꕷ	ꖜ	ꗂ	ꗩ
ɓ‑	ꔇ	ꔬ	ꕒ	ꕸ	ꖝ	ꗃ	ꗪ
mɓ‑	ꔈ	ꔭ	ꕓ	ꕹ	ꖞ	ꗄ	ꗫ
kp‑	ꔉ	ꔮ	ꕔ	ꕺ	ꖟ	ꗅ	ꗬ
kp‑̃	 	ꕕ	 	ꗭ
mgb‑	ꔊ	ꔯ	ꕖ	ꕻ	ꖠ	ꗆ	ꗮ
gb‑	ꔋ	ꔰ	ꕗ	ꕼ	ꖡ	ꗇ	ꗯ
gb‑̃	 	ꗈ	ꗰ
f‑	ꔌ	ꔱ	ꕘ	ꕽ	ꖢ	ꗉ	ꗱ
v‑	ꔍ	ꔲ	ꕙ	ꕾ	ꖣ	ꗊ	ꗲ
t‑	ꔎ	ꔳ	ꕚ	ꕿ	ꖤ	ꗋ	ꗳ
θ‑	ꔏ	ꔴ	ꕛ	ꖀ	ꖥ	ꗌ	ꗴ
d‑	ꔐ	ꔵ	ꕜ	ꖁ	ꖦ	ꗍ	ꗵ
ð‑	ꔑ	ꔶ	ꕝ	ꖂ	ꖧ	ꗎ	ꗶ
l‑	ꔒ	ꔷ	ꕞ	ꖃ	ꖨ	ꗏ	ꗷ
r‑	ꔓ	ꔸ	ꕟ	ꖄ	ꖩ	ꗐ	ꗸ
ɗ‑	ꔔ	ꔹ	ꕠ	ꖅ	ꖪ	ꗑ	ꗹ
nɗ‑	ꔕ	ꔺ	ꕡ	ꖆ	ꖫ	ꗒ	ꗺ
s‑	ꔖ	ꔻ	ꕢ	ꖇ	ꖬ	ꗓ	ꗻ
ʃ‑	ꔗ	ꔼ	ꕣ	ꖈ	ꖭ	ꗔ	ꗼ
z‑	ꔘ	ꔽ	ꕤ	ꖉ	ꖮ	ꗕ	ꗽ
ʒ‑	ꔙ	ꔾ	ꕥ	ꖊ	ꖯ	ꗖ	ꗾ
tʃ‑	ꔚ	ꔿ	ꕦ	ꖋ	ꖰ	ꗗ	ꗿ
dʒ‑	ꔛ	ꕀ	ꕧ	ꖌ	ꖱ	ꗘ	ꘀ
ndʒ‑	ꔜ	ꕁ	ꕨ	ꖍ	ꖲ	ꗙ	ꘁ
j‑	ꔝ	ꕂ	ꕩ	ꖎ	ꖳ	ꗚ	ꘂ
k‑	ꔞ	ꕃ	ꕪ	ꖏ	ꖴ	ꗛ	ꘃ
k‑̃	 	ꕫ	 
ŋg‑	ꔟ	ꕄ	ꕬ	ꖐ	ꖵ	ꗜ	ꘄ
ŋg‑̃	 	ꘅ
g‑	ꔠ	ꕅ	ꕭ	ꖑ	ꖶ	ꗝ	ꘆ
g‑̃	 	ꘇ
m‑	ꔡ	ꕆ	ꕮ	ꖒ	ꖷ	ꗞ	ꘈ
n‑	ꔢ	ꕇ	ꕯ	ꖓ	ꖸ	ꗟ	ꘉ
ɲ‑	ꔣ	ꕈ	ꕰ	ꖔ	ꖹ	ꗠ	ꘊ'''
consonants = 'eiaouɔɛ-‑̃'
inputStr = inputStr.replace('\t',' ')
prefixToSuffixToVai = {}
for char in consonants:
    prefixToSuffixToVai[char] = {}
    
for l, line in enumerate(inputStr.split('\n')[1:]):
    consonantEndIdx = 1 + line.index('‑') if '‑' in line else line.index('‑̃')
    consonant = line[0:consonantEndIdx]
    vowelsStr = line[consonantEndIdx + 1:][::1]
    if vowelsStr[0] == ' ':
        vowelsStr = vowelsStr[1:]
    
        
    print('consonant is {} vowels are "{}"       Line#{} = {}'.format(consonant,vowelsStr,l,line))
    if len(vowelsStr) == len("ꔃ ꔨ ꕎ ꕴ ꖙ ꖿ ꗦ"):
        for c, char in enumerate(vowelsStr[::2]):
            realVowel = consonants[min(c,len(consonants)-1)]
            if not consonant in prefixToSuffixToVai.keys():
                prefixToSuffixToVai[consonant] = {}
            if not realVowel in prefixToSuffixToVai[consonant].keys():
                prefixToSuffixToVai[consonant][realVowel] = {}
            
            prefixToSuffixToVai[consonant][realVowel] = char
                
            print('\t\t{} {} {}'.format(c,realVowel,char))
print('-----\n'*5)
for k in prefixToSuffixToVai.keys():
    print(k,prefixToSuffixToVai[k])
print(prefixToSuffixToVai)


def syllableToVai(latin:str) -> str:
    result = ''
    assert len(latin) <= 2, 'we do one syllable with this functyion'
    
    prefix = latin[0]
    suffix = latin[1]
    #print(prefix,suffix)
    #input()
    if (prefix + '‑') in prefixToSuffixToVai.keys():
        return prefixToSuffixToVai[(prefix + '‑')][suffix]
    elif (prefix + '‑̃') in prefixToSuffixToVai.keys():
        return prefixToSuffixToVai[prefix + '‑̃'][suffix]
    else:
            
    
        raise ValueError('it didnt work with poop: {} prefix: {} suffix {} \nvalid keys are {}'.format(latin,prefix,suffix,prefixToSuffixToVai.keys() ))
        
def latinToVai(latin:str,retrieve_all=False)->str:
    
    #TODO: if not found use epitran
    '''
    >>> import epitran
    >>> epi = epitran.Epitran('eng-Latn')
    >>> print epi.transliterate(u'Berkeley')
    bɹ̩kli'''
    
    isos = ipa.convert(latin, retrieve_all=retrieve_all)
    
    
    if retrieve_all == False:
        isos = [isos]
        
    input("{} {} \nconsonants: {}".format(latin,isos,prefixToSuffixToVai.keys()))
    vai = ''
    for c in range(len(latin),2):
        try:
            vai += syllableToVai(latin[c:c+2])
        except:
            vai += 'N/A!! '
    return vai
testStr = 'sa'
print('testing',testStr,syllableToVai(testStr))
for a in range(12):
    userStr = input('Enter a latin to translate: ')
    print(userStr,'in Vai is "{}"'.format(latinToVai(userStr)))
