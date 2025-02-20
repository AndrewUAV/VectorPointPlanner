import serial.tools.list_ports

def get_com_ports():
    ports = serial.tools.list_ports.comports()
    available_ports = [port.device for port in ports]
    return available_ports

if __name__ == "__main__":
    com_ports = get_com_ports()
    print("Доступні COM порти:", com_ports)
