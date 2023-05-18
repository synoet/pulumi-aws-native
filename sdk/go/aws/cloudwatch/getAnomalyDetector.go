// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cloudwatch

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::CloudWatch::AnomalyDetector
func LookupAnomalyDetector(ctx *pulumi.Context, args *LookupAnomalyDetectorArgs, opts ...pulumi.InvokeOption) (*LookupAnomalyDetectorResult, error) {
	var rv LookupAnomalyDetectorResult
	err := ctx.Invoke("aws-native:cloudwatch:getAnomalyDetector", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupAnomalyDetectorArgs struct {
	Id string `pulumi:"id"`
}

type LookupAnomalyDetectorResult struct {
	Configuration *AnomalyDetectorConfiguration `pulumi:"configuration"`
	Id            *string                       `pulumi:"id"`
}

func LookupAnomalyDetectorOutput(ctx *pulumi.Context, args LookupAnomalyDetectorOutputArgs, opts ...pulumi.InvokeOption) LookupAnomalyDetectorResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupAnomalyDetectorResult, error) {
			args := v.(LookupAnomalyDetectorArgs)
			r, err := LookupAnomalyDetector(ctx, &args, opts...)
			var s LookupAnomalyDetectorResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupAnomalyDetectorResultOutput)
}

type LookupAnomalyDetectorOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupAnomalyDetectorOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupAnomalyDetectorArgs)(nil)).Elem()
}

type LookupAnomalyDetectorResultOutput struct{ *pulumi.OutputState }

func (LookupAnomalyDetectorResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupAnomalyDetectorResult)(nil)).Elem()
}

func (o LookupAnomalyDetectorResultOutput) ToLookupAnomalyDetectorResultOutput() LookupAnomalyDetectorResultOutput {
	return o
}

func (o LookupAnomalyDetectorResultOutput) ToLookupAnomalyDetectorResultOutputWithContext(ctx context.Context) LookupAnomalyDetectorResultOutput {
	return o
}

func (o LookupAnomalyDetectorResultOutput) Configuration() AnomalyDetectorConfigurationPtrOutput {
	return o.ApplyT(func(v LookupAnomalyDetectorResult) *AnomalyDetectorConfiguration { return v.Configuration }).(AnomalyDetectorConfigurationPtrOutput)
}

func (o LookupAnomalyDetectorResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupAnomalyDetectorResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupAnomalyDetectorResultOutput{})
}
