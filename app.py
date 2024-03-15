from flask import Flask, render_template, jsonify, request
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
import os
# import pyttsx3


app = Flask(__name__)

# engine = pyttsx3.init()


directory = r"D:\Client_pro\Fiverr\Language_Translation\artifacts"
filename = "model"

# Create the full path using os.path.join()
model_path = os.path.join(directory, filename)

model = MBartForConditionalGeneration.from_pretrained(model_path)
tokenizer = MBart50TokenizerFast.from_pretrained(model_path, src_lang="en_XX")




@app.route("/")
def index():
    return render_template('chat.html')



@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)

    model_inputs = tokenizer(input, return_tensors="pt")
    generated_tokens = model.generate(**model_inputs, forced_bos_token_id=tokenizer.lang_code_to_id["hi_IN"])
    result  = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    
    print("Response : ", result[0])
    
    return str(result[0])



if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)


