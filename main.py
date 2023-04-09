from flask import Flask, request, render_template


app = Flask(__name__)
redis = {}


@app.route('/add', methods=['get', 'post'])
def add_page():
    global redis
    if request.method == 'POST':
        key = request.form.get('key')
        value = request.form.get('value')
        redis.update({key : value})
        with open('redis.txt', 'w') as file:
            file.write(f'{redis}')
    return render_template('add_page.html')

@app.route('/list', methods=['get'])
def list_page():
    with open('redis.txt', 'r') as file:
        data = file.read()
    return render_template('list.html', context=data)

@app.route('/del', methods=['get', 'post'])
def del_page():
    global redis
    print(redis)
    if request.method == 'POST':
        key = request.form.get('key')
        redis.pop(key)
        with open('redis.txt', 'w') as file:
            file.write(f'{redis}')
    return render_template('del_page.html')


if __name__ == '__main__':
    app.run(debug=True, port=8888)