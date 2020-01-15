from flask import Flask, request

app = Flask(__name__)

@app.route('/query')
def index():
    args = request.args
    id = args.get('id')
    date = args.get('date')
    print(id)
    print(date)
    return "\nQuery String!!\nHello, "+id+"\nToday : "+date

@app.route('/path/<param1>/<param2>')
def path_param(param1, param2):
    return "Path Param!!\n"+"param1 : "+param1+"\nparam2 : "+param2

@app.route('/body', methods=['POST'])
def request_body():
    print(request.json)

    body = request.json
    id = body['id']
    name = body['name']

    print(id)
    print(name)

    return "Request Body!!\n"+str(id)+"\n"+name


if __name__ == '__main__':
    app.run(debug=True)