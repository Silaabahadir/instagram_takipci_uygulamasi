from flask import Flask, render_template

app = Flask(__name__)

def read_file(filename):
    with open(filename, 'r', encoding='UTF-8') as file:
        return file.read().splitlines()

@app.route('/')
def home():
    following = read_file('following.txt')
    followers = read_file('followers.txt')
    not_following_back = read_file('not_following_back.txt')
    return render_template('index.html', following=following, followers=followers, not_following_back=not_following_back)

if __name__ == '__main__':
    app.run(debug=True)
