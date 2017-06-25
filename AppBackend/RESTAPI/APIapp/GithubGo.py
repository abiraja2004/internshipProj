import requests

# token = '0f2ded5698764a28ba68e8be8067cc5ea51675bb'

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

def getStargazers(repo):
    repo = repo['items'][0]['full_name']
    url = baseurl + 'repos/{}/stargazers'.format(repo)
    payload = {'per_page': '100', 'page': '8'}
    headers = {'Accept': 'application/vnd.github.v3.star+json'}
    r = requests.get(url, payload, headers=headers)
    r = r.json()
    print len(r)
    for star in r:
        print star['starred_at']


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



repo = searchRepos('tensorflow', sort='stars')











