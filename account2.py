from flask import Flask, request
app = Flask(__name__)

@app.route("/account/", methods=['GET', 'POST'])
def account():
    if request.method == 'POST':
        print request.form
        name = request.form['name']
        weight = request.form['weight']
        weight_kg = int(weight) * 0.45
        return "Hello %s" % name + ", your weight in kilograms is %d" % weight_kg + " kg"

    else:
        page ='''
        <html><body>
            <form action="" method="post" name="form">
                <label for="name">Name:</label>
                <input type="text" name="name" id="name"/>
                <label for"weight">Weight in lbs:</label>
                <input type="text" name="weight" id="weight"/>
                <br>
                <br>
                <input type="submit" name="submit" id="submit"/>
            </form>
            </body></html>'''
            
        return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

