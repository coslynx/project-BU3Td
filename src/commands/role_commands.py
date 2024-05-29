# role_commands.py (Python)

import discord

class RoleCommands:
    def __init__(self, client):
        self.client = client

    async def assign_role(self, ctx, member: discord.Member, role: discord.Role):
        try:
            await member.add_roles(role)
            await ctx.send(f"Role {role.name} has been assigned to {member.display_name}.")
        except discord.Forbidden:
            await ctx.send("I do not have permission to assign roles.")
        except discord.HTTPException:
            await ctx.send("Failed to assign the role.")

    async def remove_role(self, ctx, member: discord.Member, role: discord.Role):
        try:
            await member.remove_roles(role)
            await ctx.send(f"Role {role.name} has been removed from {member.display_name}.")
        except discord.Forbidden:
            await ctx.send("I do not have permission to remove roles.")
        except discord.HTTPException:
            await ctx.send("Failed to remove the role.")

    async def list_roles(self, ctx):
        roles = ctx.guild.roles
        role_list = [role.name for role in roles]
        await ctx.send("Available roles: " + ", ".join(role_list) + ".")

    async def check_role(self, ctx, member: discord.Member, role: discord.Role):
        if role in member.roles:
            await ctx.send(f"{member.display_name} has the role {role.name}.")
        else:
            await ctx.send(f"{member.display_name} does not have the role {role.name}.")