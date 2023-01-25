import gymnasium as gym
import numpy as np
import time

env = gym.make("CarRacing-v2", domain_randomize=True, render_mode="human")

#Action Space
# If continuous there are 3 actions :
#     0: steering, -1 is full left, +1 is full right
#     1: gas
#     2: breaking

env.reset()

brake = 0
speed = 1
steering = 0 

start = True
score = 1
terminated = True
truncated = True

while not terminated or truncated:
    env.render()
    #print(env.action_space)

    if start:
        for _ in range(30):
            print("START SPEED")
            speed = 1
            start = False
            action = np.array([0, 1, 0])
            observation, reward, terminated, truncated, info = env.step(action)

    before_before_score = before_score
    before_score = score
    score += reward

    print("REWARD", reward)
    print("PREVIOUS SCORE", before_score, "CURRENT SCORE", score)


    print("BRAKE", brake)
    print("SPEED", speed)
    print("STEERING", steering)

    

    action = np.array([steering, speed, brake])
    observation, reward, terminated, truncated, info = env.step(action)




    # print(action)
    #action = env.action_space
    #print("action", action,"\n")
    #print("observation", observation,"\n")


    #print("score ; ",score,"\n")
    #print("info", info,"\n")


    if score <= -100:
        break

env.close()
