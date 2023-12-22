// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package fis

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource schema for AWS::FIS::TargetAccountConfiguration
func LookupTargetAccountConfiguration(ctx *pulumi.Context, args *LookupTargetAccountConfigurationArgs, opts ...pulumi.InvokeOption) (*LookupTargetAccountConfigurationResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupTargetAccountConfigurationResult
	err := ctx.Invoke("aws-native:fis:getTargetAccountConfiguration", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupTargetAccountConfigurationArgs struct {
	AccountId            string `pulumi:"accountId"`
	ExperimentTemplateId string `pulumi:"experimentTemplateId"`
}

type LookupTargetAccountConfigurationResult struct {
	Description *string `pulumi:"description"`
	RoleArn     *string `pulumi:"roleArn"`
}

func LookupTargetAccountConfigurationOutput(ctx *pulumi.Context, args LookupTargetAccountConfigurationOutputArgs, opts ...pulumi.InvokeOption) LookupTargetAccountConfigurationResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupTargetAccountConfigurationResult, error) {
			args := v.(LookupTargetAccountConfigurationArgs)
			r, err := LookupTargetAccountConfiguration(ctx, &args, opts...)
			var s LookupTargetAccountConfigurationResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupTargetAccountConfigurationResultOutput)
}

type LookupTargetAccountConfigurationOutputArgs struct {
	AccountId            pulumi.StringInput `pulumi:"accountId"`
	ExperimentTemplateId pulumi.StringInput `pulumi:"experimentTemplateId"`
}

func (LookupTargetAccountConfigurationOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupTargetAccountConfigurationArgs)(nil)).Elem()
}

type LookupTargetAccountConfigurationResultOutput struct{ *pulumi.OutputState }

func (LookupTargetAccountConfigurationResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupTargetAccountConfigurationResult)(nil)).Elem()
}

func (o LookupTargetAccountConfigurationResultOutput) ToLookupTargetAccountConfigurationResultOutput() LookupTargetAccountConfigurationResultOutput {
	return o
}

func (o LookupTargetAccountConfigurationResultOutput) ToLookupTargetAccountConfigurationResultOutputWithContext(ctx context.Context) LookupTargetAccountConfigurationResultOutput {
	return o
}

func (o LookupTargetAccountConfigurationResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupTargetAccountConfigurationResult] {
	return pulumix.Output[LookupTargetAccountConfigurationResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupTargetAccountConfigurationResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupTargetAccountConfigurationResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

func (o LookupTargetAccountConfigurationResultOutput) RoleArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupTargetAccountConfigurationResult) *string { return v.RoleArn }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupTargetAccountConfigurationResultOutput{})
}
