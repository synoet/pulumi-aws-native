// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package frauddetector

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// An outcome for rule evaluation.
type Outcome struct {
	pulumi.CustomResourceState

	// The outcome ARN.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The timestamp when the outcome was created.
	CreatedTime pulumi.StringOutput `pulumi:"createdTime"`
	// The outcome description.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The timestamp when the outcome was last updated.
	LastUpdatedTime pulumi.StringOutput `pulumi:"lastUpdatedTime"`
	// The name of the outcome.
	Name pulumi.StringOutput `pulumi:"name"`
	// Tags associated with this outcome.
	Tags OutcomeTagArrayOutput `pulumi:"tags"`
}

// NewOutcome registers a new resource with the given unique name, arguments, and options.
func NewOutcome(ctx *pulumi.Context,
	name string, args *OutcomeArgs, opts ...pulumi.ResourceOption) (*Outcome, error) {
	if args == nil {
		args = &OutcomeArgs{}
	}

	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"name",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Outcome
	err := ctx.RegisterResource("aws-native:frauddetector:Outcome", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetOutcome gets an existing Outcome resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetOutcome(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *OutcomeState, opts ...pulumi.ResourceOption) (*Outcome, error) {
	var resource Outcome
	err := ctx.ReadResource("aws-native:frauddetector:Outcome", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Outcome resources.
type outcomeState struct {
}

type OutcomeState struct {
}

func (OutcomeState) ElementType() reflect.Type {
	return reflect.TypeOf((*outcomeState)(nil)).Elem()
}

type outcomeArgs struct {
	// The outcome description.
	Description *string `pulumi:"description"`
	// The name of the outcome.
	Name *string `pulumi:"name"`
	// Tags associated with this outcome.
	Tags []OutcomeTag `pulumi:"tags"`
}

// The set of arguments for constructing a Outcome resource.
type OutcomeArgs struct {
	// The outcome description.
	Description pulumi.StringPtrInput
	// The name of the outcome.
	Name pulumi.StringPtrInput
	// Tags associated with this outcome.
	Tags OutcomeTagArrayInput
}

func (OutcomeArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*outcomeArgs)(nil)).Elem()
}

type OutcomeInput interface {
	pulumi.Input

	ToOutcomeOutput() OutcomeOutput
	ToOutcomeOutputWithContext(ctx context.Context) OutcomeOutput
}

func (*Outcome) ElementType() reflect.Type {
	return reflect.TypeOf((**Outcome)(nil)).Elem()
}

func (i *Outcome) ToOutcomeOutput() OutcomeOutput {
	return i.ToOutcomeOutputWithContext(context.Background())
}

func (i *Outcome) ToOutcomeOutputWithContext(ctx context.Context) OutcomeOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OutcomeOutput)
}

type OutcomeOutput struct{ *pulumi.OutputState }

func (OutcomeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Outcome)(nil)).Elem()
}

func (o OutcomeOutput) ToOutcomeOutput() OutcomeOutput {
	return o
}

func (o OutcomeOutput) ToOutcomeOutputWithContext(ctx context.Context) OutcomeOutput {
	return o
}

// The outcome ARN.
func (o OutcomeOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *Outcome) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

// The timestamp when the outcome was created.
func (o OutcomeOutput) CreatedTime() pulumi.StringOutput {
	return o.ApplyT(func(v *Outcome) pulumi.StringOutput { return v.CreatedTime }).(pulumi.StringOutput)
}

// The outcome description.
func (o OutcomeOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Outcome) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// The timestamp when the outcome was last updated.
func (o OutcomeOutput) LastUpdatedTime() pulumi.StringOutput {
	return o.ApplyT(func(v *Outcome) pulumi.StringOutput { return v.LastUpdatedTime }).(pulumi.StringOutput)
}

// The name of the outcome.
func (o OutcomeOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Outcome) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// Tags associated with this outcome.
func (o OutcomeOutput) Tags() OutcomeTagArrayOutput {
	return o.ApplyT(func(v *Outcome) OutcomeTagArrayOutput { return v.Tags }).(OutcomeTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*OutcomeInput)(nil)).Elem(), &Outcome{})
	pulumi.RegisterOutputType(OutcomeOutput{})
}
