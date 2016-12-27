from encrypt import DictionaryEncryption

stuff = DictionaryEncryption()
word = input('Enter what you want to encrypt: ')

key = DictionaryEncryption.encode(stuff, word)
print('The key is', key)

message = DictionaryEncryption.decode(stuff, key)
print('The message is', message)
