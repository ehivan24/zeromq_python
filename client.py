import zmq
import time
import file_pb2

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.connect("tcp://localhost:5001")

print "Client: "
person = file_pb2.Person()
person.id = 1234
person.name = "Joe"
person.email = "joe@ymail.com"


while True:
    msg = person.SerializeToString()
    socket.send(msg)
    print "Sending", msg
    time.sleep(2)
