# tv.py file
# class definition
class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 2
        self.channels_list = []
        self.volume = 0

    def turn_off(self):
        self.is_on = False
    def turn_on(self):
        self.is_on = True

    def volume_up(self, number):
        if self.volume + number >10:
            print('Error')
        else:
            self.volume += number
    def volume_down(self, number):
        if self.volume - number <0:
            print('Error')
        else:
            self.volume -= number

    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no

    def set_channels(self, channels_list):
        self.channels_list=channels_list
    def show_channels(self):
        print('Channel list:')
        ii = 1
        for i in self.channels_list:
            print(f'{ii}. {i}')
            ii+=1

    def show_status(self):
        print('TV is', end=' ')
        if self.is_on == False:
            print('off')
        if self.is_on == True:
            if 1 <= self.channel_no <= len(self.channels_list):
                print('on, channel', self.channel_no, f'({self.channels_list[self.channel_no-1]}),', f'volume: {self.volume}')
            else:
                print('on, channel', self.channel_no, f'doesnt exist,', f'volume: {self.volume}')