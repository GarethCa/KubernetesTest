from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Run build.sh to delete old images, delete kubernetes resources, restart."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)