from flask import Flask,render_template

app=Flask(__name__)
@app.route('/')

def selam():
    rows=[
        ['No','Adı','Soyadı','Vize','Final'],
        ['224545045','Erdem','Nohut','90','100'],
        ['224526039','Fatih','Kaya','75','90']
        ]
    return render_template('index.html', rows=rows)

if __name__=='__main__':
    app.run(debug=True)
    
    