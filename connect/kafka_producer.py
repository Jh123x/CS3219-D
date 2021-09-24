import argparse
from kafka import KafkaProducer
from json import dumps


def start_producer(ip_servers: list, message:str):
    """Pushes a dictionary to kafka"""
    producer = KafkaProducer(
        value_serializer=lambda m: dumps(m).encode('utf-8'),
        bootstrap_servers=ip_servers)

    producer.send(
        "test",
        value={"header": message}
    )

    producer.flush()


if __name__ == "__main__":
    default_servers = ['localhost:29092', 'localhost:39092']
    parser = argparse.ArgumentParser()
    parser.add_argument("message", type=str)
    parser.add_argument("kafka_ips", type=str, nargs='*')

    args = parser.parse_args()

    start_producer(args.kafka_ips if args.kafka_ips else default_servers, args.message)