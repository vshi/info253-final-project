from flask import Flask
from flask import render_template

import helper
import youtube

app = Flask(__name__, static_folder="public_html/static", template_folder="public_html/templates")
@app.route('/')


def load_root():
    return render_template('index.html')

@app.route('/drinkwhen')
def drink_when(name=None):
    random_candidate = helper.getRandomCandidate()
    candidate_phrases = helper.getCandidatePhrases(random_candidate)
    party = helper.getCandidateParty(random_candidate)
    random_video = youtube.youtube_search(random_candidate, 15)
    vid_title = random_video[0]
    vid_id = random_video[1]
    drunk_phrase = helper.getRandomDrunkPhrase()
    return render_template('drinkwhen.html', video_title=vid_title, video_id=vid_id, candidate=random_candidate, phrases=candidate_phrases, party=party, drunk_phrase= drunk_phrase)

@app.route('/stuffcandidatessay')
def stuff_candidates_say(name=None):
    candidate_info = helper.generateCandidateInfo()
    return render_template('stuffcandidatessay.html', info=candidate_info)

@app.route('/whosaidthisstuff')
def who_said_this_stuff(name=None):
    random_shit = helper.getRandomShit()
    return render_template("whosaidthisstuff.html", info=random_shit)

if __name__ == "__main__":
    app.run()