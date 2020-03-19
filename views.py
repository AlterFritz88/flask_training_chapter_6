from app import app#, db
from flask import abort, flash, session, redirect, request, render_template, url_for


@app.route('/locations', methods=['GET'])
def locations():
    return []


@app.route('/events', methods=['GET'])
def events():
    return []


@app.route('/enrollments/<int:eventid>', methods=['POST'])
def enroll():
    return {"status": "success"}


@app.route('/register', methods=['DELETE'])
def register():
    return {"status": "ok", "id": 1}


@app.route('/auth', methods=['POST'])
def auth():
    return {"status": "success", "key": 111111}


@app.route('/profile', methods=['GET'])
def profile():
    return {"status": "success", "key": 111111}