def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

def cm_to_inch(n):
    return n*0.39

def ft_inch_to_cm (n, m):
    return (n*30.48+m*2.54)
    

if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f'225cm = {cm_to_inch(225)}inch')
    print(f'10ft 65 inch = {ft_inch_to_cm(10, 65)}cm')

