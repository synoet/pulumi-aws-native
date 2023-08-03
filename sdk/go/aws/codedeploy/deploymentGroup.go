// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package codedeploy

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::CodeDeploy::DeploymentGroup
//
// Deprecated: DeploymentGroup is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type DeploymentGroup struct {
	pulumi.CustomResourceState

	AlarmConfiguration               DeploymentGroupAlarmConfigurationPtrOutput               `pulumi:"alarmConfiguration"`
	ApplicationName                  pulumi.StringOutput                                      `pulumi:"applicationName"`
	AutoRollbackConfiguration        DeploymentGroupAutoRollbackConfigurationPtrOutput        `pulumi:"autoRollbackConfiguration"`
	AutoScalingGroups                pulumi.StringArrayOutput                                 `pulumi:"autoScalingGroups"`
	BlueGreenDeploymentConfiguration DeploymentGroupBlueGreenDeploymentConfigurationPtrOutput `pulumi:"blueGreenDeploymentConfiguration"`
	Deployment                       DeploymentGroupDeploymentPtrOutput                       `pulumi:"deployment"`
	DeploymentConfigName             pulumi.StringPtrOutput                                   `pulumi:"deploymentConfigName"`
	DeploymentGroupName              pulumi.StringPtrOutput                                   `pulumi:"deploymentGroupName"`
	DeploymentStyle                  DeploymentGroupDeploymentStylePtrOutput                  `pulumi:"deploymentStyle"`
	Ec2TagFilters                    DeploymentGroupEc2TagFilterArrayOutput                   `pulumi:"ec2TagFilters"`
	Ec2TagSet                        DeploymentGroupEc2TagSetPtrOutput                        `pulumi:"ec2TagSet"`
	EcsServices                      DeploymentGroupEcsServiceArrayOutput                     `pulumi:"ecsServices"`
	LoadBalancerInfo                 DeploymentGroupLoadBalancerInfoPtrOutput                 `pulumi:"loadBalancerInfo"`
	OnPremisesInstanceTagFilters     DeploymentGroupTagFilterArrayOutput                      `pulumi:"onPremisesInstanceTagFilters"`
	OnPremisesTagSet                 DeploymentGroupOnPremisesTagSetPtrOutput                 `pulumi:"onPremisesTagSet"`
	OutdatedInstancesStrategy        pulumi.StringPtrOutput                                   `pulumi:"outdatedInstancesStrategy"`
	ServiceRoleArn                   pulumi.StringOutput                                      `pulumi:"serviceRoleArn"`
	Tags                             DeploymentGroupTagArrayOutput                            `pulumi:"tags"`
	TriggerConfigurations            DeploymentGroupTriggerConfigArrayOutput                  `pulumi:"triggerConfigurations"`
}

// NewDeploymentGroup registers a new resource with the given unique name, arguments, and options.
func NewDeploymentGroup(ctx *pulumi.Context,
	name string, args *DeploymentGroupArgs, opts ...pulumi.ResourceOption) (*DeploymentGroup, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ApplicationName == nil {
		return nil, errors.New("invalid value for required argument 'ApplicationName'")
	}
	if args.ServiceRoleArn == nil {
		return nil, errors.New("invalid value for required argument 'ServiceRoleArn'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource DeploymentGroup
	err := ctx.RegisterResource("aws-native:codedeploy:DeploymentGroup", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDeploymentGroup gets an existing DeploymentGroup resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDeploymentGroup(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DeploymentGroupState, opts ...pulumi.ResourceOption) (*DeploymentGroup, error) {
	var resource DeploymentGroup
	err := ctx.ReadResource("aws-native:codedeploy:DeploymentGroup", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DeploymentGroup resources.
type deploymentGroupState struct {
}

type DeploymentGroupState struct {
}

func (DeploymentGroupState) ElementType() reflect.Type {
	return reflect.TypeOf((*deploymentGroupState)(nil)).Elem()
}

type deploymentGroupArgs struct {
	AlarmConfiguration               *DeploymentGroupAlarmConfiguration               `pulumi:"alarmConfiguration"`
	ApplicationName                  string                                           `pulumi:"applicationName"`
	AutoRollbackConfiguration        *DeploymentGroupAutoRollbackConfiguration        `pulumi:"autoRollbackConfiguration"`
	AutoScalingGroups                []string                                         `pulumi:"autoScalingGroups"`
	BlueGreenDeploymentConfiguration *DeploymentGroupBlueGreenDeploymentConfiguration `pulumi:"blueGreenDeploymentConfiguration"`
	Deployment                       *DeploymentGroupDeployment                       `pulumi:"deployment"`
	DeploymentConfigName             *string                                          `pulumi:"deploymentConfigName"`
	DeploymentGroupName              *string                                          `pulumi:"deploymentGroupName"`
	DeploymentStyle                  *DeploymentGroupDeploymentStyle                  `pulumi:"deploymentStyle"`
	Ec2TagFilters                    []DeploymentGroupEc2TagFilter                    `pulumi:"ec2TagFilters"`
	Ec2TagSet                        *DeploymentGroupEc2TagSet                        `pulumi:"ec2TagSet"`
	EcsServices                      []DeploymentGroupEcsService                      `pulumi:"ecsServices"`
	LoadBalancerInfo                 *DeploymentGroupLoadBalancerInfo                 `pulumi:"loadBalancerInfo"`
	OnPremisesInstanceTagFilters     []DeploymentGroupTagFilter                       `pulumi:"onPremisesInstanceTagFilters"`
	OnPremisesTagSet                 *DeploymentGroupOnPremisesTagSet                 `pulumi:"onPremisesTagSet"`
	OutdatedInstancesStrategy        *string                                          `pulumi:"outdatedInstancesStrategy"`
	ServiceRoleArn                   string                                           `pulumi:"serviceRoleArn"`
	Tags                             []DeploymentGroupTag                             `pulumi:"tags"`
	TriggerConfigurations            []DeploymentGroupTriggerConfig                   `pulumi:"triggerConfigurations"`
}

// The set of arguments for constructing a DeploymentGroup resource.
type DeploymentGroupArgs struct {
	AlarmConfiguration               DeploymentGroupAlarmConfigurationPtrInput
	ApplicationName                  pulumi.StringInput
	AutoRollbackConfiguration        DeploymentGroupAutoRollbackConfigurationPtrInput
	AutoScalingGroups                pulumi.StringArrayInput
	BlueGreenDeploymentConfiguration DeploymentGroupBlueGreenDeploymentConfigurationPtrInput
	Deployment                       DeploymentGroupDeploymentPtrInput
	DeploymentConfigName             pulumi.StringPtrInput
	DeploymentGroupName              pulumi.StringPtrInput
	DeploymentStyle                  DeploymentGroupDeploymentStylePtrInput
	Ec2TagFilters                    DeploymentGroupEc2TagFilterArrayInput
	Ec2TagSet                        DeploymentGroupEc2TagSetPtrInput
	EcsServices                      DeploymentGroupEcsServiceArrayInput
	LoadBalancerInfo                 DeploymentGroupLoadBalancerInfoPtrInput
	OnPremisesInstanceTagFilters     DeploymentGroupTagFilterArrayInput
	OnPremisesTagSet                 DeploymentGroupOnPremisesTagSetPtrInput
	OutdatedInstancesStrategy        pulumi.StringPtrInput
	ServiceRoleArn                   pulumi.StringInput
	Tags                             DeploymentGroupTagArrayInput
	TriggerConfigurations            DeploymentGroupTriggerConfigArrayInput
}

func (DeploymentGroupArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*deploymentGroupArgs)(nil)).Elem()
}

type DeploymentGroupInput interface {
	pulumi.Input

	ToDeploymentGroupOutput() DeploymentGroupOutput
	ToDeploymentGroupOutputWithContext(ctx context.Context) DeploymentGroupOutput
}

func (*DeploymentGroup) ElementType() reflect.Type {
	return reflect.TypeOf((**DeploymentGroup)(nil)).Elem()
}

func (i *DeploymentGroup) ToDeploymentGroupOutput() DeploymentGroupOutput {
	return i.ToDeploymentGroupOutputWithContext(context.Background())
}

func (i *DeploymentGroup) ToDeploymentGroupOutputWithContext(ctx context.Context) DeploymentGroupOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DeploymentGroupOutput)
}

type DeploymentGroupOutput struct{ *pulumi.OutputState }

func (DeploymentGroupOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DeploymentGroup)(nil)).Elem()
}

func (o DeploymentGroupOutput) ToDeploymentGroupOutput() DeploymentGroupOutput {
	return o
}

func (o DeploymentGroupOutput) ToDeploymentGroupOutputWithContext(ctx context.Context) DeploymentGroupOutput {
	return o
}

func (o DeploymentGroupOutput) AlarmConfiguration() DeploymentGroupAlarmConfigurationPtrOutput {
	return o.ApplyT(func(v *DeploymentGroup) DeploymentGroupAlarmConfigurationPtrOutput { return v.AlarmConfiguration }).(DeploymentGroupAlarmConfigurationPtrOutput)
}

func (o DeploymentGroupOutput) ApplicationName() pulumi.StringOutput {
	return o.ApplyT(func(v *DeploymentGroup) pulumi.StringOutput { return v.ApplicationName }).(pulumi.StringOutput)
}

func (o DeploymentGroupOutput) AutoRollbackConfiguration() DeploymentGroupAutoRollbackConfigurationPtrOutput {
	return o.ApplyT(func(v *DeploymentGroup) DeploymentGroupAutoRollbackConfigurationPtrOutput {
		return v.AutoRollbackConfiguration
	}).(DeploymentGroupAutoRollbackConfigurationPtrOutput)
}

func (o DeploymentGroupOutput) AutoScalingGroups() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *DeploymentGroup) pulumi.StringArrayOutput { return v.AutoScalingGroups }).(pulumi.StringArrayOutput)
}

func (o DeploymentGroupOutput) BlueGreenDeploymentConfiguration() DeploymentGroupBlueGreenDeploymentConfigurationPtrOutput {
	return o.ApplyT(func(v *DeploymentGroup) DeploymentGroupBlueGreenDeploymentConfigurationPtrOutput {
		return v.BlueGreenDeploymentConfiguration
	}).(DeploymentGroupBlueGreenDeploymentConfigurationPtrOutput)
}

func (o DeploymentGroupOutput) Deployment() DeploymentGroupDeploymentPtrOutput {
	return o.ApplyT(func(v *DeploymentGroup) DeploymentGroupDeploymentPtrOutput { return v.Deployment }).(DeploymentGroupDeploymentPtrOutput)
}

func (o DeploymentGroupOutput) DeploymentConfigName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DeploymentGroup) pulumi.StringPtrOutput { return v.DeploymentConfigName }).(pulumi.StringPtrOutput)
}

func (o DeploymentGroupOutput) DeploymentGroupName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DeploymentGroup) pulumi.StringPtrOutput { return v.DeploymentGroupName }).(pulumi.StringPtrOutput)
}

func (o DeploymentGroupOutput) DeploymentStyle() DeploymentGroupDeploymentStylePtrOutput {
	return o.ApplyT(func(v *DeploymentGroup) DeploymentGroupDeploymentStylePtrOutput { return v.DeploymentStyle }).(DeploymentGroupDeploymentStylePtrOutput)
}

func (o DeploymentGroupOutput) Ec2TagFilters() DeploymentGroupEc2TagFilterArrayOutput {
	return o.ApplyT(func(v *DeploymentGroup) DeploymentGroupEc2TagFilterArrayOutput { return v.Ec2TagFilters }).(DeploymentGroupEc2TagFilterArrayOutput)
}

func (o DeploymentGroupOutput) Ec2TagSet() DeploymentGroupEc2TagSetPtrOutput {
	return o.ApplyT(func(v *DeploymentGroup) DeploymentGroupEc2TagSetPtrOutput { return v.Ec2TagSet }).(DeploymentGroupEc2TagSetPtrOutput)
}

func (o DeploymentGroupOutput) EcsServices() DeploymentGroupEcsServiceArrayOutput {
	return o.ApplyT(func(v *DeploymentGroup) DeploymentGroupEcsServiceArrayOutput { return v.EcsServices }).(DeploymentGroupEcsServiceArrayOutput)
}

func (o DeploymentGroupOutput) LoadBalancerInfo() DeploymentGroupLoadBalancerInfoPtrOutput {
	return o.ApplyT(func(v *DeploymentGroup) DeploymentGroupLoadBalancerInfoPtrOutput { return v.LoadBalancerInfo }).(DeploymentGroupLoadBalancerInfoPtrOutput)
}

func (o DeploymentGroupOutput) OnPremisesInstanceTagFilters() DeploymentGroupTagFilterArrayOutput {
	return o.ApplyT(func(v *DeploymentGroup) DeploymentGroupTagFilterArrayOutput { return v.OnPremisesInstanceTagFilters }).(DeploymentGroupTagFilterArrayOutput)
}

func (o DeploymentGroupOutput) OnPremisesTagSet() DeploymentGroupOnPremisesTagSetPtrOutput {
	return o.ApplyT(func(v *DeploymentGroup) DeploymentGroupOnPremisesTagSetPtrOutput { return v.OnPremisesTagSet }).(DeploymentGroupOnPremisesTagSetPtrOutput)
}

func (o DeploymentGroupOutput) OutdatedInstancesStrategy() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DeploymentGroup) pulumi.StringPtrOutput { return v.OutdatedInstancesStrategy }).(pulumi.StringPtrOutput)
}

func (o DeploymentGroupOutput) ServiceRoleArn() pulumi.StringOutput {
	return o.ApplyT(func(v *DeploymentGroup) pulumi.StringOutput { return v.ServiceRoleArn }).(pulumi.StringOutput)
}

func (o DeploymentGroupOutput) Tags() DeploymentGroupTagArrayOutput {
	return o.ApplyT(func(v *DeploymentGroup) DeploymentGroupTagArrayOutput { return v.Tags }).(DeploymentGroupTagArrayOutput)
}

func (o DeploymentGroupOutput) TriggerConfigurations() DeploymentGroupTriggerConfigArrayOutput {
	return o.ApplyT(func(v *DeploymentGroup) DeploymentGroupTriggerConfigArrayOutput { return v.TriggerConfigurations }).(DeploymentGroupTriggerConfigArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DeploymentGroupInput)(nil)).Elem(), &DeploymentGroup{})
	pulumi.RegisterOutputType(DeploymentGroupOutput{})
}
