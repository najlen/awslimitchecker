"""
awslimitchecker/limit.py

The latest version of this package is available at:
<https://github.com/jantman/awslimitchecker>

################################################################################
Copyright 2015 Jason Antman <jason@jasonantman.com> <http://www.jasonantman.com>

    This file is part of awslimitchecker, also known as awslimitchecker.

    awslimitchecker is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    awslimitchecker is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with awslimitchecker.  If not, see <http://www.gnu.org/licenses/>.

The Copyright and Authors attributions contained herein may not be removed or
otherwise altered, except to add the Author attribution of a contributor to
this work. (Additional Terms pursuant to Section 7b of the AGPL v3)
################################################################################
While not legally required, I sincerely request that anyone who finds
bugs please submit them at <https://github.com/jantman/pydnstest> or
to me via email, and that you send any contributions or improvements
either as a pull request on GitHub, or to me via email.
################################################################################

AUTHORS:
Jason Antman <jason@jasonantman.com> <http://www.jasonantman.com>
################################################################################
"""


class AwsLimit(object):

    def __init__(self, name, service_name, default_limit,
                 limit_type=None, limit_subtype=None):
        """
        Describes one specific AWS service limit, as well as its
        current utilization, default limit, thresholds, and any
        Trusted Advisor information about this limit.

        :param name: the name of this limit (may contain spaces);
        if possible, this should be the name used by AWS, i.e. TrustedAdvisor
        :type name: string
        :param service_name: the name of the service this limit is for;
        this should be the ``service_name`` attribute of an
        :py:class:`~.AwsService` class.
        :type service_name: string
        :param default_limit: the default value of this limit for new accounts
        :type default_limit: int
        :param limit_type: the type of resource this limit describes, such as
        "On-Demand Instance" or "VPC"
        :param limit_subtype: resource sub-type for this limit, if applicable,
        such as "t2.micro" or "SecurityGroup"
        """
        self.name = name
        self.service_name = service_name
        self.default_limit = default_limit
        self.limit_type = limit_type
        self.limit_subtype = limit_subtype