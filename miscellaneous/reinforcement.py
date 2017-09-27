import gym

#Setup Environment
env = gym.make('CartPole-v0')
env.reset()

for _ in range(1000):
	env.render()
	random_action = env.action_space.sample()
	result = env.step(random_action) #Take a random action
	new_state, reward, terminal, info = result
	