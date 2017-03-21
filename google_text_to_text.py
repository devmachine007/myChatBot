# -*- coding: utf-8 -*-


import json
import requests


doItAgain = "yes"  # Control While loop


def GetTextAndTranslate(textToTranslate):


    key = "AIzaSyB39OH0NduR9j1uACbGzq_A4aqeP-aqpQM"


    #textToTranslate_encoded=urllib.urlencode(textToTranslate)
    #textToTranslate_encoded=textToTranslate.encode('utf-8')

    source = "hi"
    target = "en"

   # & q = hello & source = en & target = fr & model = nmt

    # Call to Microsoft Translator Service
    #headers = {"Authorization ": "Bearer" + token}
    translateUrl = "https://translation.googleapis.com/language/translate/v2/?key={}&q={}&source={}&target={}".format(key,
                                                                                                                      textToTranslate,
                                                                                                             source,target)
    # translateUrl = "https://api.microsofttranslator.com/v2/http.svc/Translate?text={}&to={}".format(textToTranslate, toLangCode)

    #print translateUrl

    try:
        #translationData = requests.get(translateUrl, headers=headers)  # make request
        translationData = requests.get(translateUrl)  # make request
        #translation = ElementTree.fromstring(translationData.text.encode('utf-8'))  # parse xml return values
        #print "The translation is---> ", translationData.content  # display translation
        return translationData.content

    except OSError:
        pass

    print " "


# End GetTextAndTranslate()

def jsonParser(jsonData):
    data = json.loads(jsonData)
    return str(data["data"]["translations"][0]["translatedText"])



def run(textToTranslate):
    jsonData = GetTextAndTranslate(textToTranslate)
    engText = jsonParser(jsonData)
    return engText

"""
if __name__ == "__main__":
    textToTranslate = "kesy ho"
    GetTextAndTranslate(textToTranslate)


# end main
"""
#res = run("aap log kitni equity lety ho?")
#print res