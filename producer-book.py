import rabbitpy
import json
from const import *

def producer_pagamentos():
  pagamentos = [
    {'pedido_id': 1, 'status': 'pago', 'valor': 49.9},
    {'pedido_id': 2, 'status': 'pago', 'valor': 36.0},
    {'pedido_id': 3, 'status': 'pago', 'valor': 15.0}
  ]

  notificacoes = [
    {'pedido_id': 1, 'tipo': 'email', 'mensagem': 'Seu pedido foi confirmado'},
    {'pedido_id': 2, 'tipo': 'sms', 'mensagem': 'Pagamento aprovado'},
    {'pedido_id': 3, 'tipo': 'email', 'mensagem': 'Pedido em separacao'}
  ]

  with rabbitpy.Connection(amqp_url()) as conn:
    with conn.channel() as channel:
      exchange = rabbitpy.Exchange(channel, EXCHANGE_NAME, exchange_type='direct')
      exchange.declare()

      queue_pag = rabbitpy.Queue(channel, QUEUE_PAGAMENTOS, durable=True, auto_delete=False)
      queue_pag.declare()
      queue_pag.bind(exchange, ROUTING_PAGAMENTOS)

      queue_not = rabbitpy.Queue(channel, QUEUE_NOTIFICACOES, durable=True, auto_delete=False)
      queue_not.declare()
      queue_not.bind(exchange, ROUTING_NOTIFICACOES)

      for pagamento in pagamentos:
        body = json.dumps(pagamento)
        message = rabbitpy.Message(channel, body)
        message.publish(exchange, ROUTING_PAGAMENTOS)
        print(f'Pagamento enviado: {body}')

      for notificacao in notificacoes:
        body = json.dumps(notificacao)
        message = rabbitpy.Message(channel, body)
        message.publish(exchange, ROUTING_NOTIFICACOES)
        print(f'Notificacao enviada: {body}')


if __name__ == '__main__':
  producer_pagamentos()
