#********************************************************
#
#  Program:     Project 2 -- Functions
#
#  Author:      Caleb Myers
#  Email:       cm346613@ohio.edu
#
#  Description: This file contains several functions 
#               for various tasks. This file should be
#               imported to a program in order to use
#               these functions
#
#  Date:        Febuary 12, 2017
#
#********************************************************
vowls = ['a','e','i','o','u',    # used in translate function
         'A','E','I','O','U', 
         '.','?',';',':','"',
         '!','\n',' ']



#********************************************************
#
#  Function:   translate
#
#  Purpose:    translate a string into robbers language
#
#  Parameters: string - a string
#
#  Member/Global Variables: newStr - string used to hold
#                                    the translated string
#                                    that will be returned
#                           vowls - list of characters that
#                                   won't be changed by the
#                                   function
#
#  Preconditions:  string has a vaid value
#
#  Postconditions: string is translated to robbers language
#                  and returned
#                   
#
#  Calls:  range()
#          len()
#
#********************************************************
def translate(string):
    newStr = ''
    for it in range(0,len(string)):
        if string[it] in vowls:
            newStr += string[it]
        else:
            newStr += string[it] + 'o' + string[it]
    return newStr


#********************************************************
#
#  Function:   sum
#
#  Purpose:    returns the sum of a list of numbers
#
#  Parameters: nums - a list of numbers
#
#  Member/Global Variables: newNum - holds the sum of the
#                                    list
#
#  Preconditions: nums has a valid value
#
#  Postconditions: returns the sum of nums
#
#  Calls: none
#
#********************************************************
def sum(nums):
    newNum = 0
    for num in nums:
        newNum += num
    return newNum


#********************************************************
#
#  Function:   multiply
#
#  Purpose:    returns the product of a list of numbers
#
#  Parameters: nums - a list of numbers
#
#  Member/Global Variables: newNum - holds the product of
#                                    the list
#
#  Preconditions: nums has a valid value
#
#  Postconditions: returns the product of nums
#
#  Calls: none
#
#********************************************************
def multiply(nums):
    newNum = 1
    for num in nums:
        newNum *= num
    return newNum


#********************************************************
#
#  Function:   reverse
#
#  Purpose:    returns the reverse of a string
#
#  Parameters: string - a string
#
#  Member/Global Variables: ReversedString - holds reversed string
#
#  Preconditions: string has a valid value
#
#  Postconditions: returns the reverse of string
#
#  Calls: list()
#
#********************************************************
def reverse(string):
    string = list(string)
    ReversedString = ''
    for letter in string:
        ReversedString = letter + ReversedString
    return ReversedString


#********************************************************
#
#  Function:   is_palindrome
#
#  Purpose:    finds if a string is a palindrome
#
#  Parameters: string - a string
#
#  Member/Global Variables: stringReversed - reverse of 
#                                            string
#
#  Preconditions: string has a valid value
#
#  Postconditions: returns true if string is a palindrome,
#                  false if it isn't
#
#  Calls: lower()
#         reverse()
#
#********************************************************
def is_palindrome(string):
    string = string.lower()
    stringReversed = reverse(string)
    return (string == stringReversed)


#********************************************************
#
#  Function:   overlapping
#
#  Purpose:    see if a list shares at lease one common
#              element
#
#  Parameters: list1 - a list
#              list2 - a list
#
#  Member/Global Variables: none
#
#  Preconditions: list1 and list2 have valid values
#
#  Postconditions: returns true if the lists have at least
#                  one commmon element, fasle if not
#
#  Calls: none
#
#********************************************************
def overlapping(list1,list2):
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                return True
    return False


#********************************************************
#
#  Function:   histogram
#
#  Purpose:    outputs lines of *'s. Each lines length
#              is the number in a list of numbers sent
#              as a parameter
#
#  Parameters: nums - a list of numbers
#
#  Member/Global Variables: none
#
#  Preconditions: nums has a valid value
#
#  Postconditions: outputs a histogram, data gained from
#                  nums
#
#  Calls: print()
#
#********************************************************
def histogram(nums):
    for num in nums:
        print('*' * num)
        

#********************************************************
#
#  Function:   find_longest_word
#
#  Purpose:    returns the longest_word in a list of
#              words
#
#  Parameters: words - a list of words
#
#  Member/Global Variables: longestWord - holds longest
#                                         word in list
#
#  Preconditions: words has a valid value
#
#  Postconditions: returns the longest word from words
#
#  Calls: strip()
#         len()
#
#********************************************************
def find_longest_word(words):
    longestWord = ''
    for word in words:
        word = word.strip()
        if len(word) > len(longestWord):
            longestWord = word
    return longestWord



#********************************************************
#
#  Function:   filter_long_words
#
#  Purpose:    returns a list of words from a list of 
#              words that are longer than a nubmer n
#
#  Parameters: words - a list of words
#              size - an integer
#
#  Member/Global Variables: longWords - list of words
#
#  Preconditions: words and size have valid values
#
#  Postconditions: returns a list of the words in words
#                  that are longer than size
#
#  Calls: len()
#         insert()
#
#********************************************************
def filter_long_words(words, size):
    longWords = [];
    for word in words:
        if len(word) > size:
            longWords.insert(0,word)
    return longWords


#********************************************************
#
#  Function:   is_palindrome_sentence
#
#  Purpose:    see if a sentence is a palindrome sentence
#
#  Parameters: sentence - a string containing a sentence
#
#  Member/Global Variables: none
#
#  Preconditions: sentence has a valid value
#
#  Postconditions: returns true if sentence is a palindrome,
#                  false if not
#
#  Calls: strip()
#         replace()
#         lower()
#
#********************************************************
def is_palindrome_sentence(sentence):
    sentence = sentence.strip()
    sentence = sentence.replace(' ','')
    sentence = sentence.replace('.','')
    sentence = sentence.replace('?','')
    sentence = sentence.replace('!','')
    sentence = sentence.lower()
    return is_palindrome(sentence)


#********************************************************
#
#  Function:   is_pangram
#
#  Purpose:    see if a sentence is a pangram
#
#  Parameters: sentence - a string containing a sentence
#
#  Member/Global Variables: sentenceList - list of characters
#                                          in sentence
#                           sentenceLetters - list for letters
#                                             in sentence
#
#  Preconditions: sentence has a valid value
#
#  Postconditions: returns true if sentence is a pangram,
#                  false if not
#
#  Calls: list()
#         lower()
#         len()
#
#********************************************************
def is_pangram(sentence):
    sentence = sentence.lower()
    sentenceList = list(sentence)
    sentenceLetters = []
    for item in sentenceList:
        if item >= 'a' and item <= 'z' and item not in sentenceLetters:
            sentenceLetters.insert(0,item)
    return len(sentenceLetters) == 26
