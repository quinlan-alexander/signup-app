#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
#
import webapp2
import re

class MainHandler(webapp2.RequestHandler):
    def get(self):
        writeForm(self)

def writeForm(self):
    form="""
    <h2>Signup</h2>
    <form method="post">
    <table>
    <tr>
    <td class="label">Username</td>
    <td>
    <input type="text" name="username" value="">
    </td>
    <td class="error">        
    </td>
    </tr>
    <tr>
    <td class="label">Password</td>
    <td>
    <input type="password" name="password" value="">
    </td>
    <td class="error">        
    </td>
    </tr>
    <tr>
    <td class="label">Verify Password
    </td>
    <td>
    <input type="password" name="verify" value="">
    </td>
    <td class="error">        
    </td>
    </tr>
    <tr>
    <td class="label">Email (optional)</td>
    <td>
    <input type="text" name="email" value="">
    </td>
    <td class="error">        
    </td>
    </tr>
    </table>
    <input type="submit">
    </form>
    """
    self.response.out.write(form)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
