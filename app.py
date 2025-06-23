from flask import Flask, render_template,request,redirect
import firebase_admin
from firebase_admin import credentials,db

app= Flask (__name__)
cred=credentials.Certificate("C:/Users/dudhe/Downloads/new-python-36518-firebase-adminsdk-fbsvc-285d26a5ac.json")
firebase_admin.initialize_app(cred,{"databaseURL":"https://new-python-36518-default-rtdb.firebaseio.com/"})

@app.route('/',methods=['GET','POST'])
def Home():
    if request.method=='POST':
       branch=request.form.get('branch')
       year=request.form.get('year')
       feedback=request.form.get('feedback')
       db.reference('/index').push({'branch':branch,'year':year,'feedback':feedback})
       return redirect('/')
      
    else:
       db.reference('/visit').push({'page':'index'})
       return render_template("index.html")
@app.route('/contact',methods=['GET','POST'])
def contact():
    if request.method=='POST':
       name=request.form.get('name')
       message=request.form.get('message')
       db.reference('/contacts').push({'name':name,'message':message})
       return redirect('/contact')
      
    else:
       db.reference('/visit').push({'page':'contact'})
       return render_template("contact.html")
@app.route('/about',methods=['GET','POST'])
def about():
   if request.method=='POST':
       name1=request.form.get('name1')
       db.reference('/abouts').push({'name1':name1})
       return redirect('/about')
      
   else:
       db.reference('/visit').push({'page':'about'})
       return render_template("about.html")
   
if __name__=='__main__':
  app.run(debug=True)
