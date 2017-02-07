#!/usr/bin/env python
# -*- coding: utf-8 -*-

from map_display import *
from QLearning import*
import numpy as np
import matplotlib.pyplot as plt
import sys
import time

MAX_GOAL_TRIAL = 300

if __name__ == "__main__":
    map_reward  = np.loadtxt('data/map.csv', delimiter=',') 
    agentQL     = AgentQLearning(map_reward,0.1,0.2,0.9)
    map_display = MapDisplay(map_reward)
   
    _trial = 0
    while True:
        agentQL.learn() #行動学習
        map_display.draw(agentQL.state)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        if np.array_equal(agentQL.state, np.array(map_reward.shape)-1):
            agentQL.goal_count = agentQL.goal_count + 1
            print "Goal:", agentQL.goal_count
            agentQL.reset()
        _trial = _trial + 1
        agentQL.trial.append(_trial)
        if MAX_GOAL_TRIAL < agentQL.goal_count:
            break
        #time.sleep(0.02)

    #方策の可視化
    map_display.show_policy(agentQL.q)
    pygame.display.update()
    pygame.image.save(map_display.screen, "picture/policy.jpg")

    #Q値の変化
    fig = plt.figure()
    ax  = fig.add_subplot(1,1,1)
    ax.plot(agentQL.trial, agentQL.q_value_list, label='Q Value')
    ax.set_title("Q Value")
    ax.legend(loc='best')
    ax.set_xlabel('trial')
    ax.set_ylabel('Q')
    plt.show()
