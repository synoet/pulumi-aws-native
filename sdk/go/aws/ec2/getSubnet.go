// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::EC2::Subnet
func LookupSubnet(ctx *pulumi.Context, args *LookupSubnetArgs, opts ...pulumi.InvokeOption) (*LookupSubnetResult, error) {
	var rv LookupSubnetResult
	err := ctx.Invoke("aws-native:ec2:getSubnet", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupSubnetArgs struct {
	SubnetId string `pulumi:"subnetId"`
}

type LookupSubnetResult struct {
	AssignIpv6AddressOnCreation   *bool                                    `pulumi:"assignIpv6AddressOnCreation"`
	EnableDns64                   *bool                                    `pulumi:"enableDns64"`
	Ipv6CidrBlock                 *string                                  `pulumi:"ipv6CidrBlock"`
	Ipv6CidrBlocks                []string                                 `pulumi:"ipv6CidrBlocks"`
	MapPublicIpOnLaunch           *bool                                    `pulumi:"mapPublicIpOnLaunch"`
	NetworkAclAssociationId       *string                                  `pulumi:"networkAclAssociationId"`
	PrivateDnsNameOptionsOnLaunch *PrivateDnsNameOptionsOnLaunchProperties `pulumi:"privateDnsNameOptionsOnLaunch"`
	SubnetId                      *string                                  `pulumi:"subnetId"`
	Tags                          []SubnetTag                              `pulumi:"tags"`
}

func LookupSubnetOutput(ctx *pulumi.Context, args LookupSubnetOutputArgs, opts ...pulumi.InvokeOption) LookupSubnetResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupSubnetResult, error) {
			args := v.(LookupSubnetArgs)
			r, err := LookupSubnet(ctx, &args, opts...)
			var s LookupSubnetResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupSubnetResultOutput)
}

type LookupSubnetOutputArgs struct {
	SubnetId pulumi.StringInput `pulumi:"subnetId"`
}

func (LookupSubnetOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSubnetArgs)(nil)).Elem()
}

type LookupSubnetResultOutput struct{ *pulumi.OutputState }

func (LookupSubnetResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSubnetResult)(nil)).Elem()
}

func (o LookupSubnetResultOutput) ToLookupSubnetResultOutput() LookupSubnetResultOutput {
	return o
}

func (o LookupSubnetResultOutput) ToLookupSubnetResultOutputWithContext(ctx context.Context) LookupSubnetResultOutput {
	return o
}

func (o LookupSubnetResultOutput) AssignIpv6AddressOnCreation() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupSubnetResult) *bool { return v.AssignIpv6AddressOnCreation }).(pulumi.BoolPtrOutput)
}

func (o LookupSubnetResultOutput) EnableDns64() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupSubnetResult) *bool { return v.EnableDns64 }).(pulumi.BoolPtrOutput)
}

func (o LookupSubnetResultOutput) Ipv6CidrBlock() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSubnetResult) *string { return v.Ipv6CidrBlock }).(pulumi.StringPtrOutput)
}

func (o LookupSubnetResultOutput) Ipv6CidrBlocks() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupSubnetResult) []string { return v.Ipv6CidrBlocks }).(pulumi.StringArrayOutput)
}

func (o LookupSubnetResultOutput) MapPublicIpOnLaunch() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupSubnetResult) *bool { return v.MapPublicIpOnLaunch }).(pulumi.BoolPtrOutput)
}

func (o LookupSubnetResultOutput) NetworkAclAssociationId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSubnetResult) *string { return v.NetworkAclAssociationId }).(pulumi.StringPtrOutput)
}

func (o LookupSubnetResultOutput) PrivateDnsNameOptionsOnLaunch() PrivateDnsNameOptionsOnLaunchPropertiesPtrOutput {
	return o.ApplyT(func(v LookupSubnetResult) *PrivateDnsNameOptionsOnLaunchProperties {
		return v.PrivateDnsNameOptionsOnLaunch
	}).(PrivateDnsNameOptionsOnLaunchPropertiesPtrOutput)
}

func (o LookupSubnetResultOutput) SubnetId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSubnetResult) *string { return v.SubnetId }).(pulumi.StringPtrOutput)
}

func (o LookupSubnetResultOutput) Tags() SubnetTagArrayOutput {
	return o.ApplyT(func(v LookupSubnetResult) []SubnetTag { return v.Tags }).(SubnetTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupSubnetResultOutput{})
}
