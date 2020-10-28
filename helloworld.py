from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return  """
			<title>Hello World!</title>
			<body onmousemove='moveText(event)'>
			<script>
			function moveText(e) {
			document.getElementsByTagName("p")[0].style.wordSpacing=e.clientX*-.3;
			}
			</script>
			<p style='text-align:center;font-size:15vw;word-spacing:-15vw'>
			<span style='color:#EB001BFF'>Hello </span>
			<span style='color:#F79E1BCC'>World</span>
			</p>
			</body>
			"""

if __name__ == "__main__":
	app.run()