// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ecs

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::ECS::Service
type Service struct {
	pulumi.CustomResourceState

	CapacityProviderStrategy      ServiceCapacityProviderStrategyItemArrayOutput `pulumi:"capacityProviderStrategy"`
	Cluster                       pulumi.StringPtrOutput                         `pulumi:"cluster"`
	DeploymentConfiguration       ServiceDeploymentConfigurationPtrOutput        `pulumi:"deploymentConfiguration"`
	DeploymentController          ServiceDeploymentControllerPtrOutput           `pulumi:"deploymentController"`
	DesiredCount                  pulumi.IntPtrOutput                            `pulumi:"desiredCount"`
	EnableECSManagedTags          pulumi.BoolPtrOutput                           `pulumi:"enableECSManagedTags"`
	EnableExecuteCommand          pulumi.BoolPtrOutput                           `pulumi:"enableExecuteCommand"`
	HealthCheckGracePeriodSeconds pulumi.IntPtrOutput                            `pulumi:"healthCheckGracePeriodSeconds"`
	LaunchType                    ServiceLaunchTypePtrOutput                     `pulumi:"launchType"`
	LoadBalancers                 ServiceLoadBalancerArrayOutput                 `pulumi:"loadBalancers"`
	Name                          pulumi.StringOutput                            `pulumi:"name"`
	NetworkConfiguration          ServiceNetworkConfigurationPtrOutput           `pulumi:"networkConfiguration"`
	PlacementConstraints          ServicePlacementConstraintArrayOutput          `pulumi:"placementConstraints"`
	PlacementStrategies           ServicePlacementStrategyArrayOutput            `pulumi:"placementStrategies"`
	PlatformVersion               pulumi.StringPtrOutput                         `pulumi:"platformVersion"`
	PropagateTags                 ServicePropagateTagsPtrOutput                  `pulumi:"propagateTags"`
	Role                          pulumi.StringPtrOutput                         `pulumi:"role"`
	SchedulingStrategy            ServiceSchedulingStrategyPtrOutput             `pulumi:"schedulingStrategy"`
	ServiceArn                    pulumi.StringOutput                            `pulumi:"serviceArn"`
	ServiceName                   pulumi.StringPtrOutput                         `pulumi:"serviceName"`
	ServiceRegistries             ServiceRegistryArrayOutput                     `pulumi:"serviceRegistries"`
	Tags                          ServiceTagArrayOutput                          `pulumi:"tags"`
	TaskDefinition                pulumi.StringPtrOutput                         `pulumi:"taskDefinition"`
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
	CapacityProviderStrategy      []ServiceCapacityProviderStrategyItem `pulumi:"capacityProviderStrategy"`
	Cluster                       *string                               `pulumi:"cluster"`
	DeploymentConfiguration       *ServiceDeploymentConfiguration       `pulumi:"deploymentConfiguration"`
	DeploymentController          *ServiceDeploymentController          `pulumi:"deploymentController"`
	DesiredCount                  *int                                  `pulumi:"desiredCount"`
	EnableECSManagedTags          *bool                                 `pulumi:"enableECSManagedTags"`
	EnableExecuteCommand          *bool                                 `pulumi:"enableExecuteCommand"`
	HealthCheckGracePeriodSeconds *int                                  `pulumi:"healthCheckGracePeriodSeconds"`
	LaunchType                    *ServiceLaunchType                    `pulumi:"launchType"`
	LoadBalancers                 []ServiceLoadBalancer                 `pulumi:"loadBalancers"`
	NetworkConfiguration          *ServiceNetworkConfiguration          `pulumi:"networkConfiguration"`
	PlacementConstraints          []ServicePlacementConstraint          `pulumi:"placementConstraints"`
	PlacementStrategies           []ServicePlacementStrategy            `pulumi:"placementStrategies"`
	PlatformVersion               *string                               `pulumi:"platformVersion"`
	PropagateTags                 *ServicePropagateTags                 `pulumi:"propagateTags"`
	Role                          *string                               `pulumi:"role"`
	SchedulingStrategy            *ServiceSchedulingStrategy            `pulumi:"schedulingStrategy"`
	ServiceName                   *string                               `pulumi:"serviceName"`
	ServiceRegistries             []ServiceRegistry                     `pulumi:"serviceRegistries"`
	Tags                          []ServiceTag                          `pulumi:"tags"`
	TaskDefinition                *string                               `pulumi:"taskDefinition"`
}

// The set of arguments for constructing a Service resource.
type ServiceArgs struct {
	CapacityProviderStrategy      ServiceCapacityProviderStrategyItemArrayInput
	Cluster                       pulumi.StringPtrInput
	DeploymentConfiguration       ServiceDeploymentConfigurationPtrInput
	DeploymentController          ServiceDeploymentControllerPtrInput
	DesiredCount                  pulumi.IntPtrInput
	EnableECSManagedTags          pulumi.BoolPtrInput
	EnableExecuteCommand          pulumi.BoolPtrInput
	HealthCheckGracePeriodSeconds pulumi.IntPtrInput
	LaunchType                    ServiceLaunchTypePtrInput
	LoadBalancers                 ServiceLoadBalancerArrayInput
	NetworkConfiguration          ServiceNetworkConfigurationPtrInput
	PlacementConstraints          ServicePlacementConstraintArrayInput
	PlacementStrategies           ServicePlacementStrategyArrayInput
	PlatformVersion               pulumi.StringPtrInput
	PropagateTags                 ServicePropagateTagsPtrInput
	Role                          pulumi.StringPtrInput
	SchedulingStrategy            ServiceSchedulingStrategyPtrInput
	ServiceName                   pulumi.StringPtrInput
	ServiceRegistries             ServiceRegistryArrayInput
	Tags                          ServiceTagArrayInput
	TaskDefinition                pulumi.StringPtrInput
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
