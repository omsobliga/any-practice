import json
import random
import message_pb2

vector = [random.uniform(0, 1) for i in range(768)]
data = {"id": 1, "vector": vector}
msg = message_pb2.ProductVector(**data)

with open("/tmp/vector.bin", "wb") as f:
    f.write(msg.SerializeToString())
