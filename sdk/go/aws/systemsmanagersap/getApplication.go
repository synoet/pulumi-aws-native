// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package systemsmanagersap

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for AWS::SystemsManagerSAP::Application
func LookupApplication(ctx *pulumi.Context, args *LookupApplicationArgs, opts ...pulumi.InvokeOption) (*LookupApplicationResult, error) {
	var rv LookupApplicationResult
	err := ctx.Invoke("aws-native:systemsmanagersap:getApplication", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupApplicationArgs struct {
	// The ARN of the Helix application
	Arn string `pulumi:"arn"`
}

type LookupApplicationResult struct {
	ApplicationId   *string          `pulumi:"applicationId"`
	ApplicationType *ApplicationType `pulumi:"applicationType"`
	// The ARN of the Helix application
	Arn *string `pulumi:"arn"`
	// The tags of a SystemsManagerSAP application.
	Tags []ApplicationTag `pulumi:"tags"`
}

func LookupApplicationOutput(ctx *pulumi.Context, args LookupApplicationOutputArgs, opts ...pulumi.InvokeOption) LookupApplicationResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupApplicationResult, error) {
			args := v.(LookupApplicationArgs)
			r, err := LookupApplication(ctx, &args, opts...)
			var s LookupApplicationResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupApplicationResultOutput)
}

type LookupApplicationOutputArgs struct {
	// The ARN of the Helix application
	Arn pulumi.StringInput `pulumi:"arn"`
}

func (LookupApplicationOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupApplicationArgs)(nil)).Elem()
}

type LookupApplicationResultOutput struct{ *pulumi.OutputState }

func (LookupApplicationResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupApplicationResult)(nil)).Elem()
}

func (o LookupApplicationResultOutput) ToLookupApplicationResultOutput() LookupApplicationResultOutput {
	return o
}

func (o LookupApplicationResultOutput) ToLookupApplicationResultOutputWithContext(ctx context.Context) LookupApplicationResultOutput {
	return o
}

func (o LookupApplicationResultOutput) ApplicationId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupApplicationResult) *string { return v.ApplicationId }).(pulumi.StringPtrOutput)
}

func (o LookupApplicationResultOutput) ApplicationType() ApplicationTypePtrOutput {
	return o.ApplyT(func(v LookupApplicationResult) *ApplicationType { return v.ApplicationType }).(ApplicationTypePtrOutput)
}

// The ARN of the Helix application
func (o LookupApplicationResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupApplicationResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

// The tags of a SystemsManagerSAP application.
func (o LookupApplicationResultOutput) Tags() ApplicationTagArrayOutput {
	return o.ApplyT(func(v LookupApplicationResult) []ApplicationTag { return v.Tags }).(ApplicationTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupApplicationResultOutput{})
}
