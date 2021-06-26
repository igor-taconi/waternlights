from flask import render_template


def about():
    return render_template('pages/about.html')


def contact():
    return render_template('pages/contact.html')


def index():
    return render_template('pages/index.html')
