from app import app

@app.get('/')
def index():
    return app.send_static_file('data/categories.json')