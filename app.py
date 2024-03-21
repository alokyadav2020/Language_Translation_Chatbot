from flask import Flask, render_template, jsonify, request,send_file
from werkzeug.utils import secure_filename
from src.LanguagetranslationLlama2.conponents.Text_Text_Translation import Text_Translation
from src.LanguagetranslationLlama2.config.configuration import ConfigurationManager
from src.LanguagetranslationLlama2.entity import DataTransfer
from flask_cors import CORS
from pydub import AudioSegment
import dataclasses
from pathlib import Path
from datetime import datetime
import os

from googletrans import Translator
import speech_recognition as sr

# rec = sr.Recognizer()


obj_T2T = Text_Translation()



# @dataclasses.dataclass
# class DataTransfer:
#  MESSAGE_TRANSFER = ""
#  MESSAGE_RECIEVE =""
#  AUDI_FILE: Path = None
#  AUDI_FILE_S2C:Path =None






app = Flask(__name__)
CORS(app)



dt = DataTransfer()

# engine = pyttsx3.init()


@app.route("/")
def index():
    return render_template('chat.html')





@app.route("/get", methods=["GET", "POST"])
def get():
    msg = request.form["msg"]
    input = msg
    print(input)
    return input


@app.route("/send", methods=["POST"])
def send():
    try:

        if "audio_file" not in request.files:
            msg = request.form["send_msg"]
            dt.MESSAGE_TRANSFER = msg
            print(f"this message is fron send api {dt.MESSAGE_TRANSFER}")
            transfer_msg()
            return ""
        
        file = request.files["audio_file"]
       
        if file:
            # dt.AUDI_FILE_S2C = file

            print("file get")
            uniqfilename = str(datetime.now().timestamp()).replace(".","")
            file.save(f"Data/{uniqfilename}.wav")
            dt.AUDI_FILE_S2C = f"Data/{uniqfilename}.wav"
            print(f"file name from sendfronclientapi is {dt.AUDI_FILE_S2C}")
            return  ""
    except Exception as e:
        raise e    

@app.route("/sendfromclient", methods=["POST"])
def sendfromclient():
    try:

        if "audio_file" not in request.files:

            msg = request.form["send_msg"]
            dt.MESSAGE_RECIEVE = msg
            print(f"this message is fron send api {dt.MESSAGE_RECIEVE}")
            transfer_msg()
            return "" 
        file = request.files["audio_file"]
        # file.headers["Access-Controll-Allow-Origin"]="*"
        if file:
            uniqfilename = str(datetime.now().timestamp()).replace(".","")
           
            with open(f"Data/{uniqfilename}.wav", 'wb') as f:
                f.write(file.read())


            # file.save(f"Data/{uniqfilename}.wav")
            dt.AUDI_FILE = f"Data/{uniqfilename}.wav"
            print(f"file name from sendfronclientapi is {dt.AUDI_FILE}")
        
            return  ""
    except Exception as e:
        raise e    

@app.route("/recieve_file",methods=["GET"])    
async def recieve_file():
    try:
        if dt.AUDI_FILE_S2C != None:
            audifile = transfer_audiofile_to_client()
            # adfile = obj_T2T.Speech_2_Speech_Translate(audio_arrey=audifile,tgt_lang="hin")
            dt.AUDI_FILE_S2C = None
            
            return send_file(audifile)
        if os.path.exists(audifile):
            os.remove(audifile)
    except Exception as e:
        dt.AUDI_FILE_S2C = None
        # adfile =None
        audifile = None
        raise e        
        



@app.route("/recieve", methods=["GET"])
async def recieve():
    try:
        if dt.AUDI_FILE_S2C != None:
            return  {"Message":"file001234"}
        
        if dt.MESSAGE_TRANSFER != "":
            msg_tra = transfer_msg()
            dt.MESSAGE_TRANSFER = ""
            msg = obj_T2T.Text_2_Text_Translate(text_input = msg_tra,tgt_lang="arb")
            
            return {"Message":msg}
        else:
            return {"Message":""}
    except Exception as e:
        dt.MESSAGE_TRANSFER = ""
        msg =""
        raise e


    
    

@app.route("/recievefromclinet_file", methods =["GET"])
async def   recievefromclinet_file():
    try:
        if dt.AUDI_FILE != None:
            audifile = transfer_audiofile()
            # adfile = obj_T2T.Speech_2_Speech_Translate(audio_arrey=audifile,tgt_lang="eng")
            dt.AUDI_FILE = None
            # audifile = None
            return  send_file(audifile)
        if os.path.exists(audifile):
            os.remove(audifile)
    except Exception as e:
        dt.AUDI_FILE = None
        audifile = None
        # adfile = None
        raise e        

    

@app.route("/recievefromclinet", methods=["GET"])
async def recievefromclinet():
    try:

        if dt.AUDI_FILE != None:
            return  {"Message":"file001234"}
        
        if dt.MESSAGE_RECIEVE != "":
            msg_tc = transfer_msg_toclient()
            dt.MESSAGE_RECIEVE = ""
            msg = obj_T2T.Text_2_Text_Translate(text_input= msg_tc,tgt_lang="eng")
           
            return {"Message":msg}
        else:
            return {"Message":""}
    except Exception as e:
        dt.MESSAGE_RECIEVE = ""
        msg = ""
        raise e
       

    # if dt.AUDI_FILE == None:
    #     rec_msg =  transfer_msg_toclient()
    #     print(f"this message is from recievefromclinet api {rec_msg}")
    #     if rec_msg != "":
    #         msg = obj_T2T.Text_2_Text_Translate(text_input= dt.MESSAGE_RECIEVE,src_lang="hin",tgt_lang="eng")
    #         dt.MESSAGE_RECIEVE = ""
    #         return {"Message":msg}
    #     else:
    #         return {"Message":""}

    # else:    
    #     return  {"Message":"file001234"}
    
    
        
   

def transfer_msg():
  MESSAGE_CARIER = dt.MESSAGE_TRANSFER
  if MESSAGE_CARIER == "":
      return ""
  else:
      print(f"this message is from transfer_msg function{MESSAGE_CARIER}")
      return MESSAGE_CARIER
  


def transfer_msg_toclient():  
  MESSAGE_CARIER = dt.MESSAGE_RECIEVE
  if MESSAGE_CARIER == "":
      return ""
  else:
      print(f"this message is from transfer_msg function{MESSAGE_CARIER}")
      return MESSAGE_CARIER
  

def transfer_audiofile():
    AUDIO_CARRIAR = dt.AUDI_FILE
    if AUDIO_CARRIAR == None:
        return ""
    else:
        return AUDIO_CARRIAR
    
def transfer_audiofile_to_client():
    AUDIO_CARRIAR = dt.AUDI_FILE_S2C
    if AUDIO_CARRIAR == None:
        return ""
    else:
        return AUDIO_CARRIAR    

   
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080)


