from flask import render_template


def detail():
    return render_template('ilustrations/detail.html')


def list():
    return render_template('ilustrations/list.html')
