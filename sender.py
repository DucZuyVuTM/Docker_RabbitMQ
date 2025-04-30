import pika
import time

while True:
    try:
        # Thiết lập kết nối với RabbitMQ
        connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
        channel = connection.channel()

        # Tạo hàng đợi có tên 'chat_queue'
        queue_name = "chat_queue"
        channel.queue_declare(queue=queue_name)

        # Gửi tin nhắn vào hàng đợi
        message = input(" [x] Message: ")
        channel.basic_publish(exchange='', routing_key=queue_name, body=message)

        print(f" [x] Sent: {message}")

        # Đóng kết nối sau mỗi lần gửi
        connection.close()

        # Thêm độ trễ để tránh gửi quá nhanh
        time.sleep(1)  # Gửi mỗi giây một lần

    except pika.exceptions.AMQPConnectionError as e:
        print(f" [x] Connection error: {e}. Try again in 5 seconds...")
        time.sleep(5)  # Chờ trước khi thử kết nối lại
    except KeyboardInterrupt:
        print("\n [x] Exited.")
        break