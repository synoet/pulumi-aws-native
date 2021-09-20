// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package macie

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Macie FindingsFilter resource schema.
type FindingsFilter struct {
	pulumi.CustomResourceState

	// Findings filter action.
	Action FindingsFilterFindingFilterActionPtrOutput `pulumi:"action"`
	// Findings filter ARN.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// Findings filter description
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// Findings filter criteria.
	FindingCriteria FindingsFilterFindingCriteriaOutput `pulumi:"findingCriteria"`
	// Findings filters list.
	FindingsFilterListItems FindingsFilterFindingsFilterListItemArrayOutput `pulumi:"findingsFilterListItems"`
	// Findings filter name
	Name pulumi.StringOutput `pulumi:"name"`
	// Findings filter position.
	Position pulumi.IntPtrOutput `pulumi:"position"`
}

// NewFindingsFilter registers a new resource with the given unique name, arguments, and options.
func NewFindingsFilter(ctx *pulumi.Context,
	name string, args *FindingsFilterArgs, opts ...pulumi.ResourceOption) (*FindingsFilter, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.FindingCriteria == nil {
		return nil, errors.New("invalid value for required argument 'FindingCriteria'")
	}
	if args.Name == nil {
		return nil, errors.New("invalid value for required argument 'Name'")
	}
	var resource FindingsFilter
	err := ctx.RegisterResource("aws-native:macie:FindingsFilter", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetFindingsFilter gets an existing FindingsFilter resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetFindingsFilter(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *FindingsFilterState, opts ...pulumi.ResourceOption) (*FindingsFilter, error) {
	var resource FindingsFilter
	err := ctx.ReadResource("aws-native:macie:FindingsFilter", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering FindingsFilter resources.
type findingsFilterState struct {
}

type FindingsFilterState struct {
}

func (FindingsFilterState) ElementType() reflect.Type {
	return reflect.TypeOf((*findingsFilterState)(nil)).Elem()
}

type findingsFilterArgs struct {
	// Findings filter action.
	Action *FindingsFilterFindingFilterAction `pulumi:"action"`
	// Findings filter description
	Description *string `pulumi:"description"`
	// Findings filter criteria.
	FindingCriteria FindingsFilterFindingCriteria `pulumi:"findingCriteria"`
	// Findings filter name
	Name string `pulumi:"name"`
	// Findings filter position.
	Position *int `pulumi:"position"`
}

// The set of arguments for constructing a FindingsFilter resource.
type FindingsFilterArgs struct {
	// Findings filter action.
	Action FindingsFilterFindingFilterActionPtrInput
	// Findings filter description
	Description pulumi.StringPtrInput
	// Findings filter criteria.
	FindingCriteria FindingsFilterFindingCriteriaInput
	// Findings filter name
	Name pulumi.StringInput
	// Findings filter position.
	Position pulumi.IntPtrInput
}

func (FindingsFilterArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*findingsFilterArgs)(nil)).Elem()
}

type FindingsFilterInput interface {
	pulumi.Input

	ToFindingsFilterOutput() FindingsFilterOutput
	ToFindingsFilterOutputWithContext(ctx context.Context) FindingsFilterOutput
}

func (*FindingsFilter) ElementType() reflect.Type {
	return reflect.TypeOf((*FindingsFilter)(nil))
}

func (i *FindingsFilter) ToFindingsFilterOutput() FindingsFilterOutput {
	return i.ToFindingsFilterOutputWithContext(context.Background())
}

func (i *FindingsFilter) ToFindingsFilterOutputWithContext(ctx context.Context) FindingsFilterOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FindingsFilterOutput)
}

type FindingsFilterOutput struct{ *pulumi.OutputState }

func (FindingsFilterOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*FindingsFilter)(nil))
}

func (o FindingsFilterOutput) ToFindingsFilterOutput() FindingsFilterOutput {
	return o
}

func (o FindingsFilterOutput) ToFindingsFilterOutputWithContext(ctx context.Context) FindingsFilterOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(FindingsFilterOutput{})
}
