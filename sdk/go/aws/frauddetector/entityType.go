// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package frauddetector

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// An entity type for fraud detector.
type EntityType struct {
	pulumi.CustomResourceState

	// The entity type ARN.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The timestamp when the entity type was created.
	CreatedTime pulumi.StringOutput `pulumi:"createdTime"`
	// The entity type description.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The timestamp when the entity type was last updated.
	LastUpdatedTime pulumi.StringOutput `pulumi:"lastUpdatedTime"`
	// The name of the entity type.
	Name pulumi.StringOutput `pulumi:"name"`
	// Tags associated with this entity type.
	Tags EntityTypeTagArrayOutput `pulumi:"tags"`
}

// NewEntityType registers a new resource with the given unique name, arguments, and options.
func NewEntityType(ctx *pulumi.Context,
	name string, args *EntityTypeArgs, opts ...pulumi.ResourceOption) (*EntityType, error) {
	if args == nil {
		args = &EntityTypeArgs{}
	}

	var resource EntityType
	err := ctx.RegisterResource("aws-native:frauddetector:EntityType", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetEntityType gets an existing EntityType resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetEntityType(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *EntityTypeState, opts ...pulumi.ResourceOption) (*EntityType, error) {
	var resource EntityType
	err := ctx.ReadResource("aws-native:frauddetector:EntityType", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering EntityType resources.
type entityTypeState struct {
}

type EntityTypeState struct {
}

func (EntityTypeState) ElementType() reflect.Type {
	return reflect.TypeOf((*entityTypeState)(nil)).Elem()
}

type entityTypeArgs struct {
	// The entity type description.
	Description *string `pulumi:"description"`
	// The name of the entity type.
	Name *string `pulumi:"name"`
	// Tags associated with this entity type.
	Tags []EntityTypeTag `pulumi:"tags"`
}

// The set of arguments for constructing a EntityType resource.
type EntityTypeArgs struct {
	// The entity type description.
	Description pulumi.StringPtrInput
	// The name of the entity type.
	Name pulumi.StringPtrInput
	// Tags associated with this entity type.
	Tags EntityTypeTagArrayInput
}

func (EntityTypeArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*entityTypeArgs)(nil)).Elem()
}

type EntityTypeInput interface {
	pulumi.Input

	ToEntityTypeOutput() EntityTypeOutput
	ToEntityTypeOutputWithContext(ctx context.Context) EntityTypeOutput
}

func (*EntityType) ElementType() reflect.Type {
	return reflect.TypeOf((**EntityType)(nil)).Elem()
}

func (i *EntityType) ToEntityTypeOutput() EntityTypeOutput {
	return i.ToEntityTypeOutputWithContext(context.Background())
}

func (i *EntityType) ToEntityTypeOutputWithContext(ctx context.Context) EntityTypeOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EntityTypeOutput)
}

type EntityTypeOutput struct{ *pulumi.OutputState }

func (EntityTypeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**EntityType)(nil)).Elem()
}

func (o EntityTypeOutput) ToEntityTypeOutput() EntityTypeOutput {
	return o
}

func (o EntityTypeOutput) ToEntityTypeOutputWithContext(ctx context.Context) EntityTypeOutput {
	return o
}

// The entity type ARN.
func (o EntityTypeOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *EntityType) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

// The timestamp when the entity type was created.
func (o EntityTypeOutput) CreatedTime() pulumi.StringOutput {
	return o.ApplyT(func(v *EntityType) pulumi.StringOutput { return v.CreatedTime }).(pulumi.StringOutput)
}

// The entity type description.
func (o EntityTypeOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *EntityType) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// The timestamp when the entity type was last updated.
func (o EntityTypeOutput) LastUpdatedTime() pulumi.StringOutput {
	return o.ApplyT(func(v *EntityType) pulumi.StringOutput { return v.LastUpdatedTime }).(pulumi.StringOutput)
}

// The name of the entity type.
func (o EntityTypeOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *EntityType) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// Tags associated with this entity type.
func (o EntityTypeOutput) Tags() EntityTypeTagArrayOutput {
	return o.ApplyT(func(v *EntityType) EntityTypeTagArrayOutput { return v.Tags }).(EntityTypeTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*EntityTypeInput)(nil)).Elem(), &EntityType{})
	pulumi.RegisterOutputType(EntityTypeOutput{})
}
