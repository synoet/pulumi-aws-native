// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package fms

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Designates the IAM role and Amazon Simple Notification Service (SNS) topic that AWS Firewall Manager uses to record SNS logs.
func LookupNotificationChannel(ctx *pulumi.Context, args *LookupNotificationChannelArgs, opts ...pulumi.InvokeOption) (*LookupNotificationChannelResult, error) {
	var rv LookupNotificationChannelResult
	err := ctx.Invoke("aws-native:fms:getNotificationChannel", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupNotificationChannelArgs struct {
	SnsTopicArn string `pulumi:"snsTopicArn"`
}

type LookupNotificationChannelResult struct {
	SnsRoleName *string `pulumi:"snsRoleName"`
	SnsTopicArn *string `pulumi:"snsTopicArn"`
}

func LookupNotificationChannelOutput(ctx *pulumi.Context, args LookupNotificationChannelOutputArgs, opts ...pulumi.InvokeOption) LookupNotificationChannelResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupNotificationChannelResult, error) {
			args := v.(LookupNotificationChannelArgs)
			r, err := LookupNotificationChannel(ctx, &args, opts...)
			var s LookupNotificationChannelResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupNotificationChannelResultOutput)
}

type LookupNotificationChannelOutputArgs struct {
	SnsTopicArn pulumi.StringInput `pulumi:"snsTopicArn"`
}

func (LookupNotificationChannelOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupNotificationChannelArgs)(nil)).Elem()
}

type LookupNotificationChannelResultOutput struct{ *pulumi.OutputState }

func (LookupNotificationChannelResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupNotificationChannelResult)(nil)).Elem()
}

func (o LookupNotificationChannelResultOutput) ToLookupNotificationChannelResultOutput() LookupNotificationChannelResultOutput {
	return o
}

func (o LookupNotificationChannelResultOutput) ToLookupNotificationChannelResultOutputWithContext(ctx context.Context) LookupNotificationChannelResultOutput {
	return o
}

func (o LookupNotificationChannelResultOutput) SnsRoleName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupNotificationChannelResult) *string { return v.SnsRoleName }).(pulumi.StringPtrOutput)
}

func (o LookupNotificationChannelResultOutput) SnsTopicArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupNotificationChannelResult) *string { return v.SnsTopicArn }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupNotificationChannelResultOutput{})
}
