# Fixeruper
_Simple discord bot to fix X.com embeds_
## Installation:
- Create a new application at [discord.dev](https://discord.com/developers/)
- Take note of the application token
- Take note of your [server ID](https://docs.statbot.net/docs/faq/general/how-find-id/)

Use the following command:
```docker run -d \
--name=fixeruper \
-e PUID=1000 \
-e PGID=1000 \
-e TOKEN={DISCORD_BOT_TOKEN} \
-e GUILD_ID={YOUR_GUILD_ID} \
--restart unless-stopped \
jaymeswhyte/fixeruper:latest
