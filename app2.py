from flask import Flask, render_template, jsonify, request
import os
from transformers import SeamlessM4TForTextToText,AutoProcessor



app = Flask(__name__)

# engine = pyttsx3.init()


directory ="artifacts"
filename = "fb_model"

# Create the full path using os.path.join()
model_path = os.path.join(directory, filename)

processor = AutoProcessor.from_pretrained(model_path)
model = SeamlessM4TForTextToText.from_pretrained(model_path)




@app.route("/")
def index():
    return render_template('chat.html')



@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)

    text_inputs = processor(text = input, src_lang="eng", return_tensors="pt")
    output_tokens = model.generate(**text_inputs, tgt_lang="arb")
    result  = processor.decode(output_tokens[0].tolist(), skip_special_tokens=True)
    
    print("Response : ", result)
    
    return str(result)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)


