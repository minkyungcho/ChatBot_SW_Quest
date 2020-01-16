from flask import Flask, make_response, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    return make_response(jsonify(results()))

def results():
    req = request.get_json(force=True)
    print(req)
    print("----------------------------------")
    queryText = req.get('queryResult').get('outputContexts')
    output = queryText[0].get('parameters')
    pizza = output.get('pizza')
    pizza_size = output.get('pizza-size')
    pizza_sidemenu = output.get('pizza-sidemenu')
    sidenum = output.get('sidenumber')
    address = output.get('address')
    print("주소 : "+address)
    print("메뉴 : "+pizza+" "+pizza_size+" "+pizza_sidemenu+" "+str(sidenum))
    response = {
        'fulfillmentMessages': [{
            'text': {'text':
                     ['PIZZA Bot webhook!!']
            }
        }]
    }
    return response

if __name__ == '__main__':
    app.run(debug=True)