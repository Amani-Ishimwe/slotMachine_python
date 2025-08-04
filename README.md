# 🎰 Python Slot Machine Simulator

This is a simple **text-based slot machine game** written in Python. The player can deposit money, choose how many lines to bet on, place bets per line, and spin the slot machine to try their luck. The game simulates random slot reels and calculates winnings based on matching symbols across selected lines.

---

## 🧠 Features

- Deposit and manage your virtual balance
- Bet on 1 to 3 lines per spin
- Randomly generated slot results
- Payout based on symbol values
- Clear display of winnings and lines won

---

## 🕹️ How It Works

- Each spin randomly selects a 3x3 grid of symbols (`A`, `B`, `C`, `D`) based on their frequency.
- If the same symbol appears across a full line (row), you win according to that symbol's value.
- You can play multiple rounds until you quit or run out of money.

---

## 💰 Symbols & Payouts

| Symbol | Frequency | Value (Multiplier) |
| ------ | --------- | ------------------ |
| A      | 2         | 5x                 |
| B      | 4         | 4x                 |
| C      | 6         | 3x                 |
| D      | 8         | 2x                 |

---

## 📦 How to Run

1. Make sure you have **Python 3** installed.
2. Save the following code into a file called `slot_machine.py`.
3. Open a terminal and run:

```bash
python slot_machine.py
```
