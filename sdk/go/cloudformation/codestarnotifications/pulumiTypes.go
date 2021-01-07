// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package codestarnotifications

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

type NotificationRuleAttributes struct {
}

// NotificationRuleAttributesInput is an input type that accepts NotificationRuleAttributesArgs and NotificationRuleAttributesOutput values.
// You can construct a concrete instance of `NotificationRuleAttributesInput` via:
//
//          NotificationRuleAttributesArgs{...}
type NotificationRuleAttributesInput interface {
	pulumi.Input

	ToNotificationRuleAttributesOutput() NotificationRuleAttributesOutput
	ToNotificationRuleAttributesOutputWithContext(context.Context) NotificationRuleAttributesOutput
}

type NotificationRuleAttributesArgs struct {
}

func (NotificationRuleAttributesArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*NotificationRuleAttributes)(nil)).Elem()
}

func (i NotificationRuleAttributesArgs) ToNotificationRuleAttributesOutput() NotificationRuleAttributesOutput {
	return i.ToNotificationRuleAttributesOutputWithContext(context.Background())
}

func (i NotificationRuleAttributesArgs) ToNotificationRuleAttributesOutputWithContext(ctx context.Context) NotificationRuleAttributesOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NotificationRuleAttributesOutput)
}

func (i NotificationRuleAttributesArgs) ToNotificationRuleAttributesPtrOutput() NotificationRuleAttributesPtrOutput {
	return i.ToNotificationRuleAttributesPtrOutputWithContext(context.Background())
}

func (i NotificationRuleAttributesArgs) ToNotificationRuleAttributesPtrOutputWithContext(ctx context.Context) NotificationRuleAttributesPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NotificationRuleAttributesOutput).ToNotificationRuleAttributesPtrOutputWithContext(ctx)
}

// NotificationRuleAttributesPtrInput is an input type that accepts NotificationRuleAttributesArgs, NotificationRuleAttributesPtr and NotificationRuleAttributesPtrOutput values.
// You can construct a concrete instance of `NotificationRuleAttributesPtrInput` via:
//
//          NotificationRuleAttributesArgs{...}
//
//  or:
//
//          nil
type NotificationRuleAttributesPtrInput interface {
	pulumi.Input

	ToNotificationRuleAttributesPtrOutput() NotificationRuleAttributesPtrOutput
	ToNotificationRuleAttributesPtrOutputWithContext(context.Context) NotificationRuleAttributesPtrOutput
}

type notificationRuleAttributesPtrType NotificationRuleAttributesArgs

func NotificationRuleAttributesPtr(v *NotificationRuleAttributesArgs) NotificationRuleAttributesPtrInput {
	return (*notificationRuleAttributesPtrType)(v)
}

func (*notificationRuleAttributesPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**NotificationRuleAttributes)(nil)).Elem()
}

func (i *notificationRuleAttributesPtrType) ToNotificationRuleAttributesPtrOutput() NotificationRuleAttributesPtrOutput {
	return i.ToNotificationRuleAttributesPtrOutputWithContext(context.Background())
}

func (i *notificationRuleAttributesPtrType) ToNotificationRuleAttributesPtrOutputWithContext(ctx context.Context) NotificationRuleAttributesPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NotificationRuleAttributesPtrOutput)
}

type NotificationRuleAttributesOutput struct{ *pulumi.OutputState }

func (NotificationRuleAttributesOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*NotificationRuleAttributes)(nil)).Elem()
}

func (o NotificationRuleAttributesOutput) ToNotificationRuleAttributesOutput() NotificationRuleAttributesOutput {
	return o
}

func (o NotificationRuleAttributesOutput) ToNotificationRuleAttributesOutputWithContext(ctx context.Context) NotificationRuleAttributesOutput {
	return o
}

func (o NotificationRuleAttributesOutput) ToNotificationRuleAttributesPtrOutput() NotificationRuleAttributesPtrOutput {
	return o.ToNotificationRuleAttributesPtrOutputWithContext(context.Background())
}

func (o NotificationRuleAttributesOutput) ToNotificationRuleAttributesPtrOutputWithContext(ctx context.Context) NotificationRuleAttributesPtrOutput {
	return o.ApplyT(func(v NotificationRuleAttributes) *NotificationRuleAttributes {
		return &v
	}).(NotificationRuleAttributesPtrOutput)
}

type NotificationRuleAttributesPtrOutput struct{ *pulumi.OutputState }

func (NotificationRuleAttributesPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**NotificationRuleAttributes)(nil)).Elem()
}

func (o NotificationRuleAttributesPtrOutput) ToNotificationRuleAttributesPtrOutput() NotificationRuleAttributesPtrOutput {
	return o
}

func (o NotificationRuleAttributesPtrOutput) ToNotificationRuleAttributesPtrOutputWithContext(ctx context.Context) NotificationRuleAttributesPtrOutput {
	return o
}

func (o NotificationRuleAttributesPtrOutput) Elem() NotificationRuleAttributesOutput {
	return o.ApplyT(func(v *NotificationRuleAttributes) NotificationRuleAttributes { return *v }).(NotificationRuleAttributesOutput)
}

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html
type NotificationRuleProperties struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-detailtype
	DetailType string `pulumi:"DetailType"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-eventtypeids
	EventTypeIds []string `pulumi:"EventTypeIds"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-name
	Name string `pulumi:"Name"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-resource
	Resource string `pulumi:"Resource"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-status
	Status *string `pulumi:"Status"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-tags
	Tags interface{} `pulumi:"Tags"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-targets
	Targets []NotificationRuleTarget `pulumi:"Targets"`
}

// NotificationRulePropertiesInput is an input type that accepts NotificationRulePropertiesArgs and NotificationRulePropertiesOutput values.
// You can construct a concrete instance of `NotificationRulePropertiesInput` via:
//
//          NotificationRulePropertiesArgs{...}
type NotificationRulePropertiesInput interface {
	pulumi.Input

	ToNotificationRulePropertiesOutput() NotificationRulePropertiesOutput
	ToNotificationRulePropertiesOutputWithContext(context.Context) NotificationRulePropertiesOutput
}

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html
type NotificationRulePropertiesArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-detailtype
	DetailType pulumi.StringInput `pulumi:"DetailType"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-eventtypeids
	EventTypeIds pulumi.StringArrayInput `pulumi:"EventTypeIds"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-name
	Name pulumi.StringInput `pulumi:"Name"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-resource
	Resource pulumi.StringInput `pulumi:"Resource"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-status
	Status pulumi.StringPtrInput `pulumi:"Status"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-tags
	Tags pulumi.Input `pulumi:"Tags"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-targets
	Targets NotificationRuleTargetArrayInput `pulumi:"Targets"`
}

func (NotificationRulePropertiesArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*NotificationRuleProperties)(nil)).Elem()
}

func (i NotificationRulePropertiesArgs) ToNotificationRulePropertiesOutput() NotificationRulePropertiesOutput {
	return i.ToNotificationRulePropertiesOutputWithContext(context.Background())
}

func (i NotificationRulePropertiesArgs) ToNotificationRulePropertiesOutputWithContext(ctx context.Context) NotificationRulePropertiesOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NotificationRulePropertiesOutput)
}

func (i NotificationRulePropertiesArgs) ToNotificationRulePropertiesPtrOutput() NotificationRulePropertiesPtrOutput {
	return i.ToNotificationRulePropertiesPtrOutputWithContext(context.Background())
}

func (i NotificationRulePropertiesArgs) ToNotificationRulePropertiesPtrOutputWithContext(ctx context.Context) NotificationRulePropertiesPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NotificationRulePropertiesOutput).ToNotificationRulePropertiesPtrOutputWithContext(ctx)
}

// NotificationRulePropertiesPtrInput is an input type that accepts NotificationRulePropertiesArgs, NotificationRulePropertiesPtr and NotificationRulePropertiesPtrOutput values.
// You can construct a concrete instance of `NotificationRulePropertiesPtrInput` via:
//
//          NotificationRulePropertiesArgs{...}
//
//  or:
//
//          nil
type NotificationRulePropertiesPtrInput interface {
	pulumi.Input

	ToNotificationRulePropertiesPtrOutput() NotificationRulePropertiesPtrOutput
	ToNotificationRulePropertiesPtrOutputWithContext(context.Context) NotificationRulePropertiesPtrOutput
}

type notificationRulePropertiesPtrType NotificationRulePropertiesArgs

func NotificationRulePropertiesPtr(v *NotificationRulePropertiesArgs) NotificationRulePropertiesPtrInput {
	return (*notificationRulePropertiesPtrType)(v)
}

func (*notificationRulePropertiesPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**NotificationRuleProperties)(nil)).Elem()
}

func (i *notificationRulePropertiesPtrType) ToNotificationRulePropertiesPtrOutput() NotificationRulePropertiesPtrOutput {
	return i.ToNotificationRulePropertiesPtrOutputWithContext(context.Background())
}

func (i *notificationRulePropertiesPtrType) ToNotificationRulePropertiesPtrOutputWithContext(ctx context.Context) NotificationRulePropertiesPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NotificationRulePropertiesPtrOutput)
}

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html
type NotificationRulePropertiesOutput struct{ *pulumi.OutputState }

func (NotificationRulePropertiesOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*NotificationRuleProperties)(nil)).Elem()
}

func (o NotificationRulePropertiesOutput) ToNotificationRulePropertiesOutput() NotificationRulePropertiesOutput {
	return o
}

func (o NotificationRulePropertiesOutput) ToNotificationRulePropertiesOutputWithContext(ctx context.Context) NotificationRulePropertiesOutput {
	return o
}

func (o NotificationRulePropertiesOutput) ToNotificationRulePropertiesPtrOutput() NotificationRulePropertiesPtrOutput {
	return o.ToNotificationRulePropertiesPtrOutputWithContext(context.Background())
}

func (o NotificationRulePropertiesOutput) ToNotificationRulePropertiesPtrOutputWithContext(ctx context.Context) NotificationRulePropertiesPtrOutput {
	return o.ApplyT(func(v NotificationRuleProperties) *NotificationRuleProperties {
		return &v
	}).(NotificationRulePropertiesPtrOutput)
}

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-detailtype
func (o NotificationRulePropertiesOutput) DetailType() pulumi.StringOutput {
	return o.ApplyT(func(v NotificationRuleProperties) string { return v.DetailType }).(pulumi.StringOutput)
}

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-eventtypeids
func (o NotificationRulePropertiesOutput) EventTypeIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v NotificationRuleProperties) []string { return v.EventTypeIds }).(pulumi.StringArrayOutput)
}

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-name
func (o NotificationRulePropertiesOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v NotificationRuleProperties) string { return v.Name }).(pulumi.StringOutput)
}

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-resource
func (o NotificationRulePropertiesOutput) Resource() pulumi.StringOutput {
	return o.ApplyT(func(v NotificationRuleProperties) string { return v.Resource }).(pulumi.StringOutput)
}

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-status
func (o NotificationRulePropertiesOutput) Status() pulumi.StringPtrOutput {
	return o.ApplyT(func(v NotificationRuleProperties) *string { return v.Status }).(pulumi.StringPtrOutput)
}

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-tags
func (o NotificationRulePropertiesOutput) Tags() pulumi.AnyOutput {
	return o.ApplyT(func(v NotificationRuleProperties) interface{} { return v.Tags }).(pulumi.AnyOutput)
}

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-targets
func (o NotificationRulePropertiesOutput) Targets() NotificationRuleTargetArrayOutput {
	return o.ApplyT(func(v NotificationRuleProperties) []NotificationRuleTarget { return v.Targets }).(NotificationRuleTargetArrayOutput)
}

type NotificationRulePropertiesPtrOutput struct{ *pulumi.OutputState }

func (NotificationRulePropertiesPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**NotificationRuleProperties)(nil)).Elem()
}

func (o NotificationRulePropertiesPtrOutput) ToNotificationRulePropertiesPtrOutput() NotificationRulePropertiesPtrOutput {
	return o
}

func (o NotificationRulePropertiesPtrOutput) ToNotificationRulePropertiesPtrOutputWithContext(ctx context.Context) NotificationRulePropertiesPtrOutput {
	return o
}

func (o NotificationRulePropertiesPtrOutput) Elem() NotificationRulePropertiesOutput {
	return o.ApplyT(func(v *NotificationRuleProperties) NotificationRuleProperties { return *v }).(NotificationRulePropertiesOutput)
}

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-detailtype
func (o NotificationRulePropertiesPtrOutput) DetailType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *NotificationRuleProperties) *string {
		if v == nil {
			return nil
		}
		return &v.DetailType
	}).(pulumi.StringPtrOutput)
}

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-eventtypeids
func (o NotificationRulePropertiesPtrOutput) EventTypeIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *NotificationRuleProperties) []string {
		if v == nil {
			return nil
		}
		return v.EventTypeIds
	}).(pulumi.StringArrayOutput)
}

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-name
func (o NotificationRulePropertiesPtrOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *NotificationRuleProperties) *string {
		if v == nil {
			return nil
		}
		return &v.Name
	}).(pulumi.StringPtrOutput)
}

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-resource
func (o NotificationRulePropertiesPtrOutput) Resource() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *NotificationRuleProperties) *string {
		if v == nil {
			return nil
		}
		return &v.Resource
	}).(pulumi.StringPtrOutput)
}

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-status
func (o NotificationRulePropertiesPtrOutput) Status() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *NotificationRuleProperties) *string {
		if v == nil {
			return nil
		}
		return v.Status
	}).(pulumi.StringPtrOutput)
}

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-tags
func (o NotificationRulePropertiesPtrOutput) Tags() pulumi.AnyOutput {
	return o.ApplyT(func(v *NotificationRuleProperties) interface{} {
		if v == nil {
			return nil
		}
		return v.Tags
	}).(pulumi.AnyOutput)
}

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-targets
func (o NotificationRulePropertiesPtrOutput) Targets() NotificationRuleTargetArrayOutput {
	return o.ApplyT(func(v *NotificationRuleProperties) []NotificationRuleTarget {
		if v == nil {
			return nil
		}
		return v.Targets
	}).(NotificationRuleTargetArrayOutput)
}

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codestarnotifications-notificationrule-target.html
type NotificationRuleTarget struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codestarnotifications-notificationrule-target.html#cfn-codestarnotifications-notificationrule-target-targetaddress
	TargetAddress *string `pulumi:"TargetAddress"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codestarnotifications-notificationrule-target.html#cfn-codestarnotifications-notificationrule-target-targettype
	TargetType *string `pulumi:"TargetType"`
}

// NotificationRuleTargetInput is an input type that accepts NotificationRuleTargetArgs and NotificationRuleTargetOutput values.
// You can construct a concrete instance of `NotificationRuleTargetInput` via:
//
//          NotificationRuleTargetArgs{...}
type NotificationRuleTargetInput interface {
	pulumi.Input

	ToNotificationRuleTargetOutput() NotificationRuleTargetOutput
	ToNotificationRuleTargetOutputWithContext(context.Context) NotificationRuleTargetOutput
}

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codestarnotifications-notificationrule-target.html
type NotificationRuleTargetArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codestarnotifications-notificationrule-target.html#cfn-codestarnotifications-notificationrule-target-targetaddress
	TargetAddress pulumi.StringPtrInput `pulumi:"TargetAddress"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codestarnotifications-notificationrule-target.html#cfn-codestarnotifications-notificationrule-target-targettype
	TargetType pulumi.StringPtrInput `pulumi:"TargetType"`
}

func (NotificationRuleTargetArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*NotificationRuleTarget)(nil)).Elem()
}

func (i NotificationRuleTargetArgs) ToNotificationRuleTargetOutput() NotificationRuleTargetOutput {
	return i.ToNotificationRuleTargetOutputWithContext(context.Background())
}

func (i NotificationRuleTargetArgs) ToNotificationRuleTargetOutputWithContext(ctx context.Context) NotificationRuleTargetOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NotificationRuleTargetOutput)
}

// NotificationRuleTargetArrayInput is an input type that accepts NotificationRuleTargetArray and NotificationRuleTargetArrayOutput values.
// You can construct a concrete instance of `NotificationRuleTargetArrayInput` via:
//
//          NotificationRuleTargetArray{ NotificationRuleTargetArgs{...} }
type NotificationRuleTargetArrayInput interface {
	pulumi.Input

	ToNotificationRuleTargetArrayOutput() NotificationRuleTargetArrayOutput
	ToNotificationRuleTargetArrayOutputWithContext(context.Context) NotificationRuleTargetArrayOutput
}

type NotificationRuleTargetArray []NotificationRuleTargetInput

func (NotificationRuleTargetArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]NotificationRuleTarget)(nil)).Elem()
}

func (i NotificationRuleTargetArray) ToNotificationRuleTargetArrayOutput() NotificationRuleTargetArrayOutput {
	return i.ToNotificationRuleTargetArrayOutputWithContext(context.Background())
}

func (i NotificationRuleTargetArray) ToNotificationRuleTargetArrayOutputWithContext(ctx context.Context) NotificationRuleTargetArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NotificationRuleTargetArrayOutput)
}

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codestarnotifications-notificationrule-target.html
type NotificationRuleTargetOutput struct{ *pulumi.OutputState }

func (NotificationRuleTargetOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*NotificationRuleTarget)(nil)).Elem()
}

func (o NotificationRuleTargetOutput) ToNotificationRuleTargetOutput() NotificationRuleTargetOutput {
	return o
}

func (o NotificationRuleTargetOutput) ToNotificationRuleTargetOutputWithContext(ctx context.Context) NotificationRuleTargetOutput {
	return o
}

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codestarnotifications-notificationrule-target.html#cfn-codestarnotifications-notificationrule-target-targetaddress
func (o NotificationRuleTargetOutput) TargetAddress() pulumi.StringPtrOutput {
	return o.ApplyT(func(v NotificationRuleTarget) *string { return v.TargetAddress }).(pulumi.StringPtrOutput)
}

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codestarnotifications-notificationrule-target.html#cfn-codestarnotifications-notificationrule-target-targettype
func (o NotificationRuleTargetOutput) TargetType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v NotificationRuleTarget) *string { return v.TargetType }).(pulumi.StringPtrOutput)
}

type NotificationRuleTargetArrayOutput struct{ *pulumi.OutputState }

func (NotificationRuleTargetArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]NotificationRuleTarget)(nil)).Elem()
}

func (o NotificationRuleTargetArrayOutput) ToNotificationRuleTargetArrayOutput() NotificationRuleTargetArrayOutput {
	return o
}

func (o NotificationRuleTargetArrayOutput) ToNotificationRuleTargetArrayOutputWithContext(ctx context.Context) NotificationRuleTargetArrayOutput {
	return o
}

func (o NotificationRuleTargetArrayOutput) Index(i pulumi.IntInput) NotificationRuleTargetOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) NotificationRuleTarget {
		return vs[0].([]NotificationRuleTarget)[vs[1].(int)]
	}).(NotificationRuleTargetOutput)
}

func init() {
	pulumi.RegisterOutputType(NotificationRuleAttributesOutput{})
	pulumi.RegisterOutputType(NotificationRuleAttributesPtrOutput{})
	pulumi.RegisterOutputType(NotificationRulePropertiesOutput{})
	pulumi.RegisterOutputType(NotificationRulePropertiesPtrOutput{})
	pulumi.RegisterOutputType(NotificationRuleTargetOutput{})
	pulumi.RegisterOutputType(NotificationRuleTargetArrayOutput{})
}