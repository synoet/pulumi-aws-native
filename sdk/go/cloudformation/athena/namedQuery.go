// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package athena

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html
type NamedQuery struct {
	pulumi.CustomResourceState

	// The attributes associated with the resource
	Attributes NamedQueryAttributesOutput `pulumi:"attributes"`
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrOutput `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata pulumi.AnyOutput `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties NamedQueryPropertiesOutput `pulumi:"properties"`
}

// NewNamedQuery registers a new resource with the given unique name, arguments, and options.
func NewNamedQuery(ctx *pulumi.Context,
	name string, args *NamedQueryArgs, opts ...pulumi.ResourceOption) (*NamedQuery, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Properties == nil {
		return nil, errors.New("invalid value for required argument 'Properties'")
	}
	var resource NamedQuery
	err := ctx.RegisterResource("cloudformation:Athena:NamedQuery", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetNamedQuery gets an existing NamedQuery resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetNamedQuery(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *NamedQueryState, opts ...pulumi.ResourceOption) (*NamedQuery, error) {
	var resource NamedQuery
	err := ctx.ReadResource("cloudformation:Athena:NamedQuery", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering NamedQuery resources.
type namedQueryState struct {
	// The attributes associated with the resource
	Attributes *NamedQueryAttributes `pulumi:"attributes"`
	// An explicit logical ID for the resource
	LogicalId *string `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata interface{} `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties *NamedQueryProperties `pulumi:"properties"`
}

type NamedQueryState struct {
	// The attributes associated with the resource
	Attributes NamedQueryAttributesPtrInput
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrInput
	// Arbitrary structured data associated with the resource
	Metadata pulumi.Input
	// The input properties associated with the resource
	Properties NamedQueryPropertiesPtrInput
}

func (NamedQueryState) ElementType() reflect.Type {
	return reflect.TypeOf((*namedQueryState)(nil)).Elem()
}

type namedQueryArgs struct {
	// With the deletionPolicy attribute you can preserve or (in some cases) backup a resource when its stack is deleted. You can specify a deletionPolicy attribute for each resource that you want to control. If a resource has no deletionPolicy attribute, AWS CloudFormation deletes the resource by default.
	DeletionPolicy *string `pulumi:"deletionPolicy"`
	// An explicit logical ID for the resource
	LogicalId *string `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata interface{} `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties NamedQueryProperties `pulumi:"properties"`
	// Use the updateReplacePolicy attribute to retain or (in some cases) backup the existing physical instance of a resource when it is replaced during a stack update operation.
	UpdateReplacePolicy *string `pulumi:"updateReplacePolicy"`
}

// The set of arguments for constructing a NamedQuery resource.
type NamedQueryArgs struct {
	// With the deletionPolicy attribute you can preserve or (in some cases) backup a resource when its stack is deleted. You can specify a deletionPolicy attribute for each resource that you want to control. If a resource has no deletionPolicy attribute, AWS CloudFormation deletes the resource by default.
	DeletionPolicy pulumi.StringPtrInput
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrInput
	// Arbitrary structured data associated with the resource
	Metadata pulumi.Input
	// The input properties associated with the resource
	Properties NamedQueryPropertiesInput
	// Use the updateReplacePolicy attribute to retain or (in some cases) backup the existing physical instance of a resource when it is replaced during a stack update operation.
	UpdateReplacePolicy pulumi.StringPtrInput
}

func (NamedQueryArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*namedQueryArgs)(nil)).Elem()
}

type NamedQueryInput interface {
	pulumi.Input

	ToNamedQueryOutput() NamedQueryOutput
	ToNamedQueryOutputWithContext(ctx context.Context) NamedQueryOutput
}

func (*NamedQuery) ElementType() reflect.Type {
	return reflect.TypeOf((*NamedQuery)(nil))
}

func (i *NamedQuery) ToNamedQueryOutput() NamedQueryOutput {
	return i.ToNamedQueryOutputWithContext(context.Background())
}

func (i *NamedQuery) ToNamedQueryOutputWithContext(ctx context.Context) NamedQueryOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NamedQueryOutput)
}

type NamedQueryOutput struct {
	*pulumi.OutputState
}

func (NamedQueryOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*NamedQuery)(nil))
}

func (o NamedQueryOutput) ToNamedQueryOutput() NamedQueryOutput {
	return o
}

func (o NamedQueryOutput) ToNamedQueryOutputWithContext(ctx context.Context) NamedQueryOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(NamedQueryOutput{})
}