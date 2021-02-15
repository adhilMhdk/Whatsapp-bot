from googletrans import Translator
translator = Translator()

def convertToMalayalam(words):
    translation = translator.translate(words, dest='ml')
    return str(translation.text)
