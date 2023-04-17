import json

from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    with open('games.json', 'rt', encoding='utf8') as f:
        news_list = json.load(f)
        print(news_list)
    return render_template('index.html', news=news_list)


@app.route('/games/<game>')
def Magicka(game):
    with open('games.json', 'rt', encoding='utf8') as f:
        news_list = json.load(f)
        print(news_list)
        for item in news_list['games']:
            print(item, game)
            if game == item['html']:
                return render_template(game)
    return render_template("does_not_exist.html")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.2')
