from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def anasayfa():
    title = "MY PAGE"
    rows = [
        ["No", "Adı", "Soyadı", "Vize", "Final"],
        ["123", "Nuhcan", "Atar", "50", "80"],
        ["456", "Ali", "Tutar", "60", "90"]
    ]
    
    return render_template('index1.html', rows=rows, title=title)

if __name__ == '__main__':
    app.run(debug=True)