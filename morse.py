morse_dict = {
	"а" : ".-",
	"б" : "-...",
	"в" : ".--",
	"г" : "--.",
	"д" : "-..",
	"е" : ".",
	"ж" : "...-",
	"з" : "--..", 
	"и" : "..",
	"й" : ".---",
	"к" : "-.-",
	"л" : ".-..",
	"м" : "--",
	"н" : "-.",
	"о" : "---",
	"п" : ".--.",
	"р" : ".-.",
	"с" : "...",
	"т" : "-",
	"у" : "..-",
	"ф" : "..-.",
	"х" : "....",
	"ц" : "-.-.",
	"ч" : "---.",
	"ш" : "----",
	"щ" : "--.-",
	"ъ" : "--.--",
	"ы" : "-.--",
	"ь" : "-..-",
	"э" : "..-..",
	"ю" : "..--",
	"я" : ".-.-",
	"" : ""
}

text = "ПриВет"

def morse_encode(text: str) -> str:
	text = text.lower()
	encoded_text = []
	for letter in text:
		encoded_text.append(morse_dict[letter])
	return " ".join(encoded_text)


text1 = ".-"
def morse_decode(text: str) -> str:

	#список значений
	morse_dict_values_list = list(morse_dict.values())

	#список ключей
	morse_dict_keys_list = list(morse_dict.keys())

	#индекс полученной буквы в списке значений
	index = morse_dict_values_list.index(text)
	
	result = morse_dict_keys_list[index]
	return result

morse_decode()
