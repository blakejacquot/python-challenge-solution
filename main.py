print('Hello World')

# 0
print('Problem 0')
var = 2 ** 38
print(var)
print(' ')

# 1 http://www.pythonchallenge.com/pc/def/map.html
# appears to be an ASCII problem
print('Problem 1: solution 1')
string_to_decode = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
decoded_string = ""
for char in string_to_decode:
    dec_val = ord(char)
    if char == ' ': # don't change a space
        pass
    elif char == '.': #don't change a period
        pass
    elif char == 'y': # this is a 'y' and we need to wrap to 'a'
        dec_val = ord('a')
    elif char == 'z': # this is a 'z' and we need to wrap to 'b'
        dec_val = ord('b')
    else:
        dec_val = dec_val + 2
    char_new = chr(dec_val)
    decoded_string += char_new
print decoded_string
print(' ')

print('Problem 1: solution 2')
from string import maketrans
string_to_decode = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
intab = "abcdefghijklmnopqrstuvwxyz"
outtab = "cdefghijklmnopqrstuvwxyzab"
trantab = maketrans(intab, outtab)
print string_to_decode.translate(trantab)
url = "http://www.pythonchallenge.com/pc/def/map.html"
print(url.translate(trantab))

# 2 http://www.pythonchallenge.com/pc/def/ocr.html
print('Problem 2: solutionefrrwrefiuosdfjlsoid cmdnd      c c c 1325476980tth 7ygvjkn nnnhsldfoliodjiuuyt,,,casdsd[dd[dpdpfp[fa'8U7HJK'' \8 5  L;
                                                                                                                                      'O' \HU
                                                                                                                                      'PPQKJSJSKJDF,.M,≥')JKO8,