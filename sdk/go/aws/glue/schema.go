// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package glue

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// This resource represents a schema of Glue Schema Registry.
type Schema struct {
	pulumi.CustomResourceState

	// Amazon Resource Name for the Schema.
	Arn               pulumi.StringOutput        `pulumi:"arn"`
	CheckpointVersion SchemaVersionTypePtrOutput `pulumi:"checkpointVersion"`
	// Compatibility setting for the schema.
	Compatibility SchemaCompatibilityOutput `pulumi:"compatibility"`
	// Data format name to use for the schema. Accepted values: 'AVRO', 'JSON'
	DataFormat SchemaDataFormatOutput `pulumi:"dataFormat"`
	// A description of the schema. If description is not provided, there will not be any default value for this.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// Represents the version ID associated with the initial schema version.
	InitialSchemaVersionId pulumi.StringOutput `pulumi:"initialSchemaVersionId"`
	// Name of the schema.
	Name     pulumi.StringOutput     `pulumi:"name"`
	Registry SchemaRegistryPtrOutput `pulumi:"registry"`
	// Definition for the initial schema version in plain-text.
	SchemaDefinition pulumi.StringOutput `pulumi:"schemaDefinition"`
	// List of tags to tag the schema
	Tags SchemaTagArrayOutput `pulumi:"tags"`
}

// NewSchema registers a new resource with the given unique name, arguments, and options.
func NewSchema(ctx *pulumi.Context,
	name string, args *SchemaArgs, opts ...pulumi.ResourceOption) (*Schema, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Compatibility == nil {
		return nil, errors.New("invalid value for required argument 'Compatibility'")
	}
	if args.DataFormat == nil {
		return nil, errors.New("invalid value for required argument 'DataFormat'")
	}
	if args.Name == nil {
		return nil, errors.New("invalid value for required argument 'Name'")
	}
	if args.SchemaDefinition == nil {
		return nil, errors.New("invalid value for required argument 'SchemaDefinition'")
	}
	var resource Schema
	err := ctx.RegisterResource("aws-native:glue:Schema", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSchema gets an existing Schema resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSchema(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SchemaState, opts ...pulumi.ResourceOption) (*Schema, error) {
	var resource Schema
	err := ctx.ReadResource("aws-native:glue:Schema", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Schema resources.
type schemaState struct {
}

type SchemaState struct {
}

func (SchemaState) ElementType() reflect.Type {
	return reflect.TypeOf((*schemaState)(nil)).Elem()
}

type schemaArgs struct {
	CheckpointVersion *SchemaVersionType `pulumi:"checkpointVersion"`
	// Compatibility setting for the schema.
	Compatibility SchemaCompatibility `pulumi:"compatibility"`
	// Data format name to use for the schema. Accepted values: 'AVRO', 'JSON'
	DataFormat SchemaDataFormat `pulumi:"dataFormat"`
	// A description of the schema. If description is not provided, there will not be any default value for this.
	Description *string `pulumi:"description"`
	// Name of the schema.
	Name     string          `pulumi:"name"`
	Registry *SchemaRegistry `pulumi:"registry"`
	// Definition for the initial schema version in plain-text.
	SchemaDefinition string `pulumi:"schemaDefinition"`
	// List of tags to tag the schema
	Tags []SchemaTag `pulumi:"tags"`
}

// The set of arguments for constructing a Schema resource.
type SchemaArgs struct {
	CheckpointVersion SchemaVersionTypePtrInput
	// Compatibility setting for the schema.
	Compatibility SchemaCompatibilityInput
	// Data format name to use for the schema. Accepted values: 'AVRO', 'JSON'
	DataFormat SchemaDataFormatInput
	// A description of the schema. If description is not provided, there will not be any default value for this.
	Description pulumi.StringPtrInput
	// Name of the schema.
	Name     pulumi.StringInput
	Registry SchemaRegistryPtrInput
	// Definition for the initial schema version in plain-text.
	SchemaDefinition pulumi.StringInput
	// List of tags to tag the schema
	Tags SchemaTagArrayInput
}

func (SchemaArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*schemaArgs)(nil)).Elem()
}

type SchemaInput interface {
	pulumi.Input

	ToSchemaOutput() SchemaOutput
	ToSchemaOutputWithContext(ctx context.Context) SchemaOutput
}

func (*Schema) ElementType() reflect.Type {
	return reflect.TypeOf((*Schema)(nil))
}

func (i *Schema) ToSchemaOutput() SchemaOutput {
	return i.ToSchemaOutputWithContext(context.Background())
}

func (i *Schema) ToSchemaOutputWithContext(ctx context.Context) SchemaOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SchemaOutput)
}

type SchemaOutput struct{ *pulumi.OutputState }

func (SchemaOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Schema)(nil))
}

func (o SchemaOutput) ToSchemaOutput() SchemaOutput {
	return o
}

func (o SchemaOutput) ToSchemaOutputWithContext(ctx context.Context) SchemaOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(SchemaOutput{})
}
