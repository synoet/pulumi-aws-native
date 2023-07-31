// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package route53resolver

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::Route53Resolver::ResolverEndpoint
func LookupResolverEndpoint(ctx *pulumi.Context, args *LookupResolverEndpointArgs, opts ...pulumi.InvokeOption) (*LookupResolverEndpointResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupResolverEndpointResult
	err := ctx.Invoke("aws-native:route53resolver:getResolverEndpoint", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupResolverEndpointArgs struct {
	ResolverEndpointId string `pulumi:"resolverEndpointId"`
}

type LookupResolverEndpointResult struct {
	Arn                  *string                            `pulumi:"arn"`
	HostVpcId            *string                            `pulumi:"hostVpcId"`
	IpAddressCount       *string                            `pulumi:"ipAddressCount"`
	IpAddresses          []ResolverEndpointIpAddressRequest `pulumi:"ipAddresses"`
	Name                 *string                            `pulumi:"name"`
	ResolverEndpointId   *string                            `pulumi:"resolverEndpointId"`
	ResolverEndpointType *string                            `pulumi:"resolverEndpointType"`
	Tags                 []ResolverEndpointTag              `pulumi:"tags"`
}

func LookupResolverEndpointOutput(ctx *pulumi.Context, args LookupResolverEndpointOutputArgs, opts ...pulumi.InvokeOption) LookupResolverEndpointResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupResolverEndpointResult, error) {
			args := v.(LookupResolverEndpointArgs)
			r, err := LookupResolverEndpoint(ctx, &args, opts...)
			var s LookupResolverEndpointResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupResolverEndpointResultOutput)
}

type LookupResolverEndpointOutputArgs struct {
	ResolverEndpointId pulumi.StringInput `pulumi:"resolverEndpointId"`
}

func (LookupResolverEndpointOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupResolverEndpointArgs)(nil)).Elem()
}

type LookupResolverEndpointResultOutput struct{ *pulumi.OutputState }

func (LookupResolverEndpointResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupResolverEndpointResult)(nil)).Elem()
}

func (o LookupResolverEndpointResultOutput) ToLookupResolverEndpointResultOutput() LookupResolverEndpointResultOutput {
	return o
}

func (o LookupResolverEndpointResultOutput) ToLookupResolverEndpointResultOutputWithContext(ctx context.Context) LookupResolverEndpointResultOutput {
	return o
}

func (o LookupResolverEndpointResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupResolverEndpointResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

func (o LookupResolverEndpointResultOutput) HostVpcId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupResolverEndpointResult) *string { return v.HostVpcId }).(pulumi.StringPtrOutput)
}

func (o LookupResolverEndpointResultOutput) IpAddressCount() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupResolverEndpointResult) *string { return v.IpAddressCount }).(pulumi.StringPtrOutput)
}

func (o LookupResolverEndpointResultOutput) IpAddresses() ResolverEndpointIpAddressRequestArrayOutput {
	return o.ApplyT(func(v LookupResolverEndpointResult) []ResolverEndpointIpAddressRequest { return v.IpAddresses }).(ResolverEndpointIpAddressRequestArrayOutput)
}

func (o LookupResolverEndpointResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupResolverEndpointResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o LookupResolverEndpointResultOutput) ResolverEndpointId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupResolverEndpointResult) *string { return v.ResolverEndpointId }).(pulumi.StringPtrOutput)
}

func (o LookupResolverEndpointResultOutput) ResolverEndpointType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupResolverEndpointResult) *string { return v.ResolverEndpointType }).(pulumi.StringPtrOutput)
}

func (o LookupResolverEndpointResultOutput) Tags() ResolverEndpointTagArrayOutput {
	return o.ApplyT(func(v LookupResolverEndpointResult) []ResolverEndpointTag { return v.Tags }).(ResolverEndpointTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupResolverEndpointResultOutput{})
}
