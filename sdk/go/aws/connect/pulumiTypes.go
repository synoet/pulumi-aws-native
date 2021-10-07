// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package connect

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Configuration settings for the quick connect.
type QuickConnectConfig struct {
	PhoneConfig      *QuickConnectPhoneNumberQuickConnectConfig `pulumi:"phoneConfig"`
	QueueConfig      *QuickConnectQueueQuickConnectConfig       `pulumi:"queueConfig"`
	QuickConnectType QuickConnectType                           `pulumi:"quickConnectType"`
	UserConfig       *QuickConnectUserQuickConnectConfig        `pulumi:"userConfig"`
}

// QuickConnectConfigInput is an input type that accepts QuickConnectConfigArgs and QuickConnectConfigOutput values.
// You can construct a concrete instance of `QuickConnectConfigInput` via:
//
//          QuickConnectConfigArgs{...}
type QuickConnectConfigInput interface {
	pulumi.Input

	ToQuickConnectConfigOutput() QuickConnectConfigOutput
	ToQuickConnectConfigOutputWithContext(context.Context) QuickConnectConfigOutput
}

// Configuration settings for the quick connect.
type QuickConnectConfigArgs struct {
	PhoneConfig      QuickConnectPhoneNumberQuickConnectConfigPtrInput `pulumi:"phoneConfig"`
	QueueConfig      QuickConnectQueueQuickConnectConfigPtrInput       `pulumi:"queueConfig"`
	QuickConnectType QuickConnectTypeInput                             `pulumi:"quickConnectType"`
	UserConfig       QuickConnectUserQuickConnectConfigPtrInput        `pulumi:"userConfig"`
}

func (QuickConnectConfigArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*QuickConnectConfig)(nil)).Elem()
}

func (i QuickConnectConfigArgs) ToQuickConnectConfigOutput() QuickConnectConfigOutput {
	return i.ToQuickConnectConfigOutputWithContext(context.Background())
}

func (i QuickConnectConfigArgs) ToQuickConnectConfigOutputWithContext(ctx context.Context) QuickConnectConfigOutput {
	return pulumi.ToOutputWithContext(ctx, i).(QuickConnectConfigOutput)
}

func (i QuickConnectConfigArgs) ToQuickConnectConfigPtrOutput() QuickConnectConfigPtrOutput {
	return i.ToQuickConnectConfigPtrOutputWithContext(context.Background())
}

func (i QuickConnectConfigArgs) ToQuickConnectConfigPtrOutputWithContext(ctx context.Context) QuickConnectConfigPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(QuickConnectConfigOutput).ToQuickConnectConfigPtrOutputWithContext(ctx)
}

// QuickConnectConfigPtrInput is an input type that accepts QuickConnectConfigArgs, QuickConnectConfigPtr and QuickConnectConfigPtrOutput values.
// You can construct a concrete instance of `QuickConnectConfigPtrInput` via:
//
//          QuickConnectConfigArgs{...}
//
//  or:
//
//          nil
type QuickConnectConfigPtrInput interface {
	pulumi.Input

	ToQuickConnectConfigPtrOutput() QuickConnectConfigPtrOutput
	ToQuickConnectConfigPtrOutputWithContext(context.Context) QuickConnectConfigPtrOutput
}

type quickConnectConfigPtrType QuickConnectConfigArgs

func QuickConnectConfigPtr(v *QuickConnectConfigArgs) QuickConnectConfigPtrInput {
	return (*quickConnectConfigPtrType)(v)
}

func (*quickConnectConfigPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**QuickConnectConfig)(nil)).Elem()
}

func (i *quickConnectConfigPtrType) ToQuickConnectConfigPtrOutput() QuickConnectConfigPtrOutput {
	return i.ToQuickConnectConfigPtrOutputWithContext(context.Background())
}

func (i *quickConnectConfigPtrType) ToQuickConnectConfigPtrOutputWithContext(ctx context.Context) QuickConnectConfigPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(QuickConnectConfigPtrOutput)
}

// Configuration settings for the quick connect.
type QuickConnectConfigOutput struct{ *pulumi.OutputState }

func (QuickConnectConfigOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*QuickConnectConfig)(nil)).Elem()
}

func (o QuickConnectConfigOutput) ToQuickConnectConfigOutput() QuickConnectConfigOutput {
	return o
}

func (o QuickConnectConfigOutput) ToQuickConnectConfigOutputWithContext(ctx context.Context) QuickConnectConfigOutput {
	return o
}

func (o QuickConnectConfigOutput) ToQuickConnectConfigPtrOutput() QuickConnectConfigPtrOutput {
	return o.ToQuickConnectConfigPtrOutputWithContext(context.Background())
}

func (o QuickConnectConfigOutput) ToQuickConnectConfigPtrOutputWithContext(ctx context.Context) QuickConnectConfigPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v QuickConnectConfig) *QuickConnectConfig {
		return &v
	}).(QuickConnectConfigPtrOutput)
}

func (o QuickConnectConfigOutput) PhoneConfig() QuickConnectPhoneNumberQuickConnectConfigPtrOutput {
	return o.ApplyT(func(v QuickConnectConfig) *QuickConnectPhoneNumberQuickConnectConfig { return v.PhoneConfig }).(QuickConnectPhoneNumberQuickConnectConfigPtrOutput)
}

func (o QuickConnectConfigOutput) QueueConfig() QuickConnectQueueQuickConnectConfigPtrOutput {
	return o.ApplyT(func(v QuickConnectConfig) *QuickConnectQueueQuickConnectConfig { return v.QueueConfig }).(QuickConnectQueueQuickConnectConfigPtrOutput)
}

func (o QuickConnectConfigOutput) QuickConnectType() QuickConnectTypeOutput {
	return o.ApplyT(func(v QuickConnectConfig) QuickConnectType { return v.QuickConnectType }).(QuickConnectTypeOutput)
}

func (o QuickConnectConfigOutput) UserConfig() QuickConnectUserQuickConnectConfigPtrOutput {
	return o.ApplyT(func(v QuickConnectConfig) *QuickConnectUserQuickConnectConfig { return v.UserConfig }).(QuickConnectUserQuickConnectConfigPtrOutput)
}

type QuickConnectConfigPtrOutput struct{ *pulumi.OutputState }

func (QuickConnectConfigPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**QuickConnectConfig)(nil)).Elem()
}

func (o QuickConnectConfigPtrOutput) ToQuickConnectConfigPtrOutput() QuickConnectConfigPtrOutput {
	return o
}

func (o QuickConnectConfigPtrOutput) ToQuickConnectConfigPtrOutputWithContext(ctx context.Context) QuickConnectConfigPtrOutput {
	return o
}

func (o QuickConnectConfigPtrOutput) Elem() QuickConnectConfigOutput {
	return o.ApplyT(func(v *QuickConnectConfig) QuickConnectConfig {
		if v != nil {
			return *v
		}
		var ret QuickConnectConfig
		return ret
	}).(QuickConnectConfigOutput)
}

func (o QuickConnectConfigPtrOutput) PhoneConfig() QuickConnectPhoneNumberQuickConnectConfigPtrOutput {
	return o.ApplyT(func(v *QuickConnectConfig) *QuickConnectPhoneNumberQuickConnectConfig {
		if v == nil {
			return nil
		}
		return v.PhoneConfig
	}).(QuickConnectPhoneNumberQuickConnectConfigPtrOutput)
}

func (o QuickConnectConfigPtrOutput) QueueConfig() QuickConnectQueueQuickConnectConfigPtrOutput {
	return o.ApplyT(func(v *QuickConnectConfig) *QuickConnectQueueQuickConnectConfig {
		if v == nil {
			return nil
		}
		return v.QueueConfig
	}).(QuickConnectQueueQuickConnectConfigPtrOutput)
}

func (o QuickConnectConfigPtrOutput) QuickConnectType() QuickConnectTypePtrOutput {
	return o.ApplyT(func(v *QuickConnectConfig) *QuickConnectType {
		if v == nil {
			return nil
		}
		return &v.QuickConnectType
	}).(QuickConnectTypePtrOutput)
}

func (o QuickConnectConfigPtrOutput) UserConfig() QuickConnectUserQuickConnectConfigPtrOutput {
	return o.ApplyT(func(v *QuickConnectConfig) *QuickConnectUserQuickConnectConfig {
		if v == nil {
			return nil
		}
		return v.UserConfig
	}).(QuickConnectUserQuickConnectConfigPtrOutput)
}

// The phone configuration. This is required only if QuickConnectType is PHONE_NUMBER.
type QuickConnectPhoneNumberQuickConnectConfig struct {
	PhoneNumber string `pulumi:"phoneNumber"`
}

// QuickConnectPhoneNumberQuickConnectConfigInput is an input type that accepts QuickConnectPhoneNumberQuickConnectConfigArgs and QuickConnectPhoneNumberQuickConnectConfigOutput values.
// You can construct a concrete instance of `QuickConnectPhoneNumberQuickConnectConfigInput` via:
//
//          QuickConnectPhoneNumberQuickConnectConfigArgs{...}
type QuickConnectPhoneNumberQuickConnectConfigInput interface {
	pulumi.Input

	ToQuickConnectPhoneNumberQuickConnectConfigOutput() QuickConnectPhoneNumberQuickConnectConfigOutput
	ToQuickConnectPhoneNumberQuickConnectConfigOutputWithContext(context.Context) QuickConnectPhoneNumberQuickConnectConfigOutput
}

// The phone configuration. This is required only if QuickConnectType is PHONE_NUMBER.
type QuickConnectPhoneNumberQuickConnectConfigArgs struct {
	PhoneNumber pulumi.StringInput `pulumi:"phoneNumber"`
}

func (QuickConnectPhoneNumberQuickConnectConfigArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*QuickConnectPhoneNumberQuickConnectConfig)(nil)).Elem()
}

func (i QuickConnectPhoneNumberQuickConnectConfigArgs) ToQuickConnectPhoneNumberQuickConnectConfigOutput() QuickConnectPhoneNumberQuickConnectConfigOutput {
	return i.ToQuickConnectPhoneNumberQuickConnectConfigOutputWithContext(context.Background())
}

func (i QuickConnectPhoneNumberQuickConnectConfigArgs) ToQuickConnectPhoneNumberQuickConnectConfigOutputWithContext(ctx context.Context) QuickConnectPhoneNumberQuickConnectConfigOutput {
	return pulumi.ToOutputWithContext(ctx, i).(QuickConnectPhoneNumberQuickConnectConfigOutput)
}

func (i QuickConnectPhoneNumberQuickConnectConfigArgs) ToQuickConnectPhoneNumberQuickConnectConfigPtrOutput() QuickConnectPhoneNumberQuickConnectConfigPtrOutput {
	return i.ToQuickConnectPhoneNumberQuickConnectConfigPtrOutputWithContext(context.Background())
}

func (i QuickConnectPhoneNumberQuickConnectConfigArgs) ToQuickConnectPhoneNumberQuickConnectConfigPtrOutputWithContext(ctx context.Context) QuickConnectPhoneNumberQuickConnectConfigPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(QuickConnectPhoneNumberQuickConnectConfigOutput).ToQuickConnectPhoneNumberQuickConnectConfigPtrOutputWithContext(ctx)
}

// QuickConnectPhoneNumberQuickConnectConfigPtrInput is an input type that accepts QuickConnectPhoneNumberQuickConnectConfigArgs, QuickConnectPhoneNumberQuickConnectConfigPtr and QuickConnectPhoneNumberQuickConnectConfigPtrOutput values.
// You can construct a concrete instance of `QuickConnectPhoneNumberQuickConnectConfigPtrInput` via:
//
//          QuickConnectPhoneNumberQuickConnectConfigArgs{...}
//
//  or:
//
//          nil
type QuickConnectPhoneNumberQuickConnectConfigPtrInput interface {
	pulumi.Input

	ToQuickConnectPhoneNumberQuickConnectConfigPtrOutput() QuickConnectPhoneNumberQuickConnectConfigPtrOutput
	ToQuickConnectPhoneNumberQuickConnectConfigPtrOutputWithContext(context.Context) QuickConnectPhoneNumberQuickConnectConfigPtrOutput
}

type quickConnectPhoneNumberQuickConnectConfigPtrType QuickConnectPhoneNumberQuickConnectConfigArgs

func QuickConnectPhoneNumberQuickConnectConfigPtr(v *QuickConnectPhoneNumberQuickConnectConfigArgs) QuickConnectPhoneNumberQuickConnectConfigPtrInput {
	return (*quickConnectPhoneNumberQuickConnectConfigPtrType)(v)
}

func (*quickConnectPhoneNumberQuickConnectConfigPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**QuickConnectPhoneNumberQuickConnectConfig)(nil)).Elem()
}

func (i *quickConnectPhoneNumberQuickConnectConfigPtrType) ToQuickConnectPhoneNumberQuickConnectConfigPtrOutput() QuickConnectPhoneNumberQuickConnectConfigPtrOutput {
	return i.ToQuickConnectPhoneNumberQuickConnectConfigPtrOutputWithContext(context.Background())
}

func (i *quickConnectPhoneNumberQuickConnectConfigPtrType) ToQuickConnectPhoneNumberQuickConnectConfigPtrOutputWithContext(ctx context.Context) QuickConnectPhoneNumberQuickConnectConfigPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(QuickConnectPhoneNumberQuickConnectConfigPtrOutput)
}

// The phone configuration. This is required only if QuickConnectType is PHONE_NUMBER.
type QuickConnectPhoneNumberQuickConnectConfigOutput struct{ *pulumi.OutputState }

func (QuickConnectPhoneNumberQuickConnectConfigOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*QuickConnectPhoneNumberQuickConnectConfig)(nil)).Elem()
}

func (o QuickConnectPhoneNumberQuickConnectConfigOutput) ToQuickConnectPhoneNumberQuickConnectConfigOutput() QuickConnectPhoneNumberQuickConnectConfigOutput {
	return o
}

func (o QuickConnectPhoneNumberQuickConnectConfigOutput) ToQuickConnectPhoneNumberQuickConnectConfigOutputWithContext(ctx context.Context) QuickConnectPhoneNumberQuickConnectConfigOutput {
	return o
}

func (o QuickConnectPhoneNumberQuickConnectConfigOutput) ToQuickConnectPhoneNumberQuickConnectConfigPtrOutput() QuickConnectPhoneNumberQuickConnectConfigPtrOutput {
	return o.ToQuickConnectPhoneNumberQuickConnectConfigPtrOutputWithContext(context.Background())
}

func (o QuickConnectPhoneNumberQuickConnectConfigOutput) ToQuickConnectPhoneNumberQuickConnectConfigPtrOutputWithContext(ctx context.Context) QuickConnectPhoneNumberQuickConnectConfigPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v QuickConnectPhoneNumberQuickConnectConfig) *QuickConnectPhoneNumberQuickConnectConfig {
		return &v
	}).(QuickConnectPhoneNumberQuickConnectConfigPtrOutput)
}

func (o QuickConnectPhoneNumberQuickConnectConfigOutput) PhoneNumber() pulumi.StringOutput {
	return o.ApplyT(func(v QuickConnectPhoneNumberQuickConnectConfig) string { return v.PhoneNumber }).(pulumi.StringOutput)
}

type QuickConnectPhoneNumberQuickConnectConfigPtrOutput struct{ *pulumi.OutputState }

func (QuickConnectPhoneNumberQuickConnectConfigPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**QuickConnectPhoneNumberQuickConnectConfig)(nil)).Elem()
}

func (o QuickConnectPhoneNumberQuickConnectConfigPtrOutput) ToQuickConnectPhoneNumberQuickConnectConfigPtrOutput() QuickConnectPhoneNumberQuickConnectConfigPtrOutput {
	return o
}

func (o QuickConnectPhoneNumberQuickConnectConfigPtrOutput) ToQuickConnectPhoneNumberQuickConnectConfigPtrOutputWithContext(ctx context.Context) QuickConnectPhoneNumberQuickConnectConfigPtrOutput {
	return o
}

func (o QuickConnectPhoneNumberQuickConnectConfigPtrOutput) Elem() QuickConnectPhoneNumberQuickConnectConfigOutput {
	return o.ApplyT(func(v *QuickConnectPhoneNumberQuickConnectConfig) QuickConnectPhoneNumberQuickConnectConfig {
		if v != nil {
			return *v
		}
		var ret QuickConnectPhoneNumberQuickConnectConfig
		return ret
	}).(QuickConnectPhoneNumberQuickConnectConfigOutput)
}

func (o QuickConnectPhoneNumberQuickConnectConfigPtrOutput) PhoneNumber() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *QuickConnectPhoneNumberQuickConnectConfig) *string {
		if v == nil {
			return nil
		}
		return &v.PhoneNumber
	}).(pulumi.StringPtrOutput)
}

// The queue configuration. This is required only if QuickConnectType is QUEUE.
type QuickConnectQueueQuickConnectConfig struct {
	ContactFlowArn string `pulumi:"contactFlowArn"`
	QueueArn       string `pulumi:"queueArn"`
}

// QuickConnectQueueQuickConnectConfigInput is an input type that accepts QuickConnectQueueQuickConnectConfigArgs and QuickConnectQueueQuickConnectConfigOutput values.
// You can construct a concrete instance of `QuickConnectQueueQuickConnectConfigInput` via:
//
//          QuickConnectQueueQuickConnectConfigArgs{...}
type QuickConnectQueueQuickConnectConfigInput interface {
	pulumi.Input

	ToQuickConnectQueueQuickConnectConfigOutput() QuickConnectQueueQuickConnectConfigOutput
	ToQuickConnectQueueQuickConnectConfigOutputWithContext(context.Context) QuickConnectQueueQuickConnectConfigOutput
}

// The queue configuration. This is required only if QuickConnectType is QUEUE.
type QuickConnectQueueQuickConnectConfigArgs struct {
	ContactFlowArn pulumi.StringInput `pulumi:"contactFlowArn"`
	QueueArn       pulumi.StringInput `pulumi:"queueArn"`
}

func (QuickConnectQueueQuickConnectConfigArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*QuickConnectQueueQuickConnectConfig)(nil)).Elem()
}

func (i QuickConnectQueueQuickConnectConfigArgs) ToQuickConnectQueueQuickConnectConfigOutput() QuickConnectQueueQuickConnectConfigOutput {
	return i.ToQuickConnectQueueQuickConnectConfigOutputWithContext(context.Background())
}

func (i QuickConnectQueueQuickConnectConfigArgs) ToQuickConnectQueueQuickConnectConfigOutputWithContext(ctx context.Context) QuickConnectQueueQuickConnectConfigOutput {
	return pulumi.ToOutputWithContext(ctx, i).(QuickConnectQueueQuickConnectConfigOutput)
}

func (i QuickConnectQueueQuickConnectConfigArgs) ToQuickConnectQueueQuickConnectConfigPtrOutput() QuickConnectQueueQuickConnectConfigPtrOutput {
	return i.ToQuickConnectQueueQuickConnectConfigPtrOutputWithContext(context.Background())
}

func (i QuickConnectQueueQuickConnectConfigArgs) ToQuickConnectQueueQuickConnectConfigPtrOutputWithContext(ctx context.Context) QuickConnectQueueQuickConnectConfigPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(QuickConnectQueueQuickConnectConfigOutput).ToQuickConnectQueueQuickConnectConfigPtrOutputWithContext(ctx)
}

// QuickConnectQueueQuickConnectConfigPtrInput is an input type that accepts QuickConnectQueueQuickConnectConfigArgs, QuickConnectQueueQuickConnectConfigPtr and QuickConnectQueueQuickConnectConfigPtrOutput values.
// You can construct a concrete instance of `QuickConnectQueueQuickConnectConfigPtrInput` via:
//
//          QuickConnectQueueQuickConnectConfigArgs{...}
//
//  or:
//
//          nil
type QuickConnectQueueQuickConnectConfigPtrInput interface {
	pulumi.Input

	ToQuickConnectQueueQuickConnectConfigPtrOutput() QuickConnectQueueQuickConnectConfigPtrOutput
	ToQuickConnectQueueQuickConnectConfigPtrOutputWithContext(context.Context) QuickConnectQueueQuickConnectConfigPtrOutput
}

type quickConnectQueueQuickConnectConfigPtrType QuickConnectQueueQuickConnectConfigArgs

func QuickConnectQueueQuickConnectConfigPtr(v *QuickConnectQueueQuickConnectConfigArgs) QuickConnectQueueQuickConnectConfigPtrInput {
	return (*quickConnectQueueQuickConnectConfigPtrType)(v)
}

func (*quickConnectQueueQuickConnectConfigPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**QuickConnectQueueQuickConnectConfig)(nil)).Elem()
}

func (i *quickConnectQueueQuickConnectConfigPtrType) ToQuickConnectQueueQuickConnectConfigPtrOutput() QuickConnectQueueQuickConnectConfigPtrOutput {
	return i.ToQuickConnectQueueQuickConnectConfigPtrOutputWithContext(context.Background())
}

func (i *quickConnectQueueQuickConnectConfigPtrType) ToQuickConnectQueueQuickConnectConfigPtrOutputWithContext(ctx context.Context) QuickConnectQueueQuickConnectConfigPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(QuickConnectQueueQuickConnectConfigPtrOutput)
}

// The queue configuration. This is required only if QuickConnectType is QUEUE.
type QuickConnectQueueQuickConnectConfigOutput struct{ *pulumi.OutputState }

func (QuickConnectQueueQuickConnectConfigOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*QuickConnectQueueQuickConnectConfig)(nil)).Elem()
}

func (o QuickConnectQueueQuickConnectConfigOutput) ToQuickConnectQueueQuickConnectConfigOutput() QuickConnectQueueQuickConnectConfigOutput {
	return o
}

func (o QuickConnectQueueQuickConnectConfigOutput) ToQuickConnectQueueQuickConnectConfigOutputWithContext(ctx context.Context) QuickConnectQueueQuickConnectConfigOutput {
	return o
}

func (o QuickConnectQueueQuickConnectConfigOutput) ToQuickConnectQueueQuickConnectConfigPtrOutput() QuickConnectQueueQuickConnectConfigPtrOutput {
	return o.ToQuickConnectQueueQuickConnectConfigPtrOutputWithContext(context.Background())
}

func (o QuickConnectQueueQuickConnectConfigOutput) ToQuickConnectQueueQuickConnectConfigPtrOutputWithContext(ctx context.Context) QuickConnectQueueQuickConnectConfigPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v QuickConnectQueueQuickConnectConfig) *QuickConnectQueueQuickConnectConfig {
		return &v
	}).(QuickConnectQueueQuickConnectConfigPtrOutput)
}

func (o QuickConnectQueueQuickConnectConfigOutput) ContactFlowArn() pulumi.StringOutput {
	return o.ApplyT(func(v QuickConnectQueueQuickConnectConfig) string { return v.ContactFlowArn }).(pulumi.StringOutput)
}

func (o QuickConnectQueueQuickConnectConfigOutput) QueueArn() pulumi.StringOutput {
	return o.ApplyT(func(v QuickConnectQueueQuickConnectConfig) string { return v.QueueArn }).(pulumi.StringOutput)
}

type QuickConnectQueueQuickConnectConfigPtrOutput struct{ *pulumi.OutputState }

func (QuickConnectQueueQuickConnectConfigPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**QuickConnectQueueQuickConnectConfig)(nil)).Elem()
}

func (o QuickConnectQueueQuickConnectConfigPtrOutput) ToQuickConnectQueueQuickConnectConfigPtrOutput() QuickConnectQueueQuickConnectConfigPtrOutput {
	return o
}

func (o QuickConnectQueueQuickConnectConfigPtrOutput) ToQuickConnectQueueQuickConnectConfigPtrOutputWithContext(ctx context.Context) QuickConnectQueueQuickConnectConfigPtrOutput {
	return o
}

func (o QuickConnectQueueQuickConnectConfigPtrOutput) Elem() QuickConnectQueueQuickConnectConfigOutput {
	return o.ApplyT(func(v *QuickConnectQueueQuickConnectConfig) QuickConnectQueueQuickConnectConfig {
		if v != nil {
			return *v
		}
		var ret QuickConnectQueueQuickConnectConfig
		return ret
	}).(QuickConnectQueueQuickConnectConfigOutput)
}

func (o QuickConnectQueueQuickConnectConfigPtrOutput) ContactFlowArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *QuickConnectQueueQuickConnectConfig) *string {
		if v == nil {
			return nil
		}
		return &v.ContactFlowArn
	}).(pulumi.StringPtrOutput)
}

func (o QuickConnectQueueQuickConnectConfigPtrOutput) QueueArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *QuickConnectQueueQuickConnectConfig) *string {
		if v == nil {
			return nil
		}
		return &v.QueueArn
	}).(pulumi.StringPtrOutput)
}

// A key-value pair to associate with a resource.
type QuickConnectTag struct {
	// The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
	Key string `pulumi:"key"`
	// The value for the tag. You can specify a value that is maximum of 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
	Value string `pulumi:"value"`
}

// QuickConnectTagInput is an input type that accepts QuickConnectTagArgs and QuickConnectTagOutput values.
// You can construct a concrete instance of `QuickConnectTagInput` via:
//
//          QuickConnectTagArgs{...}
type QuickConnectTagInput interface {
	pulumi.Input

	ToQuickConnectTagOutput() QuickConnectTagOutput
	ToQuickConnectTagOutputWithContext(context.Context) QuickConnectTagOutput
}

// A key-value pair to associate with a resource.
type QuickConnectTagArgs struct {
	// The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
	Key pulumi.StringInput `pulumi:"key"`
	// The value for the tag. You can specify a value that is maximum of 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
	Value pulumi.StringInput `pulumi:"value"`
}

func (QuickConnectTagArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*QuickConnectTag)(nil)).Elem()
}

func (i QuickConnectTagArgs) ToQuickConnectTagOutput() QuickConnectTagOutput {
	return i.ToQuickConnectTagOutputWithContext(context.Background())
}

func (i QuickConnectTagArgs) ToQuickConnectTagOutputWithContext(ctx context.Context) QuickConnectTagOutput {
	return pulumi.ToOutputWithContext(ctx, i).(QuickConnectTagOutput)
}

// QuickConnectTagArrayInput is an input type that accepts QuickConnectTagArray and QuickConnectTagArrayOutput values.
// You can construct a concrete instance of `QuickConnectTagArrayInput` via:
//
//          QuickConnectTagArray{ QuickConnectTagArgs{...} }
type QuickConnectTagArrayInput interface {
	pulumi.Input

	ToQuickConnectTagArrayOutput() QuickConnectTagArrayOutput
	ToQuickConnectTagArrayOutputWithContext(context.Context) QuickConnectTagArrayOutput
}

type QuickConnectTagArray []QuickConnectTagInput

func (QuickConnectTagArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]QuickConnectTag)(nil)).Elem()
}

func (i QuickConnectTagArray) ToQuickConnectTagArrayOutput() QuickConnectTagArrayOutput {
	return i.ToQuickConnectTagArrayOutputWithContext(context.Background())
}

func (i QuickConnectTagArray) ToQuickConnectTagArrayOutputWithContext(ctx context.Context) QuickConnectTagArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(QuickConnectTagArrayOutput)
}

// A key-value pair to associate with a resource.
type QuickConnectTagOutput struct{ *pulumi.OutputState }

func (QuickConnectTagOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*QuickConnectTag)(nil)).Elem()
}

func (o QuickConnectTagOutput) ToQuickConnectTagOutput() QuickConnectTagOutput {
	return o
}

func (o QuickConnectTagOutput) ToQuickConnectTagOutputWithContext(ctx context.Context) QuickConnectTagOutput {
	return o
}

// The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
func (o QuickConnectTagOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v QuickConnectTag) string { return v.Key }).(pulumi.StringOutput)
}

// The value for the tag. You can specify a value that is maximum of 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
func (o QuickConnectTagOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v QuickConnectTag) string { return v.Value }).(pulumi.StringOutput)
}

type QuickConnectTagArrayOutput struct{ *pulumi.OutputState }

func (QuickConnectTagArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]QuickConnectTag)(nil)).Elem()
}

func (o QuickConnectTagArrayOutput) ToQuickConnectTagArrayOutput() QuickConnectTagArrayOutput {
	return o
}

func (o QuickConnectTagArrayOutput) ToQuickConnectTagArrayOutputWithContext(ctx context.Context) QuickConnectTagArrayOutput {
	return o
}

func (o QuickConnectTagArrayOutput) Index(i pulumi.IntInput) QuickConnectTagOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) QuickConnectTag {
		return vs[0].([]QuickConnectTag)[vs[1].(int)]
	}).(QuickConnectTagOutput)
}

// The user configuration. This is required only if QuickConnectType is USER.
type QuickConnectUserQuickConnectConfig struct {
	ContactFlowArn string `pulumi:"contactFlowArn"`
	UserArn        string `pulumi:"userArn"`
}

// QuickConnectUserQuickConnectConfigInput is an input type that accepts QuickConnectUserQuickConnectConfigArgs and QuickConnectUserQuickConnectConfigOutput values.
// You can construct a concrete instance of `QuickConnectUserQuickConnectConfigInput` via:
//
//          QuickConnectUserQuickConnectConfigArgs{...}
type QuickConnectUserQuickConnectConfigInput interface {
	pulumi.Input

	ToQuickConnectUserQuickConnectConfigOutput() QuickConnectUserQuickConnectConfigOutput
	ToQuickConnectUserQuickConnectConfigOutputWithContext(context.Context) QuickConnectUserQuickConnectConfigOutput
}

// The user configuration. This is required only if QuickConnectType is USER.
type QuickConnectUserQuickConnectConfigArgs struct {
	ContactFlowArn pulumi.StringInput `pulumi:"contactFlowArn"`
	UserArn        pulumi.StringInput `pulumi:"userArn"`
}

func (QuickConnectUserQuickConnectConfigArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*QuickConnectUserQuickConnectConfig)(nil)).Elem()
}

func (i QuickConnectUserQuickConnectConfigArgs) ToQuickConnectUserQuickConnectConfigOutput() QuickConnectUserQuickConnectConfigOutput {
	return i.ToQuickConnectUserQuickConnectConfigOutputWithContext(context.Background())
}

func (i QuickConnectUserQuickConnectConfigArgs) ToQuickConnectUserQuickConnectConfigOutputWithContext(ctx context.Context) QuickConnectUserQuickConnectConfigOutput {
	return pulumi.ToOutputWithContext(ctx, i).(QuickConnectUserQuickConnectConfigOutput)
}

func (i QuickConnectUserQuickConnectConfigArgs) ToQuickConnectUserQuickConnectConfigPtrOutput() QuickConnectUserQuickConnectConfigPtrOutput {
	return i.ToQuickConnectUserQuickConnectConfigPtrOutputWithContext(context.Background())
}

func (i QuickConnectUserQuickConnectConfigArgs) ToQuickConnectUserQuickConnectConfigPtrOutputWithContext(ctx context.Context) QuickConnectUserQuickConnectConfigPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(QuickConnectUserQuickConnectConfigOutput).ToQuickConnectUserQuickConnectConfigPtrOutputWithContext(ctx)
}

// QuickConnectUserQuickConnectConfigPtrInput is an input type that accepts QuickConnectUserQuickConnectConfigArgs, QuickConnectUserQuickConnectConfigPtr and QuickConnectUserQuickConnectConfigPtrOutput values.
// You can construct a concrete instance of `QuickConnectUserQuickConnectConfigPtrInput` via:
//
//          QuickConnectUserQuickConnectConfigArgs{...}
//
//  or:
//
//          nil
type QuickConnectUserQuickConnectConfigPtrInput interface {
	pulumi.Input

	ToQuickConnectUserQuickConnectConfigPtrOutput() QuickConnectUserQuickConnectConfigPtrOutput
	ToQuickConnectUserQuickConnectConfigPtrOutputWithContext(context.Context) QuickConnectUserQuickConnectConfigPtrOutput
}

type quickConnectUserQuickConnectConfigPtrType QuickConnectUserQuickConnectConfigArgs

func QuickConnectUserQuickConnectConfigPtr(v *QuickConnectUserQuickConnectConfigArgs) QuickConnectUserQuickConnectConfigPtrInput {
	return (*quickConnectUserQuickConnectConfigPtrType)(v)
}

func (*quickConnectUserQuickConnectConfigPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**QuickConnectUserQuickConnectConfig)(nil)).Elem()
}

func (i *quickConnectUserQuickConnectConfigPtrType) ToQuickConnectUserQuickConnectConfigPtrOutput() QuickConnectUserQuickConnectConfigPtrOutput {
	return i.ToQuickConnectUserQuickConnectConfigPtrOutputWithContext(context.Background())
}

func (i *quickConnectUserQuickConnectConfigPtrType) ToQuickConnectUserQuickConnectConfigPtrOutputWithContext(ctx context.Context) QuickConnectUserQuickConnectConfigPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(QuickConnectUserQuickConnectConfigPtrOutput)
}

// The user configuration. This is required only if QuickConnectType is USER.
type QuickConnectUserQuickConnectConfigOutput struct{ *pulumi.OutputState }

func (QuickConnectUserQuickConnectConfigOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*QuickConnectUserQuickConnectConfig)(nil)).Elem()
}

func (o QuickConnectUserQuickConnectConfigOutput) ToQuickConnectUserQuickConnectConfigOutput() QuickConnectUserQuickConnectConfigOutput {
	return o
}

func (o QuickConnectUserQuickConnectConfigOutput) ToQuickConnectUserQuickConnectConfigOutputWithContext(ctx context.Context) QuickConnectUserQuickConnectConfigOutput {
	return o
}

func (o QuickConnectUserQuickConnectConfigOutput) ToQuickConnectUserQuickConnectConfigPtrOutput() QuickConnectUserQuickConnectConfigPtrOutput {
	return o.ToQuickConnectUserQuickConnectConfigPtrOutputWithContext(context.Background())
}

func (o QuickConnectUserQuickConnectConfigOutput) ToQuickConnectUserQuickConnectConfigPtrOutputWithContext(ctx context.Context) QuickConnectUserQuickConnectConfigPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v QuickConnectUserQuickConnectConfig) *QuickConnectUserQuickConnectConfig {
		return &v
	}).(QuickConnectUserQuickConnectConfigPtrOutput)
}

func (o QuickConnectUserQuickConnectConfigOutput) ContactFlowArn() pulumi.StringOutput {
	return o.ApplyT(func(v QuickConnectUserQuickConnectConfig) string { return v.ContactFlowArn }).(pulumi.StringOutput)
}

func (o QuickConnectUserQuickConnectConfigOutput) UserArn() pulumi.StringOutput {
	return o.ApplyT(func(v QuickConnectUserQuickConnectConfig) string { return v.UserArn }).(pulumi.StringOutput)
}

type QuickConnectUserQuickConnectConfigPtrOutput struct{ *pulumi.OutputState }

func (QuickConnectUserQuickConnectConfigPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**QuickConnectUserQuickConnectConfig)(nil)).Elem()
}

func (o QuickConnectUserQuickConnectConfigPtrOutput) ToQuickConnectUserQuickConnectConfigPtrOutput() QuickConnectUserQuickConnectConfigPtrOutput {
	return o
}

func (o QuickConnectUserQuickConnectConfigPtrOutput) ToQuickConnectUserQuickConnectConfigPtrOutputWithContext(ctx context.Context) QuickConnectUserQuickConnectConfigPtrOutput {
	return o
}

func (o QuickConnectUserQuickConnectConfigPtrOutput) Elem() QuickConnectUserQuickConnectConfigOutput {
	return o.ApplyT(func(v *QuickConnectUserQuickConnectConfig) QuickConnectUserQuickConnectConfig {
		if v != nil {
			return *v
		}
		var ret QuickConnectUserQuickConnectConfig
		return ret
	}).(QuickConnectUserQuickConnectConfigOutput)
}

func (o QuickConnectUserQuickConnectConfigPtrOutput) ContactFlowArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *QuickConnectUserQuickConnectConfig) *string {
		if v == nil {
			return nil
		}
		return &v.ContactFlowArn
	}).(pulumi.StringPtrOutput)
}

func (o QuickConnectUserQuickConnectConfigPtrOutput) UserArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *QuickConnectUserQuickConnectConfig) *string {
		if v == nil {
			return nil
		}
		return &v.UserArn
	}).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(QuickConnectConfigOutput{})
	pulumi.RegisterOutputType(QuickConnectConfigPtrOutput{})
	pulumi.RegisterOutputType(QuickConnectPhoneNumberQuickConnectConfigOutput{})
	pulumi.RegisterOutputType(QuickConnectPhoneNumberQuickConnectConfigPtrOutput{})
	pulumi.RegisterOutputType(QuickConnectQueueQuickConnectConfigOutput{})
	pulumi.RegisterOutputType(QuickConnectQueueQuickConnectConfigPtrOutput{})
	pulumi.RegisterOutputType(QuickConnectTagOutput{})
	pulumi.RegisterOutputType(QuickConnectTagArrayOutput{})
	pulumi.RegisterOutputType(QuickConnectUserQuickConnectConfigOutput{})
	pulumi.RegisterOutputType(QuickConnectUserQuickConnectConfigPtrOutput{})
}
