"""
ophyd-related setup
===================

.. autosummary::
    ~oregistry
    ~set_control_layer
    ~set_timeouts
"""

import logging

import ophyd
from ophyd.signal import EpicsSignalBase
from ophydregistry import Registry

logger = logging.getLogger(__name__)  # noqa
logger.info(__file__)  # noqa

from .config import iconfig  # noqa

DEFAULT_CONTROL_LAYER = "PyEpics"
DEFAULT_TIMEOUT = 60  # default used next...
ophyd_config = iconfig.get("OPHYD", {})


def set_control_layer(control_layer: str = DEFAULT_CONTROL_LAYER):
    """
    Communications library between ophyd and EPICS Channel Access.

    Choices are: PyEpics (default) or caproto.

    OPHYD_CONTROL_LAYER is an application of "lessons learned."

    Only used in a couple rare cases where PyEpics code was failing.
    It's defined here since it was difficult to find how to do this
    in the ophyd documentation.
    """

    control_layer = ophyd_config.get("CONTROL_LAYER", control_layer)
    ophyd.set_cl(control_layer.lower())

    logger.info("using ophyd control layer: %r", ophyd.cl.name)


def set_timeouts():
    """Set default timeout for all EpicsSignal connections & communications."""
    if not EpicsSignalBase._EpicsSignalBase__any_instantiated:
        # Only BEFORE any EpicsSignalBase (or subclass) are created!
        timeouts = ophyd_config.get("TIMEOUTS", {})
        EpicsSignalBase.set_defaults(
            auto_monitor=True,
            timeout=timeouts.get("PV_READ", DEFAULT_TIMEOUT),
            write_timeout=timeouts.get("PV_WRITE", DEFAULT_TIMEOUT),
            connection_timeout=iconfig.get("PV_CONNECTION", DEFAULT_TIMEOUT),
        )


set_control_layer()
set_timeouts()  # MUST happen before ANY EpicsSignalBase (or subclass) is created.

oregistry = Registry(auto_register=True)
"""Registry of all ophyd-style Devices and Signals."""
