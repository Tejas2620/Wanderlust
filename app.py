def search_location(query):
    destinations = ['Paris', 'Tokyo', 'New York']
    return [d for d in destinations if query.lower() in d.lower()]
