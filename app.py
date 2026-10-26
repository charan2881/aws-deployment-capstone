from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>DevOps Capstone</title>
        </head>
        <body>
            <h1>My DevOps Capstone Project</h1>
            <p>Deployed using Jenkins, Docker, Amazon ECR and Amazon ECS.</p>
            <p>Deployment successful!</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
