// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package sns

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::SNS::Subscription
func LookupSubscription(ctx *pulumi.Context, args *LookupSubscriptionArgs, opts ...pulumi.InvokeOption) (*LookupSubscriptionResult, error) {
	var rv LookupSubscriptionResult
	err := ctx.Invoke("aws-native:sns:getSubscription", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupSubscriptionArgs struct {
	Id string `pulumi:"id"`
}

type LookupSubscriptionResult struct {
	DeliveryPolicy      interface{} `pulumi:"deliveryPolicy"`
	FilterPolicy        interface{} `pulumi:"filterPolicy"`
	FilterPolicyScope   *string     `pulumi:"filterPolicyScope"`
	Id                  *string     `pulumi:"id"`
	RawMessageDelivery  *bool       `pulumi:"rawMessageDelivery"`
	RedrivePolicy       interface{} `pulumi:"redrivePolicy"`
	Region              *string     `pulumi:"region"`
	SubscriptionRoleArn *string     `pulumi:"subscriptionRoleArn"`
}

func LookupSubscriptionOutput(ctx *pulumi.Context, args LookupSubscriptionOutputArgs, opts ...pulumi.InvokeOption) LookupSubscriptionResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupSubscriptionResult, error) {
			args := v.(LookupSubscriptionArgs)
			r, err := LookupSubscription(ctx, &args, opts...)
			var s LookupSubscriptionResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupSubscriptionResultOutput)
}

type LookupSubscriptionOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupSubscriptionOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSubscriptionArgs)(nil)).Elem()
}

type LookupSubscriptionResultOutput struct{ *pulumi.OutputState }

func (LookupSubscriptionResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSubscriptionResult)(nil)).Elem()
}

func (o LookupSubscriptionResultOutput) ToLookupSubscriptionResultOutput() LookupSubscriptionResultOutput {
	return o
}

func (o LookupSubscriptionResultOutput) ToLookupSubscriptionResultOutputWithContext(ctx context.Context) LookupSubscriptionResultOutput {
	return o
}

func (o LookupSubscriptionResultOutput) DeliveryPolicy() pulumi.AnyOutput {
	return o.ApplyT(func(v LookupSubscriptionResult) interface{} { return v.DeliveryPolicy }).(pulumi.AnyOutput)
}

func (o LookupSubscriptionResultOutput) FilterPolicy() pulumi.AnyOutput {
	return o.ApplyT(func(v LookupSubscriptionResult) interface{} { return v.FilterPolicy }).(pulumi.AnyOutput)
}

func (o LookupSubscriptionResultOutput) FilterPolicyScope() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSubscriptionResult) *string { return v.FilterPolicyScope }).(pulumi.StringPtrOutput)
}

func (o LookupSubscriptionResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSubscriptionResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupSubscriptionResultOutput) RawMessageDelivery() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupSubscriptionResult) *bool { return v.RawMessageDelivery }).(pulumi.BoolPtrOutput)
}

func (o LookupSubscriptionResultOutput) RedrivePolicy() pulumi.AnyOutput {
	return o.ApplyT(func(v LookupSubscriptionResult) interface{} { return v.RedrivePolicy }).(pulumi.AnyOutput)
}

func (o LookupSubscriptionResultOutput) Region() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSubscriptionResult) *string { return v.Region }).(pulumi.StringPtrOutput)
}

func (o LookupSubscriptionResultOutput) SubscriptionRoleArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSubscriptionResult) *string { return v.SubscriptionRoleArn }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupSubscriptionResultOutput{})
}
