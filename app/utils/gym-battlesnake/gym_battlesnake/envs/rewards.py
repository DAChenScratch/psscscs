# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

import numpy as np


class Rewards:
    '''
    Base class to set up rewards for the battlesnake gym
    '''

    def get_reward(self, name, snake_id, episode):
        raise NotImplemented()


class SimpleRewards(Rewards):
    '''
    Simple class to handle a fixed reward scheme
    '''

    def __init__(self):
        self.reward_dict = {"another_turn": 1,
                            "ate_food": 1,
                            "won": 3,
                            "died": -1,
                            "ate_another_snake": 2,
                            "hit_wall": -1,
                            "hit_other_snake": -1,
                            "hit_self": -1,
                            "was_eaten": -1,
                            "other_snake_hit_body": -1,
                            "forbidden_move": -1,
                            "starved": -1}

    def get_reward(self, name, snake_id, episode):
        return self.reward_dict[name]

# Stricter penalties for dying and lower reward for moving (10 moves equivalent to win)
class TestReward1(Rewards):
    '''
    Simple class to handle a fixed reward scheme
    '''

    def __init__(self):
        self.reward_dict = {"another_turn": 0.3,
                            "ate_food": 1,
                            "won": 3,
                            "died": -3,
                            "ate_another_snake": 2,
                            "hit_wall": -5,
                            "hit_other_snake": -1,
                            "hit_self": -5,
                            "was_eaten": -2,
                            "other_snake_hit_body": -1,
                            "forbidden_move": -2,
                            "starved": -3}

    def get_reward(self, name, snake_id, episode):
        return self.reward_dict[name]

# Stricter penalties for dying and lower reward for moving (30 moves equivalent to win)
class TestReward2(Rewards):
    '''
    Simple class to handle a fixed reward scheme
    '''

    def __init__(self):
        self.reward_dict = {"another_turn": 0.1,
                            "ate_food": 1,
                            "won": 3,
                            "died": -1,
                            "ate_another_snake": 2,
                            "hit_wall": -3,
                            "hit_other_snake": -1,
                            "hit_self": -3,
                            "was_eaten": -1,
                            "other_snake_hit_body": -1,
                            "forbidden_move": -2,
                            "starved": -2}

    def get_reward(self, name, snake_id, episode):
        return self.reward_dict[name]


class TestReward3(Rewards):
    '''
    Simple class to handle a fixed reward scheme
    '''

    def __init__(self):
        self.reward_dict = {"another_turn": 0.5,
                            "ate_food": 3,
                            "won": 5,
                            "died": -2,
                            "ate_another_snake": 2,
                            "hit_wall": -3,
                            "hit_other_snake": -2,
                            "hit_self": -3,
                            "was_eaten": -1,
                            "other_snake_hit_body": -1,
                            "forbidden_move": -2,
                            "starved": -1}

    def get_reward(self, name, snake_id, episode):
        return self.reward_dict[name]