import json
import os

class Localization:
    def __init__(self, language='english'):
        """
        Initialize the Localization class with the chosen language.
        Default language is 'english'.
        """
        self.language = language
        self.language_data = self.load_language_data()

    def load_language_data(self):
        """
        Load the language data from a JSON file based on the selected language.
        If the language is not found, default to English.
        """
        language_file = f"C:/pr/Free_Knowledge_Perfection/language/{self.language}.json"

        if os.path.exists(language_file):
            with open(language_file, 'r', encoding='utf-8') as file:
                return json.load(file)
        else:
            print(f"Language file for '{self.language}' not found. Defaulting to English.")
            # Fallback to English if the selected language file does not exist
            return self.load_default_language_data()

    def load_default_language_data(self):
        """
        Load the default English language file if the specified one is not found.
        """
        english_file = "C:/pr/Free_Knowledge_Perfection/language/english.json"
        
        with open(english_file, 'r', encoding='utf-8') as file:
            return json.load(file)

    def get_message(self, category, key, **kwargs):
        """
        Retrieve a message from the language data based on category and key.
        You can also pass additional keyword arguments to format the message.
        """
        try:
            message = self.language_data[category][key]
            if kwargs:
                message = message.format(**kwargs)
            return message
        except KeyError:
            print(f"Warning: Key '{key}' not found in category '{category}'. Returning empty string.")
            return ""
    
    def change_language(self, new_language):
        """
        Change the language and reload the data.
        """
        self.language = new_language
        self.language_data = self.load_language_data()

# Example Usage
if __name__ == "__main__":
    # Initialize localization with English language by default
    localization = Localization(language='english')
    
    # Example of getting a greeting message
    greeting_message = localization.get_message('greetings', 'welcome')
    print(greeting_message)  # Output: "Welcome, how can I assist you today?"

    # Example of getting an emotion-related message with a dynamic part
    emotion_message = localization.get_message('emotions', 'happy')
    print(emotion_message)  # Output: "Your happiness helps in making better decisions."

    # Change to Arabic language
    localization.change_language('arabic')
    
    # Get a greeting message in Arabic
    arabic_greeting = localization.get_message('greetings', 'welcome')
    print(arabic_greeting)  # Output: "مرحبًا، كيف يمكنني مساعدتك اليوم؟"
