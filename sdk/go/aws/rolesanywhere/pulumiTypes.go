// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package rolesanywhere

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

var _ = internal.GetEnvOrDefault

type CrlTag struct {
	Key   string `pulumi:"key"`
	Value string `pulumi:"value"`
}

// CrlTagInput is an input type that accepts CrlTagArgs and CrlTagOutput values.
// You can construct a concrete instance of `CrlTagInput` via:
//
//	CrlTagArgs{...}
type CrlTagInput interface {
	pulumi.Input

	ToCrlTagOutput() CrlTagOutput
	ToCrlTagOutputWithContext(context.Context) CrlTagOutput
}

type CrlTagArgs struct {
	Key   pulumi.StringInput `pulumi:"key"`
	Value pulumi.StringInput `pulumi:"value"`
}

func (CrlTagArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*CrlTag)(nil)).Elem()
}

func (i CrlTagArgs) ToCrlTagOutput() CrlTagOutput {
	return i.ToCrlTagOutputWithContext(context.Background())
}

func (i CrlTagArgs) ToCrlTagOutputWithContext(ctx context.Context) CrlTagOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CrlTagOutput)
}

// CrlTagArrayInput is an input type that accepts CrlTagArray and CrlTagArrayOutput values.
// You can construct a concrete instance of `CrlTagArrayInput` via:
//
//	CrlTagArray{ CrlTagArgs{...} }
type CrlTagArrayInput interface {
	pulumi.Input

	ToCrlTagArrayOutput() CrlTagArrayOutput
	ToCrlTagArrayOutputWithContext(context.Context) CrlTagArrayOutput
}

type CrlTagArray []CrlTagInput

func (CrlTagArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]CrlTag)(nil)).Elem()
}

func (i CrlTagArray) ToCrlTagArrayOutput() CrlTagArrayOutput {
	return i.ToCrlTagArrayOutputWithContext(context.Background())
}

func (i CrlTagArray) ToCrlTagArrayOutputWithContext(ctx context.Context) CrlTagArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CrlTagArrayOutput)
}

type CrlTagOutput struct{ *pulumi.OutputState }

func (CrlTagOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*CrlTag)(nil)).Elem()
}

func (o CrlTagOutput) ToCrlTagOutput() CrlTagOutput {
	return o
}

func (o CrlTagOutput) ToCrlTagOutputWithContext(ctx context.Context) CrlTagOutput {
	return o
}

func (o CrlTagOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v CrlTag) string { return v.Key }).(pulumi.StringOutput)
}

func (o CrlTagOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v CrlTag) string { return v.Value }).(pulumi.StringOutput)
}

type CrlTagArrayOutput struct{ *pulumi.OutputState }

func (CrlTagArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]CrlTag)(nil)).Elem()
}

func (o CrlTagArrayOutput) ToCrlTagArrayOutput() CrlTagArrayOutput {
	return o
}

func (o CrlTagArrayOutput) ToCrlTagArrayOutputWithContext(ctx context.Context) CrlTagArrayOutput {
	return o
}

func (o CrlTagArrayOutput) Index(i pulumi.IntInput) CrlTagOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) CrlTag {
		return vs[0].([]CrlTag)[vs[1].(int)]
	}).(CrlTagOutput)
}

type ProfileTag struct {
	Key   string `pulumi:"key"`
	Value string `pulumi:"value"`
}

// ProfileTagInput is an input type that accepts ProfileTagArgs and ProfileTagOutput values.
// You can construct a concrete instance of `ProfileTagInput` via:
//
//	ProfileTagArgs{...}
type ProfileTagInput interface {
	pulumi.Input

	ToProfileTagOutput() ProfileTagOutput
	ToProfileTagOutputWithContext(context.Context) ProfileTagOutput
}

type ProfileTagArgs struct {
	Key   pulumi.StringInput `pulumi:"key"`
	Value pulumi.StringInput `pulumi:"value"`
}

func (ProfileTagArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ProfileTag)(nil)).Elem()
}

func (i ProfileTagArgs) ToProfileTagOutput() ProfileTagOutput {
	return i.ToProfileTagOutputWithContext(context.Background())
}

func (i ProfileTagArgs) ToProfileTagOutputWithContext(ctx context.Context) ProfileTagOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProfileTagOutput)
}

// ProfileTagArrayInput is an input type that accepts ProfileTagArray and ProfileTagArrayOutput values.
// You can construct a concrete instance of `ProfileTagArrayInput` via:
//
//	ProfileTagArray{ ProfileTagArgs{...} }
type ProfileTagArrayInput interface {
	pulumi.Input

	ToProfileTagArrayOutput() ProfileTagArrayOutput
	ToProfileTagArrayOutputWithContext(context.Context) ProfileTagArrayOutput
}

type ProfileTagArray []ProfileTagInput

func (ProfileTagArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ProfileTag)(nil)).Elem()
}

func (i ProfileTagArray) ToProfileTagArrayOutput() ProfileTagArrayOutput {
	return i.ToProfileTagArrayOutputWithContext(context.Background())
}

func (i ProfileTagArray) ToProfileTagArrayOutputWithContext(ctx context.Context) ProfileTagArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProfileTagArrayOutput)
}

type ProfileTagOutput struct{ *pulumi.OutputState }

func (ProfileTagOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ProfileTag)(nil)).Elem()
}

func (o ProfileTagOutput) ToProfileTagOutput() ProfileTagOutput {
	return o
}

func (o ProfileTagOutput) ToProfileTagOutputWithContext(ctx context.Context) ProfileTagOutput {
	return o
}

func (o ProfileTagOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v ProfileTag) string { return v.Key }).(pulumi.StringOutput)
}

func (o ProfileTagOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v ProfileTag) string { return v.Value }).(pulumi.StringOutput)
}

type ProfileTagArrayOutput struct{ *pulumi.OutputState }

func (ProfileTagArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ProfileTag)(nil)).Elem()
}

func (o ProfileTagArrayOutput) ToProfileTagArrayOutput() ProfileTagArrayOutput {
	return o
}

func (o ProfileTagArrayOutput) ToProfileTagArrayOutputWithContext(ctx context.Context) ProfileTagArrayOutput {
	return o
}

func (o ProfileTagArrayOutput) Index(i pulumi.IntInput) ProfileTagOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) ProfileTag {
		return vs[0].([]ProfileTag)[vs[1].(int)]
	}).(ProfileTagOutput)
}

type TrustAnchorNotificationSetting struct {
	Channel   *TrustAnchorNotificationChannel `pulumi:"channel"`
	Enabled   bool                            `pulumi:"enabled"`
	Event     TrustAnchorNotificationEvent    `pulumi:"event"`
	Threshold *float64                        `pulumi:"threshold"`
}

// TrustAnchorNotificationSettingInput is an input type that accepts TrustAnchorNotificationSettingArgs and TrustAnchorNotificationSettingOutput values.
// You can construct a concrete instance of `TrustAnchorNotificationSettingInput` via:
//
//	TrustAnchorNotificationSettingArgs{...}
type TrustAnchorNotificationSettingInput interface {
	pulumi.Input

	ToTrustAnchorNotificationSettingOutput() TrustAnchorNotificationSettingOutput
	ToTrustAnchorNotificationSettingOutputWithContext(context.Context) TrustAnchorNotificationSettingOutput
}

type TrustAnchorNotificationSettingArgs struct {
	Channel   TrustAnchorNotificationChannelPtrInput `pulumi:"channel"`
	Enabled   pulumi.BoolInput                       `pulumi:"enabled"`
	Event     TrustAnchorNotificationEventInput      `pulumi:"event"`
	Threshold pulumi.Float64PtrInput                 `pulumi:"threshold"`
}

func (TrustAnchorNotificationSettingArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*TrustAnchorNotificationSetting)(nil)).Elem()
}

func (i TrustAnchorNotificationSettingArgs) ToTrustAnchorNotificationSettingOutput() TrustAnchorNotificationSettingOutput {
	return i.ToTrustAnchorNotificationSettingOutputWithContext(context.Background())
}

func (i TrustAnchorNotificationSettingArgs) ToTrustAnchorNotificationSettingOutputWithContext(ctx context.Context) TrustAnchorNotificationSettingOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TrustAnchorNotificationSettingOutput)
}

// TrustAnchorNotificationSettingArrayInput is an input type that accepts TrustAnchorNotificationSettingArray and TrustAnchorNotificationSettingArrayOutput values.
// You can construct a concrete instance of `TrustAnchorNotificationSettingArrayInput` via:
//
//	TrustAnchorNotificationSettingArray{ TrustAnchorNotificationSettingArgs{...} }
type TrustAnchorNotificationSettingArrayInput interface {
	pulumi.Input

	ToTrustAnchorNotificationSettingArrayOutput() TrustAnchorNotificationSettingArrayOutput
	ToTrustAnchorNotificationSettingArrayOutputWithContext(context.Context) TrustAnchorNotificationSettingArrayOutput
}

type TrustAnchorNotificationSettingArray []TrustAnchorNotificationSettingInput

func (TrustAnchorNotificationSettingArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]TrustAnchorNotificationSetting)(nil)).Elem()
}

func (i TrustAnchorNotificationSettingArray) ToTrustAnchorNotificationSettingArrayOutput() TrustAnchorNotificationSettingArrayOutput {
	return i.ToTrustAnchorNotificationSettingArrayOutputWithContext(context.Background())
}

func (i TrustAnchorNotificationSettingArray) ToTrustAnchorNotificationSettingArrayOutputWithContext(ctx context.Context) TrustAnchorNotificationSettingArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TrustAnchorNotificationSettingArrayOutput)
}

type TrustAnchorNotificationSettingOutput struct{ *pulumi.OutputState }

func (TrustAnchorNotificationSettingOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*TrustAnchorNotificationSetting)(nil)).Elem()
}

func (o TrustAnchorNotificationSettingOutput) ToTrustAnchorNotificationSettingOutput() TrustAnchorNotificationSettingOutput {
	return o
}

func (o TrustAnchorNotificationSettingOutput) ToTrustAnchorNotificationSettingOutputWithContext(ctx context.Context) TrustAnchorNotificationSettingOutput {
	return o
}

func (o TrustAnchorNotificationSettingOutput) Channel() TrustAnchorNotificationChannelPtrOutput {
	return o.ApplyT(func(v TrustAnchorNotificationSetting) *TrustAnchorNotificationChannel { return v.Channel }).(TrustAnchorNotificationChannelPtrOutput)
}

func (o TrustAnchorNotificationSettingOutput) Enabled() pulumi.BoolOutput {
	return o.ApplyT(func(v TrustAnchorNotificationSetting) bool { return v.Enabled }).(pulumi.BoolOutput)
}

func (o TrustAnchorNotificationSettingOutput) Event() TrustAnchorNotificationEventOutput {
	return o.ApplyT(func(v TrustAnchorNotificationSetting) TrustAnchorNotificationEvent { return v.Event }).(TrustAnchorNotificationEventOutput)
}

func (o TrustAnchorNotificationSettingOutput) Threshold() pulumi.Float64PtrOutput {
	return o.ApplyT(func(v TrustAnchorNotificationSetting) *float64 { return v.Threshold }).(pulumi.Float64PtrOutput)
}

type TrustAnchorNotificationSettingArrayOutput struct{ *pulumi.OutputState }

func (TrustAnchorNotificationSettingArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]TrustAnchorNotificationSetting)(nil)).Elem()
}

func (o TrustAnchorNotificationSettingArrayOutput) ToTrustAnchorNotificationSettingArrayOutput() TrustAnchorNotificationSettingArrayOutput {
	return o
}

func (o TrustAnchorNotificationSettingArrayOutput) ToTrustAnchorNotificationSettingArrayOutputWithContext(ctx context.Context) TrustAnchorNotificationSettingArrayOutput {
	return o
}

func (o TrustAnchorNotificationSettingArrayOutput) Index(i pulumi.IntInput) TrustAnchorNotificationSettingOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) TrustAnchorNotificationSetting {
		return vs[0].([]TrustAnchorNotificationSetting)[vs[1].(int)]
	}).(TrustAnchorNotificationSettingOutput)
}

type TrustAnchorSource struct {
	SourceData interface{}      `pulumi:"sourceData"`
	SourceType *TrustAnchorType `pulumi:"sourceType"`
}

// TrustAnchorSourceInput is an input type that accepts TrustAnchorSourceArgs and TrustAnchorSourceOutput values.
// You can construct a concrete instance of `TrustAnchorSourceInput` via:
//
//	TrustAnchorSourceArgs{...}
type TrustAnchorSourceInput interface {
	pulumi.Input

	ToTrustAnchorSourceOutput() TrustAnchorSourceOutput
	ToTrustAnchorSourceOutputWithContext(context.Context) TrustAnchorSourceOutput
}

type TrustAnchorSourceArgs struct {
	SourceData pulumi.Input            `pulumi:"sourceData"`
	SourceType TrustAnchorTypePtrInput `pulumi:"sourceType"`
}

func (TrustAnchorSourceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*TrustAnchorSource)(nil)).Elem()
}

func (i TrustAnchorSourceArgs) ToTrustAnchorSourceOutput() TrustAnchorSourceOutput {
	return i.ToTrustAnchorSourceOutputWithContext(context.Background())
}

func (i TrustAnchorSourceArgs) ToTrustAnchorSourceOutputWithContext(ctx context.Context) TrustAnchorSourceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TrustAnchorSourceOutput)
}

type TrustAnchorSourceOutput struct{ *pulumi.OutputState }

func (TrustAnchorSourceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*TrustAnchorSource)(nil)).Elem()
}

func (o TrustAnchorSourceOutput) ToTrustAnchorSourceOutput() TrustAnchorSourceOutput {
	return o
}

func (o TrustAnchorSourceOutput) ToTrustAnchorSourceOutputWithContext(ctx context.Context) TrustAnchorSourceOutput {
	return o
}

func (o TrustAnchorSourceOutput) SourceData() pulumi.AnyOutput {
	return o.ApplyT(func(v TrustAnchorSource) interface{} { return v.SourceData }).(pulumi.AnyOutput)
}

func (o TrustAnchorSourceOutput) SourceType() TrustAnchorTypePtrOutput {
	return o.ApplyT(func(v TrustAnchorSource) *TrustAnchorType { return v.SourceType }).(TrustAnchorTypePtrOutput)
}

type TrustAnchorSourcePtrOutput struct{ *pulumi.OutputState }

func (TrustAnchorSourcePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**TrustAnchorSource)(nil)).Elem()
}

func (o TrustAnchorSourcePtrOutput) ToTrustAnchorSourcePtrOutput() TrustAnchorSourcePtrOutput {
	return o
}

func (o TrustAnchorSourcePtrOutput) ToTrustAnchorSourcePtrOutputWithContext(ctx context.Context) TrustAnchorSourcePtrOutput {
	return o
}

func (o TrustAnchorSourcePtrOutput) Elem() TrustAnchorSourceOutput {
	return o.ApplyT(func(v *TrustAnchorSource) TrustAnchorSource {
		if v != nil {
			return *v
		}
		var ret TrustAnchorSource
		return ret
	}).(TrustAnchorSourceOutput)
}

func (o TrustAnchorSourcePtrOutput) SourceData() pulumi.AnyOutput {
	return o.ApplyT(func(v *TrustAnchorSource) interface{} {
		if v == nil {
			return nil
		}
		return v.SourceData
	}).(pulumi.AnyOutput)
}

func (o TrustAnchorSourcePtrOutput) SourceType() TrustAnchorTypePtrOutput {
	return o.ApplyT(func(v *TrustAnchorSource) *TrustAnchorType {
		if v == nil {
			return nil
		}
		return v.SourceType
	}).(TrustAnchorTypePtrOutput)
}

type TrustAnchorSourceData0Properties struct {
	X509CertificateData string `pulumi:"x509CertificateData"`
}

// TrustAnchorSourceData0PropertiesInput is an input type that accepts TrustAnchorSourceData0PropertiesArgs and TrustAnchorSourceData0PropertiesOutput values.
// You can construct a concrete instance of `TrustAnchorSourceData0PropertiesInput` via:
//
//	TrustAnchorSourceData0PropertiesArgs{...}
type TrustAnchorSourceData0PropertiesInput interface {
	pulumi.Input

	ToTrustAnchorSourceData0PropertiesOutput() TrustAnchorSourceData0PropertiesOutput
	ToTrustAnchorSourceData0PropertiesOutputWithContext(context.Context) TrustAnchorSourceData0PropertiesOutput
}

type TrustAnchorSourceData0PropertiesArgs struct {
	X509CertificateData pulumi.StringInput `pulumi:"x509CertificateData"`
}

func (TrustAnchorSourceData0PropertiesArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*TrustAnchorSourceData0Properties)(nil)).Elem()
}

func (i TrustAnchorSourceData0PropertiesArgs) ToTrustAnchorSourceData0PropertiesOutput() TrustAnchorSourceData0PropertiesOutput {
	return i.ToTrustAnchorSourceData0PropertiesOutputWithContext(context.Background())
}

func (i TrustAnchorSourceData0PropertiesArgs) ToTrustAnchorSourceData0PropertiesOutputWithContext(ctx context.Context) TrustAnchorSourceData0PropertiesOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TrustAnchorSourceData0PropertiesOutput)
}

func (i TrustAnchorSourceData0PropertiesArgs) ToTrustAnchorSourceData0PropertiesPtrOutput() TrustAnchorSourceData0PropertiesPtrOutput {
	return i.ToTrustAnchorSourceData0PropertiesPtrOutputWithContext(context.Background())
}

func (i TrustAnchorSourceData0PropertiesArgs) ToTrustAnchorSourceData0PropertiesPtrOutputWithContext(ctx context.Context) TrustAnchorSourceData0PropertiesPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TrustAnchorSourceData0PropertiesOutput).ToTrustAnchorSourceData0PropertiesPtrOutputWithContext(ctx)
}

// TrustAnchorSourceData0PropertiesPtrInput is an input type that accepts TrustAnchorSourceData0PropertiesArgs, TrustAnchorSourceData0PropertiesPtr and TrustAnchorSourceData0PropertiesPtrOutput values.
// You can construct a concrete instance of `TrustAnchorSourceData0PropertiesPtrInput` via:
//
//	        TrustAnchorSourceData0PropertiesArgs{...}
//
//	or:
//
//	        nil
type TrustAnchorSourceData0PropertiesPtrInput interface {
	pulumi.Input

	ToTrustAnchorSourceData0PropertiesPtrOutput() TrustAnchorSourceData0PropertiesPtrOutput
	ToTrustAnchorSourceData0PropertiesPtrOutputWithContext(context.Context) TrustAnchorSourceData0PropertiesPtrOutput
}

type trustAnchorSourceData0PropertiesPtrType TrustAnchorSourceData0PropertiesArgs

func TrustAnchorSourceData0PropertiesPtr(v *TrustAnchorSourceData0PropertiesArgs) TrustAnchorSourceData0PropertiesPtrInput {
	return (*trustAnchorSourceData0PropertiesPtrType)(v)
}

func (*trustAnchorSourceData0PropertiesPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**TrustAnchorSourceData0Properties)(nil)).Elem()
}

func (i *trustAnchorSourceData0PropertiesPtrType) ToTrustAnchorSourceData0PropertiesPtrOutput() TrustAnchorSourceData0PropertiesPtrOutput {
	return i.ToTrustAnchorSourceData0PropertiesPtrOutputWithContext(context.Background())
}

func (i *trustAnchorSourceData0PropertiesPtrType) ToTrustAnchorSourceData0PropertiesPtrOutputWithContext(ctx context.Context) TrustAnchorSourceData0PropertiesPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TrustAnchorSourceData0PropertiesPtrOutput)
}

type TrustAnchorSourceData0PropertiesOutput struct{ *pulumi.OutputState }

func (TrustAnchorSourceData0PropertiesOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*TrustAnchorSourceData0Properties)(nil)).Elem()
}

func (o TrustAnchorSourceData0PropertiesOutput) ToTrustAnchorSourceData0PropertiesOutput() TrustAnchorSourceData0PropertiesOutput {
	return o
}

func (o TrustAnchorSourceData0PropertiesOutput) ToTrustAnchorSourceData0PropertiesOutputWithContext(ctx context.Context) TrustAnchorSourceData0PropertiesOutput {
	return o
}

func (o TrustAnchorSourceData0PropertiesOutput) ToTrustAnchorSourceData0PropertiesPtrOutput() TrustAnchorSourceData0PropertiesPtrOutput {
	return o.ToTrustAnchorSourceData0PropertiesPtrOutputWithContext(context.Background())
}

func (o TrustAnchorSourceData0PropertiesOutput) ToTrustAnchorSourceData0PropertiesPtrOutputWithContext(ctx context.Context) TrustAnchorSourceData0PropertiesPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v TrustAnchorSourceData0Properties) *TrustAnchorSourceData0Properties {
		return &v
	}).(TrustAnchorSourceData0PropertiesPtrOutput)
}

func (o TrustAnchorSourceData0PropertiesOutput) X509CertificateData() pulumi.StringOutput {
	return o.ApplyT(func(v TrustAnchorSourceData0Properties) string { return v.X509CertificateData }).(pulumi.StringOutput)
}

type TrustAnchorSourceData0PropertiesPtrOutput struct{ *pulumi.OutputState }

func (TrustAnchorSourceData0PropertiesPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**TrustAnchorSourceData0Properties)(nil)).Elem()
}

func (o TrustAnchorSourceData0PropertiesPtrOutput) ToTrustAnchorSourceData0PropertiesPtrOutput() TrustAnchorSourceData0PropertiesPtrOutput {
	return o
}

func (o TrustAnchorSourceData0PropertiesPtrOutput) ToTrustAnchorSourceData0PropertiesPtrOutputWithContext(ctx context.Context) TrustAnchorSourceData0PropertiesPtrOutput {
	return o
}

func (o TrustAnchorSourceData0PropertiesPtrOutput) Elem() TrustAnchorSourceData0PropertiesOutput {
	return o.ApplyT(func(v *TrustAnchorSourceData0Properties) TrustAnchorSourceData0Properties {
		if v != nil {
			return *v
		}
		var ret TrustAnchorSourceData0Properties
		return ret
	}).(TrustAnchorSourceData0PropertiesOutput)
}

func (o TrustAnchorSourceData0PropertiesPtrOutput) X509CertificateData() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *TrustAnchorSourceData0Properties) *string {
		if v == nil {
			return nil
		}
		return &v.X509CertificateData
	}).(pulumi.StringPtrOutput)
}

type TrustAnchorSourceData1Properties struct {
	AcmPcaArn string `pulumi:"acmPcaArn"`
}

// TrustAnchorSourceData1PropertiesInput is an input type that accepts TrustAnchorSourceData1PropertiesArgs and TrustAnchorSourceData1PropertiesOutput values.
// You can construct a concrete instance of `TrustAnchorSourceData1PropertiesInput` via:
//
//	TrustAnchorSourceData1PropertiesArgs{...}
type TrustAnchorSourceData1PropertiesInput interface {
	pulumi.Input

	ToTrustAnchorSourceData1PropertiesOutput() TrustAnchorSourceData1PropertiesOutput
	ToTrustAnchorSourceData1PropertiesOutputWithContext(context.Context) TrustAnchorSourceData1PropertiesOutput
}

type TrustAnchorSourceData1PropertiesArgs struct {
	AcmPcaArn pulumi.StringInput `pulumi:"acmPcaArn"`
}

func (TrustAnchorSourceData1PropertiesArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*TrustAnchorSourceData1Properties)(nil)).Elem()
}

func (i TrustAnchorSourceData1PropertiesArgs) ToTrustAnchorSourceData1PropertiesOutput() TrustAnchorSourceData1PropertiesOutput {
	return i.ToTrustAnchorSourceData1PropertiesOutputWithContext(context.Background())
}

func (i TrustAnchorSourceData1PropertiesArgs) ToTrustAnchorSourceData1PropertiesOutputWithContext(ctx context.Context) TrustAnchorSourceData1PropertiesOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TrustAnchorSourceData1PropertiesOutput)
}

func (i TrustAnchorSourceData1PropertiesArgs) ToTrustAnchorSourceData1PropertiesPtrOutput() TrustAnchorSourceData1PropertiesPtrOutput {
	return i.ToTrustAnchorSourceData1PropertiesPtrOutputWithContext(context.Background())
}

func (i TrustAnchorSourceData1PropertiesArgs) ToTrustAnchorSourceData1PropertiesPtrOutputWithContext(ctx context.Context) TrustAnchorSourceData1PropertiesPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TrustAnchorSourceData1PropertiesOutput).ToTrustAnchorSourceData1PropertiesPtrOutputWithContext(ctx)
}

// TrustAnchorSourceData1PropertiesPtrInput is an input type that accepts TrustAnchorSourceData1PropertiesArgs, TrustAnchorSourceData1PropertiesPtr and TrustAnchorSourceData1PropertiesPtrOutput values.
// You can construct a concrete instance of `TrustAnchorSourceData1PropertiesPtrInput` via:
//
//	        TrustAnchorSourceData1PropertiesArgs{...}
//
//	or:
//
//	        nil
type TrustAnchorSourceData1PropertiesPtrInput interface {
	pulumi.Input

	ToTrustAnchorSourceData1PropertiesPtrOutput() TrustAnchorSourceData1PropertiesPtrOutput
	ToTrustAnchorSourceData1PropertiesPtrOutputWithContext(context.Context) TrustAnchorSourceData1PropertiesPtrOutput
}

type trustAnchorSourceData1PropertiesPtrType TrustAnchorSourceData1PropertiesArgs

func TrustAnchorSourceData1PropertiesPtr(v *TrustAnchorSourceData1PropertiesArgs) TrustAnchorSourceData1PropertiesPtrInput {
	return (*trustAnchorSourceData1PropertiesPtrType)(v)
}

func (*trustAnchorSourceData1PropertiesPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**TrustAnchorSourceData1Properties)(nil)).Elem()
}

func (i *trustAnchorSourceData1PropertiesPtrType) ToTrustAnchorSourceData1PropertiesPtrOutput() TrustAnchorSourceData1PropertiesPtrOutput {
	return i.ToTrustAnchorSourceData1PropertiesPtrOutputWithContext(context.Background())
}

func (i *trustAnchorSourceData1PropertiesPtrType) ToTrustAnchorSourceData1PropertiesPtrOutputWithContext(ctx context.Context) TrustAnchorSourceData1PropertiesPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TrustAnchorSourceData1PropertiesPtrOutput)
}

type TrustAnchorSourceData1PropertiesOutput struct{ *pulumi.OutputState }

func (TrustAnchorSourceData1PropertiesOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*TrustAnchorSourceData1Properties)(nil)).Elem()
}

func (o TrustAnchorSourceData1PropertiesOutput) ToTrustAnchorSourceData1PropertiesOutput() TrustAnchorSourceData1PropertiesOutput {
	return o
}

func (o TrustAnchorSourceData1PropertiesOutput) ToTrustAnchorSourceData1PropertiesOutputWithContext(ctx context.Context) TrustAnchorSourceData1PropertiesOutput {
	return o
}

func (o TrustAnchorSourceData1PropertiesOutput) ToTrustAnchorSourceData1PropertiesPtrOutput() TrustAnchorSourceData1PropertiesPtrOutput {
	return o.ToTrustAnchorSourceData1PropertiesPtrOutputWithContext(context.Background())
}

func (o TrustAnchorSourceData1PropertiesOutput) ToTrustAnchorSourceData1PropertiesPtrOutputWithContext(ctx context.Context) TrustAnchorSourceData1PropertiesPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v TrustAnchorSourceData1Properties) *TrustAnchorSourceData1Properties {
		return &v
	}).(TrustAnchorSourceData1PropertiesPtrOutput)
}

func (o TrustAnchorSourceData1PropertiesOutput) AcmPcaArn() pulumi.StringOutput {
	return o.ApplyT(func(v TrustAnchorSourceData1Properties) string { return v.AcmPcaArn }).(pulumi.StringOutput)
}

type TrustAnchorSourceData1PropertiesPtrOutput struct{ *pulumi.OutputState }

func (TrustAnchorSourceData1PropertiesPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**TrustAnchorSourceData1Properties)(nil)).Elem()
}

func (o TrustAnchorSourceData1PropertiesPtrOutput) ToTrustAnchorSourceData1PropertiesPtrOutput() TrustAnchorSourceData1PropertiesPtrOutput {
	return o
}

func (o TrustAnchorSourceData1PropertiesPtrOutput) ToTrustAnchorSourceData1PropertiesPtrOutputWithContext(ctx context.Context) TrustAnchorSourceData1PropertiesPtrOutput {
	return o
}

func (o TrustAnchorSourceData1PropertiesPtrOutput) Elem() TrustAnchorSourceData1PropertiesOutput {
	return o.ApplyT(func(v *TrustAnchorSourceData1Properties) TrustAnchorSourceData1Properties {
		if v != nil {
			return *v
		}
		var ret TrustAnchorSourceData1Properties
		return ret
	}).(TrustAnchorSourceData1PropertiesOutput)
}

func (o TrustAnchorSourceData1PropertiesPtrOutput) AcmPcaArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *TrustAnchorSourceData1Properties) *string {
		if v == nil {
			return nil
		}
		return &v.AcmPcaArn
	}).(pulumi.StringPtrOutput)
}

type TrustAnchorTag struct {
	Key   string `pulumi:"key"`
	Value string `pulumi:"value"`
}

// TrustAnchorTagInput is an input type that accepts TrustAnchorTagArgs and TrustAnchorTagOutput values.
// You can construct a concrete instance of `TrustAnchorTagInput` via:
//
//	TrustAnchorTagArgs{...}
type TrustAnchorTagInput interface {
	pulumi.Input

	ToTrustAnchorTagOutput() TrustAnchorTagOutput
	ToTrustAnchorTagOutputWithContext(context.Context) TrustAnchorTagOutput
}

type TrustAnchorTagArgs struct {
	Key   pulumi.StringInput `pulumi:"key"`
	Value pulumi.StringInput `pulumi:"value"`
}

func (TrustAnchorTagArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*TrustAnchorTag)(nil)).Elem()
}

func (i TrustAnchorTagArgs) ToTrustAnchorTagOutput() TrustAnchorTagOutput {
	return i.ToTrustAnchorTagOutputWithContext(context.Background())
}

func (i TrustAnchorTagArgs) ToTrustAnchorTagOutputWithContext(ctx context.Context) TrustAnchorTagOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TrustAnchorTagOutput)
}

// TrustAnchorTagArrayInput is an input type that accepts TrustAnchorTagArray and TrustAnchorTagArrayOutput values.
// You can construct a concrete instance of `TrustAnchorTagArrayInput` via:
//
//	TrustAnchorTagArray{ TrustAnchorTagArgs{...} }
type TrustAnchorTagArrayInput interface {
	pulumi.Input

	ToTrustAnchorTagArrayOutput() TrustAnchorTagArrayOutput
	ToTrustAnchorTagArrayOutputWithContext(context.Context) TrustAnchorTagArrayOutput
}

type TrustAnchorTagArray []TrustAnchorTagInput

func (TrustAnchorTagArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]TrustAnchorTag)(nil)).Elem()
}

func (i TrustAnchorTagArray) ToTrustAnchorTagArrayOutput() TrustAnchorTagArrayOutput {
	return i.ToTrustAnchorTagArrayOutputWithContext(context.Background())
}

func (i TrustAnchorTagArray) ToTrustAnchorTagArrayOutputWithContext(ctx context.Context) TrustAnchorTagArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TrustAnchorTagArrayOutput)
}

type TrustAnchorTagOutput struct{ *pulumi.OutputState }

func (TrustAnchorTagOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*TrustAnchorTag)(nil)).Elem()
}

func (o TrustAnchorTagOutput) ToTrustAnchorTagOutput() TrustAnchorTagOutput {
	return o
}

func (o TrustAnchorTagOutput) ToTrustAnchorTagOutputWithContext(ctx context.Context) TrustAnchorTagOutput {
	return o
}

func (o TrustAnchorTagOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v TrustAnchorTag) string { return v.Key }).(pulumi.StringOutput)
}

func (o TrustAnchorTagOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v TrustAnchorTag) string { return v.Value }).(pulumi.StringOutput)
}

type TrustAnchorTagArrayOutput struct{ *pulumi.OutputState }

func (TrustAnchorTagArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]TrustAnchorTag)(nil)).Elem()
}

func (o TrustAnchorTagArrayOutput) ToTrustAnchorTagArrayOutput() TrustAnchorTagArrayOutput {
	return o
}

func (o TrustAnchorTagArrayOutput) ToTrustAnchorTagArrayOutputWithContext(ctx context.Context) TrustAnchorTagArrayOutput {
	return o
}

func (o TrustAnchorTagArrayOutput) Index(i pulumi.IntInput) TrustAnchorTagOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) TrustAnchorTag {
		return vs[0].([]TrustAnchorTag)[vs[1].(int)]
	}).(TrustAnchorTagOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*CrlTagInput)(nil)).Elem(), CrlTagArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*CrlTagArrayInput)(nil)).Elem(), CrlTagArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ProfileTagInput)(nil)).Elem(), ProfileTagArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*ProfileTagArrayInput)(nil)).Elem(), ProfileTagArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*TrustAnchorNotificationSettingInput)(nil)).Elem(), TrustAnchorNotificationSettingArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*TrustAnchorNotificationSettingArrayInput)(nil)).Elem(), TrustAnchorNotificationSettingArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*TrustAnchorSourceInput)(nil)).Elem(), TrustAnchorSourceArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*TrustAnchorSourceData0PropertiesInput)(nil)).Elem(), TrustAnchorSourceData0PropertiesArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*TrustAnchorSourceData0PropertiesPtrInput)(nil)).Elem(), TrustAnchorSourceData0PropertiesArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*TrustAnchorSourceData1PropertiesInput)(nil)).Elem(), TrustAnchorSourceData1PropertiesArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*TrustAnchorSourceData1PropertiesPtrInput)(nil)).Elem(), TrustAnchorSourceData1PropertiesArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*TrustAnchorTagInput)(nil)).Elem(), TrustAnchorTagArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*TrustAnchorTagArrayInput)(nil)).Elem(), TrustAnchorTagArray{})
	pulumi.RegisterOutputType(CrlTagOutput{})
	pulumi.RegisterOutputType(CrlTagArrayOutput{})
	pulumi.RegisterOutputType(ProfileTagOutput{})
	pulumi.RegisterOutputType(ProfileTagArrayOutput{})
	pulumi.RegisterOutputType(TrustAnchorNotificationSettingOutput{})
	pulumi.RegisterOutputType(TrustAnchorNotificationSettingArrayOutput{})
	pulumi.RegisterOutputType(TrustAnchorSourceOutput{})
	pulumi.RegisterOutputType(TrustAnchorSourcePtrOutput{})
	pulumi.RegisterOutputType(TrustAnchorSourceData0PropertiesOutput{})
	pulumi.RegisterOutputType(TrustAnchorSourceData0PropertiesPtrOutput{})
	pulumi.RegisterOutputType(TrustAnchorSourceData1PropertiesOutput{})
	pulumi.RegisterOutputType(TrustAnchorSourceData1PropertiesPtrOutput{})
	pulumi.RegisterOutputType(TrustAnchorTagOutput{})
	pulumi.RegisterOutputType(TrustAnchorTagArrayOutput{})
}
