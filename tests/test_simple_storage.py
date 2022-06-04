from brownie import accounts, SimpleStorage
def test_retrieve():
    #Act
    account = accounts[0]
    #arrange
    simple_storage = SimpleStorage.deploy({"from":account})
    expected =0
    #assert
    assert expected == simple_storage.retrieve()