#!/usr/bin/env python
# Copyright 2012-2013 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
from tests.unit import BaseAWSCommandParamsTest
import os


TWO_INSTANCE_EXPECTED = {
    'LoadBalancerName': 'my-lb',
    'Instances.member.1.InstanceId': 'i-12345678',
    'Instances.member.2.InstanceId': 'i-87654321'
}


class TestRegisterInstancesWithLoadBalancer(BaseAWSCommandParamsTest):

    prefix = 'elb register-instances-with-load-balancer'

    def test_one_instance(self):
        cmdline = self.prefix
        cmdline += ' --load-balancer-name my-lb'
        cmdline += ' --instances {"InstanceId":"i-12345678"}'
        result = {'LoadBalancerName': 'my-lb',
                  'Instances.member.1.InstanceId': 'i-12345678'}
        self.assert_params_for_cmd(cmdline, result)

    def test_shorthand(self):
        cmdline = self.prefix
        cmdline += ' --load-balancer-name my-lb'
        cmdline += ' --instances i-12345678'
        result = {'LoadBalancerName': 'my-lb',
                  'Instances.member.1.InstanceId': 'i-12345678'}
        self.assert_params_for_cmd(cmdline, result)

    def test_two_instance(self):
        cmdline = self.prefix
        cmdline += ' --load-balancer-name my-lb'
        cmdline += ' --instances {"InstanceId":"i-12345678"}'
        cmdline += ' {"InstanceId":"i-87654321"}'
        self.assert_params_for_cmd(cmdline, TWO_INSTANCE_EXPECTED)

    def test_two_instance_as_json(self):
        cmdline = self.prefix
        cmdline += ' --load-balancer-name my-lb'
        cmdline += ' --instances [{"InstanceId":"i-12345678"},'
        cmdline += '{"InstanceId":"i-87654321"}]'
        self.assert_params_for_cmd(cmdline, TWO_INSTANCE_EXPECTED)

    def test_two_instance_from_file(self):
        data_path = os.path.join(os.path.dirname(__file__),
                                 'test.json')
        cmdline = self.prefix
        cmdline += ' --load-balancer-name my-lb'
        cmdline += ' --instances file://%s' % data_path
        self.assert_params_for_cmd(cmdline, TWO_INSTANCE_EXPECTED)

    def test_two_instance_shorthand(self):
        cmdline = self.prefix
        cmdline += ' --load-balancer-name my-lb'
        cmdline += ' --instances i-12345678 i-87654321'
        self.assert_params_for_cmd(cmdline, TWO_INSTANCE_EXPECTED)


if __name__ == "__main__":
    unittest.main()
