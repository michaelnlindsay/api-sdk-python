#!/usr/bin/python
# -*- coding: utf-8 -*-


''' Copyright 2012 Smartling, Inc.
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

import json

import urllib.request as urllib2


class Callable:
    def __init__(self, anycallable):
        self.__call__ = anycallable


class JsonPostHandler(urllib2.BaseHandler):
    """ handler for json requests """

    handler_order = urllib2.HTTPHandler.handler_order - 10  # needs to run first
    # Controls how sequences are uncoded. If true, elements may be given multiple values by
    #  assigning a sequence.
    doseq = 1

    def encode_list_params(self, params):
        return params
        # return json.dumps(params)

    def http_request(self, request):
        contentType = 'application/json'
        request.add_unredirected_header('Content-Type', contentType)
        request.headers["Content-type"] = contentType
        request.data = json.dumps(request.data)
        request.data = request.data.encode()
        return request
