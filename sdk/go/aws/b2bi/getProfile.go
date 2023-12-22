// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package b2bi

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Definition of AWS::B2BI::Profile Resource Type
func LookupProfile(ctx *pulumi.Context, args *LookupProfileArgs, opts ...pulumi.InvokeOption) (*LookupProfileResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupProfileResult
	err := ctx.Invoke("aws-native:b2bi:getProfile", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupProfileArgs struct {
	ProfileId string `pulumi:"profileId"`
}

type LookupProfileResult struct {
	BusinessName *string      `pulumi:"businessName"`
	CreatedAt    *string      `pulumi:"createdAt"`
	Email        *string      `pulumi:"email"`
	LogGroupName *string      `pulumi:"logGroupName"`
	ModifiedAt   *string      `pulumi:"modifiedAt"`
	Name         *string      `pulumi:"name"`
	Phone        *string      `pulumi:"phone"`
	ProfileArn   *string      `pulumi:"profileArn"`
	ProfileId    *string      `pulumi:"profileId"`
	Tags         []ProfileTag `pulumi:"tags"`
}

func LookupProfileOutput(ctx *pulumi.Context, args LookupProfileOutputArgs, opts ...pulumi.InvokeOption) LookupProfileResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupProfileResult, error) {
			args := v.(LookupProfileArgs)
			r, err := LookupProfile(ctx, &args, opts...)
			var s LookupProfileResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupProfileResultOutput)
}

type LookupProfileOutputArgs struct {
	ProfileId pulumi.StringInput `pulumi:"profileId"`
}

func (LookupProfileOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupProfileArgs)(nil)).Elem()
}

type LookupProfileResultOutput struct{ *pulumi.OutputState }

func (LookupProfileResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupProfileResult)(nil)).Elem()
}

func (o LookupProfileResultOutput) ToLookupProfileResultOutput() LookupProfileResultOutput {
	return o
}

func (o LookupProfileResultOutput) ToLookupProfileResultOutputWithContext(ctx context.Context) LookupProfileResultOutput {
	return o
}

func (o LookupProfileResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupProfileResult] {
	return pulumix.Output[LookupProfileResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupProfileResultOutput) BusinessName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupProfileResult) *string { return v.BusinessName }).(pulumi.StringPtrOutput)
}

func (o LookupProfileResultOutput) CreatedAt() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupProfileResult) *string { return v.CreatedAt }).(pulumi.StringPtrOutput)
}

func (o LookupProfileResultOutput) Email() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupProfileResult) *string { return v.Email }).(pulumi.StringPtrOutput)
}

func (o LookupProfileResultOutput) LogGroupName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupProfileResult) *string { return v.LogGroupName }).(pulumi.StringPtrOutput)
}

func (o LookupProfileResultOutput) ModifiedAt() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupProfileResult) *string { return v.ModifiedAt }).(pulumi.StringPtrOutput)
}

func (o LookupProfileResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupProfileResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o LookupProfileResultOutput) Phone() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupProfileResult) *string { return v.Phone }).(pulumi.StringPtrOutput)
}

func (o LookupProfileResultOutput) ProfileArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupProfileResult) *string { return v.ProfileArn }).(pulumi.StringPtrOutput)
}

func (o LookupProfileResultOutput) ProfileId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupProfileResult) *string { return v.ProfileId }).(pulumi.StringPtrOutput)
}

func (o LookupProfileResultOutput) Tags() ProfileTagArrayOutput {
	return o.ApplyT(func(v LookupProfileResult) []ProfileTag { return v.Tags }).(ProfileTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupProfileResultOutput{})
}
