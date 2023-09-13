// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package rolesanywhere

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Definition of AWS::RolesAnywhere::TrustAnchor Resource Type.
func LookupTrustAnchor(ctx *pulumi.Context, args *LookupTrustAnchorArgs, opts ...pulumi.InvokeOption) (*LookupTrustAnchorResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupTrustAnchorResult
	err := ctx.Invoke("aws-native:rolesanywhere:getTrustAnchor", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupTrustAnchorArgs struct {
	TrustAnchorId string `pulumi:"trustAnchorId"`
}

type LookupTrustAnchorResult struct {
	Enabled              *bool                            `pulumi:"enabled"`
	Name                 *string                          `pulumi:"name"`
	NotificationSettings []TrustAnchorNotificationSetting `pulumi:"notificationSettings"`
	Source               *TrustAnchorSource               `pulumi:"source"`
	Tags                 []TrustAnchorTag                 `pulumi:"tags"`
	TrustAnchorArn       *string                          `pulumi:"trustAnchorArn"`
	TrustAnchorId        *string                          `pulumi:"trustAnchorId"`
}

func LookupTrustAnchorOutput(ctx *pulumi.Context, args LookupTrustAnchorOutputArgs, opts ...pulumi.InvokeOption) LookupTrustAnchorResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupTrustAnchorResult, error) {
			args := v.(LookupTrustAnchorArgs)
			r, err := LookupTrustAnchor(ctx, &args, opts...)
			var s LookupTrustAnchorResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupTrustAnchorResultOutput)
}

type LookupTrustAnchorOutputArgs struct {
	TrustAnchorId pulumi.StringInput `pulumi:"trustAnchorId"`
}

func (LookupTrustAnchorOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupTrustAnchorArgs)(nil)).Elem()
}

type LookupTrustAnchorResultOutput struct{ *pulumi.OutputState }

func (LookupTrustAnchorResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupTrustAnchorResult)(nil)).Elem()
}

func (o LookupTrustAnchorResultOutput) ToLookupTrustAnchorResultOutput() LookupTrustAnchorResultOutput {
	return o
}

func (o LookupTrustAnchorResultOutput) ToLookupTrustAnchorResultOutputWithContext(ctx context.Context) LookupTrustAnchorResultOutput {
	return o
}

func (o LookupTrustAnchorResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupTrustAnchorResult] {
	return pulumix.Output[LookupTrustAnchorResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupTrustAnchorResultOutput) Enabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupTrustAnchorResult) *bool { return v.Enabled }).(pulumi.BoolPtrOutput)
}

func (o LookupTrustAnchorResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupTrustAnchorResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o LookupTrustAnchorResultOutput) NotificationSettings() TrustAnchorNotificationSettingArrayOutput {
	return o.ApplyT(func(v LookupTrustAnchorResult) []TrustAnchorNotificationSetting { return v.NotificationSettings }).(TrustAnchorNotificationSettingArrayOutput)
}

func (o LookupTrustAnchorResultOutput) Source() TrustAnchorSourcePtrOutput {
	return o.ApplyT(func(v LookupTrustAnchorResult) *TrustAnchorSource { return v.Source }).(TrustAnchorSourcePtrOutput)
}

func (o LookupTrustAnchorResultOutput) Tags() TrustAnchorTagArrayOutput {
	return o.ApplyT(func(v LookupTrustAnchorResult) []TrustAnchorTag { return v.Tags }).(TrustAnchorTagArrayOutput)
}

func (o LookupTrustAnchorResultOutput) TrustAnchorArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupTrustAnchorResult) *string { return v.TrustAnchorArn }).(pulumi.StringPtrOutput)
}

func (o LookupTrustAnchorResultOutput) TrustAnchorId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupTrustAnchorResult) *string { return v.TrustAnchorId }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupTrustAnchorResultOutput{})
}
