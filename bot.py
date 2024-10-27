import sys

sys.dont_write_bytecode = True
import os
from core.base import base
from core.token import get_token
from core.info import game_data
from core.task import process_check_in, process_do_task, process_watch_ads
from core.claim import process_claim
from core.boost import process_buy_boost
import time
import json
from urllib.parse import parse_qs


def read_config():
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    with open(config_path, 'r') as file:
        try:
            config_content = file.read()
            return json.loads(config_content)
        except json.JSONDecodeError as e:
            return {}

def extract_user_name(auth_data: str) -> dict:
    query_params = parse_qs(auth_data)
    user_name = json.loads(query_params['user'][0]).get("username")
    return user_name

config = read_config()

class CyberFinanace:
    def __init__(self):
        # Get file directory
        self.data_file = base.file_path(file_name="data.txt")
        self.proxy_file = base.file_path(file_name="proxies.txt")
        self.config_file = base.file_path(file_name="config.json")

        # Initialize line
        self.line = base.create_line(length=50)

        # Initialize banner
        self.banner = base.create_banner(game_name="Cyber Finance")

        self.auto_check_in = config.get('auto_check_in', False)
        self.auto_do_task = config.get('auto_do_task', False)
        self.auto_watch_ads = config.get('auto_watch_ads', False)
        self.auto_claim = config.get('auto_claim', False)
        self.auto_buy_hammer = config.get('auto_buy_hammer', False)
        self.auto_buy_timer = config.get('auto_buy_timer', False)
        self.hammer_limit_price = config.get('hammer_limit_price', 1000)
        self.timer_limit_price = config.get('timer_limit_price', 1000)
        self.account_delay = config.get('account_delay', 3)
        self.cycle_delay = config.get('cycle_delay', 1000)

    def main(self):
        while True:
            accounts = open(self.data_file, "r").read().splitlines()
            proxies = open(self.proxy_file, "r").read().splitlines()
            if len(proxies) < len(accounts):
                proxies.extend([None] * (len(accounts) - len(proxies)))
            else:
                proxies = proxies
            num_acc = len(accounts)
            base.log(self.line)
            base.log(f"{base.green}Numer of accounts: {base.white}{num_acc}")

            for no, (data, proxy_info) in enumerate(zip(accounts, proxies)):
                base.log(self.line)

                user_name = extract_user_name(data)

                base.log(f"{base.green}Account number: {base.white}{no+1}/{num_acc}")
                base.log(f"{base.green}User name: {base.white}{user_name}")
                if proxy_info:
                    try:
                        parsed_proxy_info = base.parse_proxy_info(proxy_info)
                        actual_ip = base.check_ip(proxy_info=proxy_info)
                        proxies = base.format_proxy(proxy_info=proxy_info)
                    except:
                        base.log(f"{base.red}Bad proxy, proxies = None!")
                        proxies = None
                else:
                    base.log(f"{base.red}No proxy used!")
                    proxies = None

                try:
                    token = get_token(data=data)


                    if token:
                        balance = game_data(token=token, proxies=proxies)
                        base.log(f"{base.green}Balance: {base.white}{balance:,}")

                        # Check in
                        if self.auto_check_in:
                            base.log(f"{base.yellow}Auto Check-in: {base.green}ON")
                            process_check_in(token=token, proxies=proxies)
                        else:
                            base.log(f"{base.yellow}Auto Check-in: {base.red}OFF")

                        # Do task
                        if self.auto_do_task:
                            base.log(f"{base.yellow}Auto Do Task: {base.green}ON")
                            process_do_task(token=token, proxies=proxies)
                        else:
                            base.log(f"{base.yellow}Auto Do Task: {base.red}OFF")

                        # Watch ads
                        if self.auto_watch_ads:
                            base.log(f"{base.yellow}Auto Watch Ads: {base.green}ON")
                            process_watch_ads(token=token, proxies=proxies)
                        else:
                            base.log(f"{base.yellow}Auto Watch Ads: {base.red}OFF")

                        # Claim
                        if self.auto_claim:
                            base.log(f"{base.yellow}Auto Claim: {base.green}ON")
                            process_claim(token=token, proxies=proxies)
                        else:
                            base.log(f"{base.yellow}Auto Claim: {base.red}OFF")

                        # Buy Hammer
                        if self.auto_buy_hammer:
                            base.log(f"{base.yellow}Auto Buy Hammer: {base.green}ON")
                            process_buy_boost(
                                token=token,
                                limit_price=self.hammer_limit_price,
                                boost_type="HAMMER",
                                proxies=proxies,
                            )
                        else:
                            base.log(f"{base.yellow}Auto Buy Hammer: {base.red}OFF")

                        if self.auto_buy_timer:
                            base.log(f"{base.yellow}Auto Buy timer: {base.green}ON")
                            process_buy_boost(
                                token=token,
                                limit_price=self.timer_limit_price,
                                boost_type="EGG",
                                proxies=proxies,
                            )
                        else:
                            base.log(f"{base.yellow}Auto Buy timer: {base.red}OFF")

                        balance = game_data(token=token, proxies=proxies)
                        base.log(f"{base.green}Balance: {base.white}{balance:,}")
                    else:
                        base.log(f"{base.red}Token not found! Please get new query id")
                except Exception as e:
                    base.log(f"{base.red}Error: {base.white}{e}")
                time.sleep(self.account_delay)

            print()
            base.log(f"{base.yellow}Wait for {int(self.cycle_delay/1)} seconds!")
            time.sleep(self.cycle_delay)


if __name__ == "__main__":
    try:
        banner = base.create_banner(game_name="Cyber Finance")
        base.clear_terminal()
        print(banner )
        cyberfinance = CyberFinanace()
        cyberfinance.main()
    except KeyboardInterrupt:
        sys.exit()
