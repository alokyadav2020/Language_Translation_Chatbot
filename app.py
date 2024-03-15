from flask import Flask, render_template, jsonify, request
from src.LanguagetranslationLlama2.conponents.Text_Text_Translation import Text_Translation
from src.LanguagetranslationLlama2.config.configuration import ConfigurationManager
from googletrans import Translator

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
         result  = obj.Text_2_Text_Translate(input,src_lang="eng",tgt_lang="hin")

    elif language.lang == 'hi':
        result  = obj.Text_2_Text_Translate(input,src_lang="hin",tgt_lang="eng")    




    print("Response : ", result)


   
    
    return str(result)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080)


