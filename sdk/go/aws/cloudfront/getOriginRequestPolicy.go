// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cloudfront

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::CloudFront::OriginRequestPolicy
func LookupOriginRequestPolicy(ctx *pulumi.Context, args *LookupOriginRequestPolicyArgs, opts ...pulumi.InvokeOption) (*LookupOriginRequestPolicyResult, error) {
	var rv LookupOriginRequestPolicyResult
	err := ctx.Invoke("aws-native:cloudfront:getOriginRequestPolicy", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupOriginRequestPolicyArgs struct {
	Id string `pulumi:"id"`
}

type LookupOriginRequestPolicyResult struct {
	Id                        *string                    `pulumi:"id"`
	LastModifiedTime          *string                    `pulumi:"lastModifiedTime"`
	OriginRequestPolicyConfig *OriginRequestPolicyConfig `pulumi:"originRequestPolicyConfig"`
}

func LookupOriginRequestPolicyOutput(ctx *pulumi.Context, args LookupOriginRequestPolicyOutputArgs, opts ...pulumi.InvokeOption) LookupOriginRequestPolicyResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupOriginRequestPolicyResult, error) {
			args := v.(LookupOriginRequestPolicyArgs)
			r, err := LookupOriginRequestPolicy(ctx, &args, opts...)
			var s LookupOriginRequestPolicyResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupOriginRequestPolicyResultOutput)
}

type LookupOriginRequestPolicyOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupOriginRequestPolicyOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupOriginRequestPolicyArgs)(nil)).Elem()
}

type LookupOriginRequestPolicyResultOutput struct{ *pulumi.OutputState }

func (LookupOriginRequestPolicyResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupOriginRequestPolicyResult)(nil)).Elem()
}

func (o LookupOriginRequestPolicyResultOutput) ToLookupOriginRequestPolicyResultOutput() LookupOriginRequestPolicyResultOutput {
	return o
}

func (o LookupOriginRequestPolicyResultOutput) ToLookupOriginRequestPolicyResultOutputWithContext(ctx context.Context) LookupOriginRequestPolicyResultOutput {
	return o
}

func (o LookupOriginRequestPolicyResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupOriginRequestPolicyResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupOriginRequestPolicyResultOutput) LastModifiedTime() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupOriginRequestPolicyResult) *string { return v.LastModifiedTime }).(pulumi.StringPtrOutput)
}

func (o LookupOriginRequestPolicyResultOutput) OriginRequestPolicyConfig() OriginRequestPolicyConfigPtrOutput {
	return o.ApplyT(func(v LookupOriginRequestPolicyResult) *OriginRequestPolicyConfig { return v.OriginRequestPolicyConfig }).(OriginRequestPolicyConfigPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupOriginRequestPolicyResultOutput{})
}
