import json

from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    with open('games.json', 'rt', encoding='utf8') as f:
        news_list = json.load(f)
        print(news_list)
    return render_template('index.html', news=news_list)


@app.route('/templates/Magicka.html')
def Magicka():
    return render_template('Magicka.html')


@app.route('/templates/Magicka_2.html')
def Magicka_2():
    return render_template('Magicka_2.html')


@app.route('/templates/hotline_miami.html')
def hotline_miami():
    return render_template('hotline_miami.html')


@app.route('/templates/hotline_miami_2.html')
def hotline_miami_2():
    return render_template("hotline_miami_2.html")


@app.route('/templates/Minecraft.html')
def Minecraft():
    return render_template('Minecraft.html')


@app.route('/templates/Dishonored.html')
def Dishonored():
    return render_template('Dishonored.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.2')
