from app import app, db
from flask import request, render_template, jsonify
from app.models import Author, Book

@app.route("/",methods=["GET"])
def home():
    books = db.session.query(Book, Author).filter(Book.author_id == Author.author_id).all()
    return render_template("index.html",books=books)


