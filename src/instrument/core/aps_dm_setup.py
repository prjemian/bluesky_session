"""
APS Data Management setup
=========================

Read the bash shell script file used by DM to setup the environment. Parse any
``export`` lines and add their environment variables to this session.  This is
done by brute force here since the APS DM environment setup requires different
Python code than bluesky and the two often clash.

This setup must be done before any of the DM package libraries are called.
"""

import logging
import os
import pathlib

logger = logging.getLogger(__name__)
logger.info(__file__)

def dm_setup(dm_setup_file):
    '''
    '''
    if dm_setup_file is not None:
        bash_script = pathlib.Path(dm_setup_file)
        if bash_script.exists():
            logger.info("APS DM environment file: %s", str(bash_script))
            # parse environment variables from bash script
            environment = {}
            for line in open(bash_script).readlines():
                if not line.startswith("export "):
                    continue
                k, v = line.strip().split()[-1].split("=")
                environment[k] = v
            os.environ.update(environment)

            workflow_owner = os.environ["DM_STATION_NAME"].lower()
            logger.info("APS DM workflow owner: %s", workflow_owner)
        else:
            logger.warning("APS DM setup file does not exist: '%s'", bash_script)
