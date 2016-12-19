#!/apps/RH6U4/python/2.7.11/bin/python
# Biological services nodes info by Kirill Kogan June 2016

import os

lsload = 'lsload '
bhosts = 'bhosts -l '
sort1 = '|head -n +3'
sort2 = '| sed \'1d\' | head -n +2'
mylist = list(range(280,300))
mylist.remove(286)
for word in mylist:
    word = "cn"+str(word)
    print (100 * '-')
    os.system(lsload + word + sort1)
    os.system(bhosts + word + sort2)
#   print(100 * '-')
