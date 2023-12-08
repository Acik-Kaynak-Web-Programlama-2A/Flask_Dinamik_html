from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    rows = [
        ["No", "Adı", "Soyadı", "Vize", "Final"],
        ["234526065", "Gazi", "Artivinli", "60", "90"],
        ["222222222", "Mehmet", "Mehmet", "50", "70"]
    ]
    return render_template('index.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
