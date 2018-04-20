from flask import Flask,render_template
import sqlite3 , json

app = Flask(__name__)
@app.route('/')
def indexPage():
	return render_template("index.html")

@app.route('/queue')
def queuePage():
	return render_template("queue.html")

@app.route('/newCustomer')
def newCustomer():
	con = sqlite3.connect('store.db')
	cur = con.cursor()
	cur.execute("select id from cust_order")
	cid = cur.fetchall()
	cid.sort(reverse=True)
	print(int(cid[0][0])+1)
	order_num = int(cid[0][0])+1
	cur.execute("insert into cust_order(id,status) values(:id,:status)",{"id":order_num,"status":"waiting"})
	con.commit()
	return render_template('custMain.html',order_num = order_num)   

@app.route('/cust/<order_num>')
def custPage(order_num):
	return render_template('cust.html',order_num = order_num)

@app.route('/order/<order_num>')
def getOrder(order_num):
	con = sqlite3.connect('store.db')
	cur = con.cursor()
	cur.execute("select product.id,product.description,qty,price from order_line JOIN product on (order_line.product = product.id) where cust_order=:cust_order",{"cust_order":order_num})
	# cur.execute("select * from order_line where cust_order=:cust_order",cust_order=cust_order)
	return json.dumps(cur.fetchall())

@app.route('/order_line/<order_num>/<item_num>')
def addToOrder(order_num,item_num):
	con = sqlite3.connect('store.db')
	cur =con.cursor()
	cur.execute("insert into order_line(cust_order,product,qty) values(:cust_order,:product,1)",{"cust_order":order_num,"product":item_num})
	con.commit()
	cur.execute("select product.id,product.description,qty,price from order_line JOIN product on (order_line.product = product.id) where cust_order=:cust_order",{"cust_order":order_num})
	return json.dumps(cur.fetchall())	

@app.route('/getQueue')
def getQueue():
	con = sqlite3.connect('store.db')
	cur = con.cursor()
	cur.execute("select * from cust_order where status in ('ready','processing')")
	return json.dumps(cur.fetchall())
	# return '[{"id":105,"status":"Processing"},{"id":106,"status":"Ready"}]'

if __name__ == '__main__':
	app.run(debug = True)