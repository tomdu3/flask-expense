import sys
sys.path.insert(0, '/var/www/flask-expense)

activate_this = '/home/tom/projects/flask-expense/.venv/bin/activate/activate_this.py'
with open(activate_this) as f:
    exec(f.read(), dict(__file__=activate_this))


from app import app as application