import time
from brownie import FundMe, MockV3Aggregator, accounts, network, config
from scripts.tools import get_account, deploy_mock, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from web3 import Web3


def main():
    deploy_fund_me()


def deploy_fund_me():
    account = get_account()

    # Setup price feed 
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        deploy_mock()
        price_feed_adr = MockV3Aggregator[-1].address
    else:
        price_feed_adr = config["networks"][network.show_active()]["eth_usd_adr"]

    fund_me = FundMe.deploy(price_feed_adr, {"from": account})
    time.sleep(1)
    print(f"Contract deployed to {fund_me.address}")
    return fund_me
