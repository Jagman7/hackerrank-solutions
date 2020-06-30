from flask import Flask
from logic import function
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test')
def function_check():
    ############### Functions ###############
    # function.Alphabet_Rangoli()
    # function.DefaultDict_Tutorial()
    # function.Word_Order()
    # function.merge_the_tools(string='AABCAAADA',k=3)
    function.No_Idea()
    #########################################
    return ("Working [##########.............] 75% Completed")




if __name__ == "__main__":
    app.run(debug=True)
