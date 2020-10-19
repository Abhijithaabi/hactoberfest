from visual import *
from visual.graph import *
# creating planets and star
star = sphere( pos=vector(0,0,0), radius=0.5, color=color.yellow,
               mass = 1000, velocity=vector(0,0,0) )
               
planet1 = sphere( pos=vector(1,0,0), radius=0.05, color=color.blue,
                  mass = 1, velocity=vector(0,30,0),make_trail=True ,retain=1000 )

planet2 = sphere( pos=vector(0,3,0), radius=0.075, color=color.red,
                  mass = 2, velocity=vector(-35,0,0),make_trail=True ,retain=1500 )
                 
planet3 = sphere( pos=vector(0,-4,0), radius=0.1, color=color.green,
                  mass = 10, velocity=vector(160,0,0),make_trail=True ,retain=2000 )
planet4 = sphere( pos=vector(2,0,0), radius=0.05, color=color.yellow,
                  mass = 1.25,velocity=vector(0,30,0) ,make_trail=True ,retain=2500)

planet5 = sphere( pos=vector(0,4,0), radius=0.075, color=color.orange,
                  mass = 2.25, velocity=vector(-35,0,0),make_trail=True ,retain=3000)
                 
planet6 = sphere( pos=vector(0,-5,0), radius=0.1, color=color.white,
                  mass = 11, velocity=vector(160,0,0),make_trail=True ,retain=3500 )
planet7 = sphere( pos=vector(6,0,0), radius=0.1, color=color.blue,
                  mass = 13, velocity=vector(0,180,0),make_trail=True ,retain=4000 )
planet8 = sphere( pos=vector(0,-7,0), radius=0.1, color=color.green,
                  mass = 13, velocity=vector(200,0,0),make_trail=True ,retain=4500)

#initializing curves for each planet
gdisplay(xtitle="time",ytitle="velocity")
planet1_curve=gcurve(color=color.blue)
planet2_curve=gcurve(color=color.red)
planet3_curve=gcurve(color=color.green)
planet4_curve=gcurve(color=color.yellow)
planet5_curve=gcurve(color=color.orange)
planet6_curve=gcurve(color=color.white)
planet7_curve=gcurve(color=color.blue)
planet8_curve=gcurve(color=color.green)

#function to calculate gravitational force
def gravitational_force(a,b):
    G = 1 
    r_vec = a.pos-b.pos
    r_mag = mag(r_vec)
    r_hat = r_vec/r_mag
    force_mag = G*a.mass*b.mass/r_mag**2
    force_vec = -force_mag*r_hat
    return force_vec
              
dt = 0.0001
t = 0

# loop for continues rotation
while (True):
    rate(1000)
   
    # Calculate forces.
    star.force = gravitational_force(star,planet1)+gravitational_force(star,planet2)+gravitational_force(star,planet3)+gravitational_force(star,planet4)+gravitational_force(star,planet5)+gravitational_force(star,planet6)+gravitational_force(star,planet7)+gravitational_force(star,planet8)
    planet1.force = gravitational_force(planet1,star)+gravitational_force(planet1,planet2)+gravitational_force(planet1,planet3)
    planet2.force = gravitational_force(planet2,star)+gravitational_force(planet2,planet1)+gravitational_force(planet2,planet3)
    planet3.force = gravitational_force(planet3,star)+gravitational_force(planet3,planet1)+gravitational_force(planet3,planet2)
    planet4.force = gravitational_force(planet4,star)+gravitational_force(planet4,planet1)+gravitational_force(planet4,planet3)+gravitational_force(planet4,planet2)
    planet5.force = gravitational_force(planet5,star)+gravitational_force(planet5,planet1)+gravitational_force(planet2,planet5)+gravitational_force(planet5,planet3)+gravitational_force(planet5,planet4)
    planet6.force = gravitational_force(planet6,star)+gravitational_force(planet6,planet1)+gravitational_force(planet6,planet2)+gravitational_force(planet3,planet6)+gravitational_force(planet6,planet4)+gravitational_force(planet6,planet5)
    planet7.force = gravitational_force(planet7,star)+gravitational_force(planet7,planet1)+gravitational_force(planet7,planet2)+gravitational_force(planet3,planet7)+gravitational_force(planet7,planet4)+gravitational_force(planet7,planet5)+gravitational_force(planet7,planet6)
    planet8.force = gravitational_force(planet8,star)+gravitational_force(planet8,planet1)+gravitational_force(planet8,planet2)+gravitational_force(planet3,planet8)+gravitational_force(planet8,planet4)+gravitational_force(planet8,planet5)+gravitational_force(planet8,planet6)+gravitational_force(planet8,planet7)

    # updating velocity
    star.velocity = star.velocity + star.force*dt
    planet1.velocity = planet1.velocity + planet1.force*dt
    planet2.velocity = planet2.velocity + planet2.force*dt
    planet3.velocity = planet3.velocity + planet3.force*dt
    planet4.velocity = planet4.velocity + planet4.force*dt
    planet5.velocity = planet5.velocity + planet5.force*dt
    planet6.velocity = planet6.velocity + planet6.force*dt
    planet7.velocity = planet7.velocity + planet7.force*dt
    planet8.velocity = planet8.velocity + planet8.force*dt

    # Update positions.
    star.pos = star.pos + star.velocity/star.mass*dt
    planet1.pos = planet1.pos + planet1.velocity/planet1.mass*dt
    planet2.pos = planet2.pos + planet2.velocity/planet2.mass*dt
    planet3.pos = planet3.pos + planet3.velocity/planet3.mass*dt
    planet4.pos = planet4.pos + planet4.velocity/planet4.mass*dt
    planet5.pos = planet5.pos + planet5.velocity/planet5.mass*dt
    planet6.pos = planet6.pos + planet6.velocity/planet6.mass*dt
    planet7.pos = planet7.pos + planet7.velocity/planet7.mass*dt
    planet8.pos = planet8.pos + planet8.velocity/planet8.mass*dt

    #plotting graphs
    planet1_curve.plot(pos=(t,mag(planet1.velocity)))
    planet2_curve.plot(pos=(t,mag(planet2.velocity)))
    planet3_curve.plot(pos=(t,mag(planet3.velocity)))
    planet4_curve.plot(pos=(t,mag(planet4.velocity)))
    planet5_curve.plot(pos=(t,mag(planet5.velocity)))
    planet6_curve.plot(pos=(t,mag(planet6.velocity)))
    planet7_curve.plot(pos=(t,mag(planet7.velocity)))
    planet8_curve.plot(pos=(t,mag(planet8.velocity)))
    t = t + dt

    


   
     
