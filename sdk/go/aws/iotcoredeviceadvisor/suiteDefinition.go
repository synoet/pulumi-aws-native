// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package iotcoredeviceadvisor

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html
type SuiteDefinition struct {
	pulumi.CustomResourceState

	SuiteDefinitionArn pulumi.StringOutput `pulumi:"suiteDefinitionArn"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html#cfn-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration
	SuiteDefinitionConfiguration pulumi.AnyOutput    `pulumi:"suiteDefinitionConfiguration"`
	SuiteDefinitionId            pulumi.StringOutput `pulumi:"suiteDefinitionId"`
	SuiteDefinitionVersion       pulumi.StringOutput `pulumi:"suiteDefinitionVersion"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html#cfn-iotcoredeviceadvisor-suitedefinition-tags
	Tags aws.TagArrayOutput `pulumi:"tags"`
}

// NewSuiteDefinition registers a new resource with the given unique name, arguments, and options.
func NewSuiteDefinition(ctx *pulumi.Context,
	name string, args *SuiteDefinitionArgs, opts ...pulumi.ResourceOption) (*SuiteDefinition, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.SuiteDefinitionConfiguration == nil {
		return nil, errors.New("invalid value for required argument 'SuiteDefinitionConfiguration'")
	}
	var resource SuiteDefinition
	err := ctx.RegisterResource("aws-native:iotcoredeviceadvisor:SuiteDefinition", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSuiteDefinition gets an existing SuiteDefinition resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSuiteDefinition(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SuiteDefinitionState, opts ...pulumi.ResourceOption) (*SuiteDefinition, error) {
	var resource SuiteDefinition
	err := ctx.ReadResource("aws-native:iotcoredeviceadvisor:SuiteDefinition", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SuiteDefinition resources.
type suiteDefinitionState struct {
}

type SuiteDefinitionState struct {
}

func (SuiteDefinitionState) ElementType() reflect.Type {
	return reflect.TypeOf((*suiteDefinitionState)(nil)).Elem()
}

type suiteDefinitionArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html#cfn-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration
	SuiteDefinitionConfiguration interface{} `pulumi:"suiteDefinitionConfiguration"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html#cfn-iotcoredeviceadvisor-suitedefinition-tags
	Tags []aws.Tag `pulumi:"tags"`
}

// The set of arguments for constructing a SuiteDefinition resource.
type SuiteDefinitionArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html#cfn-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration
	SuiteDefinitionConfiguration pulumi.Input
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html#cfn-iotcoredeviceadvisor-suitedefinition-tags
	Tags aws.TagArrayInput
}

func (SuiteDefinitionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*suiteDefinitionArgs)(nil)).Elem()
}

type SuiteDefinitionInput interface {
	pulumi.Input

	ToSuiteDefinitionOutput() SuiteDefinitionOutput
	ToSuiteDefinitionOutputWithContext(ctx context.Context) SuiteDefinitionOutput
}

func (*SuiteDefinition) ElementType() reflect.Type {
	return reflect.TypeOf((*SuiteDefinition)(nil))
}

func (i *SuiteDefinition) ToSuiteDefinitionOutput() SuiteDefinitionOutput {
	return i.ToSuiteDefinitionOutputWithContext(context.Background())
}

func (i *SuiteDefinition) ToSuiteDefinitionOutputWithContext(ctx context.Context) SuiteDefinitionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SuiteDefinitionOutput)
}

type SuiteDefinitionOutput struct{ *pulumi.OutputState }

func (SuiteDefinitionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*SuiteDefinition)(nil))
}

func (o SuiteDefinitionOutput) ToSuiteDefinitionOutput() SuiteDefinitionOutput {
	return o
}

func (o SuiteDefinitionOutput) ToSuiteDefinitionOutputWithContext(ctx context.Context) SuiteDefinitionOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(SuiteDefinitionOutput{})
}
