from flask import Flask, render_template

# flask uygulama oluşturma başlatma
app = Flask(__name__)

# / yolu için rota belirleme ve istekleri işleme
@app.route('/')
def anasayfa():
    # tarayıcıda görüntülenecek içerik
    rows=[
    ['No','Adı','Soyadı','Vize','Final']
    ['224526079','Nuhcan','Atar','50','70']
    ['256134635','Ali','Tutar','100','100']
    ]
    return render_template("index.html", rows=rows)

# proje çalıştırıldıysa
if __name__ == '__main__':
    # uygulamayı debug modunda çalıştır
    app.run(debug=True)
    