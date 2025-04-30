import pika
import time

while True:
    try:
        # Hàm callback được gọi khi nhận được tin nhắn
        def callback(ch, method, properties, body):
            print(f" [x] Received: {body.decode()}")

        # Thiết lập kết nối với RabbitMQ
        connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
        channel = connection.channel()

        # Đảm bảo hàng đợi tồn tại
        queue_name = "chat_queue"
        channel.queue_declare(queue=queue_name)

        # Đăng ký nhận tin nhắn từ hàng đợi và gọi hàm callback
        channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

        print(' [*] Waiting for messages. Press CTRL+C to exit.')
        # Bắt đầu vòng lặp nhận tin nhắn
        channel.start_consuming()
    except pika.exceptions.AMQPConnectionError as e:
        print(f" [x] Connection error: {e}. Try again in 5 seconds...")
        time.sleep(5)  # Chờ trước khi thử kết nối lại
    except KeyboardInterrupt:
        print("\n [x] Exited.")
        break