import rabbitpy
import json
import time
from const import *


def consumer_estoque():
    with rabbitpy.Connection(amqp_url()) as conn:
        with conn.channel() as channel:
            queue = rabbitpy.Queue(channel, QUEUE_ESTOQUE, durable=True, auto_delete=False)
            while len(queue) > 0:
                message = queue.get()
                if message is None:
                    break
                reposicao = json.loads(message.body.decode())
                print(f"Atualizando estoque de {reposicao['produto']}")
                time.sleep(1)
                print(f"Estoque de {reposicao['produto']} atualizado")
                message.ack()


if __name__ == '__main__':
    consumer_estoque()
