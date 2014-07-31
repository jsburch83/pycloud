__author__ = 'jdroot'

from pycloud.pycloud.pylons.lib.base import BaseController
from pycloud.pycloud.pylons.lib.util import asjson
from pycloud.pycloud.model import Service
import tarfile
import json
from pylons import request


def get_service_json(tar=None):
    member = None
    try:
        member = tar.getmember("service.json")
    except KeyError:
        pass

    f = tar.extractfile(member)
    val = json.loads(val)
    f.close()
    return val


class ImportController(BaseController):

    def GET_import(self):
        filename = request.params.get("filename")

        if not filename.endswith(".csvm"):
            return {"error": "Invalid file"}

        tar = tarfile.open(filename, "r")
        service_json = get_service_json(tar)

        return service_json