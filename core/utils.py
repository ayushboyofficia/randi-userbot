import asyncio

async def animate_text(message, frames, delay=0.2):
    for frame in frames:
        await message.edit(frame)
        await asyncio.sleep(delay)
