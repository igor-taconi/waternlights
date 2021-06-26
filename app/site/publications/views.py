from flask import render_template


def detail():
    return render_template('publications/detail.html')


def list():
    return render_template('publications/list.html')
