from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']

    doc = {
        'name': name_receive,
        'count': count_receive,
        'address': address_receive,
        'phone': phone_receive
    }

    db.homework.insert_one(doc)

    return jsonify({'result': 'success'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['POST'])
def write_order():
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']

    order = {
        'name': name_receive,
        'count': count_receive,
        'address': address_receive,
        'phone': phone_receive
    }

    db.order.insert_one(order)
    # 성공 여부 & 성공 메시지 반환
    return jsonify({'result': 'success', 'msg': '주문이 성공적으로 접수되었습니다.'})


@app.route('/order', methods=['GET'])
def view_orders():
    orders = list(db.homework.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)