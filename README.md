# Minecraft-Online-Status

This script is designed to monitor the online/offline status of Minecraft users and notify a designated Discord channel when their status changes. It utilizes the Discord API and the Mojang and Hypixel APIs to retrieve user information and status.

## Prerequisites

- Python 3.6 or higher
- Discord.py library (`pip install discord.py`)
- Requests library (`pip install requests`)

## Installation

1. Clone or download the script to your local machine.
2. Install the required libraries mentioned above.
3. Replace the placeholders in the script with your own values:
   - `TOKEN`: Replace with your Discord bot token.
   - `ID`: Replace with the ID of the Discord channel you want to send notifications to.
   - `users`: Replace with the Minecraft usernames you want to monitor (can be multiple).
   - `key`: Replace with your Hypixel API key.
4. Save the changes.

## Usage

1. Make sure your Discord bot is invited to the server and has appropriate permissions to read and send messages in the designated channel.
2. Run the script using the command `python script_name.py` or any equivalent command for running Python scripts.
3. The script will log in as the Discord bot and start monitoring the Minecraft users' online/offline status.
4. Whenever a user's status changes, the script will send a notification message to the designated Discord channel.

Note: The script will continuously run and check the status every 10 seconds. To stop the script, you can terminate the process manually.

## Contributing

Contributions to this script are welcome. If you find any issues or have suggestions for improvements, please feel free to create a pull request or open an issue.

## License

This project is licensed under the [MIT License](LICENSE).
