from root import create_app
import os

app = create_app()

app.app_context().push()

users = [
    {'id': 1, 'username': 'gastonfenske'},
    {'id': 2, 'username': 'johndoe'},
    {'id': 3, 'username': 'otromas'},
]

@app.route('/users')
def get():
    return {'users': users}

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))