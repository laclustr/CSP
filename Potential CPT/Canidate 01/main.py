from gtts import gTTS
import os
import deepl

api_key = open("api.key", "r").read()
translator = deepl.Translator(api_key)

langs = [["AR", "BG", "CS", "DA", "DE", "EL", "ES", "ET", "FI", "FR", "HU", "ID", "IT", "JA", "KO", "LT", "LV", "NB", "NL", "PL", "PT", "RO", "RU", "SK", "SL", "SV", "TR", "UK", "ZH"], ["Arabic", "Bulgarian", "Czech", "Danish", "German", "Greek", "Spanish", "Estonian", "Finnish", "French", "Hungarian", "Indonesian", "Italian", "Japanese", "Korean", "Lithuanian", "Latvian", "Norwegian", "Dutch", "Polish", "Portuguese", "Romanian", "Russian", "Slovak", "Slovenian", "Swedish", "Turkish", "Ukrainian", "Chinese"]]

for i in range(len(langs[0])):
	print(f"{i + 1}. {langs[1][i]}")

for _ in range(int(input("\nNumber of translations: "))):
	sel_lang = langs[0][int(input("\nSelect a language: ")) - 1]

	Text_to_be_translated = input("\nEnter text to be translated: ")

	read_aloud = True if input("\nRead Aloud (y/n): ").lower() in ("y", "yes") else False
	play_slow = False
	if read_aloud:
		play_slow = True if input("\nPlay sound slowly (y/n): ").lower() in ("y", "yes") else False

	translation = translator.translate_text(Text_to_be_translated, target_lang = sel_lang)

	print(f"\nTranslated Text: {translation.text}")

	if read_aloud:
		tts = gTTS(text = translation.text, lang = sel_lang.lower(), slow = play_slow)

		tts.save("output.mp3")

		os.system("afplay output.mp3")

		read_aloud = False