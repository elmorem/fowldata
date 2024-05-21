from unittest.mock import patch

from psycopg2 import OperationalError
import pytest

from django.core.management import call_command
from django.db.utils import OperationalError

# def test_wait_for_db_ready(self):
#     with patch('core.management.commands.wait_for_db.Command.check') as patched_check:
#         patched_check.return_value = True
#         call_command('wait_for_db')
#         patched_check.assert_awaited_once_with(database=['default'])
