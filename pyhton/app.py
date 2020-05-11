from flask import Flask
import function
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test')
def function_check():
    # print(*a, sep = "\n")
    function.Alphabet_Rangoli()
    
    return ("Hello")




if __name__ == "__main__":
    app.run(debug=True)
