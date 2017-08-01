from google.cloud import language
from bs4 import BeautifulSoup
import urllib2
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from string import punctuation
from heapq import nlargest
import re
import os
import pdb
from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import sys
import Algorithmia
import requests
reload(sys)
sys.setdefaultencoding("utf-8")

# This file contains the 3 summarizers for the text on the companies homepage (the sumy is the best one so far)

# nltk summarizer from http://glowingpython.blogspot.com/2014/09/text-summarization-with-nltk.html

class FrequencySummarizer:
  def __init__(self, min_cut=0.1, max_cut=0.9):
    """
     Initilize the text summarizer.
     Words that have a frequency term lower than min_cut
     or higer than max_cut will be ignored.
    """
    self._min_cut = min_cut
    self._max_cut = max_cut
    self._stopwords = set(stopwords.words('english') + list(punctuation))

  def _compute_frequencies(self, word_sent):
    """
      Compute the frequency of each of word.
      Input:
       word_sent, a list of sentences already tokenized.
      Output:
       freq, a dictionary where freq[w] is the frequency of w.
    """
    freq = defaultdict(int)
    for s in word_sent:
      for word in s:
        if word not in self._stopwords:
          freq[word] += 1
    # frequencies normalization and fitering
    m = float(max(freq.values()))
    for w in freq.keys():
      freq[w] = freq[w]/m
      if freq[w] >= self._max_cut or freq[w] <= self._min_cut:
        del freq[w]
    return freq

  def summarize(self, text, n):
    """
      Return a list of n sentences
      which represent the summary of text.
    """
    sents = sent_tokenize(text)
    assert n <= len(sents)
    word_sent = [word_tokenize(s.lower()) for s in sents]
    self._freq = self._compute_frequencies(word_sent)
    ranking = defaultdict(int)
    for i,sent in enumerate(word_sent):
      for w in sent:
        if w in self._freq:
          ranking[i] += self._freq[w]
    sents_idx = self._rank(ranking, n)
    return [sents[j] for j in sents_idx]

  def _rank(self, ranking, n):
    """ return the first n sentences with highest ranking """
    return nlargest(n, ranking, key=ranking.get)


def analyzeText(text):
    client = language.Client()
    document = client.document_from_text(text)
    sent_analysis = document.analyze_sentiment()
    sentiment = sent_analysis.sentiment
    ent_analysis = document.analyze_entities()
    entities = ent_analysis.entities
    return sentiment, entities


def getTextFromURL(company):
    url = "https://autocomplete.clearbit.com/v1/companies/suggest?query={}".format(company)
    req = requests.get(url)
    domain = req.json()[0]['domain']
    domain = 'http://{}'.format(domain)
    req = urllib2.Request(domain, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib2.urlopen(req).read()
    soup = BeautifulSoup(html, 'html.parser')
    for script in soup(["script", "style", "ul", "a", "li", "nav", {'class': 'demo'}]):
        script.extract()
    body = soup.find('body')
    texts = body.get_text(" ").replace('\n', '')
    return texts

# def runTextAnalyzer(url):
#     # Returns sentiment, entities tuple
#     text = getTextFromURL(url)
#     return analyzeText(text)

# url = 'https://www.clarifai.com/'

def convertToWordCloud(text):
    wordCloudList = []
    sent, ent = analyzeText(text)
    for e in ent:
        wordCloudList.append([e.name, e.salience*1500])
    return wordCloudList

def nltkSummarize(text):
    fs = FrequencySummarizer()
    summary = fs.summarize(text, 3)
    return " ".join(summary)


# Github Repo Sumy Summarizer https://github.com/miso-belica/sumy

def sumySummarize(url):
    fullSummary = []
    LANGUAGE = 'english'
    SENTENCES_COUNT = 3
    parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    # or for plain text files
    # parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    # for sentence in summarizer(parser.document, SENTENCES_COUNT):
    #     summary.append(sentence)
    summary = summarizer(parser.document, SENTENCES_COUNT)
    summary = list(summary)
    # print summary.__str__()
    for s in summary:
        fullSummary.append(s.__str__())

    return " ".join(fullSummary)


def algorithmiaSummarizer(text):
    client = Algorithmia.client('simwznxkXitKpwgslrekEqZftfC1')
    algo = client.algo('nlp/Summarizer/0.1.6')
    return algo.pipe([text, 2]).result
