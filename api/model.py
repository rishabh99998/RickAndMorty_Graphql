class SingleCharacter:

    def __init__(self ,Id ,name, status, species, Type, gender, image):
        self.name = name
        self.status = status
        self.species = species
        self.Type = Type
        self.gender = gender
        self.image = image
        self.Id = Id
    
    def __str__(self):
        return f"-> {self.name} is a {self.gender}"

    def __repr__(self):
        return f"SingleCharacter({self.Id},{self.name},{self.status},{self.species},{self.Type},{self.gender},{self.image})"

class SingleCharacterInfo:

    def __init__(self , name, status, species, Type, gender, image, origin, location, episode):
        self.name = name
        self.status = status
        self.species = species
        self.Type = Type
        self.gender = gender
        self.image = image
        self.origin = origin
        self.location = location
        self.episode = episode
    
    def __str__(self):
        return f"-> {self.name} is a {self.gender}"

    def __repr__(self):
        return f"SingleCharacterInfo({self.Id},{self.name},{self.status},{self.species},{self.Type},{self.gender},{self.image},{self.origin},{self.location},{self.episode})"
        