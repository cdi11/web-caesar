from flask import Flask, request, redirect
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG']= True

form="""

<!DOCTYPE html> 
    <html>
        <head>
            <style>
                form {
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
            
            </style>
        </head>
        <body>
        <!--Create your text here-->
        <form action="submit" id="textform" methods="post">
        <label for= "rot">Rotate by:</label> 
        <input type "text" name="rot" value= "0"></input>
        <textarea type= "text" name="text">Type text here!</textarea>
        <input type="submit">

        </body>
    </html>
"""



@app.route("/") #, method=['POST'])
def blank_form():
    text = request.form['text']
    rot = request.form['rot']
    new_message=rotate_string(text,rot)
    return new_form


#@app.route('/submit')
#def encrypt():
    #


#@app.route("/submit")
#def encrypt():
    #text = request.form['text']
    #rot = request.form['rot']
    #new_message=rotate_string(text,rot)
    #return <h1>message</h1>
    #text = request.form['text']
    #rot = request.form['rot']
    #message =rotate_string(text,rot)
    #return message

app.run()
