import json
#If Json data comes as String, as it is common with Client-Server application as infomartion is send
#over the internet

value = """
    {
        "title" : "Tron: Legacy",
        "composer" : "Daft Punk",
        "release_year" : 2010,
        "budget" : 170000000,
        "actors" : null,
        "won_oscars" : false
    } """


tron = json.loads(value)
print(tron)