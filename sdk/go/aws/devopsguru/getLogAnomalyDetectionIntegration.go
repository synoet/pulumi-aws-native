// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package devopsguru

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// This resource schema represents the LogAnomalyDetectionIntegration resource in the Amazon DevOps Guru.
func LookupLogAnomalyDetectionIntegration(ctx *pulumi.Context, args *LookupLogAnomalyDetectionIntegrationArgs, opts ...pulumi.InvokeOption) (*LookupLogAnomalyDetectionIntegrationResult, error) {
	var rv LookupLogAnomalyDetectionIntegrationResult
	err := ctx.Invoke("aws-native:devopsguru:getLogAnomalyDetectionIntegration", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupLogAnomalyDetectionIntegrationArgs struct {
	AccountId string `pulumi:"accountId"`
}

type LookupLogAnomalyDetectionIntegrationResult struct {
	AccountId *string `pulumi:"accountId"`
}

func LookupLogAnomalyDetectionIntegrationOutput(ctx *pulumi.Context, args LookupLogAnomalyDetectionIntegrationOutputArgs, opts ...pulumi.InvokeOption) LookupLogAnomalyDetectionIntegrationResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupLogAnomalyDetectionIntegrationResult, error) {
			args := v.(LookupLogAnomalyDetectionIntegrationArgs)
			r, err := LookupLogAnomalyDetectionIntegration(ctx, &args, opts...)
			var s LookupLogAnomalyDetectionIntegrationResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupLogAnomalyDetectionIntegrationResultOutput)
}

type LookupLogAnomalyDetectionIntegrationOutputArgs struct {
	AccountId pulumi.StringInput `pulumi:"accountId"`
}

func (LookupLogAnomalyDetectionIntegrationOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupLogAnomalyDetectionIntegrationArgs)(nil)).Elem()
}

type LookupLogAnomalyDetectionIntegrationResultOutput struct{ *pulumi.OutputState }

func (LookupLogAnomalyDetectionIntegrationResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupLogAnomalyDetectionIntegrationResult)(nil)).Elem()
}

func (o LookupLogAnomalyDetectionIntegrationResultOutput) ToLookupLogAnomalyDetectionIntegrationResultOutput() LookupLogAnomalyDetectionIntegrationResultOutput {
	return o
}

func (o LookupLogAnomalyDetectionIntegrationResultOutput) ToLookupLogAnomalyDetectionIntegrationResultOutputWithContext(ctx context.Context) LookupLogAnomalyDetectionIntegrationResultOutput {
	return o
}

func (o LookupLogAnomalyDetectionIntegrationResultOutput) AccountId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLogAnomalyDetectionIntegrationResult) *string { return v.AccountId }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupLogAnomalyDetectionIntegrationResultOutput{})
}
