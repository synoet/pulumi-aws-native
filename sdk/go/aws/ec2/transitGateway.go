// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html
type TransitGateway struct {
	pulumi.CustomResourceState

	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-amazonsideasn
	AmazonSideAsn pulumi.IntPtrOutput `pulumi:"amazonSideAsn"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-associationdefaultroutetableid
	AssociationDefaultRouteTableId pulumi.StringPtrOutput `pulumi:"associationDefaultRouteTableId"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-autoacceptsharedattachments
	AutoAcceptSharedAttachments pulumi.StringPtrOutput `pulumi:"autoAcceptSharedAttachments"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-defaultroutetableassociation
	DefaultRouteTableAssociation pulumi.StringPtrOutput `pulumi:"defaultRouteTableAssociation"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-defaultroutetablepropagation
	DefaultRouteTablePropagation pulumi.StringPtrOutput `pulumi:"defaultRouteTablePropagation"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-description
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-dnssupport
	DnsSupport pulumi.StringPtrOutput `pulumi:"dnsSupport"`
	Id         pulumi.StringOutput    `pulumi:"id"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-multicastsupport
	MulticastSupport pulumi.StringPtrOutput `pulumi:"multicastSupport"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-propagationdefaultroutetableid
	PropagationDefaultRouteTableId pulumi.StringPtrOutput `pulumi:"propagationDefaultRouteTableId"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-tags
	Tags aws.TagArrayOutput `pulumi:"tags"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-transitgatewaycidrblocks
	TransitGatewayCidrBlocks pulumi.StringArrayOutput `pulumi:"transitGatewayCidrBlocks"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-vpnecmpsupport
	VpnEcmpSupport pulumi.StringPtrOutput `pulumi:"vpnEcmpSupport"`
}

// NewTransitGateway registers a new resource with the given unique name, arguments, and options.
func NewTransitGateway(ctx *pulumi.Context,
	name string, args *TransitGatewayArgs, opts ...pulumi.ResourceOption) (*TransitGateway, error) {
	if args == nil {
		args = &TransitGatewayArgs{}
	}

	var resource TransitGateway
	err := ctx.RegisterResource("aws-native:ec2:TransitGateway", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetTransitGateway gets an existing TransitGateway resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTransitGateway(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *TransitGatewayState, opts ...pulumi.ResourceOption) (*TransitGateway, error) {
	var resource TransitGateway
	err := ctx.ReadResource("aws-native:ec2:TransitGateway", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering TransitGateway resources.
type transitGatewayState struct {
}

type TransitGatewayState struct {
}

func (TransitGatewayState) ElementType() reflect.Type {
	return reflect.TypeOf((*transitGatewayState)(nil)).Elem()
}

type transitGatewayArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-amazonsideasn
	AmazonSideAsn *int `pulumi:"amazonSideAsn"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-associationdefaultroutetableid
	AssociationDefaultRouteTableId *string `pulumi:"associationDefaultRouteTableId"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-autoacceptsharedattachments
	AutoAcceptSharedAttachments *string `pulumi:"autoAcceptSharedAttachments"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-defaultroutetableassociation
	DefaultRouteTableAssociation *string `pulumi:"defaultRouteTableAssociation"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-defaultroutetablepropagation
	DefaultRouteTablePropagation *string `pulumi:"defaultRouteTablePropagation"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-description
	Description *string `pulumi:"description"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-dnssupport
	DnsSupport *string `pulumi:"dnsSupport"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-multicastsupport
	MulticastSupport *string `pulumi:"multicastSupport"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-propagationdefaultroutetableid
	PropagationDefaultRouteTableId *string `pulumi:"propagationDefaultRouteTableId"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-tags
	Tags []aws.Tag `pulumi:"tags"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-transitgatewaycidrblocks
	TransitGatewayCidrBlocks []string `pulumi:"transitGatewayCidrBlocks"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-vpnecmpsupport
	VpnEcmpSupport *string `pulumi:"vpnEcmpSupport"`
}

// The set of arguments for constructing a TransitGateway resource.
type TransitGatewayArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-amazonsideasn
	AmazonSideAsn pulumi.IntPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-associationdefaultroutetableid
	AssociationDefaultRouteTableId pulumi.StringPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-autoacceptsharedattachments
	AutoAcceptSharedAttachments pulumi.StringPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-defaultroutetableassociation
	DefaultRouteTableAssociation pulumi.StringPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-defaultroutetablepropagation
	DefaultRouteTablePropagation pulumi.StringPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-description
	Description pulumi.StringPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-dnssupport
	DnsSupport pulumi.StringPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-multicastsupport
	MulticastSupport pulumi.StringPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-propagationdefaultroutetableid
	PropagationDefaultRouteTableId pulumi.StringPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-tags
	Tags aws.TagArrayInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-transitgatewaycidrblocks
	TransitGatewayCidrBlocks pulumi.StringArrayInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-vpnecmpsupport
	VpnEcmpSupport pulumi.StringPtrInput
}

func (TransitGatewayArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*transitGatewayArgs)(nil)).Elem()
}

type TransitGatewayInput interface {
	pulumi.Input

	ToTransitGatewayOutput() TransitGatewayOutput
	ToTransitGatewayOutputWithContext(ctx context.Context) TransitGatewayOutput
}

func (*TransitGateway) ElementType() reflect.Type {
	return reflect.TypeOf((*TransitGateway)(nil))
}

func (i *TransitGateway) ToTransitGatewayOutput() TransitGatewayOutput {
	return i.ToTransitGatewayOutputWithContext(context.Background())
}

func (i *TransitGateway) ToTransitGatewayOutputWithContext(ctx context.Context) TransitGatewayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TransitGatewayOutput)
}

type TransitGatewayOutput struct{ *pulumi.OutputState }

func (TransitGatewayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*TransitGateway)(nil))
}

func (o TransitGatewayOutput) ToTransitGatewayOutput() TransitGatewayOutput {
	return o
}

func (o TransitGatewayOutput) ToTransitGatewayOutputWithContext(ctx context.Context) TransitGatewayOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(TransitGatewayOutput{})
}
