# sever.py
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

def get_pedido(pedido_id):
    conn =sqlite3.connect('Happy_burger.db')
    c = conn.cursor()
    c.execute("SELECT * FROM pedidos WHERE pedido_id=?",(pedido_id))
    pedido = c.fetchone()
    conn.close()
    return pedido

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pedido',methods={'GET'})
def pedido():
    pedido_id =request.args.get('pedido_id')
    pedido = get_pedido(pedido_id)
    return render_template('pedido.html' , pedido=pedido)

if __name__ == '__main__':
    app.run(debug=True)
    
    