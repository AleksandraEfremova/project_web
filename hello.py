from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <html>
        <head>
            <title>Витамины и БАДы NOW</title>
        </head>
            <body>
                <h1>Введите название и дозировку</h1>
                    <h2>
                        <form action="/whatev" method="get">
                        <input type="text" name="hello" value="">
                        <input type="submit" value="Поиск">
                        </form>
                    </h2>
            </body>
    </html>
"""
    
if __name__=="__main__":
    app.run(debug=True)