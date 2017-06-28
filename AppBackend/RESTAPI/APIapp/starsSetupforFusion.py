import GithubGo
import datetime
import dateutil.parser as dparser


benchmarks = [{'name': 'tensorflow/tensorflow',
               'stars': 34620,
               'years': 1},
               {'name': 'wordpress/wordpress',
                'stars': 2430,
                'years': 2},
                {'name': 'wordpress/wordpress',
                'stars': 6180,
                'years': 4},
               {'name': 'wordpress/wordpress',
                'stars': 8040,
                'years': 5},
                {'name': 'angular/angular.js',
                'stars': 5280,
                'years': 2},
                {'name': 'angular/angular.js',
                'stars': 7950,
                'years': 3},
                {'name': 'angular/angular.js',
                'stars': 18630,
                'years': 4}
]

def convertData(repo):
    repoBenchmarks = []
    name = repo['items'][0]['full_name']
    print repo['items'][0]['created_at']
    # "2012-01-01T00:31:50Z"
    createdAt = dparser.parse(repo['items'][0]['created_at'])
    years = datetime.datetime.today().year - createdAt.year
    for benchmark in benchmarks:
        if benchmark['years'] == years:
            repoBenchmarks.append(benchmark)
    stars = GithubGo.getStargazerCount(repo)
    fusionData = {}

    fusionData['chart'] = {
               "caption": "Number of Stars",
               "subCaption": "after {} years".format(years),
               "theme": "fint"
           }
    fusionData['data'] = [{'label': name,
                           'value': stars}]
    for r in repoBenchmarks:
        fusionData['data'].append({'label': r['name'],
                                  'value': r['stars']})

    return fusionData