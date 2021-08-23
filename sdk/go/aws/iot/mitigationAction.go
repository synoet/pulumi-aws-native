// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package iot

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-mitigationaction.html
type MitigationAction struct {
	pulumi.CustomResourceState

	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-mitigationaction.html#cfn-iot-mitigationaction-actionname
	ActionName pulumi.StringPtrOutput `pulumi:"actionName"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-mitigationaction.html#cfn-iot-mitigationaction-actionparams
	ActionParams        MitigationActionActionParamsOutput `pulumi:"actionParams"`
	MitigationActionArn pulumi.StringOutput                `pulumi:"mitigationActionArn"`
	MitigationActionId  pulumi.StringOutput                `pulumi:"mitigationActionId"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-mitigationaction.html#cfn-iot-mitigationaction-rolearn
	RoleArn pulumi.StringOutput `pulumi:"roleArn"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-mitigationaction.html#cfn-iot-mitigationaction-tags
	Tags aws.TagArrayOutput `pulumi:"tags"`
}

// NewMitigationAction registers a new resource with the given unique name, arguments, and options.
func NewMitigationAction(ctx *pulumi.Context,
	name string, args *MitigationActionArgs, opts ...pulumi.ResourceOption) (*MitigationAction, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ActionParams == nil {
		return nil, errors.New("invalid value for required argument 'ActionParams'")
	}
	if args.RoleArn == nil {
		return nil, errors.New("invalid value for required argument 'RoleArn'")
	}
	var resource MitigationAction
	err := ctx.RegisterResource("aws-native:iot:MitigationAction", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetMitigationAction gets an existing MitigationAction resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetMitigationAction(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *MitigationActionState, opts ...pulumi.ResourceOption) (*MitigationAction, error) {
	var resource MitigationAction
	err := ctx.ReadResource("aws-native:iot:MitigationAction", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering MitigationAction resources.
type mitigationActionState struct {
}

type MitigationActionState struct {
}

func (MitigationActionState) ElementType() reflect.Type {
	return reflect.TypeOf((*mitigationActionState)(nil)).Elem()
}

type mitigationActionArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-mitigationaction.html#cfn-iot-mitigationaction-actionname
	ActionName *string `pulumi:"actionName"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-mitigationaction.html#cfn-iot-mitigationaction-actionparams
	ActionParams MitigationActionActionParams `pulumi:"actionParams"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-mitigationaction.html#cfn-iot-mitigationaction-rolearn
	RoleArn string `pulumi:"roleArn"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-mitigationaction.html#cfn-iot-mitigationaction-tags
	Tags []aws.Tag `pulumi:"tags"`
}

// The set of arguments for constructing a MitigationAction resource.
type MitigationActionArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-mitigationaction.html#cfn-iot-mitigationaction-actionname
	ActionName pulumi.StringPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-mitigationaction.html#cfn-iot-mitigationaction-actionparams
	ActionParams MitigationActionActionParamsInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-mitigationaction.html#cfn-iot-mitigationaction-rolearn
	RoleArn pulumi.StringInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-mitigationaction.html#cfn-iot-mitigationaction-tags
	Tags aws.TagArrayInput
}

func (MitigationActionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*mitigationActionArgs)(nil)).Elem()
}

type MitigationActionInput interface {
	pulumi.Input

	ToMitigationActionOutput() MitigationActionOutput
	ToMitigationActionOutputWithContext(ctx context.Context) MitigationActionOutput
}

func (*MitigationAction) ElementType() reflect.Type {
	return reflect.TypeOf((*MitigationAction)(nil))
}

func (i *MitigationAction) ToMitigationActionOutput() MitigationActionOutput {
	return i.ToMitigationActionOutputWithContext(context.Background())
}

func (i *MitigationAction) ToMitigationActionOutputWithContext(ctx context.Context) MitigationActionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(MitigationActionOutput)
}

type MitigationActionOutput struct{ *pulumi.OutputState }

func (MitigationActionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*MitigationAction)(nil))
}

func (o MitigationActionOutput) ToMitigationActionOutput() MitigationActionOutput {
	return o
}

func (o MitigationActionOutput) ToMitigationActionOutputWithContext(ctx context.Context) MitigationActionOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(MitigationActionOutput{})
}
