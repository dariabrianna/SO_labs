import threading
import queue
import random
import time
from datetime import datetime

# Shared queue for IPC
buffer = queue.Queue()

# Semaphore to control production and consumption limits
producer_semaphore = threading.Semaphore(3)
consumer_semaphore = threading.Semaphore(5)

# Producer function
def producer(producer_id):
    while True:
        producer_semaphore.acquire()  # Control overproduction
        items = [random.randint(1, 100) for _ in range(3)]
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] Producer {producer_id} produced items: {items}")
        for item in items:
            buffer.put(item)  # Add each item to the buffer
        producer_semaphore.release()
        time.sleep(random.uniform(0.5, 1.5))  # Simulate work

# Consumer function
def consumer(consumer_id):
    while True:
        items = []
        for _ in range(5):
            item = buffer.get()
            items.append(item)
            buffer.task_done()  # Signal completion
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] Consumer {consumer_id} consumed items: {items}")
        consumer_semaphore.release()
        time.sleep(random.uniform(0.5, 2))  # Simulate work

# Main function
if __name__ == "__main__":
    # Start producer threads
    producers = [threading.Thread(target=producer, args=(i,)) for i in range(3)]
    for p in producers:
        p.start()

    # Start consumer threads
    consumers = [threading.Thread(target=consumer, args=(i,)) for i in range(2)]
    for c in consumers:
        c.start()

    # Join threads
    for p in producers:
        p.join()
    for c in consumers:
        c.join()
import threading
import queue
import random
import time
from datetime import datetime

# Shared queue for IPC
buffer = queue.Queue()

# Semaphore to control production and consumption limits
producer_semaphore = threading.Semaphore(3)
consumer_semaphore = threading.Semaphore(5)

# Producer function
def producer(producer_id):
    while True:
        producer_semaphore.acquire()  # Control overproduction
        items = [random.randint(1, 100) for _ in range(3)]
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] Producer {producer_id} produced items: {items}")
        for item in items:
            buffer.put(item)  # Add each item to the buffer
        producer_semaphore.release()
        time.sleep(random.uniform(0.5, 1.5))  # Simulate work

# Consumer function
def consumer(consumer_id):
    while True:
        items = []
        for _ in range(5):
            item = buffer.get()
            items.append(item)
            buffer.task_done()  # Signal completion
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] Consumer {consumer_id} consumed items: {items}")
        consumer_semaphore.release()
        time.sleep(random.uniform(0.5, 2))  # Simulate work

# Main function
if __name__ == "__main__":
    # Start producer threads
    producers = [threading.Thread(target=producer, args=(i,)) for i in range(3)]
    for p in producers:
        p.start()

    # Start consumer threads
    consumers = [threading.Thread(target=consumer, args=(i,)) for i in range(2)]
    for c in consumers:
        c.start()

    # Join threads
    for p in producers:
        p.join()
    for c in consumers:
        c.join()
