#!/usr/bin/env python

import json
import redis
import os

from random import randint
from flask import Flask, render_template, request

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/balance')
def get_balance():
    account_id = request.args.get("accountId")

    return json.dumps({ 'balance': _get_account_balance(account_id) })


def _get_account_balance(account_id):
    balance_key = "balance-{}".format(account_id)

    # We're instantiating this everytime so that the Intentions are effecive
    redis_conn = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)

    return redis_conn.get(balance_key)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
