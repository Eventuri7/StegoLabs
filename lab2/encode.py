import numpy as np
import types

def messageToBinary(message):
  if type(message) == str:
    return ''.join([ format(ord(i), "08b") for i in message ])
  elif type(message) == bytes or type(message) == np.ndarray:
    return [ format(i, "08b") for i in message ]
  elif type(message) == int or type(message) == np.uint8:
    return format(message, "08b")
  else:
    raise TypeError("Input type not supported")

def hideMessage(text_container, secret_message):

	ukrLet = "асеіорхАВСЕНІКОРТХ"
	engLet = "aceiopxABCEHIKOPTX"

	i = 0
	letter = ''
	encoded_message = ''

	binSecret = messageToBinary(secret_message)
	print(binSecret)

	if len(binSecret) > len(text_container):
		raise Exception("Your text container is too small for this message!")

	for char in text_container:
		if char in ukrLet:
			if i < len(binSecret):
				if str(binSecret[i]) == "1":
					index = ukrLet.index(char)
					letter = str(engLet[index])
				elif str(binSecret[i]) == "0":
					letter = char
				
				i += 1

			else:
				letter = char
		else:
			letter = char
		
		encoded_message += letter

	return encoded_message

def encode():
	file_name = input("Enter text-file name (example.txt): ")
	f = open(file_name, "r" , encoding='utf-8')
	text_container = f.read()
	f.close()	

	data = input("Enter your message to hide: ")

	if len(data) == 0:
		raise ValueError('Data is empty!')

	encoded_message = hideMessage(text_container, data)
	print(encoded_message)

	encoded_file_name = input("Enter the name of new encoded text (example.txt): ")
	result = open(encoded_file_name, "w", encoding='utf-8')
	result.write(encoded_message)
	result.close()



