import json #including the json library for handling .json files
import requests #For making request to the website


#Storing the requested information to DataJson
DataJson = requests.get('https://favqs.com/api/qotd').text

#Converting the DataJson into a dictionary
data = json.loads(DataJson)

quotes = data['quote']['body']
authors = data['quote']['author']

def quote():
    return quotes
def author():
    return authors
def quote_author():
    return f'{quote} by {author}'

