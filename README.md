# PMD Bot

A Discord bot written in Python 3.12 using [Pycord](https://pycord.dev)

PMD Bot recreates aspects of the Pokémon Mystery Dungeon universe for use in Discord servers.

----

### How to Use

PMD Bot is operated with modern Slash Commands. The available commands are as follows:

| Slash Commands | Effects                                             | Permissions |
|----------------|-----------------------------------------------------|-------------|
| `/pmd`         | Start of your Journey. Begins the Personality Test. | Everyone    |

----

## Install in Your Server

You can **[click here](https://discord.com/oauth2/authorize?client_id=1324951929851351062)** to install PMD Bot into your server.

----

#### [Debug/Development Instructions] Installation & Requirements for Running Your Own Instance for Debug & Development

Currently, you must populate a `.env` file with three values:

- `DISCORD_TOKEN`: must be populated with the bot's auth token from the developer portal
- `DEBUG_MODE`: Enable or disable debug mode as a boolean value, `1` or `0` (Disable this with `0` when deploying)

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

No server settings required.

### Special Thanks

This bot wouldn't have been possible without the help of the following:

The PMD Personality Quiz data provided by: [Nrosa01's PMD Quiz Online](https://github.com/Nrosa01/pmd-quiz-online)
