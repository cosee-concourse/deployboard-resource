import unittest
import json
import out
from concourse_common import testutil


class TestOutput(unittest.TestCase):

    def test_json_output_wrong_source(self):
        testutil.put_stdin(json.dumps({"source": {"SLACK_BOT_TOKEN": "test"}, "params": {"version": "1.1.0",
                                                                                         "command": "1.1.0",
                                                                                         "channel": "sdfswfew",
                                                                                         "directory": "1.1.0",
                                                                                         "pipeline_step": "1.1.0"}}))
        self.assertEquals(out.execute("/"), -1)

    def test_json_output_typo(self):
        testutil.put_stdin(json.dumps({"source": {"AWS_ACCESS_KEY": "test", "AWS_SECRET_KEY": "test"},
                                       "params": {
                                       "version": "1.1.0",
                                       "bucket": "failure",
                                       "direcory": "1.1.0"}}))
        self.assertEquals(out.execute("/"), -1)

    def test_json_output_no_bucket(self):
        testutil.put_stdin(json.dumps({"source": {"AWS_ACCESS_KEY": "test", "AWS_SECRET_KEY": "test"},
                                       "params": {
                                       "bucket": "failure",
                                       "directory": "1.1.0"}}))
        self.assertEquals(out.execute("/"), -1)

    def test_json_output_no_version(self):
        testutil.put_stdin(json.dumps({"source": {"AWS_ACCESS_KEY": "test", "AWS_SECRET_KEY": "test"},
                                       "params": {
                                           "bucket": "failure",
                                           "directory": "1.1.0"}}))
        self.assertEquals(out.execute("/"), -1)

    def test_json_output_missing_source(self):
        testutil.put_stdin(json.dumps({"params": {
                                           "version": "1.1.0",
                                           "bucket": "failure",
                                           "directory": "1.1.0"}}))
        self.assertEquals(out.execute("/"), -1)


if __name__ == '__main__':
    unittest.main()