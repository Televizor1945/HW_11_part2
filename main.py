from flask import Flask, render_template

from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)

data = load_candidates_from_json("candidates.json")


@app.route("/")
def home():
    return render_template("home.html", candidates=data)


@app.route("/candidate/<int:uid>")
def profile(uid):
    candidate = get_candidate(uid)
    return render_template("profile.html", candidate=candidate)


@app.route("/search/<candidate_name>")
def search(candidate_name):
    candidate_count, candidate_n = get_candidates_by_name(candidate_name)
    return render_template("seartch.html", count=candidate_count, candidate_list=candidate_n)


@app.route("/skill/<skill_name>")
def get_skills(skill_name):
    candidate_skill_count, candidates_name, = get_candidates_by_skill(skill_name)
    return render_template("skills.html", count_skill=candidate_skill_count, candidate_list=candidates_name, skill_name=skill_name)


app.run(debug=True)