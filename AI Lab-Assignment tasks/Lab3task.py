# Task: Model-Based Reflex Agent 
# This agent not only checks the current temperature but also remembers the previous action to avoid turning the heater on or off unnecessarily.
import os
os.system('cls')
class modelbase_agent:
    def __init__(self,desired_temp):
        self.desired_temp=desired_temp
        self.previous_action={'Living_room':'Turn on Heater',
       "Kitchen":'Turn off Heater',
       'Bathroom':'Turn off Heater',
       'Bed_room':'Turn on Heater'
       }

    def perceive_temp(self,current_temp):
        self.current_temp=current_temp

    def act(self,room,current_temp):
        if room not in self.previous_action:
            self.previous_action[room]="Turn off heater"

        if current_temp<self.desired_temp:
            action="Turn on Heater"
        else:
            action="Turn off Heater"
        
        if action==self.previous_action[room]:
            return f"No action needed. Heater is already {action.split()[-2]}."
        else:
            self.previous_action[room]=action
            return action
        

rooms={"Living_room":18,
       "Kitchen":22,
       'Bathroom':24,
       'Bed_room':22
       }

desired_temp=int(input("Enter the desired Temprature>"))
agent=modelbase_agent(desired_temp)

for room,temprature in rooms.items():
    action=agent.act(room,temprature)
    print(f"{room}: Current Temprature = {temprature}C. {action}")