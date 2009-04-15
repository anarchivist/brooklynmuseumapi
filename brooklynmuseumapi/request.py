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
    import json                 # Python >= 2.6
except ImportError:
    import simplejson as json   # otherwise require simplejson


class BrooklynMuseumAPI(object):
    """BrooklynMuseumAPI: object to perform requests to the APIs"""
    def __init__(self, api_key=None, version=1, format='json', parsing=True):
        self.url = 'http://www.brooklynmuseum.org/opencollection/api/'
        self.parsing = parsing
        if api_key is not None:
            self._params = {'api_key': api_key,
                            'version': version,
                            'format': format}
        else:
            raise


    def search(self, **kwargs):
        """BrooklynMuseumAPI.search: perform a collection.search request"""
        req_url = '%s?%s&method=collection.search&%s' % \
            (self.url, uenc(self._params), uenc(kwargs))
        rsp = urllib2.urlopen(req_url).read()
        return self.parse_response(rsp)


    def item(self, **kwargs):
        """BrooklynMuseumAPI.item: perform a collection.getItem request"""
        if 'item_type' in kwargs and 'item_id' in kwargs:
            req_url = '%s?%s&method=collection.getItem&%s' % \
                (self.url, uenc(self._params), uenc(kwargs))
            rsp = urllib2.urlopen(req_url).read()
            return self.parse_response(rsp)
        else:
            raise


    def images(self, **kwargs):
        """BrooklynMuseumAPI.images: perform a collection.getImages request"""
        if 'item_type' in kwargs and 'item_id' in kwargs:
            req_url = '%s?%s&method=collection.getImages&%s' % \
                (self.url, uenc(self._params), uenc(kwargs))
            rsp = urllib2.urlopen(req_url).read()
            return self.parse_response(rsp)
        else:
            raise


    def parse_response(self, rsp):
        """BrooklynMuseumAPI.parse_response: parse a response from the API
        
        TODO: Add handling for XML responses
        """
        if self.parsing is True:
            if (self._params['format'] == 'json'):
                return json.loads(rsp)
        else:
            return rsp
