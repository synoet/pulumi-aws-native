// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package guardduty

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::GuardDuty::Filter
//
// Deprecated: Filter is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type Filter struct {
	pulumi.CustomResourceState

	Action          pulumi.StringOutput         `pulumi:"action"`
	Description     pulumi.StringOutput         `pulumi:"description"`
	DetectorId      pulumi.StringOutput         `pulumi:"detectorId"`
	FindingCriteria FilterFindingCriteriaOutput `pulumi:"findingCriteria"`
	Name            pulumi.StringOutput         `pulumi:"name"`
	Rank            pulumi.IntOutput            `pulumi:"rank"`
	Tags            FilterTagArrayOutput        `pulumi:"tags"`
}

// NewFilter registers a new resource with the given unique name, arguments, and options.
func NewFilter(ctx *pulumi.Context,
	name string, args *FilterArgs, opts ...pulumi.ResourceOption) (*Filter, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Action == nil {
		return nil, errors.New("invalid value for required argument 'Action'")
	}
	if args.Description == nil {
		return nil, errors.New("invalid value for required argument 'Description'")
	}
	if args.DetectorId == nil {
		return nil, errors.New("invalid value for required argument 'DetectorId'")
	}
	if args.FindingCriteria == nil {
		return nil, errors.New("invalid value for required argument 'FindingCriteria'")
	}
	if args.Rank == nil {
		return nil, errors.New("invalid value for required argument 'Rank'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"detectorId",
		"name",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Filter
	err := ctx.RegisterResource("aws-native:guardduty:Filter", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetFilter gets an existing Filter resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetFilter(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *FilterState, opts ...pulumi.ResourceOption) (*Filter, error) {
	var resource Filter
	err := ctx.ReadResource("aws-native:guardduty:Filter", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Filter resources.
type filterState struct {
}

type FilterState struct {
}

func (FilterState) ElementType() reflect.Type {
	return reflect.TypeOf((*filterState)(nil)).Elem()
}

type filterArgs struct {
	Action          string                `pulumi:"action"`
	Description     string                `pulumi:"description"`
	DetectorId      string                `pulumi:"detectorId"`
	FindingCriteria FilterFindingCriteria `pulumi:"findingCriteria"`
	Name            *string               `pulumi:"name"`
	Rank            int                   `pulumi:"rank"`
	Tags            []FilterTag           `pulumi:"tags"`
}

// The set of arguments for constructing a Filter resource.
type FilterArgs struct {
	Action          pulumi.StringInput
	Description     pulumi.StringInput
	DetectorId      pulumi.StringInput
	FindingCriteria FilterFindingCriteriaInput
	Name            pulumi.StringPtrInput
	Rank            pulumi.IntInput
	Tags            FilterTagArrayInput
}

func (FilterArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*filterArgs)(nil)).Elem()
}

type FilterInput interface {
	pulumi.Input

	ToFilterOutput() FilterOutput
	ToFilterOutputWithContext(ctx context.Context) FilterOutput
}

func (*Filter) ElementType() reflect.Type {
	return reflect.TypeOf((**Filter)(nil)).Elem()
}

func (i *Filter) ToFilterOutput() FilterOutput {
	return i.ToFilterOutputWithContext(context.Background())
}

func (i *Filter) ToFilterOutputWithContext(ctx context.Context) FilterOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FilterOutput)
}

type FilterOutput struct{ *pulumi.OutputState }

func (FilterOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Filter)(nil)).Elem()
}

func (o FilterOutput) ToFilterOutput() FilterOutput {
	return o
}

func (o FilterOutput) ToFilterOutputWithContext(ctx context.Context) FilterOutput {
	return o
}

func (o FilterOutput) Action() pulumi.StringOutput {
	return o.ApplyT(func(v *Filter) pulumi.StringOutput { return v.Action }).(pulumi.StringOutput)
}

func (o FilterOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v *Filter) pulumi.StringOutput { return v.Description }).(pulumi.StringOutput)
}

func (o FilterOutput) DetectorId() pulumi.StringOutput {
	return o.ApplyT(func(v *Filter) pulumi.StringOutput { return v.DetectorId }).(pulumi.StringOutput)
}

func (o FilterOutput) FindingCriteria() FilterFindingCriteriaOutput {
	return o.ApplyT(func(v *Filter) FilterFindingCriteriaOutput { return v.FindingCriteria }).(FilterFindingCriteriaOutput)
}

func (o FilterOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Filter) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o FilterOutput) Rank() pulumi.IntOutput {
	return o.ApplyT(func(v *Filter) pulumi.IntOutput { return v.Rank }).(pulumi.IntOutput)
}

func (o FilterOutput) Tags() FilterTagArrayOutput {
	return o.ApplyT(func(v *Filter) FilterTagArrayOutput { return v.Tags }).(FilterTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*FilterInput)(nil)).Elem(), &Filter{})
	pulumi.RegisterOutputType(FilterOutput{})
}
