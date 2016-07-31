import zmq
import time
import file_pb2


print "SERVER: "
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.setsockopt(zmq.SUBSCRIBE, '')

socket.bind("tcp://*:5001")

person = file_pb2.Person()

while True:
    msg = socket.recv()
    msg = person.ParseFromString(msg)
    print "Person Id: ", person.id
    print "Person name: ", person.name
    print "Person email: ", person.email
    time.sleep(2)
