# ComfyUI Translator Node

A ComfyUI custom node for translating text using various translation engines.

## Features
- 24+ translation engines (Bing, Google, DeepL, Yandex, etc.)
- 40+ languages supported
- Auto-detect source language
- Configurable timeout
- Session preacceleration option

## Installation

1. Clone or download this folder to `ComfyUI/custom_nodes/`
2. Install requirements: `pip install -r requirements.txt`
3. Restart ComfyUI

## Usage

Find the node under **text/translation** → **Text Translator**

### Inputs
- **text**: Text to translate
- **translator**: Choose translation engine
- **from_language**: Source language (auto-detect available)
- **to_language**: Target language
- **if_use_preacceleration**: Cache sessions for faster translations
- **timeout**: Request timeout in seconds

### Output
- **translated_text**: Translated text string

## Requirements
- translators>=5.9.2

## License
MIT
