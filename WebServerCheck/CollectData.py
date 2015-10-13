import subprocess
import platform

__author__ = 'bharre001c'

import os



class EnvironmentInspector:

    def get_nginx_version(self):

        version_dict = {}

        version_cmd = subprocess.Popen('nginx -v', stderr=subprocess.PIPE, shell=True).stderr.read()

        if "nginx".lower() not in version_cmd:
            version_dict['webserver'] = "nginx not installed"
        else:
            version_dict['webserver'] = "nginx"
            if '1.2' not in  str(version_cmd).split()[2]:
                version_dict['webserver_version'] = "Not version 1.2.x"
            else:
                version_dict['webserver_version'] = str(version_cmd).split()[2]
                if "windows".lower() not in str(platform.platform()).lower():
                    root_enabled_cmd = subprocess.Popen('find / -name nginx.conf 2>/dev/null '
                                                        '| xargs -n1 grep root', stdout=subprocess.PIPE,
                                                        shell=True).stdout.read()
                    if "root" not in root_enabled_cmd:
                        version_dict['Root_Enabled'] = False
                    else:
                        version_dict['Root_Enabled'] = True
                else:
                    root_enabled_cmd = subprocess.Popen('Find-ChildItem $root -Recurse'
                                                        '| where {! $_.PSIContainer}|'
                                                        'select-string -pattern "root" $find').stdout.read()
                    if "root" not in root_enabled_cmd:
                        version_dict['Root_Enabled'] = False
                    else:
                        version_dict["Root_Enabled"] = True

        return version_dict

    def get_iis_version(self):

        version_dict ={}

        get_iis_version = subprocess.Popen(
            'get-itemproperty HKLM:\SOFTWARE\Microsoft\InetStp\  | select setupstring,versionstring',
            stdout=subprocess.PIPE,
            shell=True
        ).stdout.read()

        if "iis".lower() not in get_iis_version:
            version_dict['webserver'] = "IIS not installed"
        else:
            version_dict['webserver'] = "IIS"
            if "7.0" not in get_iis_version:
                version_dict['IIS_Version'] = "Version not 7.0.x"
            else:
                version_dict['IIS_Version'] = get_iis_version
                root_check = subprocess.Popen('appcmd --list config |findstr \i "section:enabled', stdout=subprocess.PIPE,
                                 shell=True).stdout.read()

                if "enabled" not in root_check:
                    version_dict['Root_Enabled'] = False
                else:
                    version_dict['Root_Enabled'] = True

        return version_dict
