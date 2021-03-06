
import os
import tempfile
import unittest

from rssalertbot.config import Config, dict_from_dotted_key


class ConfigTest(unittest.TestCase):

    def test_dict_from_dotted_key(self):
        d = {
            'foo': {
                'bar': 32,
            }
        }
        test = dict_from_dotted_key('foo.bar', 32)
        self.assertSequenceEqual(d, test)


    def test_config(self):
        d = {
            'foo': {
                'bar': 32,
            }
        }

        c = Config(d)
        self.assertEqual(c.get('foo.bar'), d['foo']['bar'])
        self.assertEqual(c.foo.bar, d['foo']['bar'])


    def test_config_get_set(self):
        c = Config()
        c.set('foo.bar', 32)
        self.assertEqual(c.get('foo.bar'), 32)


    def test_config_merge_dict(self):
        d1 = {
            'foo': {
                'bar': 32,
            }
        }
        d2 = {
            'foo': {
                'baz': 96,
                'bar': 96,
            }
        }
        # start
        c = Config(d1)
        self.assertEqual(c.get('foo.bar'), 32)
        self.assertIsNone(c.get('foo.baz'))

        # merge
        c.merge_dict(d2)
        self.assertEqual(c.get('foo.bar'), 96)
        self.assertEqual(c.get('foo.baz'), 96)


    def test_config_load(self):
        """
        In which we write some test data to a temporary file, then
        read it with Config.load() and validate it.
        """

        yamldata = """
foo:
    bar: 32
"""
        filename = None
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as tf:
            filename = tf.name
            tf.write(yamldata)
        self.assertIsNotNone(filename)

        c = Config()
        c.load(filename)

        self.assertEqual(c.get('foo.bar'), 32)

        # cleanup
        os.unlink(filename)
