from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def selam():
    rows=[
        ['No', 'Adı', 'Soyadı', 'Vize', 'Final'],
        ['224526520','Nuhcan','Atar','90','100']
        ['234252524','Ali','Tutar','14','65']
        ]
    return render_template("flaskk.html",rows=rows)

if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    