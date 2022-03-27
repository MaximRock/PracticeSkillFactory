import re
import string

# photo = 'images/cat_matras.jpg'
# pattern = r'.\b([A-Z,a-z]{3,})\b'
# f = ''.join(re.findall(pattern, photo)).lower()
# lst = ['jpg', 'jpeg', 'png']
#
#
# if f in lst:
#     print('верный формат фото -', f)
# else:
#     print('неверный формат фото -', f)
#

str = '35'
print(str.isdigit())

def strng(word):
 s = ".,:;!_*-+()/#%&"
 for char in s:
   if char in word:
        print("The character " +  char + " is in the word.")
   else: pass

strng("Boost!")




#
# j = 'JPG'
# if j == f:
#     print('Верно')
# else:


# lst = ['JPG', 'JPEG', 'PNG']
#
# for i in lst:
#     if i != f:
#         print('неверный формат фото -',* f)
#     else:
#         print('верный формат фото -', *f)

