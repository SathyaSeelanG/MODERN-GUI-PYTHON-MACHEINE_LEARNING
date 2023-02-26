import numpy as np
from flask import Flask, request, jsonify, render_template
from flask import Flask
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import pickle
import pandas as pd
import requests
df=pd.read_csv("faqs.csv",encoding="ISO-8859-1")



app = Flask(__name__)

model = pickle.load(open('model1.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/chat',methods=['GET','POST'])
def predict():
    '''
    For rendering results on HTML GUI'''
    

    i=1
    while i==1:
        int1 = [x for x in request.form.values()]
        for i in range(len(int1)):
            int1[i]=int1[i].lower()
        def text_seperation (x):
            return x.split()
        bow_transformer = CountVectorizer(analyzer=text_seperation).fit(df['Question'])

        messages_bowt = bow_transformer.transform(int1)
        tfidf_transformert = TfidfTransformer().fit(messages_bowt)
        messages_tfidft = tfidf_transformert.transform(messages_bowt)
        predict= model.predict(messages_tfidft)
        str1=""
        str1=str1.join(predict)
        return jsonify({"status":"success","response":str1})
        
@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
