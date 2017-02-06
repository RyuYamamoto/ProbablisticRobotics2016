#!/usr/bin/env python
# -*- coding: utf-8 -*-

from map_display import *
from QLearning import*
import numpy as np
import sys
import time

if __name__ == "__main__":
    map_reward  = np.loadtxt('data/map.csv', delimiter=',') 
    agentQL     = AgentQLearning(map_reward,0.1,0.2,0.9)
    map_display = MapDisplay(map_reward)

    while True:
        agentQL.learn()
        map_display.draw(agentQL.state)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        if np.array_equal(agentQL.state, np.array(map_reward.shape)-1):
            agentQL.goal_count = agentQL.goal_count + 1
            agentQL.reset()
        if 300 < agentQL.goal_count:
            break
        time.sleep(0.0)

    map_display.show_policy(agentQL.q)
    pygame.display.update()
    pygame.image.save(map_display.screen, "policy.jpg")
