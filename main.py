from flask import Flask, request
import rotate_string from caesar.py

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
        <form action="submit" id="textform" method="post">
        <label for= "rot">Rotate by:</label> 
        <input id= "rot" type="text" id= "rot" name="rot"></input>
        <textarea name="text"></textarea>
        <input type="submit" id="rot" name="rot">

        </body>
    </html>
"""

@app.route("/")#make only posts
def blank_form():
    return form 

@app.route("/submit")
def encrypt(rotate_string(text, rot)):
    #first_name = request.form['first_name']
    return '<h1>Hi there</h1>'

app.run()
