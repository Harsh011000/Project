import pyrebase

config={
  "apiKey": "AIzaSyAQPq8I1txvGxWNQOHs69M7GU8NAQNF7xE",
  "authDomain": "yeah-74f98.firebaseapp.com",
  "databaseURL": "https://yeah-74f98-default-rtdb.firebaseio.com",
  "projectId": "yeah-74f98",
  "storageBucket": "yeah-74f98.appspot.com",
  "messagingSenderId": "433921238077",
  "appId": "1:433921238077:web:f2bf66a86422819cac7654",
  "measurementId": "G-EX0Q103DB7"}

firebase=pyrebase.initialize_app(config)
db=firebase.database()

#db.push({"1":"ok"})

from flask import *
app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def hi():
    if request.method=="POST":
        n=request.form["Name"]
        enroll=request.form["enroll"]
        email=request.form["email"]
        age=request.form["age"]
        dob=request.form["DOB"]
        year=request.form["year"]
        gen=request.form["gender"]
        #spec=request.form["preference"]
        #inter=request.form["nature"]
        try:
            read=request.form["nature1"]
        except:
            read="None"
        try:
            mus=request.form["nature2"]
        except:
            mus="None"
        try:
            fball=request.form["nature3"]
        except:
            fball="None"
        try:
            write=request.form["nature4"]
        except:
            write="None"
        try:
            photo=request.form["nature5"]
        except:
            photo="None"
        try:
            cook=request.form["nature6"]
        except:
            cook="None"
        try:
            arts=request.form["nature7"]
        except:
            arts="None"
        try:
            trav=request.form["nature8"]
        except:
            trav="None"
        try:
            gard=request.form["nature9"]
        except:
            gard="None"
        try:
            gam=request.form["nature10"]
        except:
            gam="None"
        try:
            blog=request.form["nature11"]
        except:
            blog="None"
        try:
            web=request.form["nature12"]
        except:
            web="None"
        try:
            cric=request.form["nature13"]
        except:
            cric="None"
        try:
            trek=request.form["nature14"]
        except:
            trek="None"
        try:
            hack=request.form["nature15"]
        except:
            hack="None"
        try:
            bad=request.form["nature16"]
        except:
            bad="None"
        try:
            st=request.form["nature17"]
        except:
            st="None"
        try:
            stream=request.form["nature18"]
        except:
            stream="None"
        try:
            an=request.form["nature19"]
        except:
            an="None"
        d0={"Reading":read,
            "Music":mus,
            "Football":fball,
            "Writing":write,
            "Photography":photo,
            "Cooking":cook,
            "Arts":arts,
            "Travelling":trav,
            "Gardening":gard,
            "Gaming":gam,
            "Blogging":blog,
            "Web-series":web,
            "Cricket":cric,
            "Trekking":trek,
            "Hacking/Coding":hack,
            "Badminton":bad,
            "Stand-Ups":st,
            "Streaming":stream,
            "Anime":an}
        inter=[]
        for v in d0:
            if d0[v]=="on":
                inter.append(v)
        d={"name":n,
           "Enrollment NO":enroll,
           "Email":email,
           "Age":age,
           "DOB":dob,
           "Year":year,
           "Gender":gen,
           #"Preference":spec}
           "interest":inter}
        db.child(enroll).set(d)
        return render_template("rating page.html")
    return render_template("data.html")


if __name__=="__main__":
    app.run(debug=True)
