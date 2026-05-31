RABBITMQ_ADDR = '127.0.0.1'
RABBITMQ_USER = 'myuser'
RABBITMQ_PASSWORD = 'abc123'
RABBITMQ_VHOST = 'my_vhost'

EXCHANGE_NAME = 'app-exchange'

QUEUE_PEDIDOS = 'fila-pedidos'
QUEUE_PAGAMENTOS = 'fila-pagamentos'
QUEUE_ESTOQUE = 'fila-estoque'
QUEUE_NOTIFICACOES = 'fila-notificacoes'

ROUTING_PEDIDOS = 'pedido.criado'
ROUTING_PAGAMENTOS = 'pagamento.recebido'
ROUTING_ESTOQUE = 'estoque.repor'
ROUTING_NOTIFICACOES = 'notificacao.enviar'


def amqp_url():
	return f'amqp://{RABBITMQ_USER}:{RABBITMQ_PASSWORD}@{RABBITMQ_ADDR}:5672/{RABBITMQ_VHOST}'
