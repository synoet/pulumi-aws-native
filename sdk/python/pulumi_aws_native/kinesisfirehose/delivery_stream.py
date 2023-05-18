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
from ._enums import *
from ._inputs import *

__all__ = ['DeliveryStreamArgs', 'DeliveryStream']

@pulumi.input_type
class DeliveryStreamArgs:
    def __init__(__self__, *,
                 amazon_open_search_serverless_destination_configuration: Optional[pulumi.Input['DeliveryStreamAmazonOpenSearchServerlessDestinationConfigurationArgs']] = None,
                 amazonopensearchservice_destination_configuration: Optional[pulumi.Input['DeliveryStreamAmazonopensearchserviceDestinationConfigurationArgs']] = None,
                 delivery_stream_encryption_configuration_input: Optional[pulumi.Input['DeliveryStreamEncryptionConfigurationInputArgs']] = None,
                 delivery_stream_name: Optional[pulumi.Input[str]] = None,
                 delivery_stream_type: Optional[pulumi.Input['DeliveryStreamType']] = None,
                 elasticsearch_destination_configuration: Optional[pulumi.Input['DeliveryStreamElasticsearchDestinationConfigurationArgs']] = None,
                 extended_s3_destination_configuration: Optional[pulumi.Input['DeliveryStreamExtendedS3DestinationConfigurationArgs']] = None,
                 http_endpoint_destination_configuration: Optional[pulumi.Input['DeliveryStreamHttpEndpointDestinationConfigurationArgs']] = None,
                 kinesis_stream_source_configuration: Optional[pulumi.Input['DeliveryStreamKinesisStreamSourceConfigurationArgs']] = None,
                 redshift_destination_configuration: Optional[pulumi.Input['DeliveryStreamRedshiftDestinationConfigurationArgs']] = None,
                 s3_destination_configuration: Optional[pulumi.Input['DeliveryStreamS3DestinationConfigurationArgs']] = None,
                 splunk_destination_configuration: Optional[pulumi.Input['DeliveryStreamSplunkDestinationConfigurationArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['DeliveryStreamTagArgs']]]] = None):
        """
        The set of arguments for constructing a DeliveryStream resource.
        """
        if amazon_open_search_serverless_destination_configuration is not None:
            pulumi.set(__self__, "amazon_open_search_serverless_destination_configuration", amazon_open_search_serverless_destination_configuration)
        if amazonopensearchservice_destination_configuration is not None:
            pulumi.set(__self__, "amazonopensearchservice_destination_configuration", amazonopensearchservice_destination_configuration)
        if delivery_stream_encryption_configuration_input is not None:
            pulumi.set(__self__, "delivery_stream_encryption_configuration_input", delivery_stream_encryption_configuration_input)
        if delivery_stream_name is not None:
            pulumi.set(__self__, "delivery_stream_name", delivery_stream_name)
        if delivery_stream_type is not None:
            pulumi.set(__self__, "delivery_stream_type", delivery_stream_type)
        if elasticsearch_destination_configuration is not None:
            pulumi.set(__self__, "elasticsearch_destination_configuration", elasticsearch_destination_configuration)
        if extended_s3_destination_configuration is not None:
            pulumi.set(__self__, "extended_s3_destination_configuration", extended_s3_destination_configuration)
        if http_endpoint_destination_configuration is not None:
            pulumi.set(__self__, "http_endpoint_destination_configuration", http_endpoint_destination_configuration)
        if kinesis_stream_source_configuration is not None:
            pulumi.set(__self__, "kinesis_stream_source_configuration", kinesis_stream_source_configuration)
        if redshift_destination_configuration is not None:
            pulumi.set(__self__, "redshift_destination_configuration", redshift_destination_configuration)
        if s3_destination_configuration is not None:
            pulumi.set(__self__, "s3_destination_configuration", s3_destination_configuration)
        if splunk_destination_configuration is not None:
            pulumi.set(__self__, "splunk_destination_configuration", splunk_destination_configuration)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="amazonOpenSearchServerlessDestinationConfiguration")
    def amazon_open_search_serverless_destination_configuration(self) -> Optional[pulumi.Input['DeliveryStreamAmazonOpenSearchServerlessDestinationConfigurationArgs']]:
        return pulumi.get(self, "amazon_open_search_serverless_destination_configuration")

    @amazon_open_search_serverless_destination_configuration.setter
    def amazon_open_search_serverless_destination_configuration(self, value: Optional[pulumi.Input['DeliveryStreamAmazonOpenSearchServerlessDestinationConfigurationArgs']]):
        pulumi.set(self, "amazon_open_search_serverless_destination_configuration", value)

    @property
    @pulumi.getter(name="amazonopensearchserviceDestinationConfiguration")
    def amazonopensearchservice_destination_configuration(self) -> Optional[pulumi.Input['DeliveryStreamAmazonopensearchserviceDestinationConfigurationArgs']]:
        return pulumi.get(self, "amazonopensearchservice_destination_configuration")

    @amazonopensearchservice_destination_configuration.setter
    def amazonopensearchservice_destination_configuration(self, value: Optional[pulumi.Input['DeliveryStreamAmazonopensearchserviceDestinationConfigurationArgs']]):
        pulumi.set(self, "amazonopensearchservice_destination_configuration", value)

    @property
    @pulumi.getter(name="deliveryStreamEncryptionConfigurationInput")
    def delivery_stream_encryption_configuration_input(self) -> Optional[pulumi.Input['DeliveryStreamEncryptionConfigurationInputArgs']]:
        return pulumi.get(self, "delivery_stream_encryption_configuration_input")

    @delivery_stream_encryption_configuration_input.setter
    def delivery_stream_encryption_configuration_input(self, value: Optional[pulumi.Input['DeliveryStreamEncryptionConfigurationInputArgs']]):
        pulumi.set(self, "delivery_stream_encryption_configuration_input", value)

    @property
    @pulumi.getter(name="deliveryStreamName")
    def delivery_stream_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "delivery_stream_name")

    @delivery_stream_name.setter
    def delivery_stream_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "delivery_stream_name", value)

    @property
    @pulumi.getter(name="deliveryStreamType")
    def delivery_stream_type(self) -> Optional[pulumi.Input['DeliveryStreamType']]:
        return pulumi.get(self, "delivery_stream_type")

    @delivery_stream_type.setter
    def delivery_stream_type(self, value: Optional[pulumi.Input['DeliveryStreamType']]):
        pulumi.set(self, "delivery_stream_type", value)

    @property
    @pulumi.getter(name="elasticsearchDestinationConfiguration")
    def elasticsearch_destination_configuration(self) -> Optional[pulumi.Input['DeliveryStreamElasticsearchDestinationConfigurationArgs']]:
        return pulumi.get(self, "elasticsearch_destination_configuration")

    @elasticsearch_destination_configuration.setter
    def elasticsearch_destination_configuration(self, value: Optional[pulumi.Input['DeliveryStreamElasticsearchDestinationConfigurationArgs']]):
        pulumi.set(self, "elasticsearch_destination_configuration", value)

    @property
    @pulumi.getter(name="extendedS3DestinationConfiguration")
    def extended_s3_destination_configuration(self) -> Optional[pulumi.Input['DeliveryStreamExtendedS3DestinationConfigurationArgs']]:
        return pulumi.get(self, "extended_s3_destination_configuration")

    @extended_s3_destination_configuration.setter
    def extended_s3_destination_configuration(self, value: Optional[pulumi.Input['DeliveryStreamExtendedS3DestinationConfigurationArgs']]):
        pulumi.set(self, "extended_s3_destination_configuration", value)

    @property
    @pulumi.getter(name="httpEndpointDestinationConfiguration")
    def http_endpoint_destination_configuration(self) -> Optional[pulumi.Input['DeliveryStreamHttpEndpointDestinationConfigurationArgs']]:
        return pulumi.get(self, "http_endpoint_destination_configuration")

    @http_endpoint_destination_configuration.setter
    def http_endpoint_destination_configuration(self, value: Optional[pulumi.Input['DeliveryStreamHttpEndpointDestinationConfigurationArgs']]):
        pulumi.set(self, "http_endpoint_destination_configuration", value)

    @property
    @pulumi.getter(name="kinesisStreamSourceConfiguration")
    def kinesis_stream_source_configuration(self) -> Optional[pulumi.Input['DeliveryStreamKinesisStreamSourceConfigurationArgs']]:
        return pulumi.get(self, "kinesis_stream_source_configuration")

    @kinesis_stream_source_configuration.setter
    def kinesis_stream_source_configuration(self, value: Optional[pulumi.Input['DeliveryStreamKinesisStreamSourceConfigurationArgs']]):
        pulumi.set(self, "kinesis_stream_source_configuration", value)

    @property
    @pulumi.getter(name="redshiftDestinationConfiguration")
    def redshift_destination_configuration(self) -> Optional[pulumi.Input['DeliveryStreamRedshiftDestinationConfigurationArgs']]:
        return pulumi.get(self, "redshift_destination_configuration")

    @redshift_destination_configuration.setter
    def redshift_destination_configuration(self, value: Optional[pulumi.Input['DeliveryStreamRedshiftDestinationConfigurationArgs']]):
        pulumi.set(self, "redshift_destination_configuration", value)

    @property
    @pulumi.getter(name="s3DestinationConfiguration")
    def s3_destination_configuration(self) -> Optional[pulumi.Input['DeliveryStreamS3DestinationConfigurationArgs']]:
        return pulumi.get(self, "s3_destination_configuration")

    @s3_destination_configuration.setter
    def s3_destination_configuration(self, value: Optional[pulumi.Input['DeliveryStreamS3DestinationConfigurationArgs']]):
        pulumi.set(self, "s3_destination_configuration", value)

    @property
    @pulumi.getter(name="splunkDestinationConfiguration")
    def splunk_destination_configuration(self) -> Optional[pulumi.Input['DeliveryStreamSplunkDestinationConfigurationArgs']]:
        return pulumi.get(self, "splunk_destination_configuration")

    @splunk_destination_configuration.setter
    def splunk_destination_configuration(self, value: Optional[pulumi.Input['DeliveryStreamSplunkDestinationConfigurationArgs']]):
        pulumi.set(self, "splunk_destination_configuration", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DeliveryStreamTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DeliveryStreamTagArgs']]]]):
        pulumi.set(self, "tags", value)


class DeliveryStream(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 amazon_open_search_serverless_destination_configuration: Optional[pulumi.Input[pulumi.InputType['DeliveryStreamAmazonOpenSearchServerlessDestinationConfigurationArgs']]] = None,
                 amazonopensearchservice_destination_configuration: Optional[pulumi.Input[pulumi.InputType['DeliveryStreamAmazonopensearchserviceDestinationConfigurationArgs']]] = None,
                 delivery_stream_encryption_configuration_input: Optional[pulumi.Input[pulumi.InputType['DeliveryStreamEncryptionConfigurationInputArgs']]] = None,
                 delivery_stream_name: Optional[pulumi.Input[str]] = None,
                 delivery_stream_type: Optional[pulumi.Input['DeliveryStreamType']] = None,
                 elasticsearch_destination_configuration: Optional[pulumi.Input[pulumi.InputType['DeliveryStreamElasticsearchDestinationConfigurationArgs']]] = None,
                 extended_s3_destination_configuration: Optional[pulumi.Input[pulumi.InputType['DeliveryStreamExtendedS3DestinationConfigurationArgs']]] = None,
                 http_endpoint_destination_configuration: Optional[pulumi.Input[pulumi.InputType['DeliveryStreamHttpEndpointDestinationConfigurationArgs']]] = None,
                 kinesis_stream_source_configuration: Optional[pulumi.Input[pulumi.InputType['DeliveryStreamKinesisStreamSourceConfigurationArgs']]] = None,
                 redshift_destination_configuration: Optional[pulumi.Input[pulumi.InputType['DeliveryStreamRedshiftDestinationConfigurationArgs']]] = None,
                 s3_destination_configuration: Optional[pulumi.Input[pulumi.InputType['DeliveryStreamS3DestinationConfigurationArgs']]] = None,
                 splunk_destination_configuration: Optional[pulumi.Input[pulumi.InputType['DeliveryStreamSplunkDestinationConfigurationArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DeliveryStreamTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::KinesisFirehose::DeliveryStream

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[DeliveryStreamArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::KinesisFirehose::DeliveryStream

        :param str resource_name: The name of the resource.
        :param DeliveryStreamArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DeliveryStreamArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 amazon_open_search_serverless_destination_configuration: Optional[pulumi.Input[pulumi.InputType['DeliveryStreamAmazonOpenSearchServerlessDestinationConfigurationArgs']]] = None,
                 amazonopensearchservice_destination_configuration: Optional[pulumi.Input[pulumi.InputType['DeliveryStreamAmazonopensearchserviceDestinationConfigurationArgs']]] = None,
                 delivery_stream_encryption_configuration_input: Optional[pulumi.Input[pulumi.InputType['DeliveryStreamEncryptionConfigurationInputArgs']]] = None,
                 delivery_stream_name: Optional[pulumi.Input[str]] = None,
                 delivery_stream_type: Optional[pulumi.Input['DeliveryStreamType']] = None,
                 elasticsearch_destination_configuration: Optional[pulumi.Input[pulumi.InputType['DeliveryStreamElasticsearchDestinationConfigurationArgs']]] = None,
                 extended_s3_destination_configuration: Optional[pulumi.Input[pulumi.InputType['DeliveryStreamExtendedS3DestinationConfigurationArgs']]] = None,
                 http_endpoint_destination_configuration: Optional[pulumi.Input[pulumi.InputType['DeliveryStreamHttpEndpointDestinationConfigurationArgs']]] = None,
                 kinesis_stream_source_configuration: Optional[pulumi.Input[pulumi.InputType['DeliveryStreamKinesisStreamSourceConfigurationArgs']]] = None,
                 redshift_destination_configuration: Optional[pulumi.Input[pulumi.InputType['DeliveryStreamRedshiftDestinationConfigurationArgs']]] = None,
                 s3_destination_configuration: Optional[pulumi.Input[pulumi.InputType['DeliveryStreamS3DestinationConfigurationArgs']]] = None,
                 splunk_destination_configuration: Optional[pulumi.Input[pulumi.InputType['DeliveryStreamSplunkDestinationConfigurationArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DeliveryStreamTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DeliveryStreamArgs.__new__(DeliveryStreamArgs)

            __props__.__dict__["amazon_open_search_serverless_destination_configuration"] = amazon_open_search_serverless_destination_configuration
            __props__.__dict__["amazonopensearchservice_destination_configuration"] = amazonopensearchservice_destination_configuration
            __props__.__dict__["delivery_stream_encryption_configuration_input"] = delivery_stream_encryption_configuration_input
            __props__.__dict__["delivery_stream_name"] = delivery_stream_name
            __props__.__dict__["delivery_stream_type"] = delivery_stream_type
            __props__.__dict__["elasticsearch_destination_configuration"] = elasticsearch_destination_configuration
            __props__.__dict__["extended_s3_destination_configuration"] = extended_s3_destination_configuration
            __props__.__dict__["http_endpoint_destination_configuration"] = http_endpoint_destination_configuration
            __props__.__dict__["kinesis_stream_source_configuration"] = kinesis_stream_source_configuration
            __props__.__dict__["redshift_destination_configuration"] = redshift_destination_configuration
            __props__.__dict__["s3_destination_configuration"] = s3_destination_configuration
            __props__.__dict__["splunk_destination_configuration"] = splunk_destination_configuration
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
        super(DeliveryStream, __self__).__init__(
            'aws-native:kinesisfirehose:DeliveryStream',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DeliveryStream':
        """
        Get an existing DeliveryStream resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DeliveryStreamArgs.__new__(DeliveryStreamArgs)

        __props__.__dict__["amazon_open_search_serverless_destination_configuration"] = None
        __props__.__dict__["amazonopensearchservice_destination_configuration"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["delivery_stream_encryption_configuration_input"] = None
        __props__.__dict__["delivery_stream_name"] = None
        __props__.__dict__["delivery_stream_type"] = None
        __props__.__dict__["elasticsearch_destination_configuration"] = None
        __props__.__dict__["extended_s3_destination_configuration"] = None
        __props__.__dict__["http_endpoint_destination_configuration"] = None
        __props__.__dict__["kinesis_stream_source_configuration"] = None
        __props__.__dict__["redshift_destination_configuration"] = None
        __props__.__dict__["s3_destination_configuration"] = None
        __props__.__dict__["splunk_destination_configuration"] = None
        __props__.__dict__["tags"] = None
        return DeliveryStream(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="amazonOpenSearchServerlessDestinationConfiguration")
    def amazon_open_search_serverless_destination_configuration(self) -> pulumi.Output[Optional['outputs.DeliveryStreamAmazonOpenSearchServerlessDestinationConfiguration']]:
        return pulumi.get(self, "amazon_open_search_serverless_destination_configuration")

    @property
    @pulumi.getter(name="amazonopensearchserviceDestinationConfiguration")
    def amazonopensearchservice_destination_configuration(self) -> pulumi.Output[Optional['outputs.DeliveryStreamAmazonopensearchserviceDestinationConfiguration']]:
        return pulumi.get(self, "amazonopensearchservice_destination_configuration")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="deliveryStreamEncryptionConfigurationInput")
    def delivery_stream_encryption_configuration_input(self) -> pulumi.Output[Optional['outputs.DeliveryStreamEncryptionConfigurationInput']]:
        return pulumi.get(self, "delivery_stream_encryption_configuration_input")

    @property
    @pulumi.getter(name="deliveryStreamName")
    def delivery_stream_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "delivery_stream_name")

    @property
    @pulumi.getter(name="deliveryStreamType")
    def delivery_stream_type(self) -> pulumi.Output[Optional['DeliveryStreamType']]:
        return pulumi.get(self, "delivery_stream_type")

    @property
    @pulumi.getter(name="elasticsearchDestinationConfiguration")
    def elasticsearch_destination_configuration(self) -> pulumi.Output[Optional['outputs.DeliveryStreamElasticsearchDestinationConfiguration']]:
        return pulumi.get(self, "elasticsearch_destination_configuration")

    @property
    @pulumi.getter(name="extendedS3DestinationConfiguration")
    def extended_s3_destination_configuration(self) -> pulumi.Output[Optional['outputs.DeliveryStreamExtendedS3DestinationConfiguration']]:
        return pulumi.get(self, "extended_s3_destination_configuration")

    @property
    @pulumi.getter(name="httpEndpointDestinationConfiguration")
    def http_endpoint_destination_configuration(self) -> pulumi.Output[Optional['outputs.DeliveryStreamHttpEndpointDestinationConfiguration']]:
        return pulumi.get(self, "http_endpoint_destination_configuration")

    @property
    @pulumi.getter(name="kinesisStreamSourceConfiguration")
    def kinesis_stream_source_configuration(self) -> pulumi.Output[Optional['outputs.DeliveryStreamKinesisStreamSourceConfiguration']]:
        return pulumi.get(self, "kinesis_stream_source_configuration")

    @property
    @pulumi.getter(name="redshiftDestinationConfiguration")
    def redshift_destination_configuration(self) -> pulumi.Output[Optional['outputs.DeliveryStreamRedshiftDestinationConfiguration']]:
        return pulumi.get(self, "redshift_destination_configuration")

    @property
    @pulumi.getter(name="s3DestinationConfiguration")
    def s3_destination_configuration(self) -> pulumi.Output[Optional['outputs.DeliveryStreamS3DestinationConfiguration']]:
        return pulumi.get(self, "s3_destination_configuration")

    @property
    @pulumi.getter(name="splunkDestinationConfiguration")
    def splunk_destination_configuration(self) -> pulumi.Output[Optional['outputs.DeliveryStreamSplunkDestinationConfiguration']]:
        return pulumi.get(self, "splunk_destination_configuration")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.DeliveryStreamTag']]]:
        return pulumi.get(self, "tags")

