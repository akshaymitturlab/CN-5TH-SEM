class LeakyBucket():
  def __init__(self, bucket_size, output_rate, input_packets):
    self.size = bucket_size
    self.orate = output_rate
    self.istream = input_packets

  def congestion_control(self):
    for x in range(len(self.istream)):
      packet_size = self.istream[x]
      print(f"Packet No: {x} Packet Size: {packet_size}")

      if packet_size > self.size:
        print("\t Bucket Overflow")
      else:
        while packet_size > self.orate:
          print(f"\t {self.orate} bytes sent")
          packet_size -= self.orate

        if packet_size:
          print(f"\t Last {packet_size} bytes sent")
        
        print("\t Bucket output successful \n")


bucket_size = int(input("Enter Bucket Size: "))
output_rate = int(input("Enter Output Rate: "))
input_packets = list(map(int, input("Enter Input Packets: ").split()))

network = LeakyBucket(bucket_size, output_rate, input_packets)
network.congestion_control()