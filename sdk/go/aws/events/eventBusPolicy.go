// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package events

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::Events::EventBusPolicy
//
// Deprecated: EventBusPolicy is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type EventBusPolicy struct {
	pulumi.CustomResourceState

	Action       pulumi.StringPtrOutput           `pulumi:"action"`
	Condition    EventBusPolicyConditionPtrOutput `pulumi:"condition"`
	EventBusName pulumi.StringPtrOutput           `pulumi:"eventBusName"`
	Principal    pulumi.StringPtrOutput           `pulumi:"principal"`
	Statement    pulumi.AnyOutput                 `pulumi:"statement"`
	StatementId  pulumi.StringOutput              `pulumi:"statementId"`
}

// NewEventBusPolicy registers a new resource with the given unique name, arguments, and options.
func NewEventBusPolicy(ctx *pulumi.Context,
	name string, args *EventBusPolicyArgs, opts ...pulumi.ResourceOption) (*EventBusPolicy, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.StatementId == nil {
		return nil, errors.New("invalid value for required argument 'StatementId'")
	}
	var resource EventBusPolicy
	err := ctx.RegisterResource("aws-native:events:EventBusPolicy", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetEventBusPolicy gets an existing EventBusPolicy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetEventBusPolicy(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *EventBusPolicyState, opts ...pulumi.ResourceOption) (*EventBusPolicy, error) {
	var resource EventBusPolicy
	err := ctx.ReadResource("aws-native:events:EventBusPolicy", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering EventBusPolicy resources.
type eventBusPolicyState struct {
}

type EventBusPolicyState struct {
}

func (EventBusPolicyState) ElementType() reflect.Type {
	return reflect.TypeOf((*eventBusPolicyState)(nil)).Elem()
}

type eventBusPolicyArgs struct {
	Action       *string                  `pulumi:"action"`
	Condition    *EventBusPolicyCondition `pulumi:"condition"`
	EventBusName *string                  `pulumi:"eventBusName"`
	Principal    *string                  `pulumi:"principal"`
	Statement    interface{}              `pulumi:"statement"`
	StatementId  string                   `pulumi:"statementId"`
}

// The set of arguments for constructing a EventBusPolicy resource.
type EventBusPolicyArgs struct {
	Action       pulumi.StringPtrInput
	Condition    EventBusPolicyConditionPtrInput
	EventBusName pulumi.StringPtrInput
	Principal    pulumi.StringPtrInput
	Statement    pulumi.Input
	StatementId  pulumi.StringInput
}

func (EventBusPolicyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*eventBusPolicyArgs)(nil)).Elem()
}

type EventBusPolicyInput interface {
	pulumi.Input

	ToEventBusPolicyOutput() EventBusPolicyOutput
	ToEventBusPolicyOutputWithContext(ctx context.Context) EventBusPolicyOutput
}

func (*EventBusPolicy) ElementType() reflect.Type {
	return reflect.TypeOf((**EventBusPolicy)(nil)).Elem()
}

func (i *EventBusPolicy) ToEventBusPolicyOutput() EventBusPolicyOutput {
	return i.ToEventBusPolicyOutputWithContext(context.Background())
}

func (i *EventBusPolicy) ToEventBusPolicyOutputWithContext(ctx context.Context) EventBusPolicyOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EventBusPolicyOutput)
}

type EventBusPolicyOutput struct{ *pulumi.OutputState }

func (EventBusPolicyOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**EventBusPolicy)(nil)).Elem()
}

func (o EventBusPolicyOutput) ToEventBusPolicyOutput() EventBusPolicyOutput {
	return o
}

func (o EventBusPolicyOutput) ToEventBusPolicyOutputWithContext(ctx context.Context) EventBusPolicyOutput {
	return o
}

func (o EventBusPolicyOutput) Action() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *EventBusPolicy) pulumi.StringPtrOutput { return v.Action }).(pulumi.StringPtrOutput)
}

func (o EventBusPolicyOutput) Condition() EventBusPolicyConditionPtrOutput {
	return o.ApplyT(func(v *EventBusPolicy) EventBusPolicyConditionPtrOutput { return v.Condition }).(EventBusPolicyConditionPtrOutput)
}

func (o EventBusPolicyOutput) EventBusName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *EventBusPolicy) pulumi.StringPtrOutput { return v.EventBusName }).(pulumi.StringPtrOutput)
}

func (o EventBusPolicyOutput) Principal() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *EventBusPolicy) pulumi.StringPtrOutput { return v.Principal }).(pulumi.StringPtrOutput)
}

func (o EventBusPolicyOutput) Statement() pulumi.AnyOutput {
	return o.ApplyT(func(v *EventBusPolicy) pulumi.AnyOutput { return v.Statement }).(pulumi.AnyOutput)
}

func (o EventBusPolicyOutput) StatementId() pulumi.StringOutput {
	return o.ApplyT(func(v *EventBusPolicy) pulumi.StringOutput { return v.StatementId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*EventBusPolicyInput)(nil)).Elem(), &EventBusPolicy{})
	pulumi.RegisterOutputType(EventBusPolicyOutput{})
}
