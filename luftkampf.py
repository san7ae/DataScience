import requests, bs4
import csv

headers = {'User-Agent':
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

page = "https://www.ligainsider.de/bundesliga/ranking-top-10/luftkampfquote/"
pageTree = requests.get(page, headers=headers)
pageSoup = bs4.BeautifulSoup(pageTree.content, 'html.parser')

# Write to CSV data
outfile = open('luftkampf.csv','w', encoding="utf-8", newline='')
writer = csv.writer(outfile, delimiter=",")
writer.writerow(["Name", "Verein", "Position", "Einsatz", "SpielMinuten", "GewonneneLuftkaempfe", "GesamteLuftkaempfe"])


player_list = pageSoup.findAll("tr")

for element in player_list:
    try:
        name = element.find("a").text
        verein = element.find("a", {"class":"text-thin"}).text
        position = element.findAll("td", {"class": "text-left"})[2].text

        einsatzStr = element.findAll("td", {"class": "text-right"})[0].text
        einsatz = float(einsatzStr)

        spielminutenStr = element.findAll("td", {"class":"text-right"})[1].text
        spielminuten = float(spielminutenStr)

        gewonneneLuftkaempfeStr = element.findAll("td", {"class": "text-right"})[2].text
        gewonneneLuftkaempfe = float(gewonneneLuftkaempfeStr)

        gesamteLuftkaempfeStr = element.findAll("td", {"class": "text-right"})[3].text
        gesamteLuftkaempfe = float(gesamteLuftkaempfeStr)



        print(name)
        writer.writerow([name, verein, position, einsatz, spielminuten, gewonneneLuftkaempfe, gesamteLuftkaempfe])
    except:
        print("An exception occurred")






outfile.close()
print("======================================================================================")
print ('Done')