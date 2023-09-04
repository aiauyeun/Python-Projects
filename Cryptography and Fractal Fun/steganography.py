# steganography
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from math import ceil
from codec import Codec, CaesarCypher
class Steganography():
    
    def __init__(self):
        self.text = ''
        self.binary = ''
        self.delimiter = '#'
        self.codec = None
        self.c_shift = None
    
    #takes in a string of binary numbers and an image bitmap and modifies the rgb values of the image bitmap to encode the given binary message
    def msg_glue(self,binary,image):
        bin_lst = []
        i = 0
        j = 0
        k = 0
        for number in binary:
            bin_lst.append(number)
            
        for val in bin_lst:
            if int(val) == 1:
                if image[i][j][k] % 2 == 1:
                    k += 1
                else:
                    image[i][j][k] += 1
                    k += 1
            else:
                if image[i][j][k] % 2 == 0:
                    k += 1
                else:
                    image[i][j][k] += 1
                    k += 1
                
            if k == len(image[i][j]):
                j += 1 
                k = 0
            if j == len(image[i]):
                i += 1
                j = 0
                k = 0
        return image

    #takes in a modified image bitmap and looks for and returns any binary message it finds and only stops once it finds the delimiter.
    def bit_reader(self,image,codec):
        bit_lst = []
        gumbo = 'wheee'
        for array in image:
            for cell in array:
                for val in cell:
                    bit_lst.append(val)
        i = 0
        j = 0
        k = 0
        ayet_lst = []
        delum = ''
        binary = ''
        for value in bit_lst: 
            if len(ayet_lst) == 8:
                for num in ayet_lst:
                    delum += str(num)
                ayet_lst = []
                if codec == 'binary':
                    c_num = (ord(self.delimiter))
                    if delum == format(c_num,'08b'):
                        return binary
                if codec == 'caesar':
                    c_num = (ord(self.delimiter) + self.codec.shift)
                    if delum == format(c_num,'08b'):
                        return binary
                delum = ''
            if int(value) % 2 == 1:
                binary += '1'
                ayet_lst.append('1')
            else:
                binary += '0'
                ayet_lst.append('0')
        return gumbo

    def encode(self, filein, fileout, message, codec):
        image = cv2.imread(filein)      
        # calculate available bytes
        max_bytes = image.shape[0] * image.shape[1] * 3 // 8
        print("Maximum bytes available:", max_bytes)
        # convert into binary
        if codec == 'binary':
            self.codec = Codec(delimiter = self.delimiter) 
            binary = self.codec.encode(message + self.delimiter)
        elif codec == 'caesar':
            self.codec = CaesarCypher()
            binary = self.codec.encode(message + self.delimiter)
        
        # check if possible to encode the message
        num_bytes = ceil(len(binary)//8) + 1 
        if  num_bytes > max_bytes:
            print("Error: Insufficient bytes!")
        else:
            print("Bytes to encode:", num_bytes) 
            self.text = message
            self.binary = binary
            #msg_glue will be built to encode the binary message into the image.
            image = self.msg_glue(binary,image)
            # print('Modified image from encode')
            # print(image)
            # your code goes here
            # you may create an additional method that modifies the image array
            cv2.imwrite(fileout,image)
        
         
    def decode(self, filein, codec):
        image = cv2.imread(filein)  
        print(image) # for debugging      
        flag = True
        # convert into text
        if codec == 'binary':
            self.codec = Codec(delimiter = self.delimiter) 
        elif codec == 'caesar':
            self.codec = CaesarCypher()
        elif codec == 'huffman':
            if self.codec == None or self.codec.name != 'huffman':
                print("A Huffman tree is not set!")
                flag = False
        if flag:
            binary = self.bit_reader(image,codec)
            self.binary = binary
            self.text = self.codec.decode(binary)
            return self.text
      
    #when called    
    def print(self):
        if self.text == '':
            print("The message is not set.")
        else:
            print("Text message:", self.text)
            print("Binary message:", self.binary)          
    def show(self, filename):
        plt.imshow(mpimg.imread(filename))
        plt.show()