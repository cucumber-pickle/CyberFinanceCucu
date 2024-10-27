# Cyber Finance Telegram Bot

A Python-based automation scripts that uses no API Telegram for interacting with the Cyber Finance

[![Join our Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/cucumber_scripts)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/cucumber-pickle/Cucumber)

# REGISTRATIONS 

 **Referral Link**: [https://t.me/CyberFinanceBot/](https://t.me/CyberFinanceBot/game?startapp=cj04dmwxdWNnbWV2OTImdT1yZWY=)




## Installation
1. **Clone the Repository:**

   ```bash
   git clone https://github.com/cucumber-pickle/CyberFinanceCucu.git
   cd CyberFinanceCucu
   ```

2. **Create a virtual environment (optional but recommended)**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

   
3. **Install Dependencies:**

The bot uses Python 3 and requires some external libraries. You can install them using:

  ```bash
    pip install -r requirements.txt
  ```

## Configuration Setup:

Create a config.json file in the project root directory:

   ```json

{
  "auto_check_in": "false",
  "auto_do_task": "false",
  "auto_watch_ads": "false",
  "auto_claim": "false",
  "auto_buy_hammer": "true",
  "auto_buy_timer": "true",
  "timer_limit_price": 1000,
  "hammer_limit_price": 10000,
  "account_delay": 3,
  "cycle_delay": 100
}
   ```
- `auto_check_in`: Enable/disable auto_check_in (true/false).
- `auto_do_task`: Enable/disable auto_do_task (true/false).
- `auto_watch_ads`: Enable/disable auto_watch_ads (true/false).
- `auto_claim`: Enable/disable auto_claim (true/false).
- `auto_buy_hammer`: Enable/disable auto_buy_hammer (true/false).
- `auto_buy_timer`: Enable/disable auto_buy_timer (true/false).
- `hammer_limit_price`: Sets the maximum price limit for purchasing timers
- `hammer_limit_price`: Sets the maximum price limit for purchasing hammers
- `account_delay`: delay (in seconds) between processing different accounts
- `cycle_delay`: total duration (in seconds) for which the main loop will run before restarting or stopping

## About Proxy


You can add your proxy list in `proxies.txt` and proxy format is like example below :

Format :

```
http://host:port
http://user:pass@host:port
```

Example :

```
http://127.0.0.1:6969
http://user:pass@127.0.0.1:6969
```


## Query Setup:

Add your account tokens to a file named `data.txt` in the root directory. Each token should be on a new line.

Example:
   ```txt
query_id=AA....
user=%7B%22id%....
   ```

## Usage
Run the script with:

   ```bash
python bot.py
   ```


## How to get tgWebAppData (query_id / user_id)

1. Login telegram via portable or web version
2. Launch the bot
3. Press `F12` on the keyboard 
4. Open console
5. Сopy this code in Console for getting tgWebAppData (user= / query=):

```javascript
copy(Telegram.WebApp.initData)
```

6. you will get data that looks like this

```
query_id=AA....
user=%7B%22id%....
```
7. add it to `data.txt` file or create it if you dont have one


You can add more and run the accounts in turn by entering a query id in new line like this:
```txt
query_id=xxxxxxxxx-Rxxxxujhash=cxxx
query_id=xxxxxxxxx-Rxxxxujhash=cxxxx
```

after that run the Banana bot by writing the command

## Usage
To run the script, simply execute:

   ```bash
python bot.py
   ```
The script will start processing each account listed in query.txt, performing all configured operations.


## This bot helpfull?  Please support me by buying me a coffee: 
``` 0xc4bb02b8882c4c88891b4196a9d64a20ef8d7c36 ``` - BSC (BEP 20)

``` UQBiNbT2cqf5gLwjvfstTYvsScNj-nJZlN2NSmZ97rTcvKz0 ``` - TON

``` 0xc4bb02b8882c4c88891b4196a9d64a20ef8d7c36 ``` - Optimism

``` THaLf1cdEoaA73Kk5yiKmcRwUTuouXjM17 ``` - TRX (TRC 20)

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For questions or support, please contact [CUCUMBER TG CHAT](https://t.me/cucumber_scripts_chat)
