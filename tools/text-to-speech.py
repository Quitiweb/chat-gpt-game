import os
from google.cloud import texttospeech_v1

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "media/qw-text-to-speech-97614f4c7ac4.json"
client = texttospeech_v1.TextToSpeechClient()

text = "<speak>Hola. Qué tal estás?</speak>"
synthesis_input = texttospeech_v1.SynthesisInput(ssml=text)

voice1 = texttospeech_v1.VoiceSelectionParams(
    language_code="es-es",
    # name="eu-ES-Standard-A",
    # ssml_gender=texttospeech_v1.SsmlVoiceGender.FEMALE
)

# print(client.list_voices())
audio_config = texttospeech_v1.AudioConfig(audio_encoding=texttospeech_v1.AudioEncoding.MP3)

response = client.synthesize_speech(
    input=synthesis_input,
    voice=voice1,
    audio_config=audio_config
)

with open("media/audio_speech_v2.mp3", "wb") as output:
    output.write(response.audio_content)
