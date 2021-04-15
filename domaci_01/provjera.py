import zadatak_01 as prt

p1 = prt.particle(10,60,40,30)
#print(p1.total_time())
p1.reset()

p1 = prt.particle(10,0,40,100)
#print(p1.max_speed())
p1.reset()

p1 = prt.particle(10,45,0,0)
print(p1.velocity_to_hit_target(12,10,2))
p1.reset()

p1 = prt.particle(25,40,0,0)
print(p1.angle_to_hit_target(12,10,2))
p1.reset()

