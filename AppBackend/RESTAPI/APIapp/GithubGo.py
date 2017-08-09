import requests
import pandas as pd
import datetime

# this file contains all the different api requests for Github api



# token = '0f2ded5698764a28ba68e8be8067cc5ea51675bb'
client_id = 'c199fae32b00b0674067'
client_secret = 'a1802908a53236daa527a0cb85888c295ccacedd'
oauthString = 'client_id={}&client_secret={}'.format(client_id, client_secret)

baseurl = 'https://api.github.com/'

def searchRepos(query, **kwargs):
    url = baseurl + 'search/repositories?' + oauthString
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
    url = baseurl + 'repos/{}/stats/commit_activity?'.format(repo) + oauthString
    r = requests.get(url)
    return r.json()

def getContributors(repo):
    try:
        repo = repo['items'][0]['full_name']
    except:
        repo = repo
    url = baseurl + 'repos/{}/stats/contributors?'.format(repo) + oauthString
    r = requests.get(url)
    return r.json()

def getUser(user):
    url = baseurl + 'users/{}?'.format(user) + oauthString
    r = requests.get(url)
    return r.json()

def topContribsFollowers(repo):
    contribs = []
    for c in getContributors(repo):
        contribs.append({'author': c['author']['login'], 'total': c['total']})

    df = pd.DataFrame.from_dict(contribs)
    df = df.sort_values('total', ascending=False).head(5)
    # print df
    totalFollowers = 0
    for x in df.author:
        # print x
        followers = getUser(x)['followers']
        totalFollowers += followers

    return totalFollowers

















