#match
"""import re
a = "my name is Tarun, my age is 26"
b = re.match("my",a)
print(b)

#search
import re
a = "my name is Tarun, my age is 26"
b = re.search("is",a)
print(b)

#findall
import re
a = "my name is Tarun, my age is 26"
b = re.findall("is",a)
print(b)

#split
import re
a = "my name is Tarun, my age is 26"
b = re.split("my",a)
print(b)

#sub
import re
a = "my name is Tarun, my age is 26"
b = re.sub("Tarun","Kolli",a)
print(b)"""

'''import re
a = "my name is Tarun, my age is 26"
b = re.sub("[ .,]","#",a)
print(b)'''


'''import re
a = "my age is 26, my roll no is 06"
b = re.findall("\d+",a)
print(b)
for i in b:
    print(i)'''


'''import re
a = "my name is Tarun, my age is 26"
b = re.sub("[aeiouAEIOU]","",a)
print(b)'''


'''import re
a = "my name is nagendra, my age is 26"
b = re.findall(r"\bna\w+ra",a)
print(b)'''

import re
a = "my name is Tarun, my age is 26"
b = re.findall("26$",a)
print(b)