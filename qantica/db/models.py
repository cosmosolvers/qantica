



class Query:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
    
    def __repr__(self):
        return f"<{self.__class__.__name__} object>"
    
    def create(self):
        pass
    
    def save(self):
        pass
    
    def delete(self):
        pass
    
    def update(self):
        pass
    
    def get(self):
        pass
    
    def all(self):
        pass
    
    def filter(self):
        pass
    
    def exclude(self):
        pass
    
    def order_by(self):
        pass
    
    def sort(self):
        pass
    
    def reverse(self):
        pass
    
    def limit(self):
        pass
    
    def offset(self):
        pass
    
    def count(self):
        pass
    
    def exists(self):
        pass
    
    def values(self):
        pass
    
    def values_list(self):
        pass
    
    def distinct(self):
        pass
    
    def annotate(self):
        pass
    
    def aggregate(self):
        pass
    
    def raw(self):
        pass
    
    def extra(self):
        pass
    
    def defer(self):
        pass
    
    def only(self):
        pass
    
    def using(self):
        pass
    
    def select_for_update(self):
        pass
    
    def select_related(self):
        pass
    
    def prefetch_related(self):
        pass
    
    def get_or_create(self):
        pass
    
    def update_or_create(self):
        pass
    
    def first(self):
        pass
    
    def last(self):
        pass
    
    def in_bulk(self):
        pass
    
    def iterator(self):
        pass
    
    def _clone(self):
        pass
    
    def _fetch_all(self):
        pass
    
    def _fetch_single(self):
        pass




class Model:
    
    query = Query()

