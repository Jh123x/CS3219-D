from kafka import KafkaProducer
from json import dumps

producer = KafkaProducer(
    value_serializer=lambda m: dumps(m).encode('utf-8'),
    bootstrap_servers=['localhost:29092', 'localhost:39092'])

producer.send(
    "test",
    value={"hello": "producer"}
)

producer.flush()