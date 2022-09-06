
# line=0
# word=0
# wordcount=0
# str1="is"
# with open("D:\\test.txt") as file:
#     for i in file:
#         line=line+1
#         words = i.split()
#         word = word+len(words)
#         for w in words:
#             if w==str1:
#                 wordcount+=1
#
#
# print("Number of Line in file:",line)
# print("Number of word in file:",word)
# print("Number of word in file(is):",wordcount)

import re
# p = re.compile(ur'<a\b[^>]*>.*?</a>|((ftp|http|https):\/\/(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?)', re.MULTILINE)
# test_str = u"I was surfing http://www.google.com, where I found my tweet, check it out <a href=\"http://tinyurl.com/blah\">http://tinyurl.com/blah</a>"
#
# for item in re.finditer(p, test_str):
#     print item.group(0)

prohibitedWords = ["MVGame","Kappa","DatSheffy","DansGame","BrainSlug","SwiftRage","Kreygasm","ArsonNoSexy","GingerPower","Poooound","TooSpicy"]


# word[1] contains the user entered message
word="This is india MVGame and my country is DansGame "
themessage = str(word[1])
# would like to implement a foreach loop here but not sure how to do it in python
for themessage in prohibitedWords:
    themessage =  re.sub(prohibitedWords, "(I'm an idiot)", themessage)

print(themessage)