import numpy as np
import pandas as pd
from scipy.integrate import solve_ivp
#turning left
mass, cog_height, radius, half_width, kfront, kback = 200, 0.06,20,0.6,30000,35000
b = 30

def fun(t, y, v_current = 15):
    theta, omega = y
    dtheta = omega
    domega = 3*9.81*cog_height*theta/half_width**2 - 3*(2*kfront + 2*kback)*theta/mass + 3*v_current**2*cog_height/(radius*half_width**2)
    return dtheta,domega
t_span = (0,15)
u0 =[0.0, 0.0]
t_eval =np.linspace(0,15,30)
sol = solve_ivp(fun, t_span, u0, t_eval=t_eval)
print(sol)
