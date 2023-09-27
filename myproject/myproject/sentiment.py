import spacy
import asent 
import re

def GetPolarity(text):
    # load spacy pipeline
    nlp = spacy.blank('en')
    nlp.add_pipe('sentencizer')
    nlp.add_pipe('asent_en_v1')

    doc = nlp(text)

    polarity = str(doc._.polarity)
    split_polarity = re.split(' |=', polarity)

    return split_polarity

def GetNeg(text):
    return GetPolarity(text)[1]

def GetNeu(text):
    return GetPolarity(text)[3]

def GetPos(text):
    return GetPolarity(text)[5]

def GetComp(text):
    return GetPolarity(text)[7]

def GetSentiment(text):
    # load spacy pipeline
    nlp = spacy.blank('en')
    nlp.add_pipe('sentencizer')
    nlp.add_pipe('asent_en_v1')

    doc = nlp(text)

    return asent.visualize(doc, style='prediction')
