# coding=utf-8

import redis

#��ȡredis���ӳ�
Pool = redis.ConnectionPool(host='127.0.0.1', port = 6379, max_connections = 10)

#��redis���ӳػ�ȡһ������
conn = redis.Redis(connect_pool=pool, decode_responses=True)
print(conn.get('name').decode('utf-8'))
