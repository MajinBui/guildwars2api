from guildwars2api.resources import Resource, IDsLookupMixin


class Skins(Resource, IDsLookupMixin):
    api_class = 'skins'
    
    
class Recipes(Resource, IDsLookupMixin):
    api_class = 'recipes'
    

class Items(Resource, IDsLookupMixin):
    api_class = 'items'
    
    
class Materials(Resource, IDsLookupMixin):
    api_class = 'materials'
    
    
class Search(Resource):
    api_type = 'recipes'
    api_class = 'search'
    
    def get_input(self, item_id=None):
        """
        :param item_id: The item_id when searching for recipes with an item as an ingredient
        :return: List of item_ids that has the input as an ingredient
        """
        
        return super(Search, self).get(input=item_id)
        
    def get_output(self, item_id=None):
        """
        :param item_id: The item id when searching for the recipes that craft an item.
        :return: List of item_ids that are used to make the searched item
        """
        
        return super(Search, self).get(output=item_id)
    
class Continents(Resource, IDsLookupMixin):
    """
        'floors' each continent contains a layer of floors.
    """
    
    class Floors(Resource, IDsLookupMixin):
        api_type = 'continents'
        api_class = 'floors'
        
        def get(self, continent_id, floor_ids=None, lang=None):
            """
            :
            """
            self.api_type = 'continents/' + str(continent_id)
            return super(Continents.Floors, self).get(ids=floor_ids, lang=lang)
        
        
    api_class = 'continents'
    floors = None
    
    
    def get_all(self):
        """
        :return: All continents of the Guild Wars universe
        """
        
        return super(Continents, self).get(ids="all")
    
    
class Maps(Resource, IDsLookupMixin):
    api_class ='maps'
    
    