import GithubGo

def convertData(repo):
    fusionData = {}
    bms = ['mongodb/mongo', 'docker/compose', 'aws/aws-cli', 'wordpress/wordpress']
    try:
        followers = GithubGo.topContribsFollowers(repo)
    except:
        followers = 'no value'
    fusionData['chart'] = {
        "caption": "Top 5 Contributors Follower Count",
        "subCaption": "%s" % repo['items'][0]['full_name'],
        "theme": "fint"
    }
    fusionData['data'] = [{'label': repo['items'][0]['full_name'],
                           'value': followers}]
    for bm in bms:
        try:
            repo = bm
            fusionData['data'].append({
                'label': repo,
                'value': GithubGo.topContribsFollowers(repo)
            })
        except:
            print "contrib request failed"
    return fusionData


