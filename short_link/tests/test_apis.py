import asyncio

from httpx import AsyncClient
import pytest
from fastapi import status

from faker import Faker

fake = Faker()

from src.main import app

BASE_URL = "http://0.0.0.0:80"
DEFAULT_TEST_URL = "https://google.com/"


@pytest.fixture(scope="session")
def event_loop():
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


@pytest.mark.asyncio
async def test_create_short_link_default():
    req_body = {"url": DEFAULT_TEST_URL}
    async with AsyncClient(app=app, base_url=BASE_URL) as ac:
        res = await ac.post("/short-links", json=req_body)
        assert res.status_code in [status.HTTP_200_OK, status.HTTP_201_CREATED]


@pytest.mark.asyncio
async def test_create_short_link_aleady_exist():
    # case with trailing slash
    req_body = {"url": DEFAULT_TEST_URL}
    async with AsyncClient(app=app, base_url=BASE_URL) as ac:
        res = await ac.post("/short-links", json=req_body)
        assert res.status_code == status.HTTP_200_OK

    # case without trailing slash
    req_body = {"url": DEFAULT_TEST_URL.strip("/")}
    async with AsyncClient(app=app, base_url=BASE_URL) as ac:
        res = await ac.post("/short-links", json=req_body)
        assert res.status_code == status.HTTP_200_OK


@pytest.mark.asyncio
async def test_create_short_link_res():
    req_body = {"url": fake.url()}
    async with AsyncClient(app=app, base_url=BASE_URL) as ac:
        res = await ac.post("/short-links", json=req_body)
        assert res.status_code == status.HTTP_201_CREATED
        data = res.json()
        assert data["data"]["shortId"]
        assert data["data"]["url"]
        assert data["data"]["createdAt"]


# @pytest.mark.asyncio
# async def test_get_short_url_res():
# short_id = await db.execute(select(models.ShortURL).filter_by(url=DEFAULT_TEST_URL)).scalar_one().short_id
# async with AsyncClient(app=app, base_url=BASE_URL) as ac:
#     res = await ac.get(f"/short-links/{short_id}")
#     assert res.status_code == status.HTTP_200_OK
#     data = res.json()
#     assert data["data"]["shortId"]
#     assert data["data"]["url"]
#     assert data["data"]["createdAt"]


# @pytest.mark.asyncio
# async def test_create_short_link_res():
# short_id = await db.execute(select(models.ShortURL).filter_by(url=DEFAULT_TEST_URL)).scalar_one().short_id
# async with AsyncClient(app=app, base_url=BASE_URL) as ac:
#     res = await ac.get(f"/r/{short_id}")
#     assert res.status_code == status.HTTP_302_FOUND
