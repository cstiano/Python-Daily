import gym
import math

def run_an_episode(st, env):
	terminal = False
	time_step = 1
	rewards = list()
	while not terminal:
		action = 1
		result = env.step(action)
		s_t1, reward, terminal, info = result
		rewards.append(reward)
		print("-- t:"+str(time_step)+"--")
    	print("St", st)
    	print("At", action)
    	print("Rt+1", reward)
    	print("st+1", s_t1)
    	print("----------")
    	st = s_t1
    	time_step += 1
   	return rewards

def get_returns_for_state(rewards, state_id):
	gamma = 0.9
	Rt = rewards[state_id-1]
	Gt = Rt
	for k in range(state_id,len(rewards)):
		if k == len(rewards)-1:
			reward = -10
		else:
			reward = rewards[k]
		Gt = Gt + math.pow(gamma, k)*reward
	return Gt

def main():
	#Setup Environment
	env = gym.make('CartPole-v0')
	env.reset()

	random_action = env.action_space.sample()
	result = env.step(random_action)
	state, _, _, _ = result
	s_0 = state

	rewards = run_an_episode(s_0, env)
	for state_id in range(1, len(rewards)):
		Gt = get_returns_for_state(rewards, state_id)
		print ("Returns Gt for state: ", state_id, "is", Gt)

if __name__ == "__main__":
	main()