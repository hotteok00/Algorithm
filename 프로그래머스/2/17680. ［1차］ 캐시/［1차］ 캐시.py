def solution(cacheSize, cities):
    if cacheSize == 0: return 5 * len(cities)
    
    answer = 0
    cache = {}
    
    for city in cities:
        city = city.lower()
        answer += cache_replacement(city, cache, cacheSize)
        cache_used(cache)
        
    return answer

def cache_hit_miss(city, cache):
    if city in cache: 
        return 1
    else: 
        return 5
    
def cache_replacement(city, cache, cacheSize):
    isHit = cache_hit_miss(city, cache)
    
    if isHit == 1:
        cache[city] = cacheSize
    else:
        if len(cache) >= cacheSize:
            tmp_arr = [(city_, used) for city_, used in cache.items()]
            tmp_arr.sort(key=lambda x: x[1])
            del cache[tmp_arr[0][0]]
        cache[city] = cacheSize
        
    return isHit
    
def cache_used(cache):
    for city, used in cache.items():
        cache[city] = used - 1