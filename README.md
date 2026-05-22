# AD5292_MicroPython

## Example usage

```python
from ad5292 import AD5292
from machine import SPI

spi = SPI(0) # baudrate=50_000, polarity=0, phase=1
cs = Pin(10, Pin.OUT)
potentiometer = AD5292(spi, cs)
potentiometer.position = 512  # Set wiper position to mid-range
```
