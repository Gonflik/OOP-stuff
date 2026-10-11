from flask import Flask, render_template
from jikanpy import Jikan

jikan = Jikan()
app = Flask(__name__)

@app.route('/')
def home():
    current_season = jikan.seasons(extension='now')
    
    html_output = "<h1>Аніме поточного сезону:</h1>"
    
    for anime in current_season['data'][:15]:
        title = anime['title']
        score = anime['score'] if anime['score'] else "Немає оцінки"
        html_output += f"<p><b>{title}</b> — Оцінка: {score}</p>"
    
    return html_output

@app.route('/hells-paradise')
def hells_paradise():
    hp_data = jikan.anime(46569)['data']
    
    title = hp_data['title']
    score = hp_data['score']
    synopsis = hp_data['synopsis']
    
    return f"""
        <h1>{title}</h1>
        <p><b>Рейтинг:</b> {score}</p>
        <p><b>Опис:</b> {synopsis}</p>
        <a href="/">Назад до сезону</a>
    """

if __name__ == '__main__':
    app.run(debug=True)