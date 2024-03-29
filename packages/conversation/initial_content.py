from packages.conversation.message import (
    system,
    assistant,
    user
)

GOAL = 'show me a basic flask web dev example with templates.'

INITIAL_CONTENT = [
    system(),
    user(
        terminal_stdout='',
        goal=GOAL
    ),
    assistant('pip install flask'),
    user(
        terminal_stdout='Defaulting to user installation because normal site-packages is not writeable\n' +
                        'Collecting flask\n' +
                        'Using cached Flask-1.1.4-py2.py3-none-any.whl (94 kB)\n' +
                        'Requirement already satisfied: itsdangerous<2.0,>=0.24 in /home/yinzheng/.local/lib/python2.7/site-packages (from flask) (1.1.0)\n' +
                        'Requirement already satisfied: Jinja2<3.0,>=2.10.1 in /home/yinzheng/.local/lib/python2.7/site-packages (from flask) (2.11.3)\n' +
                        'Requirement already satisfied: Werkzeug<2.0,>=0.15 in /home/yinzheng/.local/lib/python2.7/site-packages (from flask) (1.0.1)\n' +
                        'Requirement already satisfied: click<8.0,>=5.1 in /home/yinzheng/.local/lib/python2.7/site-packages (from flask) (7.1.2)\n' +
                        'Requirement already satisfied: MarkupSafe>=0.23 in /home/yinzheng/.local/lib/python2.7/site-packages (from Jinja2<3.0,>=2.10.1->flask) (1.1.1)\n' +
                        'Installing collected packages: flask\n' +
                        'Successfully installed flask-1.1.4',
        goal=GOAL
    ),
    assistant('mkdir basic_flask_app'),
    user(
        terminal_stdout="",
        goal=GOAL
    ),
    assistant('''cat << 'EOF' > basic_flask_app/app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
EOF'''),
    user(
        terminal_stdout="",
        goal=GOAL
    ),
    assistant('mkdir basic_flask_app/templates'),
    user(
        terminal_stdout="",
        goal=GOAL
    ),
    assistant('''cat << EOF > basic_flask_app/templates/index.html
<!DOCTYPE html>
<html>
<head>
    <title>My Flask App</title>
</head>
<body>
    <h1>Welcome to My Flask App</h1>
    <p>This is the home page!</p>
</body>
</html>
EOF'''),
    user(
        terminal_stdout="",
        goal=GOAL
    ),
    assistant('''cat << 'EOF' > basic_flask_app/templates/about.html
<!DOCTYPE html>
<html>
<head>
    <title>About My Flask App</title>
</head>
<body>
    <h1>About My Flask App</h1>
    <p>This is a simple Flask app that demonstrates the use of templates!</p>
</body>
</html>
EOF
'''),
    user(
        terminal_stdout="",
        goal=GOAL
    ),
    assistant('python basic_flask_app/app.py'),
    user(
        terminal_stdout="",
        goal=GOAL
    ),
    assistant('DONE')
]
