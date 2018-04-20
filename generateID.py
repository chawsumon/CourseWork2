from flask import Flask,render_template,jsonify
import sqlite3 , json

app = Flask(__name__)
@app.route('/')
def indexPage():
	con = sqlite3.connect('store.db')
	cur = con.cursor()
	cur.execute("select id from cust_order")
	cid = cur.fetchall()
	cid.sort(reverse=True)
	print(int(cid[0][0])+1)
	return jsonify(customers=int(cid[0][0])+1)   

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug = True)
