# tv_show.py file
# main program
from tv import TV

def main():
   # object creation
    tv = TV()

   # object usage
    tv.show_status()
    tv.turn_on()
    tv.show_channels()
    tv.set_channels(['TVP1','TVP2','Polsat','TVN','Filmbox','Discovery'])
    tv.show_channels()
    tv.show_status()
    tv.set_channel(4)
    tv.show_status()
    tv.volume_up(4)
    tv.show_status()
    tv.turn_off()
    tv.show_status()
    tv.show_status()

if __name__ == "__main__":
   main() 