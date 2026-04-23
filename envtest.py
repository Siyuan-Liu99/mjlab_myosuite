from mjlab_myosuite.env_factory import make_myosuite_env

# Create a MyoSuite environment wrapped for mjlab
env = make_myosuite_env("myoElbowPose1D6MRandom-v0")
obs, info = env.reset()
action = env.action_space.sample()
obs, rewards, dones, extras = env.step(action)
env.close()
