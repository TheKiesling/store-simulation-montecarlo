from inventoryEnvironment import InventoryEnvironment


episodes = 10
env = InventoryEnvironment()
days_per_episode = 5

policy = {
    'product_A': {
        0: 3,
        1: 2,
        2: 1,
        3: 0,
        4: 0,
        5: 0
    },
    'product_B': {
        0: 2,
        1: 1,
        2: 0,
        3: 0,
        4: 0,
        5: 0
    }
}

total_reward = 0

for episode in range(episodes):
    env.reset()
    state = env.state
    for day in range(days_per_episode):
        action = {product: policy[product][state[product]] for product in env.products}
        state, reward = env.step(action)
        total_reward += reward
        print(f"Reward for Episode {episode + 1}, Day {day + 1}: {reward}")
    print(f"Episode {episode + 1}, State: {state}, Reward: {reward}")

print(f"Total Reward after {episodes} episodes: {total_reward}")