# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 10:52:03 2022

@author: ASUS
"""
import nest_asyncio
nest_asyncio.apply()


from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

