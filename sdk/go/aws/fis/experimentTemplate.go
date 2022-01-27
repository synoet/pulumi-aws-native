// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package fis

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for AWS::FIS::ExperimentTemplate
type ExperimentTemplate struct {
	pulumi.CustomResourceState

	Actions        ExperimentTemplateActionMapPtrOutput       `pulumi:"actions"`
	Description    pulumi.StringOutput                        `pulumi:"description"`
	RoleArn        pulumi.StringOutput                        `pulumi:"roleArn"`
	StopConditions ExperimentTemplateStopConditionArrayOutput `pulumi:"stopConditions"`
	Tags           pulumi.AnyOutput                           `pulumi:"tags"`
	Targets        ExperimentTemplateTargetMapOutput          `pulumi:"targets"`
}

// NewExperimentTemplate registers a new resource with the given unique name, arguments, and options.
func NewExperimentTemplate(ctx *pulumi.Context,
	name string, args *ExperimentTemplateArgs, opts ...pulumi.ResourceOption) (*ExperimentTemplate, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Description == nil {
		return nil, errors.New("invalid value for required argument 'Description'")
	}
	if args.RoleArn == nil {
		return nil, errors.New("invalid value for required argument 'RoleArn'")
	}
	if args.StopConditions == nil {
		return nil, errors.New("invalid value for required argument 'StopConditions'")
	}
	if args.Tags == nil {
		return nil, errors.New("invalid value for required argument 'Tags'")
	}
	if args.Targets == nil {
		return nil, errors.New("invalid value for required argument 'Targets'")
	}
	var resource ExperimentTemplate
	err := ctx.RegisterResource("aws-native:fis:ExperimentTemplate", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetExperimentTemplate gets an existing ExperimentTemplate resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetExperimentTemplate(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ExperimentTemplateState, opts ...pulumi.ResourceOption) (*ExperimentTemplate, error) {
	var resource ExperimentTemplate
	err := ctx.ReadResource("aws-native:fis:ExperimentTemplate", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ExperimentTemplate resources.
type experimentTemplateState struct {
}

type ExperimentTemplateState struct {
}

func (ExperimentTemplateState) ElementType() reflect.Type {
	return reflect.TypeOf((*experimentTemplateState)(nil)).Elem()
}

type experimentTemplateArgs struct {
	Actions        *ExperimentTemplateActionMap      `pulumi:"actions"`
	Description    string                            `pulumi:"description"`
	RoleArn        string                            `pulumi:"roleArn"`
	StopConditions []ExperimentTemplateStopCondition `pulumi:"stopConditions"`
	Tags           interface{}                       `pulumi:"tags"`
	Targets        ExperimentTemplateTargetMap       `pulumi:"targets"`
}

// The set of arguments for constructing a ExperimentTemplate resource.
type ExperimentTemplateArgs struct {
	Actions        ExperimentTemplateActionMapPtrInput
	Description    pulumi.StringInput
	RoleArn        pulumi.StringInput
	StopConditions ExperimentTemplateStopConditionArrayInput
	Tags           pulumi.Input
	Targets        ExperimentTemplateTargetMapInput
}

func (ExperimentTemplateArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*experimentTemplateArgs)(nil)).Elem()
}

type ExperimentTemplateInput interface {
	pulumi.Input

	ToExperimentTemplateOutput() ExperimentTemplateOutput
	ToExperimentTemplateOutputWithContext(ctx context.Context) ExperimentTemplateOutput
}

func (*ExperimentTemplate) ElementType() reflect.Type {
	return reflect.TypeOf((**ExperimentTemplate)(nil)).Elem()
}

func (i *ExperimentTemplate) ToExperimentTemplateOutput() ExperimentTemplateOutput {
	return i.ToExperimentTemplateOutputWithContext(context.Background())
}

func (i *ExperimentTemplate) ToExperimentTemplateOutputWithContext(ctx context.Context) ExperimentTemplateOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ExperimentTemplateOutput)
}

type ExperimentTemplateOutput struct{ *pulumi.OutputState }

func (ExperimentTemplateOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ExperimentTemplate)(nil)).Elem()
}

func (o ExperimentTemplateOutput) ToExperimentTemplateOutput() ExperimentTemplateOutput {
	return o
}

func (o ExperimentTemplateOutput) ToExperimentTemplateOutputWithContext(ctx context.Context) ExperimentTemplateOutput {
	return o
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ExperimentTemplateInput)(nil)).Elem(), &ExperimentTemplate{})
	pulumi.RegisterOutputType(ExperimentTemplateOutput{})
}
