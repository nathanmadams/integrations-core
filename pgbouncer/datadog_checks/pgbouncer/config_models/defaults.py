# (C) Datadog, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

# This file is autogenerated.
# To change this file you should edit assets/configuration/spec.yaml and then run the following commands:
#     ddev -x validate config -s <INTEGRATION_NAME>
#     ddev -x validate models -s <INTEGRATION_NAME>

from datadog_checks.base.utils.models.fields import get_default_field_value


def shared_service(field, value):
    return get_default_field_value(field, value)


def instance_collect_per_client_metrics(field, value):
    return False


def instance_collect_per_server_metrics(field, value):
    return False


def instance_database_url(field, value):
    return 'postgresql://<USERNAME>:<PASSWORD>@<HOSTNAME>:<PORT>/<DATABASE_URL>?sslmode=require'


def instance_disable_generic_tags(field, value):
    return False


def instance_empty_default_hostname(field, value):
    return False


def instance_host(field, value):
    return get_default_field_value(field, value)


def instance_metric_patterns(field, value):
    return get_default_field_value(field, value)


def instance_min_collection_interval(field, value):
    return 15


def instance_password(field, value):
    return get_default_field_value(field, value)


def instance_port(field, value):
    return get_default_field_value(field, value)


def instance_service(field, value):
    return get_default_field_value(field, value)


def instance_tags(field, value):
    return get_default_field_value(field, value)


def instance_use_cached(field, value):
    return True


def instance_username(field, value):
    return get_default_field_value(field, value)
