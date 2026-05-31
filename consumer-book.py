import rabbitpy
import json
import time
from const import *

def consumer_pagamentos():
    with rabbitpy.Connection(amqp_url()) as conn:
        with conn.channel() as channel:
            queue = rabbitpy.Queue(channel, QUEUE_PAGAMENTOS, durable=True, auto_delete=False)
            while len(queue) > 0:
                message = queue.get()
                if message is None:
                    break
                pagamento = json.loads(message.body.decode())
                print(f"Registrando pagamento do pedido {pagamento['pedido_id']}")
                time.sleep(1)
                print(f"Pagamento do pedido {pagamento['pedido_id']} confirmado")
                message.ack()


if __name__ == '__main__':
    consumer_pagamentos()
