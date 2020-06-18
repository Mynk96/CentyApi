from flask import Flask,render_template,url_for,request
import spacy
import json

app = Flask(__name__)

@app.route('/parsemessage', methods = ['POST'])
def parseMessage():
    if request.method == 'POST':
        messages = request.get_json()
        mymodel = spacy.load('centy2.0')
        message_response_list = []
        for message in messages:
            d = mymodel(message['data'])
            attributes_dic = {}
            for ent in d.ents:
                attributes_dic[ent.label_] = ent.text
                attributes_dic["message"] = message['data']
            message_response_list.append(attributes_dic)
        return json.dumps({
            'result':message_response_list
        })
if __name__ == '__main__':
	app.run(port=8080, threaded=True)