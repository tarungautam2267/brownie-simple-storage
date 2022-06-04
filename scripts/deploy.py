from brownie import accounts, SimpleStorage, config, network

def deploycontract():
    account = get_account()
    simple_storage=SimpleStorage.deploy({"from":account})
    print(simple_storage)
    stored_val = simple_storage.retrieve()
    print(stored_val)
    transaction = simple_storage.store(15, {"from":account})
    transaction.wait(1)
    updated_val = simple_storage.retrieve()
    print(updated_val)

def get_account():
    if network.show_active()=="development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
def main():
    deploycontract()