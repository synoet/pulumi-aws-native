// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package iot

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource-specific logging allows you to specify a logging level for a specific thing group.
func LookupResourceSpecificLogging(ctx *pulumi.Context, args *LookupResourceSpecificLoggingArgs, opts ...pulumi.InvokeOption) (*LookupResourceSpecificLoggingResult, error) {
	var rv LookupResourceSpecificLoggingResult
	err := ctx.Invoke("aws-native:iot:getResourceSpecificLogging", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupResourceSpecificLoggingArgs struct {
	// Unique Id for a Target (TargetType:TargetName), this will be internally built to serve as primary identifier for a log target.
	TargetId string `pulumi:"targetId"`
}

type LookupResourceSpecificLoggingResult struct {
	// The log level for a specific target. Valid values are: ERROR, WARN, INFO, DEBUG, or DISABLED.
	LogLevel *ResourceSpecificLoggingLogLevel `pulumi:"logLevel"`
	// Unique Id for a Target (TargetType:TargetName), this will be internally built to serve as primary identifier for a log target.
	TargetId *string `pulumi:"targetId"`
}

func LookupResourceSpecificLoggingOutput(ctx *pulumi.Context, args LookupResourceSpecificLoggingOutputArgs, opts ...pulumi.InvokeOption) LookupResourceSpecificLoggingResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupResourceSpecificLoggingResult, error) {
			args := v.(LookupResourceSpecificLoggingArgs)
			r, err := LookupResourceSpecificLogging(ctx, &args, opts...)
			var s LookupResourceSpecificLoggingResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupResourceSpecificLoggingResultOutput)
}

type LookupResourceSpecificLoggingOutputArgs struct {
	// Unique Id for a Target (TargetType:TargetName), this will be internally built to serve as primary identifier for a log target.
	TargetId pulumi.StringInput `pulumi:"targetId"`
}

func (LookupResourceSpecificLoggingOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupResourceSpecificLoggingArgs)(nil)).Elem()
}

type LookupResourceSpecificLoggingResultOutput struct{ *pulumi.OutputState }

func (LookupResourceSpecificLoggingResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupResourceSpecificLoggingResult)(nil)).Elem()
}

func (o LookupResourceSpecificLoggingResultOutput) ToLookupResourceSpecificLoggingResultOutput() LookupResourceSpecificLoggingResultOutput {
	return o
}

func (o LookupResourceSpecificLoggingResultOutput) ToLookupResourceSpecificLoggingResultOutputWithContext(ctx context.Context) LookupResourceSpecificLoggingResultOutput {
	return o
}

// The log level for a specific target. Valid values are: ERROR, WARN, INFO, DEBUG, or DISABLED.
func (o LookupResourceSpecificLoggingResultOutput) LogLevel() ResourceSpecificLoggingLogLevelPtrOutput {
	return o.ApplyT(func(v LookupResourceSpecificLoggingResult) *ResourceSpecificLoggingLogLevel { return v.LogLevel }).(ResourceSpecificLoggingLogLevelPtrOutput)
}

// Unique Id for a Target (TargetType:TargetName), this will be internally built to serve as primary identifier for a log target.
func (o LookupResourceSpecificLoggingResultOutput) TargetId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupResourceSpecificLoggingResult) *string { return v.TargetId }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupResourceSpecificLoggingResultOutput{})
}
