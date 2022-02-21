from brownie import FundMe, accounts
from scripts.tools import get_account


def main():
    fund()
    withdraw()


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(f"The entrace fee is {entrance_fee}, funding")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()

    fund_me.withdraw({"from": account})