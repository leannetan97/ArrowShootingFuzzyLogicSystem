#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import math
import random
import matplotlib.pyplot as plt
#Author : TAN LAY YAN WIF160058


# In[2]:


def calculate_max_distance(angle,v):
    return ((v**2) * (math.sin(2*math.radians(angle))))/ 9.81


# In[3]:


# self defined v in ms-1
v = 30
max_distance_for_target = calculate_max_distance(45,v)

distance = ctrl.Antecedent(np.arange(-91,91+1,0.5),'distance')
angle = ctrl.Consequent(np.arange(-20,21,0.1),'angle')

target_point = random.randint(0,92)


# In[4]:


# Auto-membership function
distance['infront_very_far_to_target'] = fuzz.trimf(distance.universe, [-91, -91, -70])
distance['infront_far_to_target'] = fuzz.trimf(distance.universe, [-80, -60, -20])
distance['infront_near_to_target'] = fuzz.trimf(distance.universe, [-30, -10, 0])
distance['behind_near_to_target'] = fuzz.trimf(distance.universe, [0, 10, 30])
distance['behind_far_to_target'] = fuzz.trimf(distance.universe, [20, 60, 80])
distance['behind_very_far_to_target'] = fuzz.trimf(distance.universe, [70, 91, 91])

angle['higher_more_lot'] = fuzz.trimf(angle.universe, [-20, -20, -10])
angle['higher_a_lot'] = fuzz.trimf(angle.universe, [-13, -6, -0.5])
angle['higher_a_bit'] = fuzz.trimf(angle.universe, [-1, 0, 0])
angle['lower_a_bit'] = fuzz.trimf(angle.universe, [0, 0, 1])
angle['lower_a_lot'] = fuzz.trimf(angle.universe, [0.5, 6, 13])
angle['lower_more_lot'] = fuzz.trimf(angle.universe, [10, 20, 20])


# In[5]:


distance.view()
angle.view()
plt.show()


# In[6]:


# Generate rules
rule1 = ctrl.Rule(distance['infront_very_far_to_target'], angle['higher_more_lot'])
rule2 = ctrl.Rule(distance['infront_far_to_target'], angle['higher_a_lot'])
rule3 = ctrl.Rule(distance['infront_near_to_target'], angle['higher_a_bit'])
rule4 = ctrl.Rule(distance['behind_near_to_target'], angle['lower_a_bit'])
rule5 = ctrl.Rule(distance['behind_far_to_target'], angle['lower_a_lot'])
rule6 = ctrl.Rule(distance['behind_very_far_to_target'], angle['lower_more_lot'])


# In[7]:


# Set up controler
angle_ctrl = ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6])
angle_estimate = ctrl.ControlSystemSimulation(angle_ctrl)


# In[8]:


def shoot(angle):
       arrow_landed_point = int(calculate_distance(angle))
       difference = arrow_landed_point - target_point
       
       print('Target standing point:',target_point)
       print('Arrow landing point:',arrow_landed_point)
       print('Distance different with the target:',difference)
       
       
       if difference == 0:
           print('You hit the target at :',angle)
           return 'Yeah!'
       else:
           angle_estimate.input['distance'] = difference
           angle_estimate.compute()
           angleChange = angle_estimate.output['angle']
           print('Angle need to change:', angleChange)
           return angleChange


# In[9]:


def calculate_distance(angle):
    return ((v**2) * (math.sin(2*math.radians(angle))))/ 9.81


# In[11]:


usershoot_angle = 45
if __name__ == "__main__":
    
    while(True):
        print('User shoot at angle:',usershoot_angle)
        angleNeedToChange = shoot(usershoot_angle)
        if(angleNeedToChange == 'Yeah!'):
            break
        usershoot_angle += angleNeedToChange
        print('------- Shoot Again --------')

