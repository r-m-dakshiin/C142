from flask import Flask,jsonify, request
import csv
import pandas as pd


all_movies = []

with open('movies.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

liked_movies = []
not_liked_movies = []
did_not_watched = []

app = Flask(__name__)

@app.route("/get-movie")

def get_movie():
    return jsonify({
        "data" : all_movies[0],
        "status" : "success"
    })

@app.route("/liked-movie", methods = ["POST"])

def liked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
        "data" : liked_movies,
        "status" : "success"
    })

@app.route("/not_liked_movie", methods = ["POST"])

def not_liked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]

    
    not_liked_movies.append(movie)
    return jsonify({
        "data" : not_liked_movies,
        "status" : "success"
    })



@app.route("/did_not_watched", methods = ["POST"])

def did_not_watched():
    movie = all_movies[0]
    all_movies = all_movies[1:]

    
    did_not_watched.append(movie)
    return jsonify({
        "data" : did_not_watched,
        "status" : "success"
    })

if __name__ == "__main__":
    app.run()