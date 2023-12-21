import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from math import pi

m_initial = 16376
m_final = 12200
m_initial2 = 9500
m_final2 = 4400
Cd = 0.045
A = 6.25
A1 = pi * 1.2
thrust = 270400
thrust2 = 167970
T = 21


def rockets(t, y):
    if t <= 21:
        h, v = y
        angle = 90 - 0.45 * t
        po1 = 1.225
        g = 9.8

        po = po1



        F_net = (thrust - 0.5 * Cd * A * po * v**2) * np.sin(np.radians(angle)) - (m_initial - (m_initial - m_final) * t / 21) * g
        dv_dt = (F_net / (m_initial - (m_initial - m_final) * t / 21))
        dh_dt = v


        return [dh_dt, dv_dt]
    else:
        h, v = y
        angle = 90 - 0.45 * t
        po1 = 0.1
        g = 9.8
        po = po1

        F_net = (thrust2 - 0.5 * Cd * A1 * po * v**2) * np.sin(np.radians(angle)) - (m_initial2 - (m_initial2 - m_final2) * t / 100) * g
        dv_dt = (F_net / (m_initial2 - (m_initial2 - m_final2) * t / 100))
        dh_dt = v

        return [dh_dt, dv_dt]


y0 = [0, 0]

solution = solve_ivp(rockets, [0, 100], y0, method='RK45', dense_output=True)

t = solution.t
h = solution.y[0]
v = solution.y[1]

plt.figure(figsize=(15, 10))
plt.plot(t, v, 'b-', linewidth=2)
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.title('Rocket Velocity vs. Time')
plt.grid(True)
plt.show()

plt.figure(figsize=(15, 10))
plt.plot(t, h, 'r-', linewidth=2)
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.title('Rocket Height vs. Time')
plt.grid(True)
plt.show()