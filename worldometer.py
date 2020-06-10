#!/usr/bin/env python
# encoding: utf-8
from bs4 import BeautifulSoup
import bs4.element
from flask import (Flask, render_template)
import requests

wm = None

ATTR_WHITELIST = {'class', 'id', 'href'}


def cleanup_tag(tag):
    """
    Removes all unnecessary attributes from a tag. These are mostly styling related.
    :param tag:
    :return:
    """
    attrs = list(tag.attrs.keys())
    for attr in attrs:
        if attr in ATTR_WHITELIST:
            continue
        if attr.startswith('data-'):
            continue
        del tag[attr]


def cleanup_fragment(item):
    """
    Removes all unnecessary attributes from a tag and all its descendants
    :param item:
    :return:
    """
    cleanup_tag(item)
    for t in item.descendants:
        if isinstance(t, bs4.element.Tag):
            cleanup_tag(t)


def load_worldometer():
    print ('Loading worldometer data')
    site = requests.get('https://www.worldometers.info/coronavirus/')
    if site.status_code != 200:
        raise RuntimeError('Cannot fetch countries')
    soup = BeautifulSoup(site.content, 'html.parser')
    item = soup.find('table')
    cleanup_fragment(item)
    return item


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('wm.html', data=wm.prettify())


def main():
    global wm
    wm = load_worldometer()
    app.run(debug=True)


if __name__ == '__main__':
    main()
