from numpy import sin, sqrt 
import pandas as pd
#turning left
mass, cog_height, radius, half_width, kfront, kback = 200, 0.06,20,0.6,30000,35000
b = 30
cog_height_p = 0.09
half_length = 0.9
def roll_angle(time):
    return (mass*v_func(time)**2*cog_height)/(radius*((half_width**2)*(2*kfront+2*kback)-mass*9.8*cog_height))
def pitch_angle(time):
    return (mass*a_func(time)*cog_height_p)/((half_length**2)*(2*kfront+2*kback)-mass*9.8*cog_height_p)
def v_func(time, start_speed = 15, acceleration = 2):
    return start_speed + acceleration*time
def a_func(time):
    return (v_func(time+0.01) - v_func(time))/0.01
#turning right
def simulate(time_range,time_step):
    n = time_range/time_step
    time = [0] * int(n+1)
    velocity = [0] * int(n+1)
    front_right = [0] * int(n+1)
    front_left = [0] * int(n+1)
    back_right = [0] * int(n+1)
    back_left = [0] * int(n+1)
    for i in range(int(n)):
        time[i+1] = time[i] + time_step
        velocity[i] = v_func(time[i])
        front_right[i] = b*sqrt((roll_angle(time[i]))*half_width*kfront + 0.25*9.8*mass - pitch_angle(time[i])*half_length*kfront)
        front_left[i] = b*sqrt(-(roll_angle(time[i]))*half_width*kfront + 0.25*9.8*mass - pitch_angle(time[i])*half_length*kfront)
        back_right[i] = b*sqrt((roll_angle(time[i]))*half_width*kback + 0.25*9.8*mass + pitch_angle(time[i])*half_length*kback)
        back_left[i] = b*sqrt(-(roll_angle(time[i]))*half_width*kback + 0.25*9.8*mass + pitch_angle(time[i])*half_length*kback)
    df = pd.DataFrame({
        "Time": time, 
        "Velocity": velocity, 
        "Ff of Front Right Tire": front_right, 
       "Ff of Front Left Tire":front_left,
        "Ff of Back Right Tire": back_right,
       "Ff of Back Left Tire": back_left,
    })
    df.fillna(0)
    return df.iloc[:-1]
print(simulate(15,0.5))



