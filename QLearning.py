#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import random
import copy

class AgentQLearning:
    def __init__(self,map_filed,epsilon,alpha,gamma):
        self.epsilon    = epsilon
        self.alpha      = alpha
        self.gamma      = gamma
        self.map_filed  = map_filed
        self.row, self.column = map_filed.shape
        
        self.goal_count     = 0
        self.state          = np.array([0,0])
        self.action_list    = self.generate_action_list()
        self.move_list      = {0:np.array([0,-1]), 1:np.array([1,0]), 2:np.array([0,1]), 3:np.array([-1,0])}
        self.q              = np.zeros((4, ) + self.map_filed.shape)
        self.goal_state     = np.array(self.map_filed.shape)-1

    def generate_action_list(self):
        action_list = []
        for i in range(self.row):
            action_list.append([])
            for j in range(self.column):
                action = [0,1,2,3]
                if i == 0:
                    action.remove(3)
                if i == self.row - 1:
                    action.remove(1)
                if j == 0:
                    action.remove(0)
                if j == self.column -1:
                    action.remove(2)
                action_list[i].append(action)
        return np.array(action_list)

    def learn(self):
        y, x = self.state
	current_acton_list = copy.deepcopy(self.action_list[y,x])
	if np.random.rand() > self.epsilon:
            max_q = self.q[current_acton_list,y,x].max()
	    action_list_index = list(np.argwhere(self.q[current_acton_list,y,x] == max_q))
	    random.shuffle(action_list_index)
            action = current_acton_list[action_list_index[0]]
	else:
	    random.shuffle(current_acton_list)
            action = current_acton_list[0]
        move = self.move_list.get(action)
	self.update_q(action, move)
        self.state += move 

    def update_q(self, action_list_index, move):
        y, x = self.state
        current_q = self.q[action_list_index, y, x];
        reward = self.map_filed[tuple(self.state + move)]
        self.q[action_list_index, y, x] = current_q + self.alpha * (reward + self.gamma * self.q_max_value(move) - current_q)

    def q_max_value(self, move):
        y, x = self.state + move
        move = self.action_list[y, x]  
        return self.q[move,y,x].max()

    def reset(self):
        self.state = np.array([0,0])

