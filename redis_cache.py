import redis

r = redis.Redis(host='localhost',port=6379, db=0)

def check_exists(id):
    if r.exists(id):
        print(f'Data found in cache!')
        return r.get(id)
    print(f'Not found in cache. Inserting...')
    return

def cache(func):
    def wrapper_cache(id):
        
        data = check_exists(id)
        if data is not None:
            return data.decode('utf-8')
        else:
            data = func(id)
            r.setex(id,1500,data)
            return data
    return wrapper_cache

@cache
def search_data_in_redis(id):
    return f"Data {id}"

def insert_data_in_redis(id,value):
    return r.set(id,value)

insert_data_in_redis(22,'My name is Carlos')
insert_data_in_redis(32,'My name is d')
insert_data_in_redis(0,'My name')
#Already data in cache
data = search_data_in_redis(22)
#Not in cache
data = search_data_in_redis(55)
