from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return '<p style="text-align:center;font-size:10em">Hello World!</p>'

if __name__ == "__main__":
	app.run()