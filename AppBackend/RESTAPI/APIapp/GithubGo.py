import requests
import pandas as pd
import datetime

# token = '0f2ded5698764a28ba68e8be8067cc5ea51675bb'
client_id = 'c199fae32b00b0674067'
client_secret = 'a1802908a53236daa527a0cb85888c295ccacedd'
oauthString = 'client_id={}&client_secret={}'.format(client_id, client_secret)

baseurl = 'https://api.github.com/'

def searchRepos(query, **kwargs):
    url = baseurl + 'search/repositories'
    params = {'q': query}
    for k in kwargs:
        params[k] = kwargs[k]
    r = requests.get(url, params)
    repo = r.json()
    return repo


    # for item in json['items']:
    #     print item['full_name']

def getStargazers(repo, page):
    repo = repo['items'][0]['full_name']
    url = baseurl + 'repos/{}/stargazers?'.format(repo) + oauthString
    payload = {'per_page': '100', 'page': page}
    headers = {'Accept': 'application/vnd.github.v3.star+json'}
    r = requests.get(url, payload, headers=headers)
    r = r.json()
    # print len(r)
    return r


def getStargazerCount(repo):
    stargazers = repo['items'][0]['stargazers_count']
    return stargazers





# gets last year of commits
def getCommitActivity(repo):
    repo = repo['items'][0]['full_name']
    url = baseurl + 'repos/{}/stats/commit_activity'.format(repo)
    r = requests.get(url)
    return r.json()

def getContributors(repo):
    repo = repo['items'][0]['full_name']
    url = baseurl + 'repos/{}/stats/contributors'.format(repo)
    r = requests.get(url)
    return r.json()





# repo = searchRepos('tensorflow', sort='stars')











