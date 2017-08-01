from bs4 import BeautifulSoup
import urllib2
import Algorithmia
import GithubGo
from itertools import islice

# This file scrapes the github's trending page for repos.
# Then gets all other relevant data through api's (stars, tags, description)
# Probably is faster to just get stars, tags, and description through original scrape

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))


# input = ["rails","rails"]




def scrapeTrending():
    repos = []
    url = 'https://github.com/trending?since=monthly'
    req = urllib2.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib2.urlopen(req).read()
    # html = urllib2.urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    repoList = soup.find('ol', {'class': "repo-list"})
    for item in repoList.find_all('li')[:10]:
        repo = item.find('a').text
        repo = repo.replace(" ", "").strip()
        print repo
        repos.append(repo)
    return repos


def getTags(repo):
    repoPath = repo.split('/')
    client = Algorithmia.client('simwznxkXitKpwgslrekEqZftfC1')
    algo = client.algo('tags/AutoTagGithub/0.1.4')
    return algo.pipe(repoPath).result

def getRepoData(repo):
    repo = GithubGo.searchRepos(repo, sort='stars')
    repo = repo['items'][0]
    stars = repo['stargazers_count']
    description = repo['description']
    return stars, description

def setupTrendingDict():
    trendingRepos = []
    repos = scrapeTrending()
    for r in repos[:5]:
        repoDict = {}
        repoDict['repo'] = r
        repoDict['tags'] = take(4, getTags(r).iteritems())

        print repoDict['tags']
        stars, description = getRepoData(r)
        repoDict['stars'] = stars
        repoDict['description'] = description
        trendingRepos.append(repoDict)
    return trendingRepos





