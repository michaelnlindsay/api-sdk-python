#!/usr/bin/python
# -*- coding: utf-8 -*-


''' Copyright 2012-2016 Smartling, Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this work except in compliance with the License.
 * You may obtain a copy of the License in the LICENSE file, or at:
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
'''

import urllib, urllib2
import sys
from Constants import ReqMethod

from MultipartPostHandler import MultipartPostHandler

class HttpClient:
     headers = {"Content-Type": "application/x-www-form-urlencoded"}
     
     def __init__(self, host, proxySettings=None):
        self.host = host
        self.proxySettings = proxySettings

     def getHttpResponseAndStatus(self, method, uri, params, handler=None, extraHeaders = {}, requestBody=""):
        if self.proxySettings:
            if self.proxySettings.username:
                proxy_str = 'http://%s:%s@%s:%s' % (self.proxySettings.username, self.proxySettings.passwd, self.proxySettings.host, self.proxySettings.port)
            else: 
                proxy_str = 'http://%s:%s' % (self.proxySettings.host, self.proxySettings.port)

            opener = urllib2.build_opener(
                handler or urllib2.HTTPHandler(),
                handler or urllib2.HTTPSHandler(),
                urllib2.ProxyHandler({"https": proxy_str}))
            urllib2.install_opener(opener)
        elif handler:
            opener = urllib2.build_opener(MultipartPostHandler)
            urllib2.install_opener(opener)
        
        if not handler:
            params = urllib.urlencode(params)

        headers = self.headers
        for k,v in extraHeaders.items():
            headers[k] = v
            
        
        url = 'https://' + self.host + uri
        if method is ReqMethod.GET: url += "?" + params
        req = urllib2.Request(url, params, headers=headers)
        req.get_method = lambda: method

        try:
            if requestBody:
                response = urllib2.urlopen(req, requestBody)
            else:
                response = urllib2.urlopen(req)
        except urllib2.HTTPError, e:
            response = e
        if sys.version_info[:2] >= (2,6):
            status_code = response.getcode() 
        else:
            status_code = response.code
            
        response_data = response.read()
        return response_data, status_code