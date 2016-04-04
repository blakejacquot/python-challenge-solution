print('Hello World')

# 0
print('Problem 0')
var = 2 ** 38
print(var)
print(' ')

# 1 http://www.pythonchallenge.com/pc/def/map.html
# appears to be an ASCII problem
print('Problem 1: solution 1')
string_to_decode = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq " \
                   "ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw " \
                   "rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. " \
                   "lmu ynnjw ml rfc spj."
decoded_string = ""
for char in string_to_decode:
    dec_val = ord(char)
    if char == ' ':  # don't change a space
        pass
    elif char == '.':  # don't change a period
        pass
    elif char == 'y':  # this is a 'y' and we need to wrap to 'a'
        dec_val = ord('a')
    elif char == 'z':  # this is a 'z' and we need to wrap to 'b'
        dec_val = ord('b')
    else:
        dec_val = dec_val + 2
    char_new = chr(dec_val)
    decoded_string += char_new
print decoded_string
print(' ')

print('Problem 1: second solution')
from string import maketrans

string_to_decode = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq " \
                   "ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw " \
                   "rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb." \
                   " lmu ynnjw ml rfc spj."
intab = "abcdefghijklmnopqrstuvwxyz"
outtab = "cdefghijklmnopqrstuvwxyzab"
trantab = maketrans(intab, outtab)
print string_to_decode.translate(trantab)
url = "http://www.pythonchallenge.com/pc/def/map.html"
print(url.translate(trantab))
# 1 solution url =  http://www.pythonchallenge.com/pcc/def/ocr.html

# 2 http://www.pythonchallenge.com/pc/def/ocr.html
print(' ')
print('Problem 2: my original solution')
import collections
import urllib2
this_url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
response = urllib2.urlopen(this_url)
contents = response.read()
mess_below = contents[835:] #search the mess below for rare characters
mess_below = contents
character_frequency = collections.Counter(mess_below)
print('Frequency of all characters = ', character_frequency)
print('Search for low-frequency characters')
low_frequency_chars = []
for item in character_frequency:
    # 1000 is empirically determined as threshold
    # characters[item] is the frequency of the character
    if character_frequency[item] < 1000:
        #print(item,character_frequency[item])
        low_frequency_chars.append(item)
print('The low-frequency characters are = ', low_frequency_chars)
decoded_string = ""
for char in contents:
    if char in low_frequency_chars:
        decoded_string += (char)
print(decoded_string)
print('Problem 2: better solution after reading known solutions')
freq_dict = {}
decoded_string = ""
for char in mess_below:
    if freq_dict.has_key(char):
        pass
    else:
        freq_dict[char] = mess_below.count(char)
        if freq_dict[char] < 1000:
            print(char)
            decoded_string += char
print(freq_dict)
print(decoded_string)



# 2 solution url = http://www.pythonchallenge.com/pcc/def/equality.html

#3 http://www.pythonchallenge.com/pc/def/equality.html
print(' ')
print('Problem 3: solution')