// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The AWS::EC2::SubnetCidrBlock resource creates association between subnet and IPv6 CIDR
type SubnetCidrBlock struct {
	pulumi.CustomResourceState

	// The IPv6 network range for the subnet, in CIDR notation. The subnet size must use a /64 prefix length
	Ipv6CidrBlock pulumi.StringOutput `pulumi:"ipv6CidrBlock"`
	// The ID of the subnet
	SubnetId pulumi.StringOutput `pulumi:"subnetId"`
}

// NewSubnetCidrBlock registers a new resource with the given unique name, arguments, and options.
func NewSubnetCidrBlock(ctx *pulumi.Context,
	name string, args *SubnetCidrBlockArgs, opts ...pulumi.ResourceOption) (*SubnetCidrBlock, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Ipv6CidrBlock == nil {
		return nil, errors.New("invalid value for required argument 'Ipv6CidrBlock'")
	}
	if args.SubnetId == nil {
		return nil, errors.New("invalid value for required argument 'SubnetId'")
	}
	var resource SubnetCidrBlock
	err := ctx.RegisterResource("aws-native:ec2:SubnetCidrBlock", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSubnetCidrBlock gets an existing SubnetCidrBlock resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSubnetCidrBlock(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SubnetCidrBlockState, opts ...pulumi.ResourceOption) (*SubnetCidrBlock, error) {
	var resource SubnetCidrBlock
	err := ctx.ReadResource("aws-native:ec2:SubnetCidrBlock", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SubnetCidrBlock resources.
type subnetCidrBlockState struct {
}

type SubnetCidrBlockState struct {
}

func (SubnetCidrBlockState) ElementType() reflect.Type {
	return reflect.TypeOf((*subnetCidrBlockState)(nil)).Elem()
}

type subnetCidrBlockArgs struct {
	// The IPv6 network range for the subnet, in CIDR notation. The subnet size must use a /64 prefix length
	Ipv6CidrBlock string `pulumi:"ipv6CidrBlock"`
	// The ID of the subnet
	SubnetId string `pulumi:"subnetId"`
}

// The set of arguments for constructing a SubnetCidrBlock resource.
type SubnetCidrBlockArgs struct {
	// The IPv6 network range for the subnet, in CIDR notation. The subnet size must use a /64 prefix length
	Ipv6CidrBlock pulumi.StringInput
	// The ID of the subnet
	SubnetId pulumi.StringInput
}

func (SubnetCidrBlockArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*subnetCidrBlockArgs)(nil)).Elem()
}

type SubnetCidrBlockInput interface {
	pulumi.Input

	ToSubnetCidrBlockOutput() SubnetCidrBlockOutput
	ToSubnetCidrBlockOutputWithContext(ctx context.Context) SubnetCidrBlockOutput
}

func (*SubnetCidrBlock) ElementType() reflect.Type {
	return reflect.TypeOf((**SubnetCidrBlock)(nil)).Elem()
}

func (i *SubnetCidrBlock) ToSubnetCidrBlockOutput() SubnetCidrBlockOutput {
	return i.ToSubnetCidrBlockOutputWithContext(context.Background())
}

func (i *SubnetCidrBlock) ToSubnetCidrBlockOutputWithContext(ctx context.Context) SubnetCidrBlockOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SubnetCidrBlockOutput)
}

type SubnetCidrBlockOutput struct{ *pulumi.OutputState }

func (SubnetCidrBlockOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**SubnetCidrBlock)(nil)).Elem()
}

func (o SubnetCidrBlockOutput) ToSubnetCidrBlockOutput() SubnetCidrBlockOutput {
	return o
}

func (o SubnetCidrBlockOutput) ToSubnetCidrBlockOutputWithContext(ctx context.Context) SubnetCidrBlockOutput {
	return o
}

// The IPv6 network range for the subnet, in CIDR notation. The subnet size must use a /64 prefix length
func (o SubnetCidrBlockOutput) Ipv6CidrBlock() pulumi.StringOutput {
	return o.ApplyT(func(v *SubnetCidrBlock) pulumi.StringOutput { return v.Ipv6CidrBlock }).(pulumi.StringOutput)
}

// The ID of the subnet
func (o SubnetCidrBlockOutput) SubnetId() pulumi.StringOutput {
	return o.ApplyT(func(v *SubnetCidrBlock) pulumi.StringOutput { return v.SubnetId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*SubnetCidrBlockInput)(nil)).Elem(), &SubnetCidrBlock{})
	pulumi.RegisterOutputType(SubnetCidrBlockOutput{})
}
