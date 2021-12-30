# Basic-Discord.py-Bot
Today, I will show you how to get a basic Discord.py bot up and running for your server(s)! Since discord.py is no longer being maintained, we will be using Nextcord today. P.S. I am using [VSCode](https://code.visualstudio.com/), it's free and easy to use.

## 1.
Click on the Green Code button on this repository, then click on `Download Zip`. Unzip the folder, then open the folder with VSCode.

## 2.
While you have the folder open in VSCode, open up a terminal by clicking on `New Terminal` on the top. Then type `pip install nextcord`. This will install the most up-to-date version of nextcord. If you plan to have a music bot or make your bot join a vc, you must also do `pip install nextcord[voice]`.

## 3.
Go to `bot.py` and change where it says `token here` to your bot's token. Keep the parenthesis where they are.

## 4.
If you want to have a different prefix than `!`, you can change it where it says `command_prefix="!"` to anything like `command_prefix="?"` or `command_prefix="."`, etc.

## 5.
Now you can run your bot! Open up a new terminal and type `python bot.py`! You should then see `Discord Bot is now online!`

Nextcord API: https://nextcord.readthedocs.io/en/latest/
Nextcord GitHub Repo: https://github.com/nextcord/nextcord
VSCode: https://code.visualstudio.com/
