import shelve
from subprocess import check_output
import flask
from flask import request, Flask, render_template, jsonify, abort, redirect
from os import environ

import os
import sys
import json
import hashlib

import random, string

import twitter, json
from flask import Flask
from flask import render_template

import helper
import youtube

app = Flask(__name__, static_folder="public_html/static", template_folder="public_html/templates")
db = shelve.open("shorten.db")
@app.route('/')


def load_root():
    return render_template('index.html')

@app.route("/create", methods=['POST'])
def create():
    """
    This POST request creates an association between a short url and a full url
    and saves it in the database (the dictionary db)
    """
    vid_title = request.form['videotitle']
    vid_id = request.form['videoid']
    candidate = request.form['candidate']
    candidate_phrases = helper.getCandidatePhrases(candidate)
    party = helper.getCandidateParty(candidate)
    drunk_phrase = helper.getRandomDrunkPhrase()
    long_url = request.form['longurl']
    short_url = ''.join(random.choice(string.lowercase+string.digits) for i in range(6))
    if long_url not in db.values():
        db[short_url] = long_url
    else:
        for s in db:
            if db[s] == long_url:
                short_url = s
                break
    return render_template('drinkwhen.html', short=short_url, long=long_url, video_title=vid_title, video_id=vid_id, candidate=candidate, phrases=candidate_phrases, party=party, drunk_phrase= drunk_phrase)

@app.route("/short/<short>", methods=['GET'])
def load_redirect(short):
    """
    Redirect the request to the URL associated =short=, otherwise return 404
    NOT FOUND
    """
    if short not in db:
        return render_template('404.html'), 404
    return redirect(db[short])

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

@app.route('/clouds')
def clouds(name=None):
    candidate_clouds = helper.generateClouds()
    return render_template('clouds.html', info=candidate_clouds)

if __name__ == "__main__":
    app.run()