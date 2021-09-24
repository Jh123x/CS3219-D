#!/usr/bin/python3
import argparse
from kafka import KafkaConsumer
from json import loads


def start_consumer(ip_servers: list) -> None:
    consumer = KafkaConsumer(
        "test",
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group-1',
        value_deserializer=lambda m: loads(m.decode('utf-8')),
        bootstrap_servers=ip_servers
    )

    for c in consumer:
        print(c.value)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("kafka_ip", type=str, nargs='*')

    args = parser.parse_args()
    test = ['localhost:29092', 'localhost:39092']
    start_consumer(test)
