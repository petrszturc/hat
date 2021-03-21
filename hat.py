import logging

from configuration import RegisteredDrivers

log = logging.getLogger(__name__)


class Hat(object):
    """Runner, controls running individual platforms and their drivers\n
    Sits on top - hence the name. Plus hat=helper for application testing, haha.
    """
    # TODO Add loading configuration and adding it here

    def __init__(self,):
        pass

    def start_platform_driver(self, driver_to_start: str, *args, **kwargs):
        driver = RegisteredDrivers.get_driver_by_name(driver_to_start)
        try:
            return driver().start(*args, **kwargs)
        except TypeError as e:
            log.error(f"{e}")
            if "Can't instantiate abstract class" in str(e):
                log.error(f"Add implementation to your driver: {e}")
            raise e
