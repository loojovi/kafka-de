#!/bin/bash

echo "Downloading required pacakges in EC2 instance"
wget https://downloads.apache.org/kafka/3.3.2/kafka_2.12-3.3.2.tgz
tar -xvf kafka-3.3.2-src.tgz
sudo yum install java-1.8.0-openjdk
cd kafka_2.12-3.3.1

# Increase memory allocated for Kafka
export KAFKA_HEAP_OPTS="-Xmx256M -Xms128M"