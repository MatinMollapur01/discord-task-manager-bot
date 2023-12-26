import discord
from discord.ext import commands
import datetime

# Bot setup with intents
intents = discord.Intents.default()
intents.messages = True  # Enable the messages intent
intents.guilds = True  # Enable the guilds intent
bot = commands.Bot(command_prefix='!', intents=intents)

# Remove the default help command
bot.remove_command('help')

# Task data structure
tasks = []

# Command to add a task
@bot.command(name='addtask')
async def add_task(ctx, *, description):
    task = {'description': description, 'completed': False, 'timestamp': datetime.datetime.now()}
    tasks.append(task)
    await ctx.send(f'Task added: {description}')

# Command to list tasks
@bot.command(name='listtasks')
async def list_tasks(ctx):
    if tasks:
        task_list = '\n'.join(f"{i+1}. {task['description']} {'(Completed)' if task['completed'] else ''}" for i, task in enumerate(tasks))
        await ctx.send(f'**Tasks:**\n{task_list}')
    else:
        await ctx.send('No tasks available.')

# Command to complete a task
@bot.command(name='completetask')
async def complete_task(ctx, task_id: int):
    if 1 <= task_id <= len(tasks):
        tasks[task_id - 1]['completed'] = True
        await ctx.send(f'Task {task_id} marked as completed.')
    else:
        await ctx.send('Invalid task ID.')

# Bot token
bot.run('MTE4OTI5Mzk1MDAyNTA3MjczMQ.G87HB9.0GXped4GoDVkPoYisRMypNfwFdZJV49AxCV1-c')
