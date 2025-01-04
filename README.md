# PMD Bot

A Discord bot written in Python using [Discord.py](https://github.com/Rapptz/discord.py)

PMD Bot runs a simulation of the Pokémon Mystery Dungeon universe for use in Discord channels.

### Installation & Requirements

Currently, you must populate a `.env` file with three values:

- `DISCORD_TOKEN`: must be populated with the bot's auth token from the developer portal
- `PMD_CHANNEL_ID`: must have the channel ID of the PMD bot channel (TEMPORARY MEASURE, VALUE TO BE REMOVED)
- `DEBUG_MODE`: Enable or disable debug mode as a boolean value, `1` or `0` (Disable this with `0` when deploying)
- `FILE_STORAGE`: Define a directory where the bot writes persistent data to, such as `/data/` or leave blank for local directory

#### Required permissions

The bot must be granted the following role permissions in order to function correctly:

TBD

#### Server Settings

TBD
