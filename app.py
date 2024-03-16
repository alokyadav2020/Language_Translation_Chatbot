from flask import Flask, render_template, jsonify, request
from src.LanguagetranslationLlama2.conponents.Text_Text_Translation import Text_Translation
from src.LanguagetranslationLlama2.config.configuration import ConfigurationManager
from googletrans import Translator
import speech_recognition as sr
from googletrans import Translator 
rec = sr.Recognizer()
translator = Translator()

obj = Text_Translation()
translator = Translator()




app = Flask(__name__)

# engine = pyttsx3.init()


@app.route("/")
def index():
    return render_template('chat.html')



@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)

    language = translator.detect(input)

    print(language.lang)

    if language.lang == 'en':
         result  = obj.Text_2_Text_Translate(input,src_lang="eng",tgt_lang="eng")

    elif language.lang == 'ar':
        result  = obj.Text_2_Text_Translate(input,src_lang="arb",tgt_lang="eng")

    elif language.lang == 'fr':
        result  = obj.Text_2_Text_Translate(input,src_lang="fra",tgt_lang="eng")    




    print("Response : ", result)


   
    
    return str(result)

# @app.route('/record', methods=['POST'])
# def record():
#   if 'audio_data' not in request.files:
#     return jsonify({'error': 'No audio data found'}), 400

#     audio_file = request.files['audio_data']
#     audio_file = request.files['audio']
#     print("-----------")
#     print(audio_file)

#     audio_file.save('recorded_audio23.wav')
#     rec_aud = rec.recognize_google('recorded_audio.mp3')
#     print("Here is the audio input :" + rec_aud)


#     # Save or process the audio data here
#     # For example:
#     audio_file.save('recordings/new_recording.webm')  # Adjust filename and path

#     return jsonify({'message': 'Audio data received successfully!'})


# @app.route('/process_audio', methods=['POST'])
# def process_audio():
#     if 'audio' not in request.files:
#         return jsonify({'error': 'No audio file provided'})

#     audio_file = request.files['audio']
#     print("-----------")
#     print(audio_file)

#     audio_file.save('recorded_audio23.wav')
#     rec_aud = rec.recognize_google('recorded_audio.mp3')
#     print("Here is the audio input :" + rec_aud)

# # Translate the text and display it
#     to_translate = translator.translate(rec_aud,src="hi",dest="hi")
#     translated_text = to_translate.text
#     print("The translated text is: ", translated_text)
    
#     # Save the audio file to disk
#     # audio_file.save('recorded_audio.wav')

#     # Here, you can process the audio file as needed
#     # For example, you can use speech-to-text APIs to transcribe the audio

#     return jsonify({'message': 'Audio received and saved'})

# @app.route('/record_voice', methods=['POST'])
# def record_voice():
#   # Get the audio data from the request.
#   audio_data = request.data

#   # Save the audio data to a file.
#   with open('audio.wav', 'wb') as f:
#     f.write(audio_data)

#   # Return a response to the JavaScript function.
#   return jsonify({'success': True})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080)


