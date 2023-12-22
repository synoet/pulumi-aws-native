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

__all__ = ['DeploymentGroupArgs', 'DeploymentGroup']

@pulumi.input_type
class DeploymentGroupArgs:
    def __init__(__self__, *,
                 application_name: pulumi.Input[str],
                 service_role_arn: pulumi.Input[str],
                 alarm_configuration: Optional[pulumi.Input['DeploymentGroupAlarmConfigurationArgs']] = None,
                 auto_rollback_configuration: Optional[pulumi.Input['DeploymentGroupAutoRollbackConfigurationArgs']] = None,
                 auto_scaling_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 blue_green_deployment_configuration: Optional[pulumi.Input['DeploymentGroupBlueGreenDeploymentConfigurationArgs']] = None,
                 deployment: Optional[pulumi.Input['DeploymentGroupDeploymentArgs']] = None,
                 deployment_config_name: Optional[pulumi.Input[str]] = None,
                 deployment_group_name: Optional[pulumi.Input[str]] = None,
                 deployment_style: Optional[pulumi.Input['DeploymentGroupDeploymentStyleArgs']] = None,
                 ec2_tag_filters: Optional[pulumi.Input[Sequence[pulumi.Input['DeploymentGroupEc2TagFilterArgs']]]] = None,
                 ec2_tag_set: Optional[pulumi.Input['DeploymentGroupEc2TagSetArgs']] = None,
                 ecs_services: Optional[pulumi.Input[Sequence[pulumi.Input['DeploymentGroupEcsServiceArgs']]]] = None,
                 load_balancer_info: Optional[pulumi.Input['DeploymentGroupLoadBalancerInfoArgs']] = None,
                 on_premises_instance_tag_filters: Optional[pulumi.Input[Sequence[pulumi.Input['DeploymentGroupTagFilterArgs']]]] = None,
                 on_premises_tag_set: Optional[pulumi.Input['DeploymentGroupOnPremisesTagSetArgs']] = None,
                 outdated_instances_strategy: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['DeploymentGroupTagArgs']]]] = None,
                 termination_hook_enabled: Optional[pulumi.Input[bool]] = None,
                 trigger_configurations: Optional[pulumi.Input[Sequence[pulumi.Input['DeploymentGroupTriggerConfigArgs']]]] = None):
        """
        The set of arguments for constructing a DeploymentGroup resource.
        """
        pulumi.set(__self__, "application_name", application_name)
        pulumi.set(__self__, "service_role_arn", service_role_arn)
        if alarm_configuration is not None:
            pulumi.set(__self__, "alarm_configuration", alarm_configuration)
        if auto_rollback_configuration is not None:
            pulumi.set(__self__, "auto_rollback_configuration", auto_rollback_configuration)
        if auto_scaling_groups is not None:
            pulumi.set(__self__, "auto_scaling_groups", auto_scaling_groups)
        if blue_green_deployment_configuration is not None:
            pulumi.set(__self__, "blue_green_deployment_configuration", blue_green_deployment_configuration)
        if deployment is not None:
            pulumi.set(__self__, "deployment", deployment)
        if deployment_config_name is not None:
            pulumi.set(__self__, "deployment_config_name", deployment_config_name)
        if deployment_group_name is not None:
            pulumi.set(__self__, "deployment_group_name", deployment_group_name)
        if deployment_style is not None:
            pulumi.set(__self__, "deployment_style", deployment_style)
        if ec2_tag_filters is not None:
            pulumi.set(__self__, "ec2_tag_filters", ec2_tag_filters)
        if ec2_tag_set is not None:
            pulumi.set(__self__, "ec2_tag_set", ec2_tag_set)
        if ecs_services is not None:
            pulumi.set(__self__, "ecs_services", ecs_services)
        if load_balancer_info is not None:
            pulumi.set(__self__, "load_balancer_info", load_balancer_info)
        if on_premises_instance_tag_filters is not None:
            pulumi.set(__self__, "on_premises_instance_tag_filters", on_premises_instance_tag_filters)
        if on_premises_tag_set is not None:
            pulumi.set(__self__, "on_premises_tag_set", on_premises_tag_set)
        if outdated_instances_strategy is not None:
            pulumi.set(__self__, "outdated_instances_strategy", outdated_instances_strategy)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if termination_hook_enabled is not None:
            pulumi.set(__self__, "termination_hook_enabled", termination_hook_enabled)
        if trigger_configurations is not None:
            pulumi.set(__self__, "trigger_configurations", trigger_configurations)

    @property
    @pulumi.getter(name="applicationName")
    def application_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "application_name")

    @application_name.setter
    def application_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "application_name", value)

    @property
    @pulumi.getter(name="serviceRoleArn")
    def service_role_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "service_role_arn")

    @service_role_arn.setter
    def service_role_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_role_arn", value)

    @property
    @pulumi.getter(name="alarmConfiguration")
    def alarm_configuration(self) -> Optional[pulumi.Input['DeploymentGroupAlarmConfigurationArgs']]:
        return pulumi.get(self, "alarm_configuration")

    @alarm_configuration.setter
    def alarm_configuration(self, value: Optional[pulumi.Input['DeploymentGroupAlarmConfigurationArgs']]):
        pulumi.set(self, "alarm_configuration", value)

    @property
    @pulumi.getter(name="autoRollbackConfiguration")
    def auto_rollback_configuration(self) -> Optional[pulumi.Input['DeploymentGroupAutoRollbackConfigurationArgs']]:
        return pulumi.get(self, "auto_rollback_configuration")

    @auto_rollback_configuration.setter
    def auto_rollback_configuration(self, value: Optional[pulumi.Input['DeploymentGroupAutoRollbackConfigurationArgs']]):
        pulumi.set(self, "auto_rollback_configuration", value)

    @property
    @pulumi.getter(name="autoScalingGroups")
    def auto_scaling_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "auto_scaling_groups")

    @auto_scaling_groups.setter
    def auto_scaling_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "auto_scaling_groups", value)

    @property
    @pulumi.getter(name="blueGreenDeploymentConfiguration")
    def blue_green_deployment_configuration(self) -> Optional[pulumi.Input['DeploymentGroupBlueGreenDeploymentConfigurationArgs']]:
        return pulumi.get(self, "blue_green_deployment_configuration")

    @blue_green_deployment_configuration.setter
    def blue_green_deployment_configuration(self, value: Optional[pulumi.Input['DeploymentGroupBlueGreenDeploymentConfigurationArgs']]):
        pulumi.set(self, "blue_green_deployment_configuration", value)

    @property
    @pulumi.getter
    def deployment(self) -> Optional[pulumi.Input['DeploymentGroupDeploymentArgs']]:
        return pulumi.get(self, "deployment")

    @deployment.setter
    def deployment(self, value: Optional[pulumi.Input['DeploymentGroupDeploymentArgs']]):
        pulumi.set(self, "deployment", value)

    @property
    @pulumi.getter(name="deploymentConfigName")
    def deployment_config_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "deployment_config_name")

    @deployment_config_name.setter
    def deployment_config_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deployment_config_name", value)

    @property
    @pulumi.getter(name="deploymentGroupName")
    def deployment_group_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "deployment_group_name")

    @deployment_group_name.setter
    def deployment_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deployment_group_name", value)

    @property
    @pulumi.getter(name="deploymentStyle")
    def deployment_style(self) -> Optional[pulumi.Input['DeploymentGroupDeploymentStyleArgs']]:
        return pulumi.get(self, "deployment_style")

    @deployment_style.setter
    def deployment_style(self, value: Optional[pulumi.Input['DeploymentGroupDeploymentStyleArgs']]):
        pulumi.set(self, "deployment_style", value)

    @property
    @pulumi.getter(name="ec2TagFilters")
    def ec2_tag_filters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DeploymentGroupEc2TagFilterArgs']]]]:
        return pulumi.get(self, "ec2_tag_filters")

    @ec2_tag_filters.setter
    def ec2_tag_filters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DeploymentGroupEc2TagFilterArgs']]]]):
        pulumi.set(self, "ec2_tag_filters", value)

    @property
    @pulumi.getter(name="ec2TagSet")
    def ec2_tag_set(self) -> Optional[pulumi.Input['DeploymentGroupEc2TagSetArgs']]:
        return pulumi.get(self, "ec2_tag_set")

    @ec2_tag_set.setter
    def ec2_tag_set(self, value: Optional[pulumi.Input['DeploymentGroupEc2TagSetArgs']]):
        pulumi.set(self, "ec2_tag_set", value)

    @property
    @pulumi.getter(name="ecsServices")
    def ecs_services(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DeploymentGroupEcsServiceArgs']]]]:
        return pulumi.get(self, "ecs_services")

    @ecs_services.setter
    def ecs_services(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DeploymentGroupEcsServiceArgs']]]]):
        pulumi.set(self, "ecs_services", value)

    @property
    @pulumi.getter(name="loadBalancerInfo")
    def load_balancer_info(self) -> Optional[pulumi.Input['DeploymentGroupLoadBalancerInfoArgs']]:
        return pulumi.get(self, "load_balancer_info")

    @load_balancer_info.setter
    def load_balancer_info(self, value: Optional[pulumi.Input['DeploymentGroupLoadBalancerInfoArgs']]):
        pulumi.set(self, "load_balancer_info", value)

    @property
    @pulumi.getter(name="onPremisesInstanceTagFilters")
    def on_premises_instance_tag_filters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DeploymentGroupTagFilterArgs']]]]:
        return pulumi.get(self, "on_premises_instance_tag_filters")

    @on_premises_instance_tag_filters.setter
    def on_premises_instance_tag_filters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DeploymentGroupTagFilterArgs']]]]):
        pulumi.set(self, "on_premises_instance_tag_filters", value)

    @property
    @pulumi.getter(name="onPremisesTagSet")
    def on_premises_tag_set(self) -> Optional[pulumi.Input['DeploymentGroupOnPremisesTagSetArgs']]:
        return pulumi.get(self, "on_premises_tag_set")

    @on_premises_tag_set.setter
    def on_premises_tag_set(self, value: Optional[pulumi.Input['DeploymentGroupOnPremisesTagSetArgs']]):
        pulumi.set(self, "on_premises_tag_set", value)

    @property
    @pulumi.getter(name="outdatedInstancesStrategy")
    def outdated_instances_strategy(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "outdated_instances_strategy")

    @outdated_instances_strategy.setter
    def outdated_instances_strategy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "outdated_instances_strategy", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DeploymentGroupTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DeploymentGroupTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="terminationHookEnabled")
    def termination_hook_enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "termination_hook_enabled")

    @termination_hook_enabled.setter
    def termination_hook_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "termination_hook_enabled", value)

    @property
    @pulumi.getter(name="triggerConfigurations")
    def trigger_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DeploymentGroupTriggerConfigArgs']]]]:
        return pulumi.get(self, "trigger_configurations")

    @trigger_configurations.setter
    def trigger_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DeploymentGroupTriggerConfigArgs']]]]):
        pulumi.set(self, "trigger_configurations", value)


warnings.warn("""DeploymentGroup is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class DeploymentGroup(pulumi.CustomResource):
    warnings.warn("""DeploymentGroup is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 alarm_configuration: Optional[pulumi.Input[pulumi.InputType['DeploymentGroupAlarmConfigurationArgs']]] = None,
                 application_name: Optional[pulumi.Input[str]] = None,
                 auto_rollback_configuration: Optional[pulumi.Input[pulumi.InputType['DeploymentGroupAutoRollbackConfigurationArgs']]] = None,
                 auto_scaling_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 blue_green_deployment_configuration: Optional[pulumi.Input[pulumi.InputType['DeploymentGroupBlueGreenDeploymentConfigurationArgs']]] = None,
                 deployment: Optional[pulumi.Input[pulumi.InputType['DeploymentGroupDeploymentArgs']]] = None,
                 deployment_config_name: Optional[pulumi.Input[str]] = None,
                 deployment_group_name: Optional[pulumi.Input[str]] = None,
                 deployment_style: Optional[pulumi.Input[pulumi.InputType['DeploymentGroupDeploymentStyleArgs']]] = None,
                 ec2_tag_filters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DeploymentGroupEc2TagFilterArgs']]]]] = None,
                 ec2_tag_set: Optional[pulumi.Input[pulumi.InputType['DeploymentGroupEc2TagSetArgs']]] = None,
                 ecs_services: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DeploymentGroupEcsServiceArgs']]]]] = None,
                 load_balancer_info: Optional[pulumi.Input[pulumi.InputType['DeploymentGroupLoadBalancerInfoArgs']]] = None,
                 on_premises_instance_tag_filters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DeploymentGroupTagFilterArgs']]]]] = None,
                 on_premises_tag_set: Optional[pulumi.Input[pulumi.InputType['DeploymentGroupOnPremisesTagSetArgs']]] = None,
                 outdated_instances_strategy: Optional[pulumi.Input[str]] = None,
                 service_role_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DeploymentGroupTagArgs']]]]] = None,
                 termination_hook_enabled: Optional[pulumi.Input[bool]] = None,
                 trigger_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DeploymentGroupTriggerConfigArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::CodeDeploy::DeploymentGroup

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DeploymentGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::CodeDeploy::DeploymentGroup

        :param str resource_name: The name of the resource.
        :param DeploymentGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DeploymentGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 alarm_configuration: Optional[pulumi.Input[pulumi.InputType['DeploymentGroupAlarmConfigurationArgs']]] = None,
                 application_name: Optional[pulumi.Input[str]] = None,
                 auto_rollback_configuration: Optional[pulumi.Input[pulumi.InputType['DeploymentGroupAutoRollbackConfigurationArgs']]] = None,
                 auto_scaling_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 blue_green_deployment_configuration: Optional[pulumi.Input[pulumi.InputType['DeploymentGroupBlueGreenDeploymentConfigurationArgs']]] = None,
                 deployment: Optional[pulumi.Input[pulumi.InputType['DeploymentGroupDeploymentArgs']]] = None,
                 deployment_config_name: Optional[pulumi.Input[str]] = None,
                 deployment_group_name: Optional[pulumi.Input[str]] = None,
                 deployment_style: Optional[pulumi.Input[pulumi.InputType['DeploymentGroupDeploymentStyleArgs']]] = None,
                 ec2_tag_filters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DeploymentGroupEc2TagFilterArgs']]]]] = None,
                 ec2_tag_set: Optional[pulumi.Input[pulumi.InputType['DeploymentGroupEc2TagSetArgs']]] = None,
                 ecs_services: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DeploymentGroupEcsServiceArgs']]]]] = None,
                 load_balancer_info: Optional[pulumi.Input[pulumi.InputType['DeploymentGroupLoadBalancerInfoArgs']]] = None,
                 on_premises_instance_tag_filters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DeploymentGroupTagFilterArgs']]]]] = None,
                 on_premises_tag_set: Optional[pulumi.Input[pulumi.InputType['DeploymentGroupOnPremisesTagSetArgs']]] = None,
                 outdated_instances_strategy: Optional[pulumi.Input[str]] = None,
                 service_role_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DeploymentGroupTagArgs']]]]] = None,
                 termination_hook_enabled: Optional[pulumi.Input[bool]] = None,
                 trigger_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DeploymentGroupTriggerConfigArgs']]]]] = None,
                 __props__=None):
        pulumi.log.warn("""DeploymentGroup is deprecated: DeploymentGroup is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DeploymentGroupArgs.__new__(DeploymentGroupArgs)

            __props__.__dict__["alarm_configuration"] = alarm_configuration
            if application_name is None and not opts.urn:
                raise TypeError("Missing required property 'application_name'")
            __props__.__dict__["application_name"] = application_name
            __props__.__dict__["auto_rollback_configuration"] = auto_rollback_configuration
            __props__.__dict__["auto_scaling_groups"] = auto_scaling_groups
            __props__.__dict__["blue_green_deployment_configuration"] = blue_green_deployment_configuration
            __props__.__dict__["deployment"] = deployment
            __props__.__dict__["deployment_config_name"] = deployment_config_name
            __props__.__dict__["deployment_group_name"] = deployment_group_name
            __props__.__dict__["deployment_style"] = deployment_style
            __props__.__dict__["ec2_tag_filters"] = ec2_tag_filters
            __props__.__dict__["ec2_tag_set"] = ec2_tag_set
            __props__.__dict__["ecs_services"] = ecs_services
            __props__.__dict__["load_balancer_info"] = load_balancer_info
            __props__.__dict__["on_premises_instance_tag_filters"] = on_premises_instance_tag_filters
            __props__.__dict__["on_premises_tag_set"] = on_premises_tag_set
            __props__.__dict__["outdated_instances_strategy"] = outdated_instances_strategy
            if service_role_arn is None and not opts.urn:
                raise TypeError("Missing required property 'service_role_arn'")
            __props__.__dict__["service_role_arn"] = service_role_arn
            __props__.__dict__["tags"] = tags
            __props__.__dict__["termination_hook_enabled"] = termination_hook_enabled
            __props__.__dict__["trigger_configurations"] = trigger_configurations
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["application_name", "deployment_group_name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(DeploymentGroup, __self__).__init__(
            'aws-native:codedeploy:DeploymentGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DeploymentGroup':
        """
        Get an existing DeploymentGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DeploymentGroupArgs.__new__(DeploymentGroupArgs)

        __props__.__dict__["alarm_configuration"] = None
        __props__.__dict__["application_name"] = None
        __props__.__dict__["auto_rollback_configuration"] = None
        __props__.__dict__["auto_scaling_groups"] = None
        __props__.__dict__["blue_green_deployment_configuration"] = None
        __props__.__dict__["deployment"] = None
        __props__.__dict__["deployment_config_name"] = None
        __props__.__dict__["deployment_group_name"] = None
        __props__.__dict__["deployment_style"] = None
        __props__.__dict__["ec2_tag_filters"] = None
        __props__.__dict__["ec2_tag_set"] = None
        __props__.__dict__["ecs_services"] = None
        __props__.__dict__["load_balancer_info"] = None
        __props__.__dict__["on_premises_instance_tag_filters"] = None
        __props__.__dict__["on_premises_tag_set"] = None
        __props__.__dict__["outdated_instances_strategy"] = None
        __props__.__dict__["service_role_arn"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["termination_hook_enabled"] = None
        __props__.__dict__["trigger_configurations"] = None
        return DeploymentGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="alarmConfiguration")
    def alarm_configuration(self) -> pulumi.Output[Optional['outputs.DeploymentGroupAlarmConfiguration']]:
        return pulumi.get(self, "alarm_configuration")

    @property
    @pulumi.getter(name="applicationName")
    def application_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "application_name")

    @property
    @pulumi.getter(name="autoRollbackConfiguration")
    def auto_rollback_configuration(self) -> pulumi.Output[Optional['outputs.DeploymentGroupAutoRollbackConfiguration']]:
        return pulumi.get(self, "auto_rollback_configuration")

    @property
    @pulumi.getter(name="autoScalingGroups")
    def auto_scaling_groups(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "auto_scaling_groups")

    @property
    @pulumi.getter(name="blueGreenDeploymentConfiguration")
    def blue_green_deployment_configuration(self) -> pulumi.Output[Optional['outputs.DeploymentGroupBlueGreenDeploymentConfiguration']]:
        return pulumi.get(self, "blue_green_deployment_configuration")

    @property
    @pulumi.getter
    def deployment(self) -> pulumi.Output[Optional['outputs.DeploymentGroupDeployment']]:
        return pulumi.get(self, "deployment")

    @property
    @pulumi.getter(name="deploymentConfigName")
    def deployment_config_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "deployment_config_name")

    @property
    @pulumi.getter(name="deploymentGroupName")
    def deployment_group_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "deployment_group_name")

    @property
    @pulumi.getter(name="deploymentStyle")
    def deployment_style(self) -> pulumi.Output[Optional['outputs.DeploymentGroupDeploymentStyle']]:
        return pulumi.get(self, "deployment_style")

    @property
    @pulumi.getter(name="ec2TagFilters")
    def ec2_tag_filters(self) -> pulumi.Output[Optional[Sequence['outputs.DeploymentGroupEc2TagFilter']]]:
        return pulumi.get(self, "ec2_tag_filters")

    @property
    @pulumi.getter(name="ec2TagSet")
    def ec2_tag_set(self) -> pulumi.Output[Optional['outputs.DeploymentGroupEc2TagSet']]:
        return pulumi.get(self, "ec2_tag_set")

    @property
    @pulumi.getter(name="ecsServices")
    def ecs_services(self) -> pulumi.Output[Optional[Sequence['outputs.DeploymentGroupEcsService']]]:
        return pulumi.get(self, "ecs_services")

    @property
    @pulumi.getter(name="loadBalancerInfo")
    def load_balancer_info(self) -> pulumi.Output[Optional['outputs.DeploymentGroupLoadBalancerInfo']]:
        return pulumi.get(self, "load_balancer_info")

    @property
    @pulumi.getter(name="onPremisesInstanceTagFilters")
    def on_premises_instance_tag_filters(self) -> pulumi.Output[Optional[Sequence['outputs.DeploymentGroupTagFilter']]]:
        return pulumi.get(self, "on_premises_instance_tag_filters")

    @property
    @pulumi.getter(name="onPremisesTagSet")
    def on_premises_tag_set(self) -> pulumi.Output[Optional['outputs.DeploymentGroupOnPremisesTagSet']]:
        return pulumi.get(self, "on_premises_tag_set")

    @property
    @pulumi.getter(name="outdatedInstancesStrategy")
    def outdated_instances_strategy(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "outdated_instances_strategy")

    @property
    @pulumi.getter(name="serviceRoleArn")
    def service_role_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "service_role_arn")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.DeploymentGroupTag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="terminationHookEnabled")
    def termination_hook_enabled(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "termination_hook_enabled")

    @property
    @pulumi.getter(name="triggerConfigurations")
    def trigger_configurations(self) -> pulumi.Output[Optional[Sequence['outputs.DeploymentGroupTriggerConfig']]]:
        return pulumi.get(self, "trigger_configurations")

