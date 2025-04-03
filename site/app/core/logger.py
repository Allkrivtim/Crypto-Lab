import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(message)s - %(asctime)s"
)

site_logger = logging.getLogger("Site")
router_logger = logging.getLogger("Router")
service_logger = logging.getLogger("Service")
database_logger = logging.getLogger("Database")