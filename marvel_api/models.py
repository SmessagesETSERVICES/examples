class character:
    def __init__(self, id, name, description, thumbnail):
        self.id = id
        self.name = name
        self.description = description
        self.thumbnail = thumbnail
        
class events:
    def __init__(self, items, collectionURI, available):
        self.items = items
        self.available = available
        self.collectionURI = collectionURI
    
    
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            items=data['items'],
            available= data['available'],
            returned=data['collectionURI']    
        )    
