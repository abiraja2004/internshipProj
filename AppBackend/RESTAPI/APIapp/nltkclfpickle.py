from nltk import word_tokenize, WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import NaiveBayesClassifier, classify, probability

import numpy as np
import pickle



def hamorspam(headline):
    stopset = list(set(stopwords.words('english')))
    def word_feats(words):
        return dict([(word, True) for word in words.split() if word not in stopset])

    f = open('/Users/Hallshit/Documents/KnowledgeVC/AppBackend/RESTAPI/APIapp/my_classifier.pickle', 'rb')
    clf = pickle.load(f)
    label = clf.classify(word_feats(headline))
    clfprob = clf.prob_classify(word_feats(headline))
    # print list(clfprob.samples())
    print clfprob.prob(1)
    print label
    return clfprob.prob(1), label

# jdfj = list(dist.samples())
# print list(clf.samples())
# clf = clf.max()
# print clf

# hamorspam('AI is not the future')

