// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package iotevents

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The AWS::IoTEvents::Input resource creates an input. To monitor your devices and processes, they must have a way to get telemetry data into AWS IoT Events. This is done by sending messages as *inputs* to AWS IoT Events. For more information, see [How to Use AWS IoT Events](https://docs.aws.amazon.com/iotevents/latest/developerguide/how-to-use-iotevents.html) in the *AWS IoT Events Developer Guide*.
type Input struct {
	pulumi.CustomResourceState

	InputDefinition InputDefinitionOutput `pulumi:"inputDefinition"`
	// A brief description of the input.
	InputDescription pulumi.StringPtrOutput `pulumi:"inputDescription"`
	// The name of the input.
	InputName pulumi.StringPtrOutput `pulumi:"inputName"`
	// An array of key-value pairs to apply to this resource.
	//
	// For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
	Tags InputTagArrayOutput `pulumi:"tags"`
}

// NewInput registers a new resource with the given unique name, arguments, and options.
func NewInput(ctx *pulumi.Context,
	name string, args *InputArgs, opts ...pulumi.ResourceOption) (*Input, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.InputDefinition == nil {
		return nil, errors.New("invalid value for required argument 'InputDefinition'")
	}
	var resource Input
	err := ctx.RegisterResource("aws-native:iotevents:Input", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetInput gets an existing Input resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetInput(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *InputState, opts ...pulumi.ResourceOption) (*Input, error) {
	var resource Input
	err := ctx.ReadResource("aws-native:iotevents:Input", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Input resources.
type inputState struct {
}

type InputState struct {
}

func (InputState) ElementType() reflect.Type {
	return reflect.TypeOf((*inputState)(nil)).Elem()
}

type inputArgs struct {
	InputDefinition InputDefinition `pulumi:"inputDefinition"`
	// A brief description of the input.
	InputDescription *string `pulumi:"inputDescription"`
	// The name of the input.
	InputName *string `pulumi:"inputName"`
	// An array of key-value pairs to apply to this resource.
	//
	// For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
	Tags []InputTag `pulumi:"tags"`
}

// The set of arguments for constructing a Input resource.
type InputArgs struct {
	InputDefinition InputDefinitionInput
	// A brief description of the input.
	InputDescription pulumi.StringPtrInput
	// The name of the input.
	InputName pulumi.StringPtrInput
	// An array of key-value pairs to apply to this resource.
	//
	// For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
	Tags InputTagArrayInput
}

func (InputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*inputArgs)(nil)).Elem()
}

type InputInput interface {
	pulumi.Input

	ToInputOutput() InputOutput
	ToInputOutputWithContext(ctx context.Context) InputOutput
}

func (*Input) ElementType() reflect.Type {
	return reflect.TypeOf((*Input)(nil))
}

func (i *Input) ToInputOutput() InputOutput {
	return i.ToInputOutputWithContext(context.Background())
}

func (i *Input) ToInputOutputWithContext(ctx context.Context) InputOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InputOutput)
}

type InputOutput struct{ *pulumi.OutputState }

func (InputOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Input)(nil))
}

func (o InputOutput) ToInputOutput() InputOutput {
	return o
}

func (o InputOutput) ToInputOutputWithContext(ctx context.Context) InputOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(InputOutput{})
}
