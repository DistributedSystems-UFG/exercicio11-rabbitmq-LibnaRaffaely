import rabbitpy
import json
import time
from const import *


def consumer_notificacoes():
    with rabbitpy.Connection(amqp_url()) as conn:
        with conn.channel() as channel:
            queue = rabbitpy.Queue(channel, QUEUE_NOTIFICACOES, durable=True, auto_delete=False)
            while len(queue) > 0:
                message = queue.get()
                if message is None:
                    break
                notificacao = json.loads(message.body.decode())
                print(f"Enviando {notificacao['tipo']} do pedido {notificacao['pedido_id']}")
                time.sleep(1)
                print(f"{notificacao['tipo']} enviado")
                message.ack()


if __name__ == '__main__':
    consumer_notificacoes()
