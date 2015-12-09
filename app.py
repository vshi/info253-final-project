from flask import Flask
from flask import render_template

import helper

app = Flask(__name__, static_folder="public_html/static", template_folder="public_html/templates")
@app.route('/')


def load_root():

    return render_template('index.html')


@app.route('/shitcandidatessay')
def shit_candidates_say(name=None):
    candidate_info = helper.generateCandidateInfo()
    return render_template('shitcandidatessay.html', info=candidate_info)

@app.route('/whosaidthisshit')
def who_said_this_shit(name=None):
    random_shit = helper.getRandomShit()
    return render_template("whosaidthisshit.html", info=random_shit)


# @app.route('/<path:name>')
# def load_file(name=None):
#     url = 'public_html/' + name
#     f = open(url, 'r')
#     raw_data = f.read()
#     return raw_data

if __name__ == "__main__":
    app.run()