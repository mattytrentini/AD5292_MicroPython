import time

class AD5292:
    def __init__(self, spi, cs):
        self.spi = spi
        self.cs = cs
        self.cs(1)  # Chip select is active low

    @property
    def position(self):
        return 512  # TODO: Read the position value

    @position.setter
    def position(self, value):
        assert 0 <= value < 1024
        command = (0x01 << 10) | (value & 0x03FF)
        self._send_command(command)
        time.sleep_ms(6)

    def _send_command(self, command):
        self.cs(0)
        self.spi.write(bytearray([(command >> 8) & 0xFF, command & 0xFF]))
        self.cs(1)

    def read_control_register(self):
        command = (0x02 << 10)  # Assuming this is the correct command for reading the control register
        self._send_command(command)
        # Read response from the device
        response = bytearray(2)
        self.cs(0)
        self.spi.readinto(response)
        self.cs(1)
        return response[1]  # Assuming the control register value is in the LSB

    def write_control_register(self, value):
        if value > 7:
            return False  # Invalid control register value
        command = (0x03 << 10) | (value & 0x07)  # Assuming this is the correct command for writing the control register
        self._send_command(command)
        return True
