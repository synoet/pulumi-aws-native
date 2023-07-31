# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['EndpointArgs', 'Endpoint']

@pulumi.input_type
class EndpointArgs:
    def __init__(__self__, *,
                 endpoint_type: pulumi.Input[str],
                 engine_name: pulumi.Input[str],
                 certificate_arn: Optional[pulumi.Input[str]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 doc_db_settings: Optional[pulumi.Input['EndpointDocDbSettingsArgs']] = None,
                 dynamo_db_settings: Optional[pulumi.Input['EndpointDynamoDbSettingsArgs']] = None,
                 elasticsearch_settings: Optional[pulumi.Input['EndpointElasticsearchSettingsArgs']] = None,
                 endpoint_identifier: Optional[pulumi.Input[str]] = None,
                 extra_connection_attributes: Optional[pulumi.Input[str]] = None,
                 gcp_my_sql_settings: Optional[pulumi.Input['EndpointGcpMySQLSettingsArgs']] = None,
                 ibm_db2_settings: Optional[pulumi.Input['EndpointIbmDb2SettingsArgs']] = None,
                 kafka_settings: Optional[pulumi.Input['EndpointKafkaSettingsArgs']] = None,
                 kinesis_settings: Optional[pulumi.Input['EndpointKinesisSettingsArgs']] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 microsoft_sql_server_settings: Optional[pulumi.Input['EndpointMicrosoftSqlServerSettingsArgs']] = None,
                 mongo_db_settings: Optional[pulumi.Input['EndpointMongoDbSettingsArgs']] = None,
                 my_sql_settings: Optional[pulumi.Input['EndpointMySqlSettingsArgs']] = None,
                 neptune_settings: Optional[pulumi.Input['EndpointNeptuneSettingsArgs']] = None,
                 oracle_settings: Optional[pulumi.Input['EndpointOracleSettingsArgs']] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 postgre_sql_settings: Optional[pulumi.Input['EndpointPostgreSqlSettingsArgs']] = None,
                 redis_settings: Optional[pulumi.Input['EndpointRedisSettingsArgs']] = None,
                 redshift_settings: Optional[pulumi.Input['EndpointRedshiftSettingsArgs']] = None,
                 resource_identifier: Optional[pulumi.Input[str]] = None,
                 s3_settings: Optional[pulumi.Input['EndpointS3SettingsArgs']] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 ssl_mode: Optional[pulumi.Input[str]] = None,
                 sybase_settings: Optional[pulumi.Input['EndpointSybaseSettingsArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['EndpointTagArgs']]]] = None,
                 username: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Endpoint resource.
        """
        pulumi.set(__self__, "endpoint_type", endpoint_type)
        pulumi.set(__self__, "engine_name", engine_name)
        if certificate_arn is not None:
            pulumi.set(__self__, "certificate_arn", certificate_arn)
        if database_name is not None:
            pulumi.set(__self__, "database_name", database_name)
        if doc_db_settings is not None:
            pulumi.set(__self__, "doc_db_settings", doc_db_settings)
        if dynamo_db_settings is not None:
            pulumi.set(__self__, "dynamo_db_settings", dynamo_db_settings)
        if elasticsearch_settings is not None:
            pulumi.set(__self__, "elasticsearch_settings", elasticsearch_settings)
        if endpoint_identifier is not None:
            pulumi.set(__self__, "endpoint_identifier", endpoint_identifier)
        if extra_connection_attributes is not None:
            pulumi.set(__self__, "extra_connection_attributes", extra_connection_attributes)
        if gcp_my_sql_settings is not None:
            pulumi.set(__self__, "gcp_my_sql_settings", gcp_my_sql_settings)
        if ibm_db2_settings is not None:
            pulumi.set(__self__, "ibm_db2_settings", ibm_db2_settings)
        if kafka_settings is not None:
            pulumi.set(__self__, "kafka_settings", kafka_settings)
        if kinesis_settings is not None:
            pulumi.set(__self__, "kinesis_settings", kinesis_settings)
        if kms_key_id is not None:
            pulumi.set(__self__, "kms_key_id", kms_key_id)
        if microsoft_sql_server_settings is not None:
            pulumi.set(__self__, "microsoft_sql_server_settings", microsoft_sql_server_settings)
        if mongo_db_settings is not None:
            pulumi.set(__self__, "mongo_db_settings", mongo_db_settings)
        if my_sql_settings is not None:
            pulumi.set(__self__, "my_sql_settings", my_sql_settings)
        if neptune_settings is not None:
            pulumi.set(__self__, "neptune_settings", neptune_settings)
        if oracle_settings is not None:
            pulumi.set(__self__, "oracle_settings", oracle_settings)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if postgre_sql_settings is not None:
            pulumi.set(__self__, "postgre_sql_settings", postgre_sql_settings)
        if redis_settings is not None:
            pulumi.set(__self__, "redis_settings", redis_settings)
        if redshift_settings is not None:
            pulumi.set(__self__, "redshift_settings", redshift_settings)
        if resource_identifier is not None:
            pulumi.set(__self__, "resource_identifier", resource_identifier)
        if s3_settings is not None:
            pulumi.set(__self__, "s3_settings", s3_settings)
        if server_name is not None:
            pulumi.set(__self__, "server_name", server_name)
        if ssl_mode is not None:
            pulumi.set(__self__, "ssl_mode", ssl_mode)
        if sybase_settings is not None:
            pulumi.set(__self__, "sybase_settings", sybase_settings)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if username is not None:
            pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Input[str]:
        return pulumi.get(self, "endpoint_type")

    @endpoint_type.setter
    def endpoint_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "endpoint_type", value)

    @property
    @pulumi.getter(name="engineName")
    def engine_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "engine_name")

    @engine_name.setter
    def engine_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "engine_name", value)

    @property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "certificate_arn")

    @certificate_arn.setter
    def certificate_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate_arn", value)

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "database_name")

    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "database_name", value)

    @property
    @pulumi.getter(name="docDbSettings")
    def doc_db_settings(self) -> Optional[pulumi.Input['EndpointDocDbSettingsArgs']]:
        return pulumi.get(self, "doc_db_settings")

    @doc_db_settings.setter
    def doc_db_settings(self, value: Optional[pulumi.Input['EndpointDocDbSettingsArgs']]):
        pulumi.set(self, "doc_db_settings", value)

    @property
    @pulumi.getter(name="dynamoDbSettings")
    def dynamo_db_settings(self) -> Optional[pulumi.Input['EndpointDynamoDbSettingsArgs']]:
        return pulumi.get(self, "dynamo_db_settings")

    @dynamo_db_settings.setter
    def dynamo_db_settings(self, value: Optional[pulumi.Input['EndpointDynamoDbSettingsArgs']]):
        pulumi.set(self, "dynamo_db_settings", value)

    @property
    @pulumi.getter(name="elasticsearchSettings")
    def elasticsearch_settings(self) -> Optional[pulumi.Input['EndpointElasticsearchSettingsArgs']]:
        return pulumi.get(self, "elasticsearch_settings")

    @elasticsearch_settings.setter
    def elasticsearch_settings(self, value: Optional[pulumi.Input['EndpointElasticsearchSettingsArgs']]):
        pulumi.set(self, "elasticsearch_settings", value)

    @property
    @pulumi.getter(name="endpointIdentifier")
    def endpoint_identifier(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "endpoint_identifier")

    @endpoint_identifier.setter
    def endpoint_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint_identifier", value)

    @property
    @pulumi.getter(name="extraConnectionAttributes")
    def extra_connection_attributes(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "extra_connection_attributes")

    @extra_connection_attributes.setter
    def extra_connection_attributes(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "extra_connection_attributes", value)

    @property
    @pulumi.getter(name="gcpMySqlSettings")
    def gcp_my_sql_settings(self) -> Optional[pulumi.Input['EndpointGcpMySQLSettingsArgs']]:
        return pulumi.get(self, "gcp_my_sql_settings")

    @gcp_my_sql_settings.setter
    def gcp_my_sql_settings(self, value: Optional[pulumi.Input['EndpointGcpMySQLSettingsArgs']]):
        pulumi.set(self, "gcp_my_sql_settings", value)

    @property
    @pulumi.getter(name="ibmDb2Settings")
    def ibm_db2_settings(self) -> Optional[pulumi.Input['EndpointIbmDb2SettingsArgs']]:
        return pulumi.get(self, "ibm_db2_settings")

    @ibm_db2_settings.setter
    def ibm_db2_settings(self, value: Optional[pulumi.Input['EndpointIbmDb2SettingsArgs']]):
        pulumi.set(self, "ibm_db2_settings", value)

    @property
    @pulumi.getter(name="kafkaSettings")
    def kafka_settings(self) -> Optional[pulumi.Input['EndpointKafkaSettingsArgs']]:
        return pulumi.get(self, "kafka_settings")

    @kafka_settings.setter
    def kafka_settings(self, value: Optional[pulumi.Input['EndpointKafkaSettingsArgs']]):
        pulumi.set(self, "kafka_settings", value)

    @property
    @pulumi.getter(name="kinesisSettings")
    def kinesis_settings(self) -> Optional[pulumi.Input['EndpointKinesisSettingsArgs']]:
        return pulumi.get(self, "kinesis_settings")

    @kinesis_settings.setter
    def kinesis_settings(self, value: Optional[pulumi.Input['EndpointKinesisSettingsArgs']]):
        pulumi.set(self, "kinesis_settings", value)

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "kms_key_id")

    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_id", value)

    @property
    @pulumi.getter(name="microsoftSqlServerSettings")
    def microsoft_sql_server_settings(self) -> Optional[pulumi.Input['EndpointMicrosoftSqlServerSettingsArgs']]:
        return pulumi.get(self, "microsoft_sql_server_settings")

    @microsoft_sql_server_settings.setter
    def microsoft_sql_server_settings(self, value: Optional[pulumi.Input['EndpointMicrosoftSqlServerSettingsArgs']]):
        pulumi.set(self, "microsoft_sql_server_settings", value)

    @property
    @pulumi.getter(name="mongoDbSettings")
    def mongo_db_settings(self) -> Optional[pulumi.Input['EndpointMongoDbSettingsArgs']]:
        return pulumi.get(self, "mongo_db_settings")

    @mongo_db_settings.setter
    def mongo_db_settings(self, value: Optional[pulumi.Input['EndpointMongoDbSettingsArgs']]):
        pulumi.set(self, "mongo_db_settings", value)

    @property
    @pulumi.getter(name="mySqlSettings")
    def my_sql_settings(self) -> Optional[pulumi.Input['EndpointMySqlSettingsArgs']]:
        return pulumi.get(self, "my_sql_settings")

    @my_sql_settings.setter
    def my_sql_settings(self, value: Optional[pulumi.Input['EndpointMySqlSettingsArgs']]):
        pulumi.set(self, "my_sql_settings", value)

    @property
    @pulumi.getter(name="neptuneSettings")
    def neptune_settings(self) -> Optional[pulumi.Input['EndpointNeptuneSettingsArgs']]:
        return pulumi.get(self, "neptune_settings")

    @neptune_settings.setter
    def neptune_settings(self, value: Optional[pulumi.Input['EndpointNeptuneSettingsArgs']]):
        pulumi.set(self, "neptune_settings", value)

    @property
    @pulumi.getter(name="oracleSettings")
    def oracle_settings(self) -> Optional[pulumi.Input['EndpointOracleSettingsArgs']]:
        return pulumi.get(self, "oracle_settings")

    @oracle_settings.setter
    def oracle_settings(self, value: Optional[pulumi.Input['EndpointOracleSettingsArgs']]):
        pulumi.set(self, "oracle_settings", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter(name="postgreSqlSettings")
    def postgre_sql_settings(self) -> Optional[pulumi.Input['EndpointPostgreSqlSettingsArgs']]:
        return pulumi.get(self, "postgre_sql_settings")

    @postgre_sql_settings.setter
    def postgre_sql_settings(self, value: Optional[pulumi.Input['EndpointPostgreSqlSettingsArgs']]):
        pulumi.set(self, "postgre_sql_settings", value)

    @property
    @pulumi.getter(name="redisSettings")
    def redis_settings(self) -> Optional[pulumi.Input['EndpointRedisSettingsArgs']]:
        return pulumi.get(self, "redis_settings")

    @redis_settings.setter
    def redis_settings(self, value: Optional[pulumi.Input['EndpointRedisSettingsArgs']]):
        pulumi.set(self, "redis_settings", value)

    @property
    @pulumi.getter(name="redshiftSettings")
    def redshift_settings(self) -> Optional[pulumi.Input['EndpointRedshiftSettingsArgs']]:
        return pulumi.get(self, "redshift_settings")

    @redshift_settings.setter
    def redshift_settings(self, value: Optional[pulumi.Input['EndpointRedshiftSettingsArgs']]):
        pulumi.set(self, "redshift_settings", value)

    @property
    @pulumi.getter(name="resourceIdentifier")
    def resource_identifier(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "resource_identifier")

    @resource_identifier.setter
    def resource_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_identifier", value)

    @property
    @pulumi.getter(name="s3Settings")
    def s3_settings(self) -> Optional[pulumi.Input['EndpointS3SettingsArgs']]:
        return pulumi.get(self, "s3_settings")

    @s3_settings.setter
    def s3_settings(self, value: Optional[pulumi.Input['EndpointS3SettingsArgs']]):
        pulumi.set(self, "s3_settings", value)

    @property
    @pulumi.getter(name="serverName")
    def server_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "server_name")

    @server_name.setter
    def server_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server_name", value)

    @property
    @pulumi.getter(name="sslMode")
    def ssl_mode(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "ssl_mode")

    @ssl_mode.setter
    def ssl_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ssl_mode", value)

    @property
    @pulumi.getter(name="sybaseSettings")
    def sybase_settings(self) -> Optional[pulumi.Input['EndpointSybaseSettingsArgs']]:
        return pulumi.get(self, "sybase_settings")

    @sybase_settings.setter
    def sybase_settings(self, value: Optional[pulumi.Input['EndpointSybaseSettingsArgs']]):
        pulumi.set(self, "sybase_settings", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['EndpointTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['EndpointTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "username", value)


warnings.warn("""Endpoint is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class Endpoint(pulumi.CustomResource):
    warnings.warn("""Endpoint is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate_arn: Optional[pulumi.Input[str]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 doc_db_settings: Optional[pulumi.Input[pulumi.InputType['EndpointDocDbSettingsArgs']]] = None,
                 dynamo_db_settings: Optional[pulumi.Input[pulumi.InputType['EndpointDynamoDbSettingsArgs']]] = None,
                 elasticsearch_settings: Optional[pulumi.Input[pulumi.InputType['EndpointElasticsearchSettingsArgs']]] = None,
                 endpoint_identifier: Optional[pulumi.Input[str]] = None,
                 endpoint_type: Optional[pulumi.Input[str]] = None,
                 engine_name: Optional[pulumi.Input[str]] = None,
                 extra_connection_attributes: Optional[pulumi.Input[str]] = None,
                 gcp_my_sql_settings: Optional[pulumi.Input[pulumi.InputType['EndpointGcpMySQLSettingsArgs']]] = None,
                 ibm_db2_settings: Optional[pulumi.Input[pulumi.InputType['EndpointIbmDb2SettingsArgs']]] = None,
                 kafka_settings: Optional[pulumi.Input[pulumi.InputType['EndpointKafkaSettingsArgs']]] = None,
                 kinesis_settings: Optional[pulumi.Input[pulumi.InputType['EndpointKinesisSettingsArgs']]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 microsoft_sql_server_settings: Optional[pulumi.Input[pulumi.InputType['EndpointMicrosoftSqlServerSettingsArgs']]] = None,
                 mongo_db_settings: Optional[pulumi.Input[pulumi.InputType['EndpointMongoDbSettingsArgs']]] = None,
                 my_sql_settings: Optional[pulumi.Input[pulumi.InputType['EndpointMySqlSettingsArgs']]] = None,
                 neptune_settings: Optional[pulumi.Input[pulumi.InputType['EndpointNeptuneSettingsArgs']]] = None,
                 oracle_settings: Optional[pulumi.Input[pulumi.InputType['EndpointOracleSettingsArgs']]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 postgre_sql_settings: Optional[pulumi.Input[pulumi.InputType['EndpointPostgreSqlSettingsArgs']]] = None,
                 redis_settings: Optional[pulumi.Input[pulumi.InputType['EndpointRedisSettingsArgs']]] = None,
                 redshift_settings: Optional[pulumi.Input[pulumi.InputType['EndpointRedshiftSettingsArgs']]] = None,
                 resource_identifier: Optional[pulumi.Input[str]] = None,
                 s3_settings: Optional[pulumi.Input[pulumi.InputType['EndpointS3SettingsArgs']]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 ssl_mode: Optional[pulumi.Input[str]] = None,
                 sybase_settings: Optional[pulumi.Input[pulumi.InputType['EndpointSybaseSettingsArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EndpointTagArgs']]]]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::DMS::Endpoint

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EndpointArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::DMS::Endpoint

        :param str resource_name: The name of the resource.
        :param EndpointArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EndpointArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate_arn: Optional[pulumi.Input[str]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 doc_db_settings: Optional[pulumi.Input[pulumi.InputType['EndpointDocDbSettingsArgs']]] = None,
                 dynamo_db_settings: Optional[pulumi.Input[pulumi.InputType['EndpointDynamoDbSettingsArgs']]] = None,
                 elasticsearch_settings: Optional[pulumi.Input[pulumi.InputType['EndpointElasticsearchSettingsArgs']]] = None,
                 endpoint_identifier: Optional[pulumi.Input[str]] = None,
                 endpoint_type: Optional[pulumi.Input[str]] = None,
                 engine_name: Optional[pulumi.Input[str]] = None,
                 extra_connection_attributes: Optional[pulumi.Input[str]] = None,
                 gcp_my_sql_settings: Optional[pulumi.Input[pulumi.InputType['EndpointGcpMySQLSettingsArgs']]] = None,
                 ibm_db2_settings: Optional[pulumi.Input[pulumi.InputType['EndpointIbmDb2SettingsArgs']]] = None,
                 kafka_settings: Optional[pulumi.Input[pulumi.InputType['EndpointKafkaSettingsArgs']]] = None,
                 kinesis_settings: Optional[pulumi.Input[pulumi.InputType['EndpointKinesisSettingsArgs']]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 microsoft_sql_server_settings: Optional[pulumi.Input[pulumi.InputType['EndpointMicrosoftSqlServerSettingsArgs']]] = None,
                 mongo_db_settings: Optional[pulumi.Input[pulumi.InputType['EndpointMongoDbSettingsArgs']]] = None,
                 my_sql_settings: Optional[pulumi.Input[pulumi.InputType['EndpointMySqlSettingsArgs']]] = None,
                 neptune_settings: Optional[pulumi.Input[pulumi.InputType['EndpointNeptuneSettingsArgs']]] = None,
                 oracle_settings: Optional[pulumi.Input[pulumi.InputType['EndpointOracleSettingsArgs']]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 postgre_sql_settings: Optional[pulumi.Input[pulumi.InputType['EndpointPostgreSqlSettingsArgs']]] = None,
                 redis_settings: Optional[pulumi.Input[pulumi.InputType['EndpointRedisSettingsArgs']]] = None,
                 redshift_settings: Optional[pulumi.Input[pulumi.InputType['EndpointRedshiftSettingsArgs']]] = None,
                 resource_identifier: Optional[pulumi.Input[str]] = None,
                 s3_settings: Optional[pulumi.Input[pulumi.InputType['EndpointS3SettingsArgs']]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 ssl_mode: Optional[pulumi.Input[str]] = None,
                 sybase_settings: Optional[pulumi.Input[pulumi.InputType['EndpointSybaseSettingsArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EndpointTagArgs']]]]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""Endpoint is deprecated: Endpoint is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EndpointArgs.__new__(EndpointArgs)

            __props__.__dict__["certificate_arn"] = certificate_arn
            __props__.__dict__["database_name"] = database_name
            __props__.__dict__["doc_db_settings"] = doc_db_settings
            __props__.__dict__["dynamo_db_settings"] = dynamo_db_settings
            __props__.__dict__["elasticsearch_settings"] = elasticsearch_settings
            __props__.__dict__["endpoint_identifier"] = endpoint_identifier
            if endpoint_type is None and not opts.urn:
                raise TypeError("Missing required property 'endpoint_type'")
            __props__.__dict__["endpoint_type"] = endpoint_type
            if engine_name is None and not opts.urn:
                raise TypeError("Missing required property 'engine_name'")
            __props__.__dict__["engine_name"] = engine_name
            __props__.__dict__["extra_connection_attributes"] = extra_connection_attributes
            __props__.__dict__["gcp_my_sql_settings"] = gcp_my_sql_settings
            __props__.__dict__["ibm_db2_settings"] = ibm_db2_settings
            __props__.__dict__["kafka_settings"] = kafka_settings
            __props__.__dict__["kinesis_settings"] = kinesis_settings
            __props__.__dict__["kms_key_id"] = kms_key_id
            __props__.__dict__["microsoft_sql_server_settings"] = microsoft_sql_server_settings
            __props__.__dict__["mongo_db_settings"] = mongo_db_settings
            __props__.__dict__["my_sql_settings"] = my_sql_settings
            __props__.__dict__["neptune_settings"] = neptune_settings
            __props__.__dict__["oracle_settings"] = oracle_settings
            __props__.__dict__["password"] = password
            __props__.__dict__["port"] = port
            __props__.__dict__["postgre_sql_settings"] = postgre_sql_settings
            __props__.__dict__["redis_settings"] = redis_settings
            __props__.__dict__["redshift_settings"] = redshift_settings
            __props__.__dict__["resource_identifier"] = resource_identifier
            __props__.__dict__["s3_settings"] = s3_settings
            __props__.__dict__["server_name"] = server_name
            __props__.__dict__["ssl_mode"] = ssl_mode
            __props__.__dict__["sybase_settings"] = sybase_settings
            __props__.__dict__["tags"] = tags
            __props__.__dict__["username"] = username
            __props__.__dict__["external_id"] = None
        super(Endpoint, __self__).__init__(
            'aws-native:dms:Endpoint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Endpoint':
        """
        Get an existing Endpoint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EndpointArgs.__new__(EndpointArgs)

        __props__.__dict__["certificate_arn"] = None
        __props__.__dict__["database_name"] = None
        __props__.__dict__["doc_db_settings"] = None
        __props__.__dict__["dynamo_db_settings"] = None
        __props__.__dict__["elasticsearch_settings"] = None
        __props__.__dict__["endpoint_identifier"] = None
        __props__.__dict__["endpoint_type"] = None
        __props__.__dict__["engine_name"] = None
        __props__.__dict__["external_id"] = None
        __props__.__dict__["extra_connection_attributes"] = None
        __props__.__dict__["gcp_my_sql_settings"] = None
        __props__.__dict__["ibm_db2_settings"] = None
        __props__.__dict__["kafka_settings"] = None
        __props__.__dict__["kinesis_settings"] = None
        __props__.__dict__["kms_key_id"] = None
        __props__.__dict__["microsoft_sql_server_settings"] = None
        __props__.__dict__["mongo_db_settings"] = None
        __props__.__dict__["my_sql_settings"] = None
        __props__.__dict__["neptune_settings"] = None
        __props__.__dict__["oracle_settings"] = None
        __props__.__dict__["password"] = None
        __props__.__dict__["port"] = None
        __props__.__dict__["postgre_sql_settings"] = None
        __props__.__dict__["redis_settings"] = None
        __props__.__dict__["redshift_settings"] = None
        __props__.__dict__["resource_identifier"] = None
        __props__.__dict__["s3_settings"] = None
        __props__.__dict__["server_name"] = None
        __props__.__dict__["ssl_mode"] = None
        __props__.__dict__["sybase_settings"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["username"] = None
        return Endpoint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "certificate_arn")

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "database_name")

    @property
    @pulumi.getter(name="docDbSettings")
    def doc_db_settings(self) -> pulumi.Output[Optional['outputs.EndpointDocDbSettings']]:
        return pulumi.get(self, "doc_db_settings")

    @property
    @pulumi.getter(name="dynamoDbSettings")
    def dynamo_db_settings(self) -> pulumi.Output[Optional['outputs.EndpointDynamoDbSettings']]:
        return pulumi.get(self, "dynamo_db_settings")

    @property
    @pulumi.getter(name="elasticsearchSettings")
    def elasticsearch_settings(self) -> pulumi.Output[Optional['outputs.EndpointElasticsearchSettings']]:
        return pulumi.get(self, "elasticsearch_settings")

    @property
    @pulumi.getter(name="endpointIdentifier")
    def endpoint_identifier(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "endpoint_identifier")

    @property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Output[str]:
        return pulumi.get(self, "endpoint_type")

    @property
    @pulumi.getter(name="engineName")
    def engine_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "engine_name")

    @property
    @pulumi.getter(name="externalId")
    def external_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "external_id")

    @property
    @pulumi.getter(name="extraConnectionAttributes")
    def extra_connection_attributes(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "extra_connection_attributes")

    @property
    @pulumi.getter(name="gcpMySqlSettings")
    def gcp_my_sql_settings(self) -> pulumi.Output[Optional['outputs.EndpointGcpMySQLSettings']]:
        return pulumi.get(self, "gcp_my_sql_settings")

    @property
    @pulumi.getter(name="ibmDb2Settings")
    def ibm_db2_settings(self) -> pulumi.Output[Optional['outputs.EndpointIbmDb2Settings']]:
        return pulumi.get(self, "ibm_db2_settings")

    @property
    @pulumi.getter(name="kafkaSettings")
    def kafka_settings(self) -> pulumi.Output[Optional['outputs.EndpointKafkaSettings']]:
        return pulumi.get(self, "kafka_settings")

    @property
    @pulumi.getter(name="kinesisSettings")
    def kinesis_settings(self) -> pulumi.Output[Optional['outputs.EndpointKinesisSettings']]:
        return pulumi.get(self, "kinesis_settings")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter(name="microsoftSqlServerSettings")
    def microsoft_sql_server_settings(self) -> pulumi.Output[Optional['outputs.EndpointMicrosoftSqlServerSettings']]:
        return pulumi.get(self, "microsoft_sql_server_settings")

    @property
    @pulumi.getter(name="mongoDbSettings")
    def mongo_db_settings(self) -> pulumi.Output[Optional['outputs.EndpointMongoDbSettings']]:
        return pulumi.get(self, "mongo_db_settings")

    @property
    @pulumi.getter(name="mySqlSettings")
    def my_sql_settings(self) -> pulumi.Output[Optional['outputs.EndpointMySqlSettings']]:
        return pulumi.get(self, "my_sql_settings")

    @property
    @pulumi.getter(name="neptuneSettings")
    def neptune_settings(self) -> pulumi.Output[Optional['outputs.EndpointNeptuneSettings']]:
        return pulumi.get(self, "neptune_settings")

    @property
    @pulumi.getter(name="oracleSettings")
    def oracle_settings(self) -> pulumi.Output[Optional['outputs.EndpointOracleSettings']]:
        return pulumi.get(self, "oracle_settings")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def port(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="postgreSqlSettings")
    def postgre_sql_settings(self) -> pulumi.Output[Optional['outputs.EndpointPostgreSqlSettings']]:
        return pulumi.get(self, "postgre_sql_settings")

    @property
    @pulumi.getter(name="redisSettings")
    def redis_settings(self) -> pulumi.Output[Optional['outputs.EndpointRedisSettings']]:
        return pulumi.get(self, "redis_settings")

    @property
    @pulumi.getter(name="redshiftSettings")
    def redshift_settings(self) -> pulumi.Output[Optional['outputs.EndpointRedshiftSettings']]:
        return pulumi.get(self, "redshift_settings")

    @property
    @pulumi.getter(name="resourceIdentifier")
    def resource_identifier(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "resource_identifier")

    @property
    @pulumi.getter(name="s3Settings")
    def s3_settings(self) -> pulumi.Output[Optional['outputs.EndpointS3Settings']]:
        return pulumi.get(self, "s3_settings")

    @property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "server_name")

    @property
    @pulumi.getter(name="sslMode")
    def ssl_mode(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "ssl_mode")

    @property
    @pulumi.getter(name="sybaseSettings")
    def sybase_settings(self) -> pulumi.Output[Optional['outputs.EndpointSybaseSettings']]:
        return pulumi.get(self, "sybase_settings")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.EndpointTag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def username(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "username")

