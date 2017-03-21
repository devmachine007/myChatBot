#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import sys
import google_text_to_text

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

CLIENT_ACCESS_TOKEN = '9682c56f97a34c5e95ae56c2f7b38656'


def run(query):

    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    request = ai.text_request()

    request.lang = 'en'  # optional, default value equal 'en'
    # request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"
    #en_query = google_text_to_text.run(query)
    en_query = query #Testing purpose, remove it later
    request.query = en_query

    response = request.getresponse()

    return response




def main():
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    request = ai.text_request()

    request.lang = 'en'  # optional, default value equal 'en'

    #request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"
    while True:
        query = raw_input("Welcome to myChatBot:\n")
        en_query = google_text_to_text.run(query)
        request.query = en_query

        response = request.getresponse()

        print (response.read())

"""
if __name__ == '__main__':
    main()

"""
