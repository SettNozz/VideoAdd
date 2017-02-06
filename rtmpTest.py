import librtmp

conn = librtmp.RTMP('rtmp://localhost/myapp/mystream')
# Attempt to connect
conn.connect()
# Get a file-like object to access to the stream
#stream = conn.create_stream()
# Read 1024 bytes of data
#data = stream.read(1024)
#packet_read
#packet = conn.read_packet()
#packet.body
#print(type(packet))
