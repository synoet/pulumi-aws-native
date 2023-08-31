// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package medialive

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::MediaLive::Input
//
// Deprecated: Input is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type Input struct {
	pulumi.CustomResourceState

	Arn                 pulumi.StringOutput                     `pulumi:"arn"`
	Destinations        InputDestinationRequestArrayOutput      `pulumi:"destinations"`
	InputDevices        InputDeviceSettingsArrayOutput          `pulumi:"inputDevices"`
	InputSecurityGroups pulumi.StringArrayOutput                `pulumi:"inputSecurityGroups"`
	MediaConnectFlows   InputMediaConnectFlowRequestArrayOutput `pulumi:"mediaConnectFlows"`
	Name                pulumi.StringPtrOutput                  `pulumi:"name"`
	RoleArn             pulumi.StringPtrOutput                  `pulumi:"roleArn"`
	Sources             InputSourceRequestArrayOutput           `pulumi:"sources"`
	Tags                pulumi.AnyOutput                        `pulumi:"tags"`
	Type                pulumi.StringPtrOutput                  `pulumi:"type"`
	Vpc                 InputVpcRequestPtrOutput                `pulumi:"vpc"`
}

// NewInput registers a new resource with the given unique name, arguments, and options.
func NewInput(ctx *pulumi.Context,
	name string, args *InputArgs, opts ...pulumi.ResourceOption) (*Input, error) {
	if args == nil {
		args = &InputArgs{}
	}

	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"type",
		"vpc",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Input
	err := ctx.RegisterResource("aws-native:medialive:Input", name, args, &resource, opts...)
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
	err := ctx.ReadResource("aws-native:medialive:Input", name, id, state, &resource, opts...)
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
	Destinations        []InputDestinationRequest      `pulumi:"destinations"`
	InputDevices        []InputDeviceSettings          `pulumi:"inputDevices"`
	InputSecurityGroups []string                       `pulumi:"inputSecurityGroups"`
	MediaConnectFlows   []InputMediaConnectFlowRequest `pulumi:"mediaConnectFlows"`
	Name                *string                        `pulumi:"name"`
	RoleArn             *string                        `pulumi:"roleArn"`
	Sources             []InputSourceRequest           `pulumi:"sources"`
	Tags                interface{}                    `pulumi:"tags"`
	Type                *string                        `pulumi:"type"`
	Vpc                 *InputVpcRequest               `pulumi:"vpc"`
}

// The set of arguments for constructing a Input resource.
type InputArgs struct {
	Destinations        InputDestinationRequestArrayInput
	InputDevices        InputDeviceSettingsArrayInput
	InputSecurityGroups pulumi.StringArrayInput
	MediaConnectFlows   InputMediaConnectFlowRequestArrayInput
	Name                pulumi.StringPtrInput
	RoleArn             pulumi.StringPtrInput
	Sources             InputSourceRequestArrayInput
	Tags                pulumi.Input
	Type                pulumi.StringPtrInput
	Vpc                 InputVpcRequestPtrInput
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
	return reflect.TypeOf((**Input)(nil)).Elem()
}

func (i *Input) ToInputOutput() InputOutput {
	return i.ToInputOutputWithContext(context.Background())
}

func (i *Input) ToInputOutputWithContext(ctx context.Context) InputOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InputOutput)
}

type InputOutput struct{ *pulumi.OutputState }

func (InputOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Input)(nil)).Elem()
}

func (o InputOutput) ToInputOutput() InputOutput {
	return o
}

func (o InputOutput) ToInputOutputWithContext(ctx context.Context) InputOutput {
	return o
}

func (o InputOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *Input) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

func (o InputOutput) Destinations() InputDestinationRequestArrayOutput {
	return o.ApplyT(func(v *Input) InputDestinationRequestArrayOutput { return v.Destinations }).(InputDestinationRequestArrayOutput)
}

func (o InputOutput) InputDevices() InputDeviceSettingsArrayOutput {
	return o.ApplyT(func(v *Input) InputDeviceSettingsArrayOutput { return v.InputDevices }).(InputDeviceSettingsArrayOutput)
}

func (o InputOutput) InputSecurityGroups() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Input) pulumi.StringArrayOutput { return v.InputSecurityGroups }).(pulumi.StringArrayOutput)
}

func (o InputOutput) MediaConnectFlows() InputMediaConnectFlowRequestArrayOutput {
	return o.ApplyT(func(v *Input) InputMediaConnectFlowRequestArrayOutput { return v.MediaConnectFlows }).(InputMediaConnectFlowRequestArrayOutput)
}

func (o InputOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Input) pulumi.StringPtrOutput { return v.Name }).(pulumi.StringPtrOutput)
}

func (o InputOutput) RoleArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Input) pulumi.StringPtrOutput { return v.RoleArn }).(pulumi.StringPtrOutput)
}

func (o InputOutput) Sources() InputSourceRequestArrayOutput {
	return o.ApplyT(func(v *Input) InputSourceRequestArrayOutput { return v.Sources }).(InputSourceRequestArrayOutput)
}

func (o InputOutput) Tags() pulumi.AnyOutput {
	return o.ApplyT(func(v *Input) pulumi.AnyOutput { return v.Tags }).(pulumi.AnyOutput)
}

func (o InputOutput) Type() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Input) pulumi.StringPtrOutput { return v.Type }).(pulumi.StringPtrOutput)
}

func (o InputOutput) Vpc() InputVpcRequestPtrOutput {
	return o.ApplyT(func(v *Input) InputVpcRequestPtrOutput { return v.Vpc }).(InputVpcRequestPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*InputInput)(nil)).Elem(), &Input{})
	pulumi.RegisterOutputType(InputOutput{})
}
