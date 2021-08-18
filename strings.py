#String is the combination of the characters

message='Hello world'
print(message)

message1="Hello buddy's"
print(message1)


message2='Hello buddy\'s'
print(message2[::-1])


message3='"This" is important'
print(message3)


paragraph="""Hello world and guys How are you doing
All good?"""
print(paragraph)

#Length of the message
print("The length of the message is",len(message))

#Indexing, #Slicing
print(message[0])#First character in a string
print(message[10])#Last character in a string
print(message[0:5])#First word character in a string, #First inclusive, Second is #Exclusive. Upto and not including 5th
print(message[:5])#First word character in a string, #First inclusive, Second is #Exclusive. Upto and not including 5th
print(message[6:])

#Methods
print(message.lower())
print(message.count('Hello'))
print(message.count('l'))
print(message.find('world'))#Gives the start of the string
print(message.find('universe'))# Response: -1 because universe does not exist in the message
print(message.find('world'))
message.replace('world','Universe')#Gives the start of the string 
print(message)#Gives the start of the string. Because it does not replace in place
new_message=message.replace('world','Universe')
print(new_message)

greeting='Hello'
name='Mari'
message=greeting+name
print(message) #May not be best way as there is no whitespace
message=greeting+', '+name
print(message)


message='{} {},Welcome'.format(greeting,name)
print(message)

#fstring
message=f'{greeting},{name},welcome'
print(message)

#we can use/apply methods within the placeholders
message=f'{greeting},{name.upper()},welcome'
print(message)

print(dir(message))
print(message.isupper())

"""['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 
'zfill']
"""
print(help(str.lower))

#enumerate(string)