from flask import Flask, request, jsonify
import requests, json, base64
from datetime import datetime

app = Flask(_name_)
GITHUB_TOKEN = "ghp_YOUR_TOKEN"
REPO = "sarika2026/horseranker"

@app.route("/fetch")
def fetch_race():
    fixture = request.args.get("fixture") # CR
    race = request.args.get("race") # 7
    date = datetime.now().strftime("%d.%m.%Y")
    
    url = f"https://www.tabtouch.com.au/ozbet/plsql/ozbet.ToteForARace?p_device=TEXT&p_date={date}&p_fixture_id={fixture}&p_contest_number={race}"
    
    txt = requests.get(url, timeout=10).text
    data = parse_tabtouch(txt) # use parser from before
    
    upload_to_github(data) # overwrite data.json
    
    return jsonify({"status":"ok","horses":len(data["horses"])})

if _name_ == "_main_":
    app.run()
