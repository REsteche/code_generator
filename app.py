from dotenv import dotenv_values

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key =  dotenv_values(".env.example")["OPENAI_API_KEY"]


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        user_request = request.form["code"]
        response = openai.Completion.create(
            model="code-cushman-001",
            prompt=user_request,
            temperature=0,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
        return redirect(url_for("index", result=response['choices'][0]['text']))

    result = request.args.get("result")
    return render_template("index.html", result=result)
