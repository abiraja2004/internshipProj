import GithubGo
import datetime
import pandas as pd
import starhistorybenchmarks



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
    fusionChart['chart'] = {"caption": "{} Star Growth".format(repo['items'][0]['full_name']),
    "subCaption": "First two years",
    "xAxisName": "Date",
    "yAxisName": "Stars",

    "lineThickness": "2",
    "paletteColors": "#0075c2",
    "baseFontColor": "#333333",
    "baseFont": "Helvetica Neue,Arial",
    "captionFontSize": "14",
    "subcaptionFontSize": "14",
    "subcaptionFontBold": "0",
    "showBorder": "0",
    "bgColor": "#ffffff",
    "showShadow": "0",
    "canvasBgColor": "#ffffff",
    "canvasBorderAlpha": "0",
    "divlineAlpha": "100",
    "divlineColor": "#999999",
    "divlineThickness": "1",
    "divLineIsDashed": "1",
    "divLineDashLen": "1",
    "divLineGapLen": "1",
    "showXAxisLine": "1",
    "xAxisLineThickness": "1",
    "xAxisLineColor": "#999999",
    "showAlternateHGridColor": "0",
    "labelDisplay": "auto",
    "slantLabels": "1"
    # "labelStep": "150",

}
    df = pd.DataFrame(data=dosYearsOfStars)

    df = df.groupby(df['label']).max()
    print df
    df.index = pd.to_datetime(df.index, format='%m-%y')
    df = df.sort_index()
    df['label'] = df.index
    df['label'] = df['label'].apply(lambda x: datetime.datetime.strftime(x, format='%m-%Y'))
    starhistory = df.to_dict(orient='records')

    fusionChart['data'] = starhistory
    return fusionChart

    # print stars