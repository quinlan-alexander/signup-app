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
import os
import re
from string import letters

import webapp2
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

def render(self, template, **params):
    t = jinja_env.get_template(template)
    self.response.out.write(t.render(params))

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASSWORD_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

class MainHandler(webapp2.RequestHandler):
    def get(self):
        render(self, "signup-form.html")

    def post(self):
        have_error = False
        username = self.request.get("username")
        password = self.request.get("password")
        confirm = self.request.get("verify")
        email = self.request.get("email")
        params = dict(username = username,
                      email = email)
        if not valid_username(username):
            params['error_username'] = "That's not a valid username."
            have_error = True

        if not valid_password(password, confirm):
            params['error_password'] = "That wasn't a valid password."
            have_error = True
        elif password != confirm:
            params['error_verify'] = "Your passwords didn't match."
            have_error = True

        if not valid_email(email):
            params['error_email'] = "That's not a valid email."
            have_error = True

        if have_error:
            render(self, 'signup-form.html', **params)
        else:
            self.redirect('/welcome?username=' + username)
        #if not valid_user(username,password,confirm,email):
            #writeForm(self,username,"","",email)
        #else:
            #self.response.out.write("<h2>Welcome "+username+"!</h2>")

def valid_user(username,password,confirm,email):
    if not valid_username(username):
        return False
    if not valid_password(password,confirm):
        return False
    if not valid_email(email):
        return False
    return True

def valid_username(username):
    return USER_RE.match(username)

def valid_password(password, confirm):
    if (PASSWORD_RE.match(password)):
        return True
    else:
        return False

def valid_email(email):
    if len(email) == 0:
        return True
    return EMAIL_RE.match(email)

class Welcome(webapp2.RequestHandler):
    def get(self):
        username = self.request.get('username')
        if valid_username(username):
            render(self, 'welcome.html', username = username)
        else:
            self.redirect('/')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', Welcome)
], debug=True)