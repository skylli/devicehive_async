# Copyright (C) 2018 DataArt
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================

from aiodevicehive.device_hive import DeviceHive
import logging
import aiohttp
import asyncio

async def make_reqeust():

    url = 'http://192.168.0.12/api/rest'
    login = 'sky'
    password = "sky9527"
    device_hive_api = DeviceHive(url, login=login, password=password)
    user = await device_hive_api.get_current_user()
    info = await device_hive_api.create_long_token( user.id, minutes = 3, actions=["*"],
                     network_ids=["*"], device_type_ids=["*"], device_ids=["*"])
    print(info)
    await device_hive_api.disconnect()

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger( __name__ )
loop = asyncio.get_event_loop()
loop.run_until_complete(make_reqeust())
