class Phone():
    def __init__(self, model, color, price):
        self.model = model
        self.color = color
        self.price = price
        self.turn_on_off = False
        self.current_app = ''
        self.charge = 100
    
    def turn_on(self):
        self.turn_on_off = True
    def turn_off(self):
        self.turn_on_off = False

    def change_app(self, app):
        self.current_app = app

    def uncharge(self, percente):
        self.charge -= percente
    def _charge(self, percente):
        self.charge += percente

    def info(self):
        print('turn_on_off:', self.turn_on_off)
        print('current_app:', self.current_app)
        print('charge:', self.charge)


my_phone = Phone('Redmi', 'red', '100')
my_phone.turn_on()
my_phone.change_app('Telegram')
my_phone.uncharge(20)
my_phone.info()
    
