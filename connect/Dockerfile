FROM confluentinc/cp-kafka-connect-base:latest
ENV CONNECT_PLUGIN_PATH="/usr/share/java,/use/share/confluent-hub-componenets"
RUN confluent-hub install --no-prompt neo4j/kafka-connect-neo4j:latest