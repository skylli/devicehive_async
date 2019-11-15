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

from devicehive.device_hive import DeviceHive
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
url = 'http://iotcloud.nielink.com/api/rest'
refresh_token = 'eyJhbGciOiJIUzI1NiJ9.eyJwYXlsb2FkIjp7ImEiOlswXSwiZSI6MTU3Mzc1MDAyMDU3MCwidCI6MSwidSI6MiwibiI6WyIqIl0sImR0IjpbIioiXX19.J7gRKNclxEro4RSMsTKTCMPfx0n3fVgm8HS2CfBUHeE'
device_hive_api = DeviceHive(url, refresh_token=refresh_token)
info = device_hive_api.get_info()
print(info)
cluster_info = device_hive_api.get_cluster_info()
print("get info ", cluster_info)