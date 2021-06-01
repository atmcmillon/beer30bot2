## The Return of Beer30Bot!

# What is Beer30Bot2?
With a mix of both in-person and virtual cocktail hours, parties, and tastings, it's hard to know what you want to drink these days. Beer30Bot2 is a discord bot that informs users of some different breweries to sample while working from home, or while hanging out with the guild, or any other time you feel adventurous about imbibements!

Beer30Bot2 uses a few different python modules:

`os
discord
discord.ext, commands
art, text2art
datetime, datetime
OpenBreweryDB
time, localtime, strftime`

These allow users to make commands to Beer30Bot2 that either tell them the time, or gives them beer recommendations. The two primary jobs are a repeated task that notifies the group that it is Beer:30, followed by the function that recommends breweries to people from the `pandas`-based OpenBreweryDB library.

Secondary functions tell the channel the current time in ascii code with a user's request, prints to the channel a user's word request as ascii art, and notifies the developer that it is online when it is running.

# Current Issues
Beer30Bot2 has a few setbacks currently. The daily-repeated task (`beer_30()`) doesn't print to the channel and instead returns errors dependent on what solution(s) I try. I also want the brewery recommendation function (`recmeone()`) to tell users that their city/state request is not in the OpenBreweryDB database so they can try another location, or make it optional to only search breweries by state and make city an optional argument. Some cities or states also have two words in the name, so users have to change a request such as `Los Angeles` to `"Los Angeles"`.

# List of Command Functions Available
`beerme` --Turns a user's one-word input into ascii art and returns it to the channel.
`bio` --Tells the channel about itself, including its back end location.
`popatop` --Reports to the channel the current time, in ascii art, based on a user request.
`recmeone` --Gives the user a user-selected quantity of beers to try from places of their choice or somewhere else in the world.

# Requirements
Beer30Bot2 requires the above python modules to operate. `os` and `time` are built-in to the Python language, so no need to fret there. For everything else, use `python3 -m pip install libname` in your terminal for `art`, `datetime`, `discord/discord.ext/discord.utils`, and `openbrewerydb`.
