from .models import async_session
from .models import User, Producer, Item
from sqlalchemy import select


async def set_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()


async def get_producers():
    async with async_session() as session:
        return await session.scalars(select(Producer))


async def get_producer_item(producer_id):
    async with async_session() as session:
        return await session.scalars(select(Item).where(Item.producer == producer_id))

async def get_item(item_id):
    async with async_session() as session:
        return await session.scalar(select(Item).where(Item.id == item_id))
