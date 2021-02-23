import requests
from api.model import SingleCharacterInfo
from api.Exception import RAM_Exception

def query(id):
    query = ("""query{
                character(id:%d){
                    name
                    status
                    species
                    type
                    gender
                    image
                    origin{
                        name
                        }
                    location{
                        name
                        }
                    episode{
                        name
                        episode
                        }
                }
            }""" %(id))
    return query


class characterInfo:
    def infoData(self,id):
        url = 'https://rickandmortyapi.com/graphql/'
        json = {'query':query(id)}
        r = requests.post(url=url, json=json)
        if r.status_code != 200:
            raise RAM_Exception(r.status_code)
        json_response = r.json()
        Character = json_response['data']['character']
        return SingleCharacterInfo(Character['name'],Character['status'],Character['species'],Character['type'],Character['gender'],Character['image'],Character['origin'],Character['location'],Character['episode'])
        