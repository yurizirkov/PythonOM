from flask import Flask, render_template #escape, request, 
app = Flask(__name__)

@app.route('/')
def index():
    title = "Homepage"
    return render_template("index.html", title=title)
    

    #name = request.args.get("name", "World")
    #return f'Hello, {escape(name)}!'

    #$env:FLASK_APP = "hello"
    #flask run

@app.route('/about')
def about():
    title = "About"
    return render_template("about.html", title=title)
    

@app.route('/contact')
def contact():
    title = "Contact"
    return render_template("contact.html", title=title)
    

@app.route('/footer')
def footer():
    title = "Footer"
    return render_template("footer.html", title=title)


