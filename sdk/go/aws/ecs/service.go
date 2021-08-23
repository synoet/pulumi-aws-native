// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ecs

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html
type Service struct {
	pulumi.CustomResourceState

	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-capacityproviderstrategy
	CapacityProviderStrategy ServiceCapacityProviderStrategyItemArrayOutput `pulumi:"capacityProviderStrategy"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-cluster
	Cluster pulumi.StringPtrOutput `pulumi:"cluster"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-deploymentconfiguration
	DeploymentConfiguration ServiceDeploymentConfigurationPtrOutput `pulumi:"deploymentConfiguration"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-deploymentcontroller
	DeploymentController ServiceDeploymentControllerPtrOutput `pulumi:"deploymentController"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-desiredcount
	DesiredCount pulumi.IntPtrOutput `pulumi:"desiredCount"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-enableecsmanagedtags
	EnableECSManagedTags pulumi.BoolPtrOutput `pulumi:"enableECSManagedTags"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-enableexecutecommand
	EnableExecuteCommand pulumi.BoolPtrOutput `pulumi:"enableExecuteCommand"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-healthcheckgraceperiodseconds
	HealthCheckGracePeriodSeconds pulumi.IntPtrOutput `pulumi:"healthCheckGracePeriodSeconds"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-launchtype
	LaunchType pulumi.StringPtrOutput `pulumi:"launchType"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-loadbalancers
	LoadBalancers ServiceLoadBalancerArrayOutput `pulumi:"loadBalancers"`
	Name          pulumi.StringOutput            `pulumi:"name"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-networkconfiguration
	NetworkConfiguration ServiceNetworkConfigurationPtrOutput `pulumi:"networkConfiguration"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-placementconstraints
	PlacementConstraints ServicePlacementConstraintArrayOutput `pulumi:"placementConstraints"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-placementstrategies
	PlacementStrategies ServicePlacementStrategyArrayOutput `pulumi:"placementStrategies"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-platformversion
	PlatformVersion pulumi.StringPtrOutput `pulumi:"platformVersion"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-propagatetags
	PropagateTags pulumi.StringPtrOutput `pulumi:"propagateTags"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-role
	Role pulumi.StringPtrOutput `pulumi:"role"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-schedulingstrategy
	SchedulingStrategy pulumi.StringPtrOutput `pulumi:"schedulingStrategy"`
	ServiceArn         pulumi.StringOutput    `pulumi:"serviceArn"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-servicename
	ServiceName pulumi.StringPtrOutput `pulumi:"serviceName"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-serviceregistries
	ServiceRegistries ServiceServiceRegistryArrayOutput `pulumi:"serviceRegistries"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-tags
	Tags aws.TagArrayOutput `pulumi:"tags"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-taskdefinition
	TaskDefinition pulumi.StringPtrOutput `pulumi:"taskDefinition"`
}

// NewService registers a new resource with the given unique name, arguments, and options.
func NewService(ctx *pulumi.Context,
	name string, args *ServiceArgs, opts ...pulumi.ResourceOption) (*Service, error) {
	if args == nil {
		args = &ServiceArgs{}
	}

	var resource Service
	err := ctx.RegisterResource("aws-native:ecs:Service", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetService gets an existing Service resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetService(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ServiceState, opts ...pulumi.ResourceOption) (*Service, error) {
	var resource Service
	err := ctx.ReadResource("aws-native:ecs:Service", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Service resources.
type serviceState struct {
}

type ServiceState struct {
}

func (ServiceState) ElementType() reflect.Type {
	return reflect.TypeOf((*serviceState)(nil)).Elem()
}

type serviceArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-capacityproviderstrategy
	CapacityProviderStrategy []ServiceCapacityProviderStrategyItem `pulumi:"capacityProviderStrategy"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-cluster
	Cluster *string `pulumi:"cluster"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-deploymentconfiguration
	DeploymentConfiguration *ServiceDeploymentConfiguration `pulumi:"deploymentConfiguration"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-deploymentcontroller
	DeploymentController *ServiceDeploymentController `pulumi:"deploymentController"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-desiredcount
	DesiredCount *int `pulumi:"desiredCount"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-enableecsmanagedtags
	EnableECSManagedTags *bool `pulumi:"enableECSManagedTags"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-enableexecutecommand
	EnableExecuteCommand *bool `pulumi:"enableExecuteCommand"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-healthcheckgraceperiodseconds
	HealthCheckGracePeriodSeconds *int `pulumi:"healthCheckGracePeriodSeconds"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-launchtype
	LaunchType *string `pulumi:"launchType"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-loadbalancers
	LoadBalancers []ServiceLoadBalancer `pulumi:"loadBalancers"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-networkconfiguration
	NetworkConfiguration *ServiceNetworkConfiguration `pulumi:"networkConfiguration"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-placementconstraints
	PlacementConstraints []ServicePlacementConstraint `pulumi:"placementConstraints"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-placementstrategies
	PlacementStrategies []ServicePlacementStrategy `pulumi:"placementStrategies"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-platformversion
	PlatformVersion *string `pulumi:"platformVersion"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-propagatetags
	PropagateTags *string `pulumi:"propagateTags"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-role
	Role *string `pulumi:"role"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-schedulingstrategy
	SchedulingStrategy *string `pulumi:"schedulingStrategy"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-servicename
	ServiceName *string `pulumi:"serviceName"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-serviceregistries
	ServiceRegistries []ServiceServiceRegistry `pulumi:"serviceRegistries"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-tags
	Tags []aws.Tag `pulumi:"tags"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-taskdefinition
	TaskDefinition *string `pulumi:"taskDefinition"`
}

// The set of arguments for constructing a Service resource.
type ServiceArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-capacityproviderstrategy
	CapacityProviderStrategy ServiceCapacityProviderStrategyItemArrayInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-cluster
	Cluster pulumi.StringPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-deploymentconfiguration
	DeploymentConfiguration ServiceDeploymentConfigurationPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-deploymentcontroller
	DeploymentController ServiceDeploymentControllerPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-desiredcount
	DesiredCount pulumi.IntPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-enableecsmanagedtags
	EnableECSManagedTags pulumi.BoolPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-enableexecutecommand
	EnableExecuteCommand pulumi.BoolPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-healthcheckgraceperiodseconds
	HealthCheckGracePeriodSeconds pulumi.IntPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-launchtype
	LaunchType pulumi.StringPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-loadbalancers
	LoadBalancers ServiceLoadBalancerArrayInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-networkconfiguration
	NetworkConfiguration ServiceNetworkConfigurationPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-placementconstraints
	PlacementConstraints ServicePlacementConstraintArrayInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-placementstrategies
	PlacementStrategies ServicePlacementStrategyArrayInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-platformversion
	PlatformVersion pulumi.StringPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-propagatetags
	PropagateTags pulumi.StringPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-role
	Role pulumi.StringPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-schedulingstrategy
	SchedulingStrategy pulumi.StringPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-servicename
	ServiceName pulumi.StringPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-serviceregistries
	ServiceRegistries ServiceServiceRegistryArrayInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-tags
	Tags aws.TagArrayInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#cfn-ecs-service-taskdefinition
	TaskDefinition pulumi.StringPtrInput
}

func (ServiceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*serviceArgs)(nil)).Elem()
}

type ServiceInput interface {
	pulumi.Input

	ToServiceOutput() ServiceOutput
	ToServiceOutputWithContext(ctx context.Context) ServiceOutput
}

func (*Service) ElementType() reflect.Type {
	return reflect.TypeOf((*Service)(nil))
}

func (i *Service) ToServiceOutput() ServiceOutput {
	return i.ToServiceOutputWithContext(context.Background())
}

func (i *Service) ToServiceOutputWithContext(ctx context.Context) ServiceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ServiceOutput)
}

type ServiceOutput struct{ *pulumi.OutputState }

func (ServiceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Service)(nil))
}

func (o ServiceOutput) ToServiceOutput() ServiceOutput {
	return o
}

func (o ServiceOutput) ToServiceOutputWithContext(ctx context.Context) ServiceOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(ServiceOutput{})
}
