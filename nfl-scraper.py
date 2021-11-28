

#date='20210117'
#away_team='TB'
#away_team_mascot='Buccaneers'
#home_team='NO'
#home_team_mascot='Saints'

def get_nfl_score(date, home_team, away_team, home_team_mascot, away_team_mascot):
    import pandas as pd
    import requests
    from bs4 import BeautifulSoup

    url="https://www.cbssports.com/nfl/gametracker/recap/NFL_"+date+"_"+away_team+"@"+home_team+"/"
    res = requests.get(url)
    soup = BeautifulSoup(res.content,'lxml')
    table = soup.find("table",{"class":"linescore"})
    df = pd.read_html(str(table))[0]

    hometeamscore=df.loc[df[0].str.startswith(home_team_mascot, na=False),5].values[0]
    awayteamscore=df.loc[df[0].str.startswith(away_team_mascot, na=False),5].values[0]

    return [hometeamscore, awayteamscore]


#print(get_nfl_score(date, home_team, away_team, home_team_mascot, away_team_mascot))