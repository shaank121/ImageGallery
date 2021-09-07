from flask import Flask,request
import requests
import os
from  dotenv import load_dotenv
from flask_cors import CORS 

load_dotenv(dotenv_path="./.env.local") 

UNSPLASH_KEY=os.environ.get("UNSPLASH_KEY","")
UNSPLASH_URL=os.environ.get("UNSPLASH_URL","")


DEBUG=os.environ.get("DEBUG",True)

app=Flask(__name__)
app.config["DEBUG"]=DEBUG
CORS(app)


@app.route("/new-image")
def new_image():
    word=request.args.get("query")
    print(word)
    headers={
            "Accept-Version": "v1",
            "Authorization": "Client-ID "+ UNSPLASH_KEY            
    }

    print("test")
    params={
        "query":word
        }
    print(headers)
    print(params)
    response=requests.get(url=UNSPLASH_URL,headers=headers,params=params)
    
    data=response.json()
    return data

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5050)