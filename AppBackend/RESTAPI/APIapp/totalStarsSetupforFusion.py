import GithubGo
import datetime
import dateutil.parser as dparser


benchmarks = [{'name': 'tensorflow/tensorflow',
               'stars': 34620,
               'years': 1},
                {'name': 'wordpress/wordpress',
                'stars': 1500,
                'years': 1},
               {'name': 'wordpress/wordpress',
                'stars': 2430,
                'years': 2},
                {'name': 'wordpress/wordpress',
                'stars': 4320,
                'years': 3},
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
                'years': 4},
                {'name': 'mongodb/mongo',
                'stars': 1500,
                'years': 1},
                {'name': 'mongodb/mongo',
                'stars': 2310,
                'years': 2},
                {'name': 'mongodb/mongo',
                'stars': 3090,
                'years': 3},
                {'name': 'mongodb/mongo',
                'stars': 3870,
                'years': 4},
                {'name': 'mongodb/mongo',
                'stars': 5000,
                'years': 5},
               {"name": 'django/django',
                'stars': 5280,
                'years': 1},
                {"name": 'django/django',
                'stars': 8850,
                'years': 2},
                {"name": 'django/django',
                'stars': 12390,
                'years': 3},
                {"name": 'django/django',
                'stars': 17730,
                'years': 4},
                {"name": 'django/django',
                'stars': 24870,
                'years': 5}
]

def convertData(repo):
    repoBenchmarks = []
    name = repo['items'][0]['full_name']
    # print repo['items'][0]['created_at']
    # "2012-01-01T00:31:50Z"
    createdAt = dparser.parse(repo['items'][0]['created_at'])
    years = datetime.datetime.today().year - createdAt.year
    for benchmark in benchmarks:
        if benchmark['years'] == years:
            repoBenchmarks.append(benchmark)
    stars = GithubGo.getStargazerCount(repo)
    fusionData = {}

    fusionData['chart'] = {
               "caption": "Total Stars",
               "subCaption": "after {} years".format(years),
               # "theme": "zune"
               "bgcolor": "#ffffff",
           }
    fusionData['data'] = [{'label': name,
                           'value': stars}]
    for r in repoBenchmarks:
        fusionData['data'].append({'label': r['name'],
                                  'value': r['stars']})

    return fusionData