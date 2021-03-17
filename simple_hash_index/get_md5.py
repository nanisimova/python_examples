import hashlib

text = "tpxmuwr@somehost.ru"

print(hashlib.md5(text.encode()).hexdigest())

#print(hashlib.md5(text.encode()).hexdigest() )
#print(hashlib.sha1(text.encode()).hexdigest() )
#print(hashlib.sha224(text.encode()).hexdigest() )


