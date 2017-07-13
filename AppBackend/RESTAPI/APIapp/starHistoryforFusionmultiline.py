import GithubGo
import datetime
import pandas as pd
import starhistorybenchmarks
import pdb
import numpy as np




def convertData(repo):
    # repo = repo['items'][0]['full_name']
    print repo['items'][0]['full_name']
    firstCreated = ''
    currentStars = 0
    dosYearsOfStars = []
    numberOfPages = iter(range(1, 300))
    for p in numberOfPages:
        print p
        stars = GithubGo.getStargazers(repo, p)

        try:
            topdate = datetime.datetime.strptime(stars[0]['starred_at'], '%Y-%m-%dT%H:%M:%SZ')
            print topdate
        except:
            break
        botdate = datetime.datetime.strptime(stars[-1]['starred_at'], '%Y-%m-%dT%H:%M:%SZ')
        print botdate
        if p == 1:
            currentStars += 100
            firstCreated = topdate
        if (botdate - firstCreated).days >= 704:
            print "two years reached"
            break

        if (botdate - topdate).days < 1:
            dosYearsOfStars.append({'label': botdate.strftime('%m-%y'), 'value': currentStars})
            currentStars += 500
            print dosYearsOfStars
            next(numberOfPages)
            next(numberOfPages)
            next(numberOfPages)
            next(numberOfPages)
        elif (botdate - topdate).days >= 1 and (botdate - topdate).days <= 5:
            dosYearsOfStars.append({'label': botdate.strftime('%m-%y'), 'value': currentStars})
            currentStars += 300
            print dosYearsOfStars
            next(numberOfPages)
            next(numberOfPages)
        else:
            dosYearsOfStars.append({'label': botdate.strftime('%m-%y'), 'value': currentStars})
            currentStars += 200
            next(numberOfPages)


            # stars.to_csv('/Users/Hallshit/Documents/GithubAPITests/samplestargazers.csv')
    fusionChart = {}
    fusionChart['chart'] = {
        "caption": "First Two Year Star Growth",
        "subCaption": "{}".format(repo['items'][0]['full_name']),
        "captionFontSize": "14",
        "subcaptionFontSize": "14",
        "subcaptionFontBold": "0",
        "paletteColors": "#0075c2,#1aaf5d,#ff0000,#ff6600,#42d7f4",
        "bgcolor": "#ffffff",
        "showBorder": "0",
        "showShadow": "0",
        "showCanvasBorder": "0",
        "usePlotGradientColor": "0",
        "legendBorderAlpha": "0",
        "legendShadow": "0",
        "showAxisLines": "1",
        "showAlternateHGridColor": "0",
        "divlineThickness": "1",
        "divLineIsDashed": "1",
        "divLineDashLen": "1",
        "divLineGapLen": "1",
        "xAxisName": "Time",
        "yAxisName": "Stars",
        "showValues": "0",

}
    fusionChart['categories'] = [{'category': [{'label': 0}]}]
    for x in range(1,25):
        fusionChart['categories'][0]['category'].append({'label': x})
        print x

    # pdb.set_trace()



    df = pd.DataFrame(data=dosYearsOfStars)


    df = df.groupby(df['label']).max()

    df.index = pd.to_datetime(df.index, format='%m-%y')
    df = df.sort_index()


    df['label'] = df.index
    # pdb.set_trace()
    df['label'] = df['label'] - df['label'].iloc[0]
    df['label'] = df['label'].apply(lambda x: round(x.days/30))
    df = df.groupby(df['label']).max()
    df = df.sort_index()
    df['label'] = df.index
    print "Original df"
    print df

    # pdb.set_trace()
    last = int(df['label'].tail(1).values[0])
    print last
    # pdb.set_trace()

    for x in range(0, last):
        if (df.loc[df['label'] == float(x)]).empty:
            v0 = df['value'].iloc[x-1]
            v2 = df['value'].iloc[x]
            m0 = df['label'].iloc[x-1]
            m1 = x
            m2 = df['label'].iloc[x]
            print v0, v2, m0, m1, m2
            value = (v0*(m2-m1) + v2*(m1-m0))/(m2-m0)
            print value
            # pdb.set_trace()
            df = df.append(pd.DataFrame([[int(value), float(x)]], columns=['value', 'label']))
            df = df.sort_values('label')

            print df

        else:
            print x


    print df

    starhistory = df.to_dict(orient='records')
    # pdb.set_trace()
    values = df.to_dict('list')['value']
    data = [{'value': values[0]}]
    for x in values[1:]:
        data.append({'value': x})
    fusionChart['dataset'] = []

    fusionChart['dataset'].append({'seriesname': repo['items'][0]['full_name'],
                                   'data': data})
    fusionChart['dataset'].append(starhistorybenchmarks.msangular)
    fusionChart['dataset'].append(starhistorybenchmarks.msmongodb)
    fusionChart['dataset'].append(starhistorybenchmarks.mswordpress)
    fusionChart['dataset'].append(starhistorybenchmarks.msdjango)


    # fusionChart['trendlines'] = [ {
    #         "line": [
    #             {
    #                 "startvalue": "100",
    #                 "color": "#6baa01",
    #                 "valueOnRight": "1",
    #                 "displayvalue": "Average"
    #
    #             }]
    # }]
    print fusionChart['dataset']
    return fusionChart

# repo = GithubGo.searchRepos('mongodb/mongo')
# print convertData(repo)