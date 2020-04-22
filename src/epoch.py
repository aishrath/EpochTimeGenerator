"""
   Copyright 2020 Aishwareeya Rath

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
import time

from fastapi import *
from starlette.responses import Response

app = FastAPI()


@app.get("/")
def unix_time():
    """ Returns the current Unix timestamp. """
    t = str(int(time.time()))
    return Response("%s\n" % t, media_type="text/plain")
