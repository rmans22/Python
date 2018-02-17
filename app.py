import MySQLdb
from werkzeug.utils import redirect
from flask.helpers import url_for

from flask import Flask
from flask import render_template
from flask import request
from functions import mainFunction

connect = MySQLdb.connect(host='localhost', user='root', passwd='', db='demo')
cur = connect.cursor()

app = Flask(__name__)

@app.route('/')
def index():
	cur.execute("SELECT * FROM test")
	result = cur.fetchall()
	return render_template('users.html', result=result)

@app.route('/edit/<id>', methods=['GET'])
def edit(id):
	
	user_id = request.args.get('id', id)
	
	if request.method == 'GET':
		try:
			sql = "SELECT * FROM test WHERE id= " + id + ' LIMIT 1'
			cur.execute(sql)
			result = cur.fetchall()
			return render_template('edit.html', result=result)
		except:
			return redirect(url_for('index'))
	else:
		return redirect(url_for('index'))
	
if __name__ == '__main__':
	app.run(debug=True)