import discord
from discord.ext import commands
import checks
import asyncio

class srReader():
    def __init__(self, bot):
        self.bot = bot

    @checks.is_owner()
    @commands.command(name='srReader', pass_context=True)
    async def srReader(self, ctx):
        '''Reader'''
        await self.bot.delete_message(ctx.message)

        msg = await self.bot.say('Reader')
        await self.bot.add_reaction(msg, discord.utils.get(self.bot.get_all_emojis(), id='white_check_mark'))
        await self.bot.add_reaction(msg, discord.utils.get(self.bot.get_all_emojis(), id='negative_squared_cross_mark'))
        await asyncio.sleep(0.1)
        while True:
            res = await self.bot.wait_for_reaction([discord.utils.get(self.bot.get_all_emojis(), id='white_check_mark'), discord.utils.get(self.bot.get_all_emojis(), id='negative_squared_cross_mark')], message=msg)
            if res.reaction.emoji == discord.utils.get(self.bot.get_all_emojis(), id='white_check_mark'):
                await self.bot.remove_reaction(msg, discord.utils.get(self.bot.get_all_emojis(), id='white_check_mark'), res.user)
                await self.bot.add_roles(res.user, discord.utils.get(msg.server.roles, name="Reader"))
            elif res.reaction.emoji == discord.utils.get(self.bot.get_all_emojis(), id='negative_squared_cross_mark'):
                await self.bot.remove_reaction(msg, discord.utils.get(self.bot.get_all_emojis(), id='negative_squared_cross_mark'), res.user)
                await self.bot.remove_roles(res.user, discord.utils.get(msg.server.roles, name="Reader"))

def setup(bot):
    bot.add_cog(srReader(bot))