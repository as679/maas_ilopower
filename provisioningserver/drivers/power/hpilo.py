"""HP iLo Power Driver."""

__all__ = []

from importlib import (
    import_module,
    invalidate_caches,
)
from time import sleep
from provisioningserver.drivers.power import PowerDriver
from provisioningserver.logger import get_maas_logger


maaslog = get_maas_logger("drivers.power.hpilo")


class HPiloPowerDriver(PowerDriver):

    name = 'hpilo'
    description = "HP iLo Power Driver."
    settings = []
    hpilo = None

    def _power_control_hpilo(self, power_change, power_address=None, power_user=None, power_pass=None, **extra):
        client = self.hpilo.Ilo(power_address, power_user, power_pass)
        if power_change == 'on':
            client.set_host_power(host_power=True)
        elif power_change == 'off':
            client.set_host_power(host_power=False)
        sleep(1)
        return client.get_host_power_status().lower()

    def _try_hpilo_import(self):
        try:
            if self.hpilo is None:
                self.hpilo = import_module('hpilo')
        except ImportError:
            return False
        else:
            return True

    def detect_missing_packages(self):
        if not self._try_hpilo_import():
            return ["python-hpilo"]
        return []

    def power_on(self, system_id, context):
        self._power_control_hpilo('on', **context)

    def power_off(self, system_id, context):
        self._power_control_hpilo('off', **context)

    def power_query(self, system_id, context):
        return self._power_control_hpilo('query', **context)
