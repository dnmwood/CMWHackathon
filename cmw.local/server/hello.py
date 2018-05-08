from flask import Flask
import json
app = Flask(__name__)

app_initialized = False

@app.route("/init", methods=['POST'])
def init():
    # do initialization stuff

    # say the server is initialized at the end
    app_initialized = True
    return "I am initializing the server!"

@app.route("/percentage", methods=['GET'])
def percentage():
    if not app_initialized:
      return "Init first!"
    else:
      # grab the percentages and return them as json
      # with json.dumps

      return "I am getting band percentages!"