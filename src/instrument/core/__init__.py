"""
Utility support to start bluesky sessions.

Also contains setup code that MUST run before other code in this directory.
"""

from ..configs.loaders import iconfig
from ..utils.aps_helper_functions import aps_dm_setup
from ..utils.helper_functions import debug_python
from ..utils.helper_functions import mpl_setup

debug_python()
mpl_setup()
aps_dm_setup(iconfig.get("DM_SETUP_FILE"))
