// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package eks

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::EKS::Nodegroup
//
// Deprecated: Nodegroup is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type Nodegroup struct {
	pulumi.CustomResourceState

	AmiType            pulumi.StringPtrOutput                        `pulumi:"amiType"`
	Arn                pulumi.StringOutput                           `pulumi:"arn"`
	CapacityType       pulumi.StringPtrOutput                        `pulumi:"capacityType"`
	ClusterName        pulumi.StringOutput                           `pulumi:"clusterName"`
	DiskSize           pulumi.Float64PtrOutput                       `pulumi:"diskSize"`
	ForceUpdateEnabled pulumi.BoolPtrOutput                          `pulumi:"forceUpdateEnabled"`
	InstanceTypes      pulumi.StringArrayOutput                      `pulumi:"instanceTypes"`
	Labels             pulumi.AnyOutput                              `pulumi:"labels"`
	LaunchTemplate     NodegroupLaunchTemplateSpecificationPtrOutput `pulumi:"launchTemplate"`
	NodeRole           pulumi.StringOutput                           `pulumi:"nodeRole"`
	NodegroupName      pulumi.StringPtrOutput                        `pulumi:"nodegroupName"`
	ReleaseVersion     pulumi.StringPtrOutput                        `pulumi:"releaseVersion"`
	RemoteAccess       NodegroupRemoteAccessPtrOutput                `pulumi:"remoteAccess"`
	ScalingConfig      NodegroupScalingConfigPtrOutput               `pulumi:"scalingConfig"`
	Subnets            pulumi.StringArrayOutput                      `pulumi:"subnets"`
	Tags               pulumi.AnyOutput                              `pulumi:"tags"`
	Taints             NodegroupTaintArrayOutput                     `pulumi:"taints"`
	UpdateConfig       NodegroupUpdateConfigPtrOutput                `pulumi:"updateConfig"`
	Version            pulumi.StringPtrOutput                        `pulumi:"version"`
}

// NewNodegroup registers a new resource with the given unique name, arguments, and options.
func NewNodegroup(ctx *pulumi.Context,
	name string, args *NodegroupArgs, opts ...pulumi.ResourceOption) (*Nodegroup, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ClusterName == nil {
		return nil, errors.New("invalid value for required argument 'ClusterName'")
	}
	if args.NodeRole == nil {
		return nil, errors.New("invalid value for required argument 'NodeRole'")
	}
	if args.Subnets == nil {
		return nil, errors.New("invalid value for required argument 'Subnets'")
	}
	var resource Nodegroup
	err := ctx.RegisterResource("aws-native:eks:Nodegroup", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetNodegroup gets an existing Nodegroup resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetNodegroup(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *NodegroupState, opts ...pulumi.ResourceOption) (*Nodegroup, error) {
	var resource Nodegroup
	err := ctx.ReadResource("aws-native:eks:Nodegroup", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Nodegroup resources.
type nodegroupState struct {
}

type NodegroupState struct {
}

func (NodegroupState) ElementType() reflect.Type {
	return reflect.TypeOf((*nodegroupState)(nil)).Elem()
}

type nodegroupArgs struct {
	AmiType            *string                               `pulumi:"amiType"`
	CapacityType       *string                               `pulumi:"capacityType"`
	ClusterName        string                                `pulumi:"clusterName"`
	DiskSize           *float64                              `pulumi:"diskSize"`
	ForceUpdateEnabled *bool                                 `pulumi:"forceUpdateEnabled"`
	InstanceTypes      []string                              `pulumi:"instanceTypes"`
	Labels             interface{}                           `pulumi:"labels"`
	LaunchTemplate     *NodegroupLaunchTemplateSpecification `pulumi:"launchTemplate"`
	NodeRole           string                                `pulumi:"nodeRole"`
	NodegroupName      *string                               `pulumi:"nodegroupName"`
	ReleaseVersion     *string                               `pulumi:"releaseVersion"`
	RemoteAccess       *NodegroupRemoteAccess                `pulumi:"remoteAccess"`
	ScalingConfig      *NodegroupScalingConfig               `pulumi:"scalingConfig"`
	Subnets            []string                              `pulumi:"subnets"`
	Tags               interface{}                           `pulumi:"tags"`
	Taints             []NodegroupTaint                      `pulumi:"taints"`
	UpdateConfig       *NodegroupUpdateConfig                `pulumi:"updateConfig"`
	Version            *string                               `pulumi:"version"`
}

// The set of arguments for constructing a Nodegroup resource.
type NodegroupArgs struct {
	AmiType            pulumi.StringPtrInput
	CapacityType       pulumi.StringPtrInput
	ClusterName        pulumi.StringInput
	DiskSize           pulumi.Float64PtrInput
	ForceUpdateEnabled pulumi.BoolPtrInput
	InstanceTypes      pulumi.StringArrayInput
	Labels             pulumi.Input
	LaunchTemplate     NodegroupLaunchTemplateSpecificationPtrInput
	NodeRole           pulumi.StringInput
	NodegroupName      pulumi.StringPtrInput
	ReleaseVersion     pulumi.StringPtrInput
	RemoteAccess       NodegroupRemoteAccessPtrInput
	ScalingConfig      NodegroupScalingConfigPtrInput
	Subnets            pulumi.StringArrayInput
	Tags               pulumi.Input
	Taints             NodegroupTaintArrayInput
	UpdateConfig       NodegroupUpdateConfigPtrInput
	Version            pulumi.StringPtrInput
}

func (NodegroupArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*nodegroupArgs)(nil)).Elem()
}

type NodegroupInput interface {
	pulumi.Input

	ToNodegroupOutput() NodegroupOutput
	ToNodegroupOutputWithContext(ctx context.Context) NodegroupOutput
}

func (*Nodegroup) ElementType() reflect.Type {
	return reflect.TypeOf((**Nodegroup)(nil)).Elem()
}

func (i *Nodegroup) ToNodegroupOutput() NodegroupOutput {
	return i.ToNodegroupOutputWithContext(context.Background())
}

func (i *Nodegroup) ToNodegroupOutputWithContext(ctx context.Context) NodegroupOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NodegroupOutput)
}

type NodegroupOutput struct{ *pulumi.OutputState }

func (NodegroupOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Nodegroup)(nil)).Elem()
}

func (o NodegroupOutput) ToNodegroupOutput() NodegroupOutput {
	return o
}

func (o NodegroupOutput) ToNodegroupOutputWithContext(ctx context.Context) NodegroupOutput {
	return o
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*NodegroupInput)(nil)).Elem(), &Nodegroup{})
	pulumi.RegisterOutputType(NodegroupOutput{})
}
