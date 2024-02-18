import os

import redis


class RedisManager:

    __redis_client = None

    @staticmethod
    def get_redis_client():

        if RedisManager.__redis_client is None:
            redis_host = os.getenv('REDIS_HOST')
            redis_port = os.getenv('REDIS_PORT')
            redis_db = os.getenv('REDIS_DB')
            connection_pool = redis.ConnectionPool(host=redis_host, port=redis_port, db=redis_db)
            RedisManager.__redis_client = redis.StrictRedis(connection_pool=connection_pool)

        return RedisManager.__redis_client
