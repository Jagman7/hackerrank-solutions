from flask import Flask
import function
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test')
def function_check():
    ############### Functions ###############
    # function.Alphabet_Rangoli()   
    function.DefaultDict_Tutorial()
    #########################################
    return ("Working [##########.............] 75% Completed")




if __name__ == "__main__":
    app.run(debug=True)
