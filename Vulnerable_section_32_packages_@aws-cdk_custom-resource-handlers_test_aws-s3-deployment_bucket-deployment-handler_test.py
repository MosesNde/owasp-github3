 import os
 import unittest
 import json
import sys
import traceback
 import logging
import botocore
 import tempfile
 from botocore.vendored import requests
 from botocore.exceptions import ClientError
from unittest.mock import MagicMock
from unittest.mock import patch
 
 # set TEST_AWSCLI_PATH to point to the "aws" stub we have here
 scriptdir=os.path.dirname(os.path.realpath(__file__))
 os.environ['TEST_AWSCLI_PATH'] = os.path.join(scriptdir, 'aws')
 
 class TestHandler(unittest.TestCase):
     def setUp(self):
        logger = logging.getLogger()
 
         # clean up old aws.out file (from previous runs)
         try: os.remove("aws.out")
         resp = invoke_handler("Create", {}, expected_status="FAILED")
         self.assertEqual(resp["Reason"], "missing request resource property 'SourceBucketNames'. props: {}")
 
     def test_create_update(self):
         invoke_handler("Create", {
             "SourceBucketNames": ["<source-bucket>"],