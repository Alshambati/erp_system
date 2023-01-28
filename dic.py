import codecs
import string

from typing import Tuple

# prepare map from numbers to letters
_encode_table = {'ا':'a','ب':'b','ت':'t','ث':'T','ج':'g','ح':'h','خ':'H','د':'d','ذ':'z','ر':'r','ز':'Z','س':'s','ش':'S','ص':'u','ض':'v','ط':'q','ظ':'w','ع':'P','غ':'j','ف':'f','ق':'x','ك':'k','ل':'l','م':'m','ن':'J','ه':'p','و':'F','ي':'y','ى':'Y','أ':'A','ؤ':'O','ة':'L'}
# prepare inverse map
_decode_table = {v: k for k, v in _encode_table.items()}
_decode_table[',']='               '
_decode_table[';']=' ;  '
_decode_table['/']=''


def custom_encode(text: str) -> str:
    # example encoder that converts ints to letters
    # see https://docs.python.org/3/library/codecs.html#codecs.Codec.encode
    textt=''
    u=0
    for x in text:
       if x in _encode_table:
           textt=textt+''.join(_encode_table[x])
           u=1
       else:
           textt=textt+''+x
    if u==1:
        textt=textt+"/"
    return textt


def custom_decode(binary: str) -> str:
    # example decoder that converts letters to ints
    # see https://docs.python.org/3/library/codecs.html#codecs.Codec.decode
    #return ''.join(_decode_table[x] for x in binary),''
    textemp=''
    if len(binary)==0:
        return binary

    if binary[len(binary)-1]!='/':
        if binary[len(binary) - 1] != ',' and binary[len(binary) - 2] != '/':
           return binary

    for x in binary:
       if x in _decode_table:
           textemp=textemp+''.join(_decode_table[x])
       else:
           textemp=textemp+''+x
    return textemp





"""def main():

    # register your custom codec
    # note that CodecInfo.name is used later


    binary = ""
    # decode letters to numbers
    a=custom_encode(binary)
    # encode numbers to letters
    p=custom_decode(a)
    print(a,p)

    # encode(decode(...)) should be an identity function
    #print(binary , binary2)"""


