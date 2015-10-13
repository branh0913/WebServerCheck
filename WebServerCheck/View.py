import platform
from flask import Flask

__author__ = 'bharre001c'


import CollectData
from flask.ext.restful import Resource,Api, reqparse

app = Flask(__name__)
data_collector_endpoint = Api(app)

class GetWebserverVersion(Resource):

    def get(self):

        coll_data_inst = CollectData.EnvironmentInspector()

        version_dict = coll_data_inst.get_nginx_version()

        if "windows" in str(platform.platform()) and version_dict['webserver'] == "nginx not installed":
            pass
        else:
            return version_dict


data_collector_endpoint.add_resource(GetWebserverVersion, "/getVersion")

if __name__:
    app.run(debug=True)






