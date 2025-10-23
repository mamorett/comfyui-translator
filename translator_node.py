import translators as ts

class TranslatorNode:
    """
    A ComfyUI node that translates text using various translation engines
    """
    
    # List of available translators from the translators library
    TRANSLATORS = [
        "bing", "google", "yandex", "baidu", "sogou", "tencent", 
        "deepl", "alibaba", "iciba", "iflytek", "reverso", "itranslate",
        "caiyun", "argos", "papago", "youdao", "mglip", "niutrans",
        "volcEngine", "translateCom", "myMemory", "utibet"
    ]
    
    # Common languages with their codes
    LANGUAGES = {
        "auto": "auto",
        "English": "en",
        "Spanish": "es",
        "French": "fr",
        "German": "de",
        "Italian": "it",
        "Portuguese": "pt",
        "Russian": "ru",
        "Japanese": "ja",
        "Korean": "ko",
        "Chinese (Simplified)": "zh",
        "Chinese (Traditional)": "zh-TW",
        "Arabic": "ar",
        "Hindi": "hi",
        "Turkish": "tr",
        "Dutch": "nl",
        "Polish": "pl",
        "Swedish": "sv",
        "Danish": "da",
        "Finnish": "fi",
        "Norwegian": "no",
        "Czech": "cs",
        "Greek": "el",
        "Hebrew": "he",
        "Thai": "th",
        "Vietnamese": "vi",
        "Indonesian": "id",
        "Malay": "ms",
        "Filipino": "fil",
        "Ukrainian": "uk",
        "Romanian": "ro",
        "Hungarian": "hu",
        "Bulgarian": "bg",
        "Croatian": "hr",
        "Slovak": "sk",
        "Lithuanian": "lt",
        "Latvian": "lv",
        "Estonian": "et",
        "Slovenian": "sl",
        "Serbian": "sr",
        "Catalan": "ca",
        "Bengali": "bn",
        "Tamil": "ta",
        "Telugu": "te",
        "Urdu": "ur",
        "Persian": "fa",
        "Swahili": "sw",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {
                    "multiline": True,
                    "default": "Hello, world!"
                }),
                "translator": (cls.TRANSLATORS, {
                    "default": "bing"
                }),
                "from_language": (list(cls.LANGUAGES.keys()), {
                    "default": "auto"
                }),
                "to_language": (list(cls.LANGUAGES.keys()), {
                    "default": "English"
                }),
            },
            "optional": {
                "if_use_preacceleration": ("BOOLEAN", {
                    "default": False
                }),
                "timeout": ("FLOAT", {
                    "default": 10.0,
                    "min": 1.0,
                    "max": 60.0,
                    "step": 0.5
                }),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("translated_text",)
    FUNCTION = "translate"
    CATEGORY = "text/translation"
    
    def translate(self, text, translator, from_language, to_language, 
                  if_use_preacceleration=False, timeout=10.0):
        """
        Translates the input text using the specified translator
        
        Args:
            text: The text to translate
            translator: The translation engine to use
            from_language: Source language (display name)
            to_language: Target language (display name)
            if_use_preacceleration: Whether to use session caching
            timeout: Request timeout in seconds
            
        Returns:
            Translated text as a string
        """
        try:
            # Convert language display names to codes
            from_lang_code = self.LANGUAGES[from_language]
            to_lang_code = self.LANGUAGES[to_language]
            
            # Optional preacceleration
            if if_use_preacceleration:
                try:
                    ts.preaccelerate_and_speedtest()
                except Exception as e:
                    print(f"Preacceleration warning: {e}")
            
            # Perform translation
            translated = ts.translate_text(
                query_text=text,
                translator=translator,
                from_language=from_lang_code,
                to_language=to_lang_code,
                timeout=timeout,
                if_ignore_empty_query=True,
                if_print_warning=True
            )
            
            return (translated,)
            
        except Exception as e:
            error_msg = f"Translation error: {str(e)}"
            print(error_msg)
            return (f"[ERROR] {error_msg}",)

# Node registration for ComfyUI
NODE_CLASS_MAPPINGS = {
    "TranslatorNode": TranslatorNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TranslatorNode": "Text Translator"
}
