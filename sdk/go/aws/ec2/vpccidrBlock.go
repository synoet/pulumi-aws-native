// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::EC2::VPCCidrBlock
//
// Deprecated: VPCCidrBlock is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type VPCCidrBlock struct {
	pulumi.CustomResourceState

	AmazonProvidedIpv6CidrBlock pulumi.BoolPtrOutput   `pulumi:"amazonProvidedIpv6CidrBlock"`
	CidrBlock                   pulumi.StringPtrOutput `pulumi:"cidrBlock"`
	Ipv4IpamPoolId              pulumi.StringPtrOutput `pulumi:"ipv4IpamPoolId"`
	Ipv4NetmaskLength           pulumi.IntPtrOutput    `pulumi:"ipv4NetmaskLength"`
	Ipv6CidrBlock               pulumi.StringPtrOutput `pulumi:"ipv6CidrBlock"`
	Ipv6IpamPoolId              pulumi.StringPtrOutput `pulumi:"ipv6IpamPoolId"`
	Ipv6NetmaskLength           pulumi.IntPtrOutput    `pulumi:"ipv6NetmaskLength"`
	Ipv6Pool                    pulumi.StringPtrOutput `pulumi:"ipv6Pool"`
	VpcId                       pulumi.StringOutput    `pulumi:"vpcId"`
}

// NewVPCCidrBlock registers a new resource with the given unique name, arguments, and options.
func NewVPCCidrBlock(ctx *pulumi.Context,
	name string, args *VPCCidrBlockArgs, opts ...pulumi.ResourceOption) (*VPCCidrBlock, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.VpcId == nil {
		return nil, errors.New("invalid value for required argument 'VpcId'")
	}
	var resource VPCCidrBlock
	err := ctx.RegisterResource("aws-native:ec2:VPCCidrBlock", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetVPCCidrBlock gets an existing VPCCidrBlock resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetVPCCidrBlock(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *VPCCidrBlockState, opts ...pulumi.ResourceOption) (*VPCCidrBlock, error) {
	var resource VPCCidrBlock
	err := ctx.ReadResource("aws-native:ec2:VPCCidrBlock", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering VPCCidrBlock resources.
type vpccidrBlockState struct {
}

type VPCCidrBlockState struct {
}

func (VPCCidrBlockState) ElementType() reflect.Type {
	return reflect.TypeOf((*vpccidrBlockState)(nil)).Elem()
}

type vpccidrBlockArgs struct {
	AmazonProvidedIpv6CidrBlock *bool   `pulumi:"amazonProvidedIpv6CidrBlock"`
	CidrBlock                   *string `pulumi:"cidrBlock"`
	Ipv4IpamPoolId              *string `pulumi:"ipv4IpamPoolId"`
	Ipv4NetmaskLength           *int    `pulumi:"ipv4NetmaskLength"`
	Ipv6CidrBlock               *string `pulumi:"ipv6CidrBlock"`
	Ipv6IpamPoolId              *string `pulumi:"ipv6IpamPoolId"`
	Ipv6NetmaskLength           *int    `pulumi:"ipv6NetmaskLength"`
	Ipv6Pool                    *string `pulumi:"ipv6Pool"`
	VpcId                       string  `pulumi:"vpcId"`
}

// The set of arguments for constructing a VPCCidrBlock resource.
type VPCCidrBlockArgs struct {
	AmazonProvidedIpv6CidrBlock pulumi.BoolPtrInput
	CidrBlock                   pulumi.StringPtrInput
	Ipv4IpamPoolId              pulumi.StringPtrInput
	Ipv4NetmaskLength           pulumi.IntPtrInput
	Ipv6CidrBlock               pulumi.StringPtrInput
	Ipv6IpamPoolId              pulumi.StringPtrInput
	Ipv6NetmaskLength           pulumi.IntPtrInput
	Ipv6Pool                    pulumi.StringPtrInput
	VpcId                       pulumi.StringInput
}

func (VPCCidrBlockArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*vpccidrBlockArgs)(nil)).Elem()
}

type VPCCidrBlockInput interface {
	pulumi.Input

	ToVPCCidrBlockOutput() VPCCidrBlockOutput
	ToVPCCidrBlockOutputWithContext(ctx context.Context) VPCCidrBlockOutput
}

func (*VPCCidrBlock) ElementType() reflect.Type {
	return reflect.TypeOf((**VPCCidrBlock)(nil)).Elem()
}

func (i *VPCCidrBlock) ToVPCCidrBlockOutput() VPCCidrBlockOutput {
	return i.ToVPCCidrBlockOutputWithContext(context.Background())
}

func (i *VPCCidrBlock) ToVPCCidrBlockOutputWithContext(ctx context.Context) VPCCidrBlockOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VPCCidrBlockOutput)
}

type VPCCidrBlockOutput struct{ *pulumi.OutputState }

func (VPCCidrBlockOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**VPCCidrBlock)(nil)).Elem()
}

func (o VPCCidrBlockOutput) ToVPCCidrBlockOutput() VPCCidrBlockOutput {
	return o
}

func (o VPCCidrBlockOutput) ToVPCCidrBlockOutputWithContext(ctx context.Context) VPCCidrBlockOutput {
	return o
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*VPCCidrBlockInput)(nil)).Elem(), &VPCCidrBlock{})
	pulumi.RegisterOutputType(VPCCidrBlockOutput{})
}
