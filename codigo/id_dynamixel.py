# escanear_ids.py
from dynamixel_sdk import PortHandler, PacketHandler

port = PortHandler('/dev/ttyUSB0')  # Puerto usb a seleccionar
packet = PacketHandler(1.0)
port.openPort()
port.setBaudRate(1000000)  

for dxl_id in range(1, 20):
    dxl_model, comm_result, _ = packet.ping(port, dxl_id)
    if comm_result == 0:
        print(f"Se detectó un servo con ID {dxl_id}")

port.closePort()
