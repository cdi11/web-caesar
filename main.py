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
        <input id= "rot" type="text" id= "rot" name="rot"></input>
        <textarea name="text">Type text here!</textarea>
        <input type="submit" id="rot" name="rot">

        </body>
    </html>
"""

@app.route("/") #, method=['POST'])
def blank_form():
    return form

#@app.route('/submit')
#def encrypt():
    #


@app.route("/submit")
def encrypt():
    text = request.form['text']
    rot = request.form['rot']
    message =rotate_string(text,rot)
    return message

app.run()
