// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ecs

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Create an Elastic Container Service (ECS) cluster.
type Cluster struct {
	pulumi.CustomResourceState

	// The Amazon Resource Name (ARN) of the Amazon ECS cluster, such as arn:aws:ecs:us-east-2:123456789012:cluster/MyECSCluster.
	Arn               pulumi.StringOutput      `pulumi:"arn"`
	CapacityProviders pulumi.StringArrayOutput `pulumi:"capacityProviders"`
	// A user-generated string that you use to identify your cluster. If you don't specify a name, AWS CloudFormation generates a unique physical ID for the name.
	ClusterName                     pulumi.StringPtrOutput                         `pulumi:"clusterName"`
	ClusterSettings                 ClusterSettingsArrayOutput                     `pulumi:"clusterSettings"`
	Configuration                   ClusterConfigurationPtrOutput                  `pulumi:"configuration"`
	DefaultCapacityProviderStrategy ClusterCapacityProviderStrategyItemArrayOutput `pulumi:"defaultCapacityProviderStrategy"`
	Tags                            ClusterTagArrayOutput                          `pulumi:"tags"`
}

// NewCluster registers a new resource with the given unique name, arguments, and options.
func NewCluster(ctx *pulumi.Context,
	name string, args *ClusterArgs, opts ...pulumi.ResourceOption) (*Cluster, error) {
	if args == nil {
		args = &ClusterArgs{}
	}

	var resource Cluster
	err := ctx.RegisterResource("aws-native:ecs:Cluster", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCluster gets an existing Cluster resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCluster(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ClusterState, opts ...pulumi.ResourceOption) (*Cluster, error) {
	var resource Cluster
	err := ctx.ReadResource("aws-native:ecs:Cluster", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Cluster resources.
type clusterState struct {
}

type ClusterState struct {
}

func (ClusterState) ElementType() reflect.Type {
	return reflect.TypeOf((*clusterState)(nil)).Elem()
}

type clusterArgs struct {
	CapacityProviders []string `pulumi:"capacityProviders"`
	// A user-generated string that you use to identify your cluster. If you don't specify a name, AWS CloudFormation generates a unique physical ID for the name.
	ClusterName                     *string                               `pulumi:"clusterName"`
	ClusterSettings                 []ClusterSettings                     `pulumi:"clusterSettings"`
	Configuration                   *ClusterConfiguration                 `pulumi:"configuration"`
	DefaultCapacityProviderStrategy []ClusterCapacityProviderStrategyItem `pulumi:"defaultCapacityProviderStrategy"`
	Tags                            []ClusterTag                          `pulumi:"tags"`
}

// The set of arguments for constructing a Cluster resource.
type ClusterArgs struct {
	CapacityProviders pulumi.StringArrayInput
	// A user-generated string that you use to identify your cluster. If you don't specify a name, AWS CloudFormation generates a unique physical ID for the name.
	ClusterName                     pulumi.StringPtrInput
	ClusterSettings                 ClusterSettingsArrayInput
	Configuration                   ClusterConfigurationPtrInput
	DefaultCapacityProviderStrategy ClusterCapacityProviderStrategyItemArrayInput
	Tags                            ClusterTagArrayInput
}

func (ClusterArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*clusterArgs)(nil)).Elem()
}

type ClusterInput interface {
	pulumi.Input

	ToClusterOutput() ClusterOutput
	ToClusterOutputWithContext(ctx context.Context) ClusterOutput
}

func (*Cluster) ElementType() reflect.Type {
	return reflect.TypeOf((**Cluster)(nil)).Elem()
}

func (i *Cluster) ToClusterOutput() ClusterOutput {
	return i.ToClusterOutputWithContext(context.Background())
}

func (i *Cluster) ToClusterOutputWithContext(ctx context.Context) ClusterOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ClusterOutput)
}

type ClusterOutput struct{ *pulumi.OutputState }

func (ClusterOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Cluster)(nil)).Elem()
}

func (o ClusterOutput) ToClusterOutput() ClusterOutput {
	return o
}

func (o ClusterOutput) ToClusterOutputWithContext(ctx context.Context) ClusterOutput {
	return o
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ClusterInput)(nil)).Elem(), &Cluster{})
	pulumi.RegisterOutputType(ClusterOutput{})
}
