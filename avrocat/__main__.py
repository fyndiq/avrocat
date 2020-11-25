"""
Kafka Avro producer and consumer.

Usage:
  avrocat produce -t <topic> ([-v <value>] | [-f <file>]) [-k <key>] [-b <broker>]
                             [-r <registry>] [-n <num_messages>] [-s <per_second]
                             [-X <extra_config>]
  avrocat consume -t <topic> [--exit] [-g <group>] [-b <broker>] [-r <registry]
                             [(-P <partitions> -k <key>)] [-X <extra_config>]
                             [--enable-timestamps] [--enable-headers] [--remove-null-values]

Commands:
  produce                             Produce Avro message to a topic.
  consumer                            Consume Avro messages from one or multiple topics.

Options:
  -t --topic=<topic>                    One (P) or multiple (C) comma separated topics.
  -v --value=<value>                    Message value (JSON).
  -f --file=<file>                      Read value from file (JSON).
  -k --key=<key>                        Message key.
  -n --num-messages=<num_messages>      Number of messages to produce [default: 1].
  -s --per-second=<per_seconds>         Number of messages per second.
  -b --broker=<broker>                  Kafka broker address [default: localhost:9094].
  -r --registry=<registry>              Schema registry URL [default: http://localhost:8081].
  -g --group=<group>                    Consumer group.
  -P --partitions=<partitions>          Number of partitions on topic. Must be set when using --key
                                        [default: 8].
  -X --extra-config=<extra_config>      Extra configuration properties passed to librdkafka.
                                        Example: -X prop=val,prop=val
  --enable-timestamps                   Display message timestamps [default: False].
  --enable-headers                      Display message headers [default: False].
  --remove-null-values                  Remove null values from consumed messages [default: False].
  --exit                                Exit after last message is consumed.
"""
from docopt import docopt

from avrocat import AvroCat

arguments = docopt(__doc__)


def main():
    consume = arguments.pop('consume')
    produce = arguments.pop('produce')
    breakpoint()
    avrocat = AvroCat(**arguments)
    if consume:
        avrocat.consume()
    elif produce:
        avrocat.produce()


if __name__ == "__main__":
    main()
