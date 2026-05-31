import rabbitpy
import json
from const import *


def producer_pedidos():
    pedidos = [
        {'pedido_id': 1, 'cliente': 'Ana', 'produto': 'Livro', 'quantidade': 1},
        {'pedido_id': 2, 'cliente': 'Bruno', 'produto': 'Caderno', 'quantidade': 3},
        {'pedido_id': 3, 'cliente': 'Carla', 'produto': 'Caneta', 'quantidade': 10}
    ]

    reposicoes = [
        {'produto': 'Livro', 'quantidade': 20},
        {'produto': 'Caneta', 'quantidade': 100}
    ]

    with rabbitpy.Connection(amqp_url()) as conn:
        with conn.channel() as channel:
            exchange = rabbitpy.Exchange(channel, EXCHANGE_NAME, exchange_type='direct')
            exchange.declare()

            queue = rabbitpy.Queue(channel, QUEUE_PEDIDOS, durable=True, auto_delete=False)
            queue.declare()
            queue.bind(exchange, ROUTING_PEDIDOS)

            queue_estoque = rabbitpy.Queue(channel, QUEUE_ESTOQUE, durable=True, auto_delete=False)
            queue_estoque.declare()
            queue_estoque.bind(exchange, ROUTING_ESTOQUE)

            for pedido in pedidos:
                body = json.dumps(pedido)
                message = rabbitpy.Message(channel, body)
                message.publish(exchange, ROUTING_PEDIDOS)
                print(f'Pedido enviado: {body}')

            for reposicao in reposicoes:
                body = json.dumps(reposicao)
                message = rabbitpy.Message(channel, body)
                message.publish(exchange, ROUTING_ESTOQUE)
                print(f'Reposicao enviada: {body}')


if __name__ == '__main__':
    producer_pedidos()
