a = input('a=')
b = input('b=')
c = input('c=')
a = int (a)
b = int (b)
c = int (c)
cuboid_volume = a * b *c
cuboid_surface_area = (a*b+b*c+c*a)*2
print(f'The volume of a cuboid is {cuboid_volume}')
print(f'The surface area of a cuboid is {cuboid_surface_area}')