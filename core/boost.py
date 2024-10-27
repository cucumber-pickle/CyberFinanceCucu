import requests

from core.base import base
from core.headers import headers


def boost(token, boost_type,  proxies=None):
    url = "https://api.cyberfin.xyz/api/v1/mining/boost/info"

    try:
        response = requests.get(
            url=url, headers=headers(token=token), proxies=proxies, timeout=20
        )
        data = response.json()
        price = data["message"][boost_type]

        return int(price)
    except:
        return None


def buy_boost(token, boost_type, proxies=None):
    url = "https://api.cyberfin.xyz/api/v1/mining/boost/apply"
    payload = {"boostType": boost_type}

    try:
        response = requests.post(
            url=url,
            headers=headers(token=token),
            json=payload,
            proxies=proxies,
            timeout=20,
        )
        data = response.json()
        status = data["code"]
        return status
    except:
        return None


def process_buy_boost(token, limit_price, boost_type, proxies=None):
    while True:
        if boost_type =="EGG":
            boost_name = "Timer"
            price = boost(token=token,boost_type="eggPrice", proxies=proxies)
        else:
            boost_name = "Hammer"
            price = boost(token=token, boost_type="hammerPrice", proxies=proxies)
        if price < limit_price:
            base.log(
                f"{base.white}Auto Buy {boost_name}: {base.green}Start buying boost {base.white}| {base.yellow}Hammer Price: {base.white}{price:,} - {base.yellow}Limit Price: {base.white}{limit_price}"
            )
            buy_boost_status = buy_boost(token=token, boost_type=boost_type, proxies=proxies)
            if buy_boost_status == 200:
                base.log(f"{base.white}Auto Buy {boost_name}: {base.green}Success")
            else:
                base.log(
                    f"{base.white}Auto Buy {boost_name}: {base.red}Re-check your balance"
                )
                break
        else:
            base.log(
                f"{base.white}Auto Buy {boost_name}: {base.red}Limit reached. Stop! {base.white}| {base.yellow}{boost_name} Price: {base.white}{price:,} - {base.yellow}Limit Price: {base.white}{limit_price}"
            )
            break
