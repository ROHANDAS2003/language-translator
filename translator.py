# translator.py

from deep_translator import GoogleTranslator
from langdetect import detect_langs
from language_mapping import LANGUAGE_MAPPING

def translate(text, target_language):
    """
    Translate text to target_language using deep-translator module.
    """
    translator = GoogleTranslator(source='auto', target=target_language)
    translated_text = translator.translate(text)
    return translated_text

def detect_language(text):
    """
    Detect the language of the text.
    """
    detected_langs = detect_langs(text)
    # Return the language code of the most probable language
    return detected_langs[0].lang

def main():
    # Main function to interact with the user
    print("Welcome to the Language Translator!")
    # Prompt the user for input text
    text = input("Enter the text you want to translate: ")
    
    # Detect the source language of the text
    source_language = detect_language(text)
    print(f"Detected source language: {source_language}")
    
    # Prompt the user for the target language
    target_language_name = input("Enter the target language: ").lower()
    # Convert target_language_name to language code using LANGUAGE_MAPPING
    target_language = LANGUAGE_MAPPING.get(target_language_name)
    if not target_language:
        print("Invalid target language!")
        return
    
    # Call the translate function and display the result
    translation = translate(text, target_language)
    print(f"Translation to {target_language}: {translation}")

if __name__ == "__main__":
    main()
