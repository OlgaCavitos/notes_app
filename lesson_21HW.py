#Task 1

import os
import unittest
import tempfile


class LoggingOpen:
    counter = 0
    log_file = "log_2.txt"

    def __init__(self, filename, mode="r", *args, **kwargs):
        self.filename = filename
        self.mode = mode
        self.args = args
        self.kwargs = kwargs
        self._file = None

    def _log(self, message):
        with open(self.log_file, "a", encoding="utf-8") as log:
            log.write(message + "\n")

    def __enter__(self):
        LoggingOpen.counter += 1
        self._file = open(self.filename, self.mode, *self.args, **self.kwargs)
        msg = f"Open the file: {self.filename} in: {self.mode} (Opened file {LoggingOpen.counter} times)"
        self._log(msg)
        return self._file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._file and not self._file.closed:
            self._file.close()
            self._log(f"File {self.filename} closed")
        return False


#Task2

class TestLoggingOpen(unittest.TestCase):
    def setUp(self):
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.test_filename = temp_file.name
        temp_file.close()

        log_temp = tempfile.NamedTemporaryFile(delete=False)
        self.log_filename = log_temp.name
        log_temp.close()

        LoggingOpen.log_file = self.log_filename
        LoggingOpen.counter = 0

    def tearDown(self):
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)
        if os.path.exists(self.log_filename):
            os.remove(self.log_filename)

    def read_log(self):
        with open(self.log_filename, "r", encoding="utf-8") as log:
            return log.read()

    def test_write_read_file(self):
        text = "Some text"
        with LoggingOpen(self.test_filename, "w", encoding="utf-8") as f:
            f.write(text)

        with LoggingOpen(self.test_filename, "r", encoding="utf-8") as f:
            content = f.read()


        self.assertEqual(content, text)
        self.assertEqual(LoggingOpen.counter, 2)

    def test_logging(self):
        with LoggingOpen(self.test_filename, "w", encoding="utf-8") as f:
            f.write("Log text")

        log_content = self.read_log()


        self.assertIn("Open the file", log_content)
        self.assertIn("closed", log_content.lower())




if __name__ == "__main__":
    unittest.main()
