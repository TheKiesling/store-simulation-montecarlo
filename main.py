from inventoryEnvironment import InventoryEnvironment


episodes = 10
env = InventoryEnvironment()
days_per_episode = 5

policy = {
    'product_A': 2,
    'product_B': 1
}

total_reward = 0

for episode in range(episodes):
    env.reset()
    for day in range(days_per_episode):
        action = policy
        state, reward = env.step(action)
        total_reward += reward
        print(f"Reward for Episode {episode + 1}, Day {day + 1}: {reward}")
    print(f"Episode {episode + 1}, State: {state}, Reward: {reward}")

print(f"Total Reward after {episodes} episodes: {total_reward}")