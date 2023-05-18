// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package glue

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// This resource adds Key-Value metadata to a Schema version of Glue Schema Registry.
type SchemaVersionMetadata struct {
	pulumi.CustomResourceState

	// Metadata key
	Key pulumi.StringOutput `pulumi:"key"`
	// Represents the version ID associated with the schema version.
	SchemaVersionId pulumi.StringOutput `pulumi:"schemaVersionId"`
	// Metadata value
	Value pulumi.StringOutput `pulumi:"value"`
}

// NewSchemaVersionMetadata registers a new resource with the given unique name, arguments, and options.
func NewSchemaVersionMetadata(ctx *pulumi.Context,
	name string, args *SchemaVersionMetadataArgs, opts ...pulumi.ResourceOption) (*SchemaVersionMetadata, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Key == nil {
		return nil, errors.New("invalid value for required argument 'Key'")
	}
	if args.SchemaVersionId == nil {
		return nil, errors.New("invalid value for required argument 'SchemaVersionId'")
	}
	if args.Value == nil {
		return nil, errors.New("invalid value for required argument 'Value'")
	}
	var resource SchemaVersionMetadata
	err := ctx.RegisterResource("aws-native:glue:SchemaVersionMetadata", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSchemaVersionMetadata gets an existing SchemaVersionMetadata resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSchemaVersionMetadata(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SchemaVersionMetadataState, opts ...pulumi.ResourceOption) (*SchemaVersionMetadata, error) {
	var resource SchemaVersionMetadata
	err := ctx.ReadResource("aws-native:glue:SchemaVersionMetadata", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SchemaVersionMetadata resources.
type schemaVersionMetadataState struct {
}

type SchemaVersionMetadataState struct {
}

func (SchemaVersionMetadataState) ElementType() reflect.Type {
	return reflect.TypeOf((*schemaVersionMetadataState)(nil)).Elem()
}

type schemaVersionMetadataArgs struct {
	// Metadata key
	Key string `pulumi:"key"`
	// Represents the version ID associated with the schema version.
	SchemaVersionId string `pulumi:"schemaVersionId"`
	// Metadata value
	Value string `pulumi:"value"`
}

// The set of arguments for constructing a SchemaVersionMetadata resource.
type SchemaVersionMetadataArgs struct {
	// Metadata key
	Key pulumi.StringInput
	// Represents the version ID associated with the schema version.
	SchemaVersionId pulumi.StringInput
	// Metadata value
	Value pulumi.StringInput
}

func (SchemaVersionMetadataArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*schemaVersionMetadataArgs)(nil)).Elem()
}

type SchemaVersionMetadataInput interface {
	pulumi.Input

	ToSchemaVersionMetadataOutput() SchemaVersionMetadataOutput
	ToSchemaVersionMetadataOutputWithContext(ctx context.Context) SchemaVersionMetadataOutput
}

func (*SchemaVersionMetadata) ElementType() reflect.Type {
	return reflect.TypeOf((**SchemaVersionMetadata)(nil)).Elem()
}

func (i *SchemaVersionMetadata) ToSchemaVersionMetadataOutput() SchemaVersionMetadataOutput {
	return i.ToSchemaVersionMetadataOutputWithContext(context.Background())
}

func (i *SchemaVersionMetadata) ToSchemaVersionMetadataOutputWithContext(ctx context.Context) SchemaVersionMetadataOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SchemaVersionMetadataOutput)
}

type SchemaVersionMetadataOutput struct{ *pulumi.OutputState }

func (SchemaVersionMetadataOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**SchemaVersionMetadata)(nil)).Elem()
}

func (o SchemaVersionMetadataOutput) ToSchemaVersionMetadataOutput() SchemaVersionMetadataOutput {
	return o
}

func (o SchemaVersionMetadataOutput) ToSchemaVersionMetadataOutputWithContext(ctx context.Context) SchemaVersionMetadataOutput {
	return o
}

// Metadata key
func (o SchemaVersionMetadataOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v *SchemaVersionMetadata) pulumi.StringOutput { return v.Key }).(pulumi.StringOutput)
}

// Represents the version ID associated with the schema version.
func (o SchemaVersionMetadataOutput) SchemaVersionId() pulumi.StringOutput {
	return o.ApplyT(func(v *SchemaVersionMetadata) pulumi.StringOutput { return v.SchemaVersionId }).(pulumi.StringOutput)
}

// Metadata value
func (o SchemaVersionMetadataOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v *SchemaVersionMetadata) pulumi.StringOutput { return v.Value }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*SchemaVersionMetadataInput)(nil)).Elem(), &SchemaVersionMetadata{})
	pulumi.RegisterOutputType(SchemaVersionMetadataOutput{})
}
