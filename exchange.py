import pika
import sys

conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = conn.channel()
channel.exchange_declare(exchange='actions', exchange_type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'
message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='actions',
                      routing_key=routing_key,
                      body=message)

print(" [x] Sent %r" % message)

conn.close()