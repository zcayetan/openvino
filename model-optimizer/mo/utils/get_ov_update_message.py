"""
 Copyright (C) 2018-2020 Intel Corporation

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

import datetime

msg_fmt = 'It\'s been a while, check for a new version of ' + \
          'Intel(R) Distribution of OpenVINO(TM) toolkit here {0} or on the GitHub*'


def get_ov_update_message():
    expected_update_date = datetime.date(year=2020, month=10, day=1)
    current_date = datetime.date.today()

    link = 'https://software.intel.com/en-us/openvino-toolkit/choose-download?cid=&source=upgrade&content=2020_3_LTS'

    return msg_fmt.format(link) if current_date >= expected_update_date else None
