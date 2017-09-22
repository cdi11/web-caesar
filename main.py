from flask import Flask, request, redirect
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG']= True

form="""

<!DOCTYPE html> 
    <html>
        <head>
            <style>
                form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
            
            </style>
        </head>
        <body>
        <!--Create your text here-->
        <form method="post">
        <form action="submit" id="textform" methods="post">
        <label for= "rot">Rotate by:</label> 
        <input min = "0" max ="26" type= "number" name="rot" value= "0" methods="post"></input>
        <textarea type= "text" name="text" methods="post">{0}</textarea>
        <br>
        <input type="submit">

        </body>
    </html>
"""



@app.route("/")
def blank_form():
    return form.format("")
    
    
    #new_message=rotate_string(new_text,new_rot)
    
@app.route("/", methods = ['POST'])
def encrypt():
    text_mesg = request.form['text']
    rot_num = request.form['rot']
    #encrypted_txt=''
    encryptd_txt = rotate_string(text_mesg, int(rot_num))
    return form.format(encryptd_txt)

#Build response content...
    #encrypted_message = rotate_string(get-text, get-rot)
    #new_message_encrypt= '<p>encrypted_message</p>'
    #content =  new_message_encrypt

    #return content
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
