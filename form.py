
from flask import Flask, request, render_template,jsonifyapp = Flask(__name__)

def do_something(text1,text2):
    lyrics = api.getLyrics(title, artist)   results = text1 + text2
    results= model.gen_tags(lyrics, 8)
    return results@app.route('/')

def home():
    return render_template('home.html')@app.route('/join', methods=['GET','POST'])

def my_form_post():
    title = request.form['title']
    word = request.args.get('title')
    artist = request.form['artist']
    results = do_something(title, artist)
    result = {
        "output": results
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
