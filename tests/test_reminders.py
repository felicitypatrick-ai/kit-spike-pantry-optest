import unittest

from app.reminders import reminder_message


class ReminderTests(unittest.TestCase):
    def test_message_names_family_and_time(self):
        text = reminder_message("Garcia", "10:30")
        self.assertIn("Garcia", text)
        self.assertIn("10:30", text)
