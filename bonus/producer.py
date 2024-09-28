# https://aiokafka.readthedocs.io/en/stable/


import asyncio
from aiokafka import AIOKafkaProducer

async def send_one():
    # สร้าง instance ของ AIOKafkaProducer
    producer = AIOKafkaProducer(
        bootstrap_servers=['192.168.43.194:9096', '192.168.43.113:9096', '192.168.43.11:9096', '192.168.43.147:9096']  # เชื่อมต่อกับ Kafka brokers หลายตัว
    )
    # เริ่ม producer
    await producer.start()
    try:
        # ส่งข้อความ
        await producer.send_and_wait("my_topic", b"Hello, World!")
        print("Message sent successfully!")
    finally:
        # ปิด producer
        await producer.stop()

# รันฟังก์ชัน send_one
asyncio.run(send_one())
