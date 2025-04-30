# Commands

## To build project for the first time (after installing Docker):

```
docker network create rabbitmq-net
docker network connect rabbitmq-net rabbitmq
docker build -t rabbitmq-python .
```

## To run project:

1. Start file `receiver.py`
```
docker run --rm -it --network rabbitmq-net rabbitmq-python
```

2. Start file `sender.py` in another terminal
```
docker run --rm -it --network rabbitmq-net rabbitmq-python python sender.py
```

3. Enjoy!

## To save changes in Docker image:
```
docker build -t rabbitmq-python .
```
