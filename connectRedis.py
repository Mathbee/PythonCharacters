# coding=utf-8

import redis

#获取redis连接池
Pool = redis.ConnectionPool(host='127.0.0.1', port = 6379, max_connections = 10)

#从redis连接池获取一个链接
conn = redis.Redis(connect_pool=pool, decode_responses=True)
print(conn.get('name').decode('utf-8'))
