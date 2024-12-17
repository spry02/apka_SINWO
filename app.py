from flask import Flask
from datetime import datetime

app=Flask(__name__)

@app.route('/')
def index():
    return f"""
    <html>
        <head>
            <title>Wiktor_Musiał_SINWO_Docker</title>
        </head>
        <body>
            <p>Imię i nazwisko: Wiktor Musiał</p>
            <p>Numer indeksu: 349569</p>
            <p>Data i godzina: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}</p>
        </body>
    </html>
"""

if __name__=="__main__":
    app.run(host="localhost", port=7777)