# codecs
import numpy as np
class Codec():
    
    def __init__(self,delimiter = '#'):
        self.name = 'binary'
        self.delimiter = delimiter

    # convert text or numbers into binary form    
    def encode(self, text):
        if type(text) == str:
            return ''.join([format(ord(i), "08b") for i in text])
        else:
            print('Format error')
    

    # convert binary data into text takes in a string of binary and returns a string of english.
    def decode(self, data):
        binary = []        
        for i in range(0,len(data),8):
            byte = data[i: i+8]
            if byte == self.encode(self.delimiter):
                break
            binary.append(byte)
        text = ''
        for byte in binary:
            text += chr(int(byte,2))       
        return text 


class CaesarCypher(Codec):

    def __init__(self, shift=3):
        self.name = 'caesar'
        self.delimiter = '#'  
        self.shift = shift    
        self.chars = 256      # total number of characters
    # convert text into binary form
    # your code should be similar to the corresponding code used for Codec

    def encode(self, text):
        caesar_str = ''
        if type(text) == str:
            for i in text:
                caesar_num = (ord(i) + self.shift)%256
                caesar_str += ''.join(format(caesar_num, "08b"))
            return caesar_str
        else:
            print('Format error')
    
    # convert binary data into text
    # your code should be similar to the corresponding code used for Codec
    def decode(self, data):
        caesar_rev = ''
        output = 0
        binary = []        
        for i in range(0,len(data),8):
            byte = data[i: i+8]
            if byte == self.encode(self.delimiter):
                break
            binary.append(byte)
        text = ''
        for byte in binary:
            caesar_rev = (int(byte,2) - self.shift)%256
            text += chr(caesar_rev)
            # print('before')
            # print(text)
            # caesar_rev = (ord(str(text)) - self.shift)%256
            # print('modified')
            # print(caesar_rev)
        return text


        return text 
# a helper class used for class HuffmanCodes that implements a Huffman tree
class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.left = left
        self.right = right
        self.freq = freq
        self.symbol = symbol
        self.code = ''

if __name__ == '__main__':
    text = 'hello' 
    #text = 'Casino Royale 10:30 Order martini' 
    print('Original:', text)
    
    c = Codec()
    binary = c.encode(text + c.delimiter)
    print('Binary:', binary)
    data = c.decode(binary)
    print('Text:', data) 
    
    cc = CaesarCypher()
    binary = cc.encode(text + cc.delimiter)
    print('Binary:', binary)
    data = cc.decode(binary)
    print('Text:', data)
