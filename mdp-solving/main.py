import random, operator
import numpy as np

sample_number_per_episode = 100
transaction_number = 10000
N_episodes = 200


class Environment:

    def __init__(self):
        # Definle fatigue state
        self.N_score = 101
        self.N_fatigue = 2
        self.fatigue_state = {"sober": 0, "fatigue": 1}
        self.state = [60, self.fatigue_state["sober"]]
        self.score = 60
        self.score_max = 100
        # Define action space
        self.action_dim = 2  # driving or not
        self.action_dict = {"driving": 0, "rest": 1}
        # Reward related
        self.reward_threshold = 70
        self.punish_threshold = 60
        self.k_in = 0.01
        self.k_de = 0.5
        self.k_reward = 0.002
        self.k_punish = 0.004
        self.original_unit_price = 0.7
        self.mileage = 6
        self.sleepy = 0.1
        self.catch = 0.888

    def generate_reward(self):
        if self.score > self.reward_threshold:
            revenue = (1 + self.k_reward * (self.score - self.reward_threshold)) * self.original_unit_price * self.mileage
        elif self.score < self.punish_threshold:
            revenue= (1 - self.k_punish * (self.punish_threshold - self.score)) * self.original_unit_price * self.mileage
        else:
            revenue = self.original_unit_price * self.mileage
        reward = revenue - (1 + self.k_reward * (self.score_max - self.reward_threshold)) * self.original_unit_price * self.mileage
        return reward, revenue

    def reset(self):
        # Reset agent state to top-left grid corner
        self.state = [60, self.fatigue_state["sober"]]
        self.score = 60
        return self.state

    def step(self, action):
        reward, revenue = self.generate_reward()

        if self.state[1] == self.fatigue_state["sober"]:
            self.score += self.k_in * revenue * np.log (self.score_max - self.score)
        else:
            if action == self.action_dict["driving"]:
                if np.random.uniform(0, 1) < self.catch:
                    self.score -= self.k_de * revenue * np.log(self.score_max - self.score)
                    if self.score < 0:
                        self.score = 0
                else:
                    self.score += self.k_in * revenue * np.log(self.score_max - self.score)
            else:
                reward = 0
                revenue = 0

        state_next = []
        state_next.append(int(np.round(self.score)))
        state_next.append(np.random.choice(2, p=(1-self.sleepy, self.sleepy)))
        self.state = state_next

        return state_next, reward, revenue

    def allowed_actions(self):
        actions_allowed = [self.action_dict["driving"], self.action_dict["rest"]]
        actions_allowed = np.array(actions_allowed, dtype=int)
        return actions_allowed


class Agent:
    def __init__(self, env):
        # Agent learning parameters
        self.N_score = env.N_score
        self.action_dim = env.action_dim
        self.epsilon = 1.0  # initial exploration probability
        self.epsilon_decay = 0.99  # epsilon decay after each episode
        self.beta = 0.9  # Q learning rate
        self.gamma = 0.99  # reward discount factor
        # Initialize Q
        self.Q = np.zeros((self.N_score, self.action_dim), dtype=float)

    def get_action(self, env):
        # get action if sober
        if env.state[1] == env.fatigue_state["sober"]:
            return env.action_dict['driving']
        # Epsilon-greedy agent policy
        if random.uniform(0, 1) < self.epsilon:
            # explore
            return np.random.choice(env.allowed_actions())
        else:
            # exploit on allowed actions
            state = env.state
            actions_allowed = env.allowed_actions()
            Q_s = self.Q[state[0], actions_allowed]
            actions_greedy = actions_allowed[np.flatnonzero(Q_s == np.max(Q_s))]
            return np.random.choice(actions_greedy)

    def train(self, memory):
        # -----------------------------
        # Update:
        #
        # Q[s,a] <- Q[s,a] + beta * (R[s,a] + gamma * max(Q[s,:]) - Q[s,a])
        #
        #  R[s,a] = reward for taking action a from state s
        #  beta = learning rate
        #  gamma = discount factor
        # -----------------------------
        (state, action, state_next, reward) = memory
        sa = (state[0], action)
        temp = self.gamma * np.max(self.Q[(state_next[0], )])
        self.Q[sa] = (1-self.beta) * self.Q[sa] + self.beta * (reward + temp - self.Q[sa])

    def display_greedy_policy(self, N_episodes):
        # greedy policy = argmax[a'] Q[s,a']
        greedy_policy = np.zeros(self.N_score, dtype=int)
        for x in range(self.N_score):
            greedy_policy[x] = np.argmax(self.Q[x, :])
        print("\nGreedy policy:")
        print(greedy_policy)


if __name__ == '__main__':

    for i in range(sample_number_per_episode):
        print("------------------------------")
        print("sample: "+str(i))
        # Settings
        env = Environment()
        agent = Agent(env)

        # Train agent
        print("\nTraining agent...\n")
        with open("results/sample-" + str(i), "w") as f:
            for episode in range(N_episodes):
                # Generate an episode
                reward_episode = 0
                iter_fatigue = 0
                iter_fatigue_driving = 0
                revenue_iter = 0
                iter_score = 0
                state = env.reset()  # starting state
                for iter_episode in range(transaction_number):
                    iter_score += env.score
                    action = agent.get_action(env)  # get action
                    if env.state[1] == env.fatigue_state["fatigue"]:
                        iter_fatigue += 1
                        if action == env.action_dict["driving"]:
                            iter_fatigue_driving += 1
                    state_next, reward, revenue = env.step(action)  # evolve state by action
                    revenue_iter += revenue
                    agent.train((state, action, state_next, reward))  # train agent
                    iter_episode += 1
                    reward_episode += reward
                    state = state_next  # transition to next state
                f.write(str(iter_score/transaction_number) + " " +str(iter_fatigue_driving/transaction_number) + " " + str(revenue_iter) + "\n")
                f.flush()
                # Decay agent exploration parameter
                agent.epsilon = max(agent.epsilon * agent.epsilon_decay, 0.01)

                # Print
                if (episode == 0) or (episode + 1) % 10 == 0:
                    print("[episode {}/{}] eps = {:.3F} -> iter = {}, rew = {:.1F}, rev = {:.1F}".format(
                        episode + 1, N_episodes, agent.epsilon, iter_episode, reward_episode, revenue_iter))

                # Print greedy policy
                if (episode == N_episodes - 1):
                    agent.display_greedy_policy(N_episodes)
                    for (key, val) in sorted(env.action_dict.items(), key=operator.itemgetter(1)):
                        print(" action['{}'] = {}".format(key, val))
                    print()
            #f.write(str(state[0]) + " " + str(state[1]) + " " + str(action) + " " + str(reward) + "\n")