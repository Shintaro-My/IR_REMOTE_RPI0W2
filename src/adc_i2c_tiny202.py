import smbus

class ADC_I2C_TINY202:
    def __init__(self, bus=11, addr=0x20) -> None:
        self.bus = smbus.SMBus(bus)
        self.addr = addr
    def get(self, num=0):
        self.bus.write_byte(self.addr, num)
        return self.bus.read_word_data(self.addr, 0)
    
if __name__ == '__main__':
    import time
    adc = ADC_I2C_TINY202()
    
    while True:
        try:
            print( adc.get() )
            time.sleep(.1)
        except KeyboardInterrupt:
            print('abort.')
            break