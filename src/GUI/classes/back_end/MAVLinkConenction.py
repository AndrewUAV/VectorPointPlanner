from pymavlink import mavutil


class MavlinkConnection:
    def __init__(self, device, baudrate):
        self.master = mavutil.mavlink_connection(device=device, baud=baudrate)

    def connect_status(self):
        print("Очікується підключення....")
        self.master.wait_heartbeat()
        print("Пристрій підключено")

    def get_receive_data(self):
        while True:
            msg = self.master.recv_match()
            if not msg: continue

            if msg.get_type() == "HEARTBEAT":
                print("\n\n*****Got message: %s*****" % msg.get_type())
                print("Message: %s" % msg)
                print("\nAs dictionary: %s" % msg.to_dict())
                print("\nSystem status: %s" % msg.system_status)