# -*- coding: utf-8 -*-
from flask import Flask
import os
from pathlib import Path

folder = "Data/Logs"
hits_path = folder + "hits.txt"

if not os.path.exists(folder):
    os.makedirs(folder)
    print("directories made.")

Path(hits_path).touch(exist_ok=True)
print("file present check")


def get_count():
    with open(hits_path, "r+") as file:
        val = file.readline()
        if val == "":
            return 0
        else:
            return int(val)


def new_view():
    try:
        hits = get_count()
        hits += 1
        with open(hits_path, 'w') as file:
            file.write(str(hits))
        return hits
    except Exception as e:
        print(e)


app = Flask(__name__)


@app.route("/")
def index():
    views = new_view()
    return f"hello world! i have been requested {views} times"


if __name__ == '__main__':
    pass
    app.run(host="0.0.0.0", port=5000, debug=True)
