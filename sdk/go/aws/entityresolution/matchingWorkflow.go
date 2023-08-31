// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package entityresolution

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// MatchingWorkflow defined in AWS Entity Resolution service
type MatchingWorkflow struct {
	pulumi.CustomResourceState

	CreatedAt pulumi.StringOutput `pulumi:"createdAt"`
	// The description of the MatchingWorkflow
	Description          pulumi.StringPtrOutput                     `pulumi:"description"`
	InputSourceConfig    MatchingWorkflowInputSourceArrayOutput     `pulumi:"inputSourceConfig"`
	OutputSourceConfig   MatchingWorkflowOutputSourceArrayOutput    `pulumi:"outputSourceConfig"`
	ResolutionTechniques MatchingWorkflowResolutionTechniquesOutput `pulumi:"resolutionTechniques"`
	RoleArn              pulumi.StringOutput                        `pulumi:"roleArn"`
	Tags                 MatchingWorkflowTagArrayOutput             `pulumi:"tags"`
	UpdatedAt            pulumi.StringOutput                        `pulumi:"updatedAt"`
	WorkflowArn          pulumi.StringOutput                        `pulumi:"workflowArn"`
	// The name of the MatchingWorkflow
	WorkflowName pulumi.StringOutput `pulumi:"workflowName"`
}

// NewMatchingWorkflow registers a new resource with the given unique name, arguments, and options.
func NewMatchingWorkflow(ctx *pulumi.Context,
	name string, args *MatchingWorkflowArgs, opts ...pulumi.ResourceOption) (*MatchingWorkflow, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.InputSourceConfig == nil {
		return nil, errors.New("invalid value for required argument 'InputSourceConfig'")
	}
	if args.OutputSourceConfig == nil {
		return nil, errors.New("invalid value for required argument 'OutputSourceConfig'")
	}
	if args.ResolutionTechniques == nil {
		return nil, errors.New("invalid value for required argument 'ResolutionTechniques'")
	}
	if args.RoleArn == nil {
		return nil, errors.New("invalid value for required argument 'RoleArn'")
	}
	if args.WorkflowName == nil {
		return nil, errors.New("invalid value for required argument 'WorkflowName'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"workflowName",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource MatchingWorkflow
	err := ctx.RegisterResource("aws-native:entityresolution:MatchingWorkflow", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetMatchingWorkflow gets an existing MatchingWorkflow resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetMatchingWorkflow(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *MatchingWorkflowState, opts ...pulumi.ResourceOption) (*MatchingWorkflow, error) {
	var resource MatchingWorkflow
	err := ctx.ReadResource("aws-native:entityresolution:MatchingWorkflow", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering MatchingWorkflow resources.
type matchingWorkflowState struct {
}

type MatchingWorkflowState struct {
}

func (MatchingWorkflowState) ElementType() reflect.Type {
	return reflect.TypeOf((*matchingWorkflowState)(nil)).Elem()
}

type matchingWorkflowArgs struct {
	// The description of the MatchingWorkflow
	Description          *string                              `pulumi:"description"`
	InputSourceConfig    []MatchingWorkflowInputSource        `pulumi:"inputSourceConfig"`
	OutputSourceConfig   []MatchingWorkflowOutputSource       `pulumi:"outputSourceConfig"`
	ResolutionTechniques MatchingWorkflowResolutionTechniques `pulumi:"resolutionTechniques"`
	RoleArn              string                               `pulumi:"roleArn"`
	Tags                 []MatchingWorkflowTag                `pulumi:"tags"`
	// The name of the MatchingWorkflow
	WorkflowName string `pulumi:"workflowName"`
}

// The set of arguments for constructing a MatchingWorkflow resource.
type MatchingWorkflowArgs struct {
	// The description of the MatchingWorkflow
	Description          pulumi.StringPtrInput
	InputSourceConfig    MatchingWorkflowInputSourceArrayInput
	OutputSourceConfig   MatchingWorkflowOutputSourceArrayInput
	ResolutionTechniques MatchingWorkflowResolutionTechniquesInput
	RoleArn              pulumi.StringInput
	Tags                 MatchingWorkflowTagArrayInput
	// The name of the MatchingWorkflow
	WorkflowName pulumi.StringInput
}

func (MatchingWorkflowArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*matchingWorkflowArgs)(nil)).Elem()
}

type MatchingWorkflowInput interface {
	pulumi.Input

	ToMatchingWorkflowOutput() MatchingWorkflowOutput
	ToMatchingWorkflowOutputWithContext(ctx context.Context) MatchingWorkflowOutput
}

func (*MatchingWorkflow) ElementType() reflect.Type {
	return reflect.TypeOf((**MatchingWorkflow)(nil)).Elem()
}

func (i *MatchingWorkflow) ToMatchingWorkflowOutput() MatchingWorkflowOutput {
	return i.ToMatchingWorkflowOutputWithContext(context.Background())
}

func (i *MatchingWorkflow) ToMatchingWorkflowOutputWithContext(ctx context.Context) MatchingWorkflowOutput {
	return pulumi.ToOutputWithContext(ctx, i).(MatchingWorkflowOutput)
}

type MatchingWorkflowOutput struct{ *pulumi.OutputState }

func (MatchingWorkflowOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**MatchingWorkflow)(nil)).Elem()
}

func (o MatchingWorkflowOutput) ToMatchingWorkflowOutput() MatchingWorkflowOutput {
	return o
}

func (o MatchingWorkflowOutput) ToMatchingWorkflowOutputWithContext(ctx context.Context) MatchingWorkflowOutput {
	return o
}

func (o MatchingWorkflowOutput) CreatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v *MatchingWorkflow) pulumi.StringOutput { return v.CreatedAt }).(pulumi.StringOutput)
}

// The description of the MatchingWorkflow
func (o MatchingWorkflowOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *MatchingWorkflow) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

func (o MatchingWorkflowOutput) InputSourceConfig() MatchingWorkflowInputSourceArrayOutput {
	return o.ApplyT(func(v *MatchingWorkflow) MatchingWorkflowInputSourceArrayOutput { return v.InputSourceConfig }).(MatchingWorkflowInputSourceArrayOutput)
}

func (o MatchingWorkflowOutput) OutputSourceConfig() MatchingWorkflowOutputSourceArrayOutput {
	return o.ApplyT(func(v *MatchingWorkflow) MatchingWorkflowOutputSourceArrayOutput { return v.OutputSourceConfig }).(MatchingWorkflowOutputSourceArrayOutput)
}

func (o MatchingWorkflowOutput) ResolutionTechniques() MatchingWorkflowResolutionTechniquesOutput {
	return o.ApplyT(func(v *MatchingWorkflow) MatchingWorkflowResolutionTechniquesOutput { return v.ResolutionTechniques }).(MatchingWorkflowResolutionTechniquesOutput)
}

func (o MatchingWorkflowOutput) RoleArn() pulumi.StringOutput {
	return o.ApplyT(func(v *MatchingWorkflow) pulumi.StringOutput { return v.RoleArn }).(pulumi.StringOutput)
}

func (o MatchingWorkflowOutput) Tags() MatchingWorkflowTagArrayOutput {
	return o.ApplyT(func(v *MatchingWorkflow) MatchingWorkflowTagArrayOutput { return v.Tags }).(MatchingWorkflowTagArrayOutput)
}

func (o MatchingWorkflowOutput) UpdatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v *MatchingWorkflow) pulumi.StringOutput { return v.UpdatedAt }).(pulumi.StringOutput)
}

func (o MatchingWorkflowOutput) WorkflowArn() pulumi.StringOutput {
	return o.ApplyT(func(v *MatchingWorkflow) pulumi.StringOutput { return v.WorkflowArn }).(pulumi.StringOutput)
}

// The name of the MatchingWorkflow
func (o MatchingWorkflowOutput) WorkflowName() pulumi.StringOutput {
	return o.ApplyT(func(v *MatchingWorkflow) pulumi.StringOutput { return v.WorkflowName }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*MatchingWorkflowInput)(nil)).Elem(), &MatchingWorkflow{})
	pulumi.RegisterOutputType(MatchingWorkflowOutput{})
}
