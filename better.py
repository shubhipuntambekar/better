from flask import Flask

from configs.routes import routes_bp

app = Flask(__name__)
app.register_blueprint(routes_bp)


@app.route('/health')
def health_check():
    return "Status: Up!"


if __name__ == "__main__":
    app.run(debug=True)
