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
import os
import inspect
import sys
#from pydrive.auth import GoogleAuth
#from pydrive.drive import GoogleDrive
from pdfScript import pdfPageFunction, pdfValueFinder
import csv
#from fileScript import fileDirectory, listSpecificFile, removeFiles, moveFiles
#import gDrive
import sys

##Inserting access to lib directory##
sys.path.insert(0, 'lib')

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	html_template = """ 
        <html>
        <body>
           <form method=POST action="gDrive.py">
              <p>Input ldap and click "run_ChungLee"</p>
              <input type="text" name="text_value"><br>
              <input type=submit value="run_ChungLee"></input>
           </form>
        </body>
        </html>
    	"""
        print "---------------------------------"
        print webapp2.RequestHandler.response
        print "---------------------------------" 
        self.response.write(html_template)
        

class run_gDrive(webapp2.RequestHandler):
    def post(self):
        text_value = self.request.get("text_value")
        html_template = """ 
        <html>
        <body>
           <p>Chill for a bit while Chung Lee kicks invoices around ;)))</p>
        </body>
        </html>
      """
        self.response.write(html_template)
        import gDrive
        html_template = """<html><body> Thanks for waiting {}</body></html>""".format(text_value)
        self.response.write(html_template)


app = webapp2.WSGIApplication([('/', MainHandler), ('/gDrive.py',run_gDrive)], debug=True)
