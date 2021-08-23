// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package iot

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicruledestination.html
type TopicRuleDestination struct {
	pulumi.CustomResourceState

	Arn pulumi.StringOutput `pulumi:"arn"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicruledestination.html#cfn-iot-topicruledestination-httpurlproperties
	HttpUrlProperties TopicRuleDestinationHttpUrlDestinationSummaryPtrOutput `pulumi:"httpUrlProperties"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicruledestination.html#cfn-iot-topicruledestination-status
	Status       pulumi.StringPtrOutput `pulumi:"status"`
	StatusReason pulumi.StringOutput    `pulumi:"statusReason"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicruledestination.html#cfn-iot-topicruledestination-vpcproperties
	VpcProperties TopicRuleDestinationVpcDestinationPropertiesPtrOutput `pulumi:"vpcProperties"`
}

// NewTopicRuleDestination registers a new resource with the given unique name, arguments, and options.
func NewTopicRuleDestination(ctx *pulumi.Context,
	name string, args *TopicRuleDestinationArgs, opts ...pulumi.ResourceOption) (*TopicRuleDestination, error) {
	if args == nil {
		args = &TopicRuleDestinationArgs{}
	}

	var resource TopicRuleDestination
	err := ctx.RegisterResource("aws-native:iot:TopicRuleDestination", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetTopicRuleDestination gets an existing TopicRuleDestination resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTopicRuleDestination(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *TopicRuleDestinationState, opts ...pulumi.ResourceOption) (*TopicRuleDestination, error) {
	var resource TopicRuleDestination
	err := ctx.ReadResource("aws-native:iot:TopicRuleDestination", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering TopicRuleDestination resources.
type topicRuleDestinationState struct {
}

type TopicRuleDestinationState struct {
}

func (TopicRuleDestinationState) ElementType() reflect.Type {
	return reflect.TypeOf((*topicRuleDestinationState)(nil)).Elem()
}

type topicRuleDestinationArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicruledestination.html#cfn-iot-topicruledestination-httpurlproperties
	HttpUrlProperties *TopicRuleDestinationHttpUrlDestinationSummary `pulumi:"httpUrlProperties"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicruledestination.html#cfn-iot-topicruledestination-status
	Status *string `pulumi:"status"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicruledestination.html#cfn-iot-topicruledestination-vpcproperties
	VpcProperties *TopicRuleDestinationVpcDestinationProperties `pulumi:"vpcProperties"`
}

// The set of arguments for constructing a TopicRuleDestination resource.
type TopicRuleDestinationArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicruledestination.html#cfn-iot-topicruledestination-httpurlproperties
	HttpUrlProperties TopicRuleDestinationHttpUrlDestinationSummaryPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicruledestination.html#cfn-iot-topicruledestination-status
	Status pulumi.StringPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicruledestination.html#cfn-iot-topicruledestination-vpcproperties
	VpcProperties TopicRuleDestinationVpcDestinationPropertiesPtrInput
}

func (TopicRuleDestinationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*topicRuleDestinationArgs)(nil)).Elem()
}

type TopicRuleDestinationInput interface {
	pulumi.Input

	ToTopicRuleDestinationOutput() TopicRuleDestinationOutput
	ToTopicRuleDestinationOutputWithContext(ctx context.Context) TopicRuleDestinationOutput
}

func (*TopicRuleDestination) ElementType() reflect.Type {
	return reflect.TypeOf((*TopicRuleDestination)(nil))
}

func (i *TopicRuleDestination) ToTopicRuleDestinationOutput() TopicRuleDestinationOutput {
	return i.ToTopicRuleDestinationOutputWithContext(context.Background())
}

func (i *TopicRuleDestination) ToTopicRuleDestinationOutputWithContext(ctx context.Context) TopicRuleDestinationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TopicRuleDestinationOutput)
}

type TopicRuleDestinationOutput struct{ *pulumi.OutputState }

func (TopicRuleDestinationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*TopicRuleDestination)(nil))
}

func (o TopicRuleDestinationOutput) ToTopicRuleDestinationOutput() TopicRuleDestinationOutput {
	return o
}

func (o TopicRuleDestinationOutput) ToTopicRuleDestinationOutputWithContext(ctx context.Context) TopicRuleDestinationOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(TopicRuleDestinationOutput{})
}
