#!/usr/bin/env python3

#   Copyright 2014-2018 PUNCH Cyber Analytics Group
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from abc import abstractmethod
from typing import Optional

from stoq.data_classes import ArchiverResponse, Payload, RequestMeta
from stoq.plugins import BasePlugin


class ArchiverPlugin(BasePlugin):
    @abstractmethod
    def archive(
        self, payload: Payload, request_meta: RequestMeta
    ) -> Optional[ArchiverResponse]:
        pass

    @abstractmethod
    def get(self, task: str) -> Optional[Payload]:
        pass