import discord
from discord.ext import commands
import checks
import asyncio

class srPhotographer():
    def __init__(self, bot):
        self.bot = bot

    @checks.is_owner()
    @commands.command(name='srPhotographer', pass_context=True)
    async def srPhotographer(self, ctx):
        '''Photographer'''
        await self.bot.delete_message(ctx.message)

        msg = await self.bot.say('Photographer')
        await self.bot.add_reaction(msg, '\U0001f4e5')
        await self.bot.add_reaction(msg, '\U0001f4e4')
        await asyncio.sleep(0.1)
        while True:
            res = await self.bot.wait_for_reaction(['\U0001f4e5', '\U0001f4e4'], message=msg)
            if res.reaction.emoji == '\U0001f4e5':
                await self.bot.remove_reaction(msg, '\U0001f4e5', res.user)
                await self.bot.add_roles(res.user, discord.utils.get(msg.server.roles, name="Photographer"))
            elif res.reaction.emoji == '\U0001f4e4':
                await self.bot.remove_reaction(msg, '\U0001f4e4', res.user)
                await self.bot.remove_roles(res.user, discord.utils.get(msg.server.roles, name="Photographer"))

def setup(bot):
    bot.add_cog(srPhotographer(bot))