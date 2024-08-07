from flask import Flask,request,jsonify
import Voice_to_Text,Data_Recommendation,Gemini_API
app = Flask(__name__)

@app.route('/')
def home():
    Gemini_API.Start_a_Chat()
    return "Hello There "


@app.route('/voice_input')
def voice():
    path=request.args.get('Path')
    text_data=Voice_to_Text.speech_to_text(path)
    return Data_Recommendation.show_recommendation(text_data)

@app.route('/image')
def image():
    path=request.args.get('Path')
    return jsonify(Gemini_API.images(path))

app.run(debug=True)

