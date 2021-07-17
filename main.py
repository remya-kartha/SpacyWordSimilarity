from flask import Flask,render_template,request
import spacy


app = Flask(__name__)

@app.route("/")
def showHomePage():
    return render_template("index.html")

@app.route("/checkSimilarity",methods=['POST'])
def checkSimilarity():
    #load the model
    nlp = spacy.load('en_core_web_md')
    word1 = request.form.get('firstWord')
    word2 = request.form.get('secondWord')
    print("first word",word1)
    print("second word",word2)
    doc_1 = nlp(word1)
    doc_2 = nlp(word2)
    similarity = doc_1.similarity(doc_2)    
    print("Similarity:", similarity )
    return render_template('index.html',similarity_text=f'''Similarity score of words "{word1}" and "{word2}" : {similarity}  ''')

if __name__ == '__main__':
    print(__name__)
    # run the app
    app.run(debug=True)