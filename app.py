from flask import Flask,jsonify,request
app=Flask(__name__)

contacts=[{
        "id":1,
        "name":"Peter",
        "Mobile Number":"9562348952",
        "done":False

    },
    {
        "id":2,
        "name":"Gwen",
        "Mobile Number":"9436581205",
        "done":False
    },
    {
    "id":3,
        "name":"Misty",
        "Mobile Number":"9854136057",
        "done":False 
    },
    {
        "id":4,
        "name":"Ash",
        "Mobile Number":"8240652157",
        "done":False 
    }
]

@app.route("/add-data",methods=["POST"])
def add_contact():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data"
        },400)
    contact={
        "id":contacts[-1]["id"]+1,
        "name":request.json["name"],
        "Mobile Number":request.json.get("Mobile Number",""),
        "status":False
    }
    contacts.append(contact)
    return jsonify({
        "status":"Success",
        "message":"Contact added successfully"
    })

@app.route("/get-data")
def get_contact():
    return jsonify({
        "data":contacts
    })

if (__name__=="__main__"):
    app.run(debug=True)