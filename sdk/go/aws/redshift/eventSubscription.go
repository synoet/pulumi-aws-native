// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package redshift

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The `AWS::Redshift::EventSubscription` resource creates an Amazon Redshift Event Subscription.
type EventSubscription struct {
	pulumi.CustomResourceState

	// The name of the Amazon Redshift event notification subscription.
	CustSubscriptionId pulumi.StringOutput `pulumi:"custSubscriptionId"`
	// The AWS account associated with the Amazon Redshift event notification subscription.
	CustomerAwsId pulumi.StringOutput `pulumi:"customerAwsId"`
	// A boolean value; set to true to activate the subscription, and set to false to create the subscription but not activate it.
	Enabled pulumi.BoolPtrOutput `pulumi:"enabled"`
	// Specifies the Amazon Redshift event categories to be published by the event notification subscription.
	EventCategories EventSubscriptionEventCategoriesItemArrayOutput `pulumi:"eventCategories"`
	// The list of Amazon Redshift event categories specified in the event notification subscription.
	EventCategoriesList pulumi.StringArrayOutput `pulumi:"eventCategoriesList"`
	// Specifies the Amazon Redshift event severity to be published by the event notification subscription.
	Severity EventSubscriptionSeverityPtrOutput `pulumi:"severity"`
	// The Amazon Resource Name (ARN) of the Amazon SNS topic used to transmit the event notifications.
	SnsTopicArn pulumi.StringPtrOutput `pulumi:"snsTopicArn"`
	// A list of one or more identifiers of Amazon Redshift source objects.
	SourceIds pulumi.StringArrayOutput `pulumi:"sourceIds"`
	// A list of the sources that publish events to the Amazon Redshift event notification subscription.
	SourceIdsList pulumi.StringArrayOutput `pulumi:"sourceIdsList"`
	// The type of source that will be generating the events.
	SourceType EventSubscriptionSourceTypePtrOutput `pulumi:"sourceType"`
	// The status of the Amazon Redshift event notification subscription.
	Status EventSubscriptionStatusOutput `pulumi:"status"`
	// The date and time the Amazon Redshift event notification subscription was created.
	SubscriptionCreationTime pulumi.StringOutput `pulumi:"subscriptionCreationTime"`
	// The name of the Amazon Redshift event notification subscription
	SubscriptionName pulumi.StringOutput `pulumi:"subscriptionName"`
	// An array of key-value pairs to apply to this resource.
	Tags EventSubscriptionTagArrayOutput `pulumi:"tags"`
}

// NewEventSubscription registers a new resource with the given unique name, arguments, and options.
func NewEventSubscription(ctx *pulumi.Context,
	name string, args *EventSubscriptionArgs, opts ...pulumi.ResourceOption) (*EventSubscription, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.SubscriptionName == nil {
		return nil, errors.New("invalid value for required argument 'SubscriptionName'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"subscriptionName",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource EventSubscription
	err := ctx.RegisterResource("aws-native:redshift:EventSubscription", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetEventSubscription gets an existing EventSubscription resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetEventSubscription(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *EventSubscriptionState, opts ...pulumi.ResourceOption) (*EventSubscription, error) {
	var resource EventSubscription
	err := ctx.ReadResource("aws-native:redshift:EventSubscription", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering EventSubscription resources.
type eventSubscriptionState struct {
}

type EventSubscriptionState struct {
}

func (EventSubscriptionState) ElementType() reflect.Type {
	return reflect.TypeOf((*eventSubscriptionState)(nil)).Elem()
}

type eventSubscriptionArgs struct {
	// A boolean value; set to true to activate the subscription, and set to false to create the subscription but not activate it.
	Enabled *bool `pulumi:"enabled"`
	// Specifies the Amazon Redshift event categories to be published by the event notification subscription.
	EventCategories []EventSubscriptionEventCategoriesItem `pulumi:"eventCategories"`
	// Specifies the Amazon Redshift event severity to be published by the event notification subscription.
	Severity *EventSubscriptionSeverity `pulumi:"severity"`
	// The Amazon Resource Name (ARN) of the Amazon SNS topic used to transmit the event notifications.
	SnsTopicArn *string `pulumi:"snsTopicArn"`
	// A list of one or more identifiers of Amazon Redshift source objects.
	SourceIds []string `pulumi:"sourceIds"`
	// The type of source that will be generating the events.
	SourceType *EventSubscriptionSourceType `pulumi:"sourceType"`
	// The name of the Amazon Redshift event notification subscription
	SubscriptionName string `pulumi:"subscriptionName"`
	// An array of key-value pairs to apply to this resource.
	Tags []EventSubscriptionTag `pulumi:"tags"`
}

// The set of arguments for constructing a EventSubscription resource.
type EventSubscriptionArgs struct {
	// A boolean value; set to true to activate the subscription, and set to false to create the subscription but not activate it.
	Enabled pulumi.BoolPtrInput
	// Specifies the Amazon Redshift event categories to be published by the event notification subscription.
	EventCategories EventSubscriptionEventCategoriesItemArrayInput
	// Specifies the Amazon Redshift event severity to be published by the event notification subscription.
	Severity EventSubscriptionSeverityPtrInput
	// The Amazon Resource Name (ARN) of the Amazon SNS topic used to transmit the event notifications.
	SnsTopicArn pulumi.StringPtrInput
	// A list of one or more identifiers of Amazon Redshift source objects.
	SourceIds pulumi.StringArrayInput
	// The type of source that will be generating the events.
	SourceType EventSubscriptionSourceTypePtrInput
	// The name of the Amazon Redshift event notification subscription
	SubscriptionName pulumi.StringInput
	// An array of key-value pairs to apply to this resource.
	Tags EventSubscriptionTagArrayInput
}

func (EventSubscriptionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*eventSubscriptionArgs)(nil)).Elem()
}

type EventSubscriptionInput interface {
	pulumi.Input

	ToEventSubscriptionOutput() EventSubscriptionOutput
	ToEventSubscriptionOutputWithContext(ctx context.Context) EventSubscriptionOutput
}

func (*EventSubscription) ElementType() reflect.Type {
	return reflect.TypeOf((**EventSubscription)(nil)).Elem()
}

func (i *EventSubscription) ToEventSubscriptionOutput() EventSubscriptionOutput {
	return i.ToEventSubscriptionOutputWithContext(context.Background())
}

func (i *EventSubscription) ToEventSubscriptionOutputWithContext(ctx context.Context) EventSubscriptionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EventSubscriptionOutput)
}

type EventSubscriptionOutput struct{ *pulumi.OutputState }

func (EventSubscriptionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**EventSubscription)(nil)).Elem()
}

func (o EventSubscriptionOutput) ToEventSubscriptionOutput() EventSubscriptionOutput {
	return o
}

func (o EventSubscriptionOutput) ToEventSubscriptionOutputWithContext(ctx context.Context) EventSubscriptionOutput {
	return o
}

// The name of the Amazon Redshift event notification subscription.
func (o EventSubscriptionOutput) CustSubscriptionId() pulumi.StringOutput {
	return o.ApplyT(func(v *EventSubscription) pulumi.StringOutput { return v.CustSubscriptionId }).(pulumi.StringOutput)
}

// The AWS account associated with the Amazon Redshift event notification subscription.
func (o EventSubscriptionOutput) CustomerAwsId() pulumi.StringOutput {
	return o.ApplyT(func(v *EventSubscription) pulumi.StringOutput { return v.CustomerAwsId }).(pulumi.StringOutput)
}

// A boolean value; set to true to activate the subscription, and set to false to create the subscription but not activate it.
func (o EventSubscriptionOutput) Enabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *EventSubscription) pulumi.BoolPtrOutput { return v.Enabled }).(pulumi.BoolPtrOutput)
}

// Specifies the Amazon Redshift event categories to be published by the event notification subscription.
func (o EventSubscriptionOutput) EventCategories() EventSubscriptionEventCategoriesItemArrayOutput {
	return o.ApplyT(func(v *EventSubscription) EventSubscriptionEventCategoriesItemArrayOutput { return v.EventCategories }).(EventSubscriptionEventCategoriesItemArrayOutput)
}

// The list of Amazon Redshift event categories specified in the event notification subscription.
func (o EventSubscriptionOutput) EventCategoriesList() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *EventSubscription) pulumi.StringArrayOutput { return v.EventCategoriesList }).(pulumi.StringArrayOutput)
}

// Specifies the Amazon Redshift event severity to be published by the event notification subscription.
func (o EventSubscriptionOutput) Severity() EventSubscriptionSeverityPtrOutput {
	return o.ApplyT(func(v *EventSubscription) EventSubscriptionSeverityPtrOutput { return v.Severity }).(EventSubscriptionSeverityPtrOutput)
}

// The Amazon Resource Name (ARN) of the Amazon SNS topic used to transmit the event notifications.
func (o EventSubscriptionOutput) SnsTopicArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *EventSubscription) pulumi.StringPtrOutput { return v.SnsTopicArn }).(pulumi.StringPtrOutput)
}

// A list of one or more identifiers of Amazon Redshift source objects.
func (o EventSubscriptionOutput) SourceIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *EventSubscription) pulumi.StringArrayOutput { return v.SourceIds }).(pulumi.StringArrayOutput)
}

// A list of the sources that publish events to the Amazon Redshift event notification subscription.
func (o EventSubscriptionOutput) SourceIdsList() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *EventSubscription) pulumi.StringArrayOutput { return v.SourceIdsList }).(pulumi.StringArrayOutput)
}

// The type of source that will be generating the events.
func (o EventSubscriptionOutput) SourceType() EventSubscriptionSourceTypePtrOutput {
	return o.ApplyT(func(v *EventSubscription) EventSubscriptionSourceTypePtrOutput { return v.SourceType }).(EventSubscriptionSourceTypePtrOutput)
}

// The status of the Amazon Redshift event notification subscription.
func (o EventSubscriptionOutput) Status() EventSubscriptionStatusOutput {
	return o.ApplyT(func(v *EventSubscription) EventSubscriptionStatusOutput { return v.Status }).(EventSubscriptionStatusOutput)
}

// The date and time the Amazon Redshift event notification subscription was created.
func (o EventSubscriptionOutput) SubscriptionCreationTime() pulumi.StringOutput {
	return o.ApplyT(func(v *EventSubscription) pulumi.StringOutput { return v.SubscriptionCreationTime }).(pulumi.StringOutput)
}

// The name of the Amazon Redshift event notification subscription
func (o EventSubscriptionOutput) SubscriptionName() pulumi.StringOutput {
	return o.ApplyT(func(v *EventSubscription) pulumi.StringOutput { return v.SubscriptionName }).(pulumi.StringOutput)
}

// An array of key-value pairs to apply to this resource.
func (o EventSubscriptionOutput) Tags() EventSubscriptionTagArrayOutput {
	return o.ApplyT(func(v *EventSubscription) EventSubscriptionTagArrayOutput { return v.Tags }).(EventSubscriptionTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*EventSubscriptionInput)(nil)).Elem(), &EventSubscription{})
	pulumi.RegisterOutputType(EventSubscriptionOutput{})
}
