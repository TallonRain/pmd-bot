# PMD Bot

A Discord bot written in Python using [Pycord](https://pycord.dev)

PMD Bot runs a simulation of the Pokémon Mystery Dungeon universe for use in Discord channels.

## [Recommended] Install in Your Server

You can [click here](https://discord.com/oauth2/authorize?client_id=1324951929851351062) to install PMD Bot into your server.

### [Optional] Installation & Requirements for Running Your Own Instance

Currently, you must populate a `.env` file with three values:

- `DISCORD_TOKEN`: must be populated with the bot's auth token from the developer portal
- `PMD_CHANNEL_ID`: must have the channel ID of the PMD bot channel (TEMPORARY MEASURE, VALUE TO BE REMOVED)
- `DEBUG_MODE`: Enable or disable debug mode as a boolean value, `1` or `0` (Disable this with `0` when deploying)
- `FILE_STORAGE`: Define a directory where the bot writes persistent data to, such as `/data/` or leave blank for local directory

#### Required permissions

The bot must be granted the following role permissions in order to function correctly:

- View Channel
- Send Messages
- Embed Links
- Read Message History
- Use Applicaion Commands
- Send Messages in Threads

This list is subject to change. Additional permissions may be required in future builds of PMD Bot.

#### Server Settings

Assign a bot channel for your server and then configure PMD Bot for it.
Further details TBD.

### Special Thanks

This bot wouldn't have been possible without the help of the following:

The PMD Personality Quiz data provided by: [Nrosa01's PMD Quiz Online](https://github.com/Nrosa01/pmd-quiz-online)
