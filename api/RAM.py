import requests
from api.model import SingleCharacter
from api.Exception import RAM_Exception

def query():
    query = """query {
                characters {
                    results {
                    id
                    name
                    status
                    species
                    type
                    gender
                    image
                    }
                }
            }"""
    return query


class RickAndMorty:

    def graphData(self):
        url = 'https://rickandmortyapi.com/graphql/'
        json = {'query':query()}
        r = requests.post(url, json=json)
        if r.status_code != 200:
            raise RAM_Exception(r.status_code)    
        json_response = r.json()
        Characters=json_response['data']['characters']['results']

        return [ SingleCharacter(Character['id'],Character['name'],Character['status'],Character['species'],Character['type'],Character['gender'],Character['image']) for Character in Characters ]
        