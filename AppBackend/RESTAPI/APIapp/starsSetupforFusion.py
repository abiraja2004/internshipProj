import GithubGo
import datetime
import dateutil.parser as dparser


def convertData(repo):
    name = repo['items'][0]['full_name']
    # "2012-01-01T00:31:50Z"
    createdAt = dparser.parse(repo['items'][0]['created_at'])
    years = datetime.datetime.today().year - createdAt.year
    stars = GithubGo.getStargazerCount(repo)
    fusionData = {}

    fusionData['chart'] = {
               "caption": "Number of Stars",
               "subCaption": "{} years".format(years),
               "theme": "fint"
           }
    fusionData['data'] = [{'label': name,
                           'value': stars}]
    return fusionData