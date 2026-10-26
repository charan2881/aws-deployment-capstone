from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>My DevOps Project</title>
        </head>
        <body style="font-family: Arial; text-align: center; padding: 50px;">
            <h1>Welcome to My DevOps Project!</h1>
            <h2>Version 2 Successfully Deployed!</h2>
            <p>Deployed automatically using Jenkins CI/CD.</p>
            <p>Technologies: GitHub, Jenkins, Docker, AWS ECR and ECS</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
