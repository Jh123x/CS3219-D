from kafka.admin import KafkaAdminClient, ConfigResource, ConfigResourceType
from pprint import pprint

from kafka.admin.new_topic import NewTopic

KAFKA_URLS = ["localhost:19092", "localhost:29092", "localhost:39092"]
KAFKA_TOPIC = "test"

admin_client = KafkaAdminClient(
    bootstrap_servers=KAFKA_URLS,
    client_id = 't'
    )
# admin_client.delete_topics(['test'])
admin_client.create_topics([NewTopic('test', 3, 3)])