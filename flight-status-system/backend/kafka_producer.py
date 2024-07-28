from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def send_notification(notification):
    producer.send('flight_notifications', notification)

notification = {'user': 'user1', 'message': 'Your flight has been delayed'}
send_notification(notification)
