# Copyright (C) 2009 Mark A. Matienzo
#
# This file is part of the brooklynmuseumapi Python module.
#
# brooklynmuseumapi is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# brooklynmuseumapi is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with brooklynmuseumapi.  If not, see <http://www.gnu.org/licenses/>.

# request.py - request classes for brooklynmuseumapi


from urllib import urlencode as uenc
import urllib2

try:
    import json
except ImportError:
    import simplejson as json


class BrooklynMuseumAPIRequest(object):
    """docstring for BrooklynMuseumAPIRequest"""
    def __init__(self, api_key=None, version=1, format='json'):
        self.url = 'http://www.brooklynmuseum.org/opencollection/api/'
        if api_key is not None:
            self._params = {'api_key': api_key,
                            'version': version,
                            'format': format}
        else:
            raise


    def search(self, **kwargs):
        req_url = '%s?%s&method=collection.search&%s' % \
            (self.url, uenc(self._params), uenc(kwargs))
        rsp = urllib2.urlopen(req_url).read()
        if self._params['format'] == 'json':
            return json.loads(rsp)
        else:
            return rsp

    def item(self, **kwargs):
        if 'item_type' in kwargs and 'item_id' in kwargs:
            req_url = '%s?%s&method=collection.getItem&%s' % \
                (self.url, uenc(self._params), uenc(kwargs))
            rsp = urllib2.urlopen(req_url).read()
            if self._params['format'] == 'json':
                return json.loads(rsp)
            else:
                return rsp
        else:
            raise
    
    def images(self, **kwargs):
        if 'item_type' in kwargs and 'item_id' in kwargs:
            req_url = '%s?%s&method=collection.getImages&%s' % \
                (self.url, uenc(self._params), uenc(kwargs))
            rsp = urllib2.urlopen(req_url).read()
            if self._params['format'] == 'json':
                return json.loads(rsp)
            else:
                return rsp
        else:
            raise