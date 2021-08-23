// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastgroupsource.html
type TransitGatewayMulticastGroupSource struct {
	pulumi.CustomResourceState

	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastgroupsource.html#cfn-ec2-transitgatewaymulticastgroupsource-groupipaddress
	GroupIpAddress pulumi.StringOutput `pulumi:"groupIpAddress"`
	GroupMember    pulumi.BoolOutput   `pulumi:"groupMember"`
	GroupSource    pulumi.BoolOutput   `pulumi:"groupSource"`
	MemberType     pulumi.StringOutput `pulumi:"memberType"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastgroupsource.html#cfn-ec2-transitgatewaymulticastgroupsource-networkinterfaceid
	NetworkInterfaceId         pulumi.StringOutput `pulumi:"networkInterfaceId"`
	ResourceId                 pulumi.StringOutput `pulumi:"resourceId"`
	ResourceType               pulumi.StringOutput `pulumi:"resourceType"`
	SourceType                 pulumi.StringOutput `pulumi:"sourceType"`
	SubnetId                   pulumi.StringOutput `pulumi:"subnetId"`
	TransitGatewayAttachmentId pulumi.StringOutput `pulumi:"transitGatewayAttachmentId"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastgroupsource.html#cfn-ec2-transitgatewaymulticastgroupsource-transitgatewaymulticastdomainid
	TransitGatewayMulticastDomainId pulumi.StringOutput `pulumi:"transitGatewayMulticastDomainId"`
}

// NewTransitGatewayMulticastGroupSource registers a new resource with the given unique name, arguments, and options.
func NewTransitGatewayMulticastGroupSource(ctx *pulumi.Context,
	name string, args *TransitGatewayMulticastGroupSourceArgs, opts ...pulumi.ResourceOption) (*TransitGatewayMulticastGroupSource, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.GroupIpAddress == nil {
		return nil, errors.New("invalid value for required argument 'GroupIpAddress'")
	}
	if args.NetworkInterfaceId == nil {
		return nil, errors.New("invalid value for required argument 'NetworkInterfaceId'")
	}
	if args.TransitGatewayMulticastDomainId == nil {
		return nil, errors.New("invalid value for required argument 'TransitGatewayMulticastDomainId'")
	}
	var resource TransitGatewayMulticastGroupSource
	err := ctx.RegisterResource("aws-native:ec2:TransitGatewayMulticastGroupSource", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetTransitGatewayMulticastGroupSource gets an existing TransitGatewayMulticastGroupSource resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTransitGatewayMulticastGroupSource(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *TransitGatewayMulticastGroupSourceState, opts ...pulumi.ResourceOption) (*TransitGatewayMulticastGroupSource, error) {
	var resource TransitGatewayMulticastGroupSource
	err := ctx.ReadResource("aws-native:ec2:TransitGatewayMulticastGroupSource", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering TransitGatewayMulticastGroupSource resources.
type transitGatewayMulticastGroupSourceState struct {
}

type TransitGatewayMulticastGroupSourceState struct {
}

func (TransitGatewayMulticastGroupSourceState) ElementType() reflect.Type {
	return reflect.TypeOf((*transitGatewayMulticastGroupSourceState)(nil)).Elem()
}

type transitGatewayMulticastGroupSourceArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastgroupsource.html#cfn-ec2-transitgatewaymulticastgroupsource-groupipaddress
	GroupIpAddress string `pulumi:"groupIpAddress"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastgroupsource.html#cfn-ec2-transitgatewaymulticastgroupsource-networkinterfaceid
	NetworkInterfaceId string `pulumi:"networkInterfaceId"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastgroupsource.html#cfn-ec2-transitgatewaymulticastgroupsource-transitgatewaymulticastdomainid
	TransitGatewayMulticastDomainId string `pulumi:"transitGatewayMulticastDomainId"`
}

// The set of arguments for constructing a TransitGatewayMulticastGroupSource resource.
type TransitGatewayMulticastGroupSourceArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastgroupsource.html#cfn-ec2-transitgatewaymulticastgroupsource-groupipaddress
	GroupIpAddress pulumi.StringInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastgroupsource.html#cfn-ec2-transitgatewaymulticastgroupsource-networkinterfaceid
	NetworkInterfaceId pulumi.StringInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewaymulticastgroupsource.html#cfn-ec2-transitgatewaymulticastgroupsource-transitgatewaymulticastdomainid
	TransitGatewayMulticastDomainId pulumi.StringInput
}

func (TransitGatewayMulticastGroupSourceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*transitGatewayMulticastGroupSourceArgs)(nil)).Elem()
}

type TransitGatewayMulticastGroupSourceInput interface {
	pulumi.Input

	ToTransitGatewayMulticastGroupSourceOutput() TransitGatewayMulticastGroupSourceOutput
	ToTransitGatewayMulticastGroupSourceOutputWithContext(ctx context.Context) TransitGatewayMulticastGroupSourceOutput
}

func (*TransitGatewayMulticastGroupSource) ElementType() reflect.Type {
	return reflect.TypeOf((*TransitGatewayMulticastGroupSource)(nil))
}

func (i *TransitGatewayMulticastGroupSource) ToTransitGatewayMulticastGroupSourceOutput() TransitGatewayMulticastGroupSourceOutput {
	return i.ToTransitGatewayMulticastGroupSourceOutputWithContext(context.Background())
}

func (i *TransitGatewayMulticastGroupSource) ToTransitGatewayMulticastGroupSourceOutputWithContext(ctx context.Context) TransitGatewayMulticastGroupSourceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TransitGatewayMulticastGroupSourceOutput)
}

type TransitGatewayMulticastGroupSourceOutput struct{ *pulumi.OutputState }

func (TransitGatewayMulticastGroupSourceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*TransitGatewayMulticastGroupSource)(nil))
}

func (o TransitGatewayMulticastGroupSourceOutput) ToTransitGatewayMulticastGroupSourceOutput() TransitGatewayMulticastGroupSourceOutput {
	return o
}

func (o TransitGatewayMulticastGroupSourceOutput) ToTransitGatewayMulticastGroupSourceOutputWithContext(ctx context.Context) TransitGatewayMulticastGroupSourceOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(TransitGatewayMulticastGroupSourceOutput{})
}
