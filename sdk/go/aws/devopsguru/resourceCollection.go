// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package devopsguru

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// This resource schema represents the ResourceCollection resource in the Amazon DevOps Guru.
type ResourceCollection struct {
	pulumi.CustomResourceState

	ResourceCollectionFilter ResourceCollectionFilterOutput `pulumi:"resourceCollectionFilter"`
	// The type of ResourceCollection
	ResourceCollectionType ResourceCollectionTypeOutput `pulumi:"resourceCollectionType"`
}

// NewResourceCollection registers a new resource with the given unique name, arguments, and options.
func NewResourceCollection(ctx *pulumi.Context,
	name string, args *ResourceCollectionArgs, opts ...pulumi.ResourceOption) (*ResourceCollection, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ResourceCollectionFilter == nil {
		return nil, errors.New("invalid value for required argument 'ResourceCollectionFilter'")
	}
	var resource ResourceCollection
	err := ctx.RegisterResource("aws-native:devopsguru:ResourceCollection", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetResourceCollection gets an existing ResourceCollection resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetResourceCollection(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ResourceCollectionState, opts ...pulumi.ResourceOption) (*ResourceCollection, error) {
	var resource ResourceCollection
	err := ctx.ReadResource("aws-native:devopsguru:ResourceCollection", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ResourceCollection resources.
type resourceCollectionState struct {
}

type ResourceCollectionState struct {
}

func (ResourceCollectionState) ElementType() reflect.Type {
	return reflect.TypeOf((*resourceCollectionState)(nil)).Elem()
}

type resourceCollectionArgs struct {
	ResourceCollectionFilter ResourceCollectionFilter `pulumi:"resourceCollectionFilter"`
}

// The set of arguments for constructing a ResourceCollection resource.
type ResourceCollectionArgs struct {
	ResourceCollectionFilter ResourceCollectionFilterInput
}

func (ResourceCollectionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*resourceCollectionArgs)(nil)).Elem()
}

type ResourceCollectionInput interface {
	pulumi.Input

	ToResourceCollectionOutput() ResourceCollectionOutput
	ToResourceCollectionOutputWithContext(ctx context.Context) ResourceCollectionOutput
}

func (*ResourceCollection) ElementType() reflect.Type {
	return reflect.TypeOf((**ResourceCollection)(nil)).Elem()
}

func (i *ResourceCollection) ToResourceCollectionOutput() ResourceCollectionOutput {
	return i.ToResourceCollectionOutputWithContext(context.Background())
}

func (i *ResourceCollection) ToResourceCollectionOutputWithContext(ctx context.Context) ResourceCollectionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ResourceCollectionOutput)
}

type ResourceCollectionOutput struct{ *pulumi.OutputState }

func (ResourceCollectionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ResourceCollection)(nil)).Elem()
}

func (o ResourceCollectionOutput) ToResourceCollectionOutput() ResourceCollectionOutput {
	return o
}

func (o ResourceCollectionOutput) ToResourceCollectionOutputWithContext(ctx context.Context) ResourceCollectionOutput {
	return o
}

func (o ResourceCollectionOutput) ResourceCollectionFilter() ResourceCollectionFilterOutput {
	return o.ApplyT(func(v *ResourceCollection) ResourceCollectionFilterOutput { return v.ResourceCollectionFilter }).(ResourceCollectionFilterOutput)
}

// The type of ResourceCollection
func (o ResourceCollectionOutput) ResourceCollectionType() ResourceCollectionTypeOutput {
	return o.ApplyT(func(v *ResourceCollection) ResourceCollectionTypeOutput { return v.ResourceCollectionType }).(ResourceCollectionTypeOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ResourceCollectionInput)(nil)).Elem(), &ResourceCollection{})
	pulumi.RegisterOutputType(ResourceCollectionOutput{})
}
