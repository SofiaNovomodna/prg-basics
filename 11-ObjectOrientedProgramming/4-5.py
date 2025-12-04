import random

class thermometer:
    def __init__(self):
        self.temperature = random.randint(34.0, 42.0)+round(random.random(), 1)
        self.is_on = False

    def on(self):
        self.is_on = True
    def off(self):
        self.is_on = False

    def measure(self):
        self.temperature = random.randint(34.0, 42.0)+round(random.random(), 1)

    def __str__(self):
        if self.is_on == True:
            result = f'Temperature: {self.temperature}'
            if self.temperature >=41.0:
                return f'CRITICAL TEMPERATURE!! {self.temperature}'
            elif self.temperature >37.0:
                result += '(fever)'
            return result
    
    
    
thermometer1 = thermometer()
thermometer1.on()
print(thermometer1)
thermometer1.measure()
print(thermometer1)
thermometer1.off()