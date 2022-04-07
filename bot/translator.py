# Imports the Google Cloud Translation library
from google.cloud import translate


# Initialize Translation client
def translate_text(text, lang_code="en-US", project_id="cosc-310-assignment"):
    """Translating Text."""

    client = translate.TranslationServiceClient()

    location = "global"

    parent = f"projects/{project_id}/locations/{location}"

    # Translate text from English to French
    # Detail on supported types can be found here:
    # https://cloud.google.com/translate/docs/supported-formats
    response = client.translate_text(
        request={
            "parent": parent,
            "contents": [text],
            "mime_type": "text/plain",  # mime types: text/plain, text/html
            "source_language_code": lang_code,
            "target_language_code": "en-US",
        }
    )

    # Display the translation for each input text provided
    translated_response = ""
    for translation in response.translations:
        print("Translated text: {}".format(translation.translated_text))
        translated_response += translation.translated_text
    return translated_response


def detect_language(in_string, project_id="cosc-310-assignment"):
    """Detecting the language of a text string."""

    client = translate.TranslationServiceClient()

    location = "global"

    parent = f"projects/{project_id}/locations/{location}"

    # Detail on supported types can be found here:
    # https://cloud.google.com/translate/docs/supported-formats
    response = client.detect_language(
        content=in_string,
        parent=parent,
        mime_type="text/plain",  # mime types: text/plain, text/html
    )

    # Display list of detected languages sorted by detection confidence.
    # The most probable language is first.

    # for language in response.languages:
    #     # The language detected
    #     print("Language code: {}".format(language.language_code))
    #     # Confidence of detection result for this language
    #     print("Confidence: {}".format(language.confidence))
    return response.languages[0].language_code


def get_translation(in_string):
    lang_code = detect_language(in_string)
    if 'en' not in lang_code:
        return translate_text(text=in_string, lang_code=lang_code)
    else:
        return in_string