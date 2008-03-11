# Copyright (c) 2006,2007 Mitch Garnaat http://garnaat.org/
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
from boto.pyami.config import Config, BotoConfigLocations
import os, sys
import logging
import logging.config

Version = '1.0a'
UserAgent = 'Boto/%s (%s)' % (Version, sys.platform)
config = Config()

def init_logging():
    for file in BotoConfigLocations:
        try:
            logging.config.fileConfig(os.path.expanduser(file))
        except:
            pass

log = logging
init_logging()

def connect_sqs(aws_access_key_id=None, aws_secret_access_key=None, **kwargs):
    from boto.sqs.connection import SQSConnection
    return SQSConnection(aws_access_key_id, aws_secret_access_key, **kwargs)
    
def connect_s3(aws_access_key_id=None, aws_secret_access_key=None, **kwargs):
    from boto.s3.connection import S3Connection
    return S3Connection(aws_access_key_id, aws_secret_access_key, **kwargs)

def connect_ec2(aws_access_key_id=None, aws_secret_access_key=None, **kwargs):
    from boto.ec2.connection import EC2Connection
    return EC2Connection(aws_access_key_id, aws_secret_access_key, **kwargs)

def connect_sdb(aws_access_key_id=None, aws_secret_access_key=None, **kwargs):
    from boto.sdb.connection import SDBConnection
    return SDBConnection(aws_access_key_id, aws_secret_access_key, **kwargs)

def connect_fps(aws_access_key_id=None, aws_secret_access_key=None, **kwargs):
    from boto.fps.connection import FPSConnection
    return FPSConnection(aws_access_key_id, aws_secret_access_key, **kwargs)

def check_extensions(module_name, module_path):
    """
    This function checks for extensions to boto modules.  It should be called in the
    __init__.py file of all boto modules.  See:
    http://code.google.com/p/boto/wiki/ExtendModules

    for details.
    """
    option_name = '%s_extend' % module_name
    version = config.get('Boto', option_name, None)
    if version:
        dirname = module_path[0]
        path = os.path.join(dirname, version)
        if os.path.isdir(path):
            log.info('extending module %s with: %s' % (module_name, path))
            module_path.insert(0, path)
