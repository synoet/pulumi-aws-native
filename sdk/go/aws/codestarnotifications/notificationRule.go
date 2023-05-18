// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package codestarnotifications

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::CodeStarNotifications::NotificationRule
type NotificationRule struct {
	pulumi.CustomResourceState

	Arn           pulumi.StringOutput               `pulumi:"arn"`
	CreatedBy     pulumi.StringPtrOutput            `pulumi:"createdBy"`
	DetailType    NotificationRuleDetailTypeOutput  `pulumi:"detailType"`
	EventTypeId   pulumi.StringPtrOutput            `pulumi:"eventTypeId"`
	EventTypeIds  pulumi.StringArrayOutput          `pulumi:"eventTypeIds"`
	Name          pulumi.StringOutput               `pulumi:"name"`
	Resource      pulumi.StringOutput               `pulumi:"resource"`
	Status        NotificationRuleStatusPtrOutput   `pulumi:"status"`
	Tags          pulumi.AnyOutput                  `pulumi:"tags"`
	TargetAddress pulumi.StringPtrOutput            `pulumi:"targetAddress"`
	Targets       NotificationRuleTargetArrayOutput `pulumi:"targets"`
}

// NewNotificationRule registers a new resource with the given unique name, arguments, and options.
func NewNotificationRule(ctx *pulumi.Context,
	name string, args *NotificationRuleArgs, opts ...pulumi.ResourceOption) (*NotificationRule, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DetailType == nil {
		return nil, errors.New("invalid value for required argument 'DetailType'")
	}
	if args.EventTypeIds == nil {
		return nil, errors.New("invalid value for required argument 'EventTypeIds'")
	}
	if args.Resource == nil {
		return nil, errors.New("invalid value for required argument 'Resource'")
	}
	if args.Targets == nil {
		return nil, errors.New("invalid value for required argument 'Targets'")
	}
	var resource NotificationRule
	err := ctx.RegisterResource("aws-native:codestarnotifications:NotificationRule", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetNotificationRule gets an existing NotificationRule resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetNotificationRule(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *NotificationRuleState, opts ...pulumi.ResourceOption) (*NotificationRule, error) {
	var resource NotificationRule
	err := ctx.ReadResource("aws-native:codestarnotifications:NotificationRule", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering NotificationRule resources.
type notificationRuleState struct {
}

type NotificationRuleState struct {
}

func (NotificationRuleState) ElementType() reflect.Type {
	return reflect.TypeOf((*notificationRuleState)(nil)).Elem()
}

type notificationRuleArgs struct {
	CreatedBy     *string                    `pulumi:"createdBy"`
	DetailType    NotificationRuleDetailType `pulumi:"detailType"`
	EventTypeId   *string                    `pulumi:"eventTypeId"`
	EventTypeIds  []string                   `pulumi:"eventTypeIds"`
	Name          *string                    `pulumi:"name"`
	Resource      string                     `pulumi:"resource"`
	Status        *NotificationRuleStatus    `pulumi:"status"`
	Tags          interface{}                `pulumi:"tags"`
	TargetAddress *string                    `pulumi:"targetAddress"`
	Targets       []NotificationRuleTarget   `pulumi:"targets"`
}

// The set of arguments for constructing a NotificationRule resource.
type NotificationRuleArgs struct {
	CreatedBy     pulumi.StringPtrInput
	DetailType    NotificationRuleDetailTypeInput
	EventTypeId   pulumi.StringPtrInput
	EventTypeIds  pulumi.StringArrayInput
	Name          pulumi.StringPtrInput
	Resource      pulumi.StringInput
	Status        NotificationRuleStatusPtrInput
	Tags          pulumi.Input
	TargetAddress pulumi.StringPtrInput
	Targets       NotificationRuleTargetArrayInput
}

func (NotificationRuleArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*notificationRuleArgs)(nil)).Elem()
}

type NotificationRuleInput interface {
	pulumi.Input

	ToNotificationRuleOutput() NotificationRuleOutput
	ToNotificationRuleOutputWithContext(ctx context.Context) NotificationRuleOutput
}

func (*NotificationRule) ElementType() reflect.Type {
	return reflect.TypeOf((**NotificationRule)(nil)).Elem()
}

func (i *NotificationRule) ToNotificationRuleOutput() NotificationRuleOutput {
	return i.ToNotificationRuleOutputWithContext(context.Background())
}

func (i *NotificationRule) ToNotificationRuleOutputWithContext(ctx context.Context) NotificationRuleOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NotificationRuleOutput)
}

type NotificationRuleOutput struct{ *pulumi.OutputState }

func (NotificationRuleOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**NotificationRule)(nil)).Elem()
}

func (o NotificationRuleOutput) ToNotificationRuleOutput() NotificationRuleOutput {
	return o
}

func (o NotificationRuleOutput) ToNotificationRuleOutputWithContext(ctx context.Context) NotificationRuleOutput {
	return o
}

func (o NotificationRuleOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *NotificationRule) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

func (o NotificationRuleOutput) CreatedBy() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *NotificationRule) pulumi.StringPtrOutput { return v.CreatedBy }).(pulumi.StringPtrOutput)
}

func (o NotificationRuleOutput) DetailType() NotificationRuleDetailTypeOutput {
	return o.ApplyT(func(v *NotificationRule) NotificationRuleDetailTypeOutput { return v.DetailType }).(NotificationRuleDetailTypeOutput)
}

func (o NotificationRuleOutput) EventTypeId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *NotificationRule) pulumi.StringPtrOutput { return v.EventTypeId }).(pulumi.StringPtrOutput)
}

func (o NotificationRuleOutput) EventTypeIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *NotificationRule) pulumi.StringArrayOutput { return v.EventTypeIds }).(pulumi.StringArrayOutput)
}

func (o NotificationRuleOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *NotificationRule) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o NotificationRuleOutput) Resource() pulumi.StringOutput {
	return o.ApplyT(func(v *NotificationRule) pulumi.StringOutput { return v.Resource }).(pulumi.StringOutput)
}

func (o NotificationRuleOutput) Status() NotificationRuleStatusPtrOutput {
	return o.ApplyT(func(v *NotificationRule) NotificationRuleStatusPtrOutput { return v.Status }).(NotificationRuleStatusPtrOutput)
}

func (o NotificationRuleOutput) Tags() pulumi.AnyOutput {
	return o.ApplyT(func(v *NotificationRule) pulumi.AnyOutput { return v.Tags }).(pulumi.AnyOutput)
}

func (o NotificationRuleOutput) TargetAddress() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *NotificationRule) pulumi.StringPtrOutput { return v.TargetAddress }).(pulumi.StringPtrOutput)
}

func (o NotificationRuleOutput) Targets() NotificationRuleTargetArrayOutput {
	return o.ApplyT(func(v *NotificationRule) NotificationRuleTargetArrayOutput { return v.Targets }).(NotificationRuleTargetArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*NotificationRuleInput)(nil)).Elem(), &NotificationRule{})
	pulumi.RegisterOutputType(NotificationRuleOutput{})
}
