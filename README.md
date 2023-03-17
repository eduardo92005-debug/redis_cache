Redis Cache Python using

## 📋 Description
Redis is an in-memory data structure store that can be used as a database, cache, and message broker. It is often referred to as a "data structure server" because it can support various data structures such as strings, hashes, lists, sets, and more. Redis is known for its performance, high availability, and scalability, making it a popular choice for many applications that require fast and reliable data access.

Redis supports various features such as transactions, pub/sub messaging, Lua scripting, and more. It also has support for clustering, allowing it to scale horizontally by distributing data across multiple nodes.

Redis is often used as a cache, where frequently accessed data can be stored in memory to improve performance. It can also be used as a message broker, where it provides a fast and reliable way to exchange messages between applications.

Redis has a wide range of use cases, from simple caching to complex data processing and analysis. It is widely adopted by many companies and organizations, including GitHub, Twitter, and Craigslist.

Overall, Redis is a powerful and versatile tool that provides fast and reliable data access, making it a valuable addition to any technology stack.
## 📦 How to use
## Install docker
1. Install Docker on your machine, if you haven't already done so.

2. Open your terminal or command prompt and execute the following command to download the redis image:

3. ```docker pull redis```

4. Once the image is downloaded, run the following command to start a RabbitMQ container on port 8080:

6. ```docker run -d --name redis-container -p 6379:6379```

7. This command will start a Redis container and expose port 6379.

8. After the container is started:

9. You can also use the redis-cli

10.``` docker exec -it redis-container bash``` 

### Install package redis in python
1. ```python3 -m pip install redis```
### Use Redis
1. Run ```python3 redis_cache.py```

