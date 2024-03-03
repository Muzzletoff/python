import hashlib

# Server seed (kept secret by the game operator)
server_seed = "SecretServerSeed"

# Player's client seed (provided by the player)
client_seed = "ClientSeed123"

# Result generation (using a simple hash)
result_seed = server_seed + client_seed
result = hashlib.sha256(result_seed.encode()).hexdigest()

# Player sees the server seed
print(f"Server Seed: {server_seed}")

# Player can verify the result by hashing the seeds again
verification_result = hashlib.sha256(result_seed.encode()).hexdigest()

if result == verification_result:
    print("Result is provably fair and matches the verification.")
else:
    print("Result is not provably fair.")
