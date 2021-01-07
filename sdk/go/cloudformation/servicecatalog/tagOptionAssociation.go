// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package servicecatalog

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoptionassociation.html
type TagOptionAssociation struct {
	pulumi.CustomResourceState

	// The attributes associated with the resource
	Attributes TagOptionAssociationAttributesOutput `pulumi:"attributes"`
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrOutput `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata pulumi.AnyOutput `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties TagOptionAssociationPropertiesOutput `pulumi:"properties"`
}

// NewTagOptionAssociation registers a new resource with the given unique name, arguments, and options.
func NewTagOptionAssociation(ctx *pulumi.Context,
	name string, args *TagOptionAssociationArgs, opts ...pulumi.ResourceOption) (*TagOptionAssociation, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Properties == nil {
		return nil, errors.New("invalid value for required argument 'Properties'")
	}
	var resource TagOptionAssociation
	err := ctx.RegisterResource("cloudformation:ServiceCatalog:TagOptionAssociation", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetTagOptionAssociation gets an existing TagOptionAssociation resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTagOptionAssociation(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *TagOptionAssociationState, opts ...pulumi.ResourceOption) (*TagOptionAssociation, error) {
	var resource TagOptionAssociation
	err := ctx.ReadResource("cloudformation:ServiceCatalog:TagOptionAssociation", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering TagOptionAssociation resources.
type tagOptionAssociationState struct {
	// The attributes associated with the resource
	Attributes *TagOptionAssociationAttributes `pulumi:"attributes"`
	// An explicit logical ID for the resource
	LogicalId *string `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata interface{} `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties *TagOptionAssociationProperties `pulumi:"properties"`
}

type TagOptionAssociationState struct {
	// The attributes associated with the resource
	Attributes TagOptionAssociationAttributesPtrInput
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrInput
	// Arbitrary structured data associated with the resource
	Metadata pulumi.Input
	// The input properties associated with the resource
	Properties TagOptionAssociationPropertiesPtrInput
}

func (TagOptionAssociationState) ElementType() reflect.Type {
	return reflect.TypeOf((*tagOptionAssociationState)(nil)).Elem()
}

type tagOptionAssociationArgs struct {
	// With the deletionPolicy attribute you can preserve or (in some cases) backup a resource when its stack is deleted. You can specify a deletionPolicy attribute for each resource that you want to control. If a resource has no deletionPolicy attribute, AWS CloudFormation deletes the resource by default.
	DeletionPolicy *string `pulumi:"deletionPolicy"`
	// An explicit logical ID for the resource
	LogicalId *string `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata interface{} `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties TagOptionAssociationProperties `pulumi:"properties"`
	// Use the updateReplacePolicy attribute to retain or (in some cases) backup the existing physical instance of a resource when it is replaced during a stack update operation.
	UpdateReplacePolicy *string `pulumi:"updateReplacePolicy"`
}

// The set of arguments for constructing a TagOptionAssociation resource.
type TagOptionAssociationArgs struct {
	// With the deletionPolicy attribute you can preserve or (in some cases) backup a resource when its stack is deleted. You can specify a deletionPolicy attribute for each resource that you want to control. If a resource has no deletionPolicy attribute, AWS CloudFormation deletes the resource by default.
	DeletionPolicy pulumi.StringPtrInput
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrInput
	// Arbitrary structured data associated with the resource
	Metadata pulumi.Input
	// The input properties associated with the resource
	Properties TagOptionAssociationPropertiesInput
	// Use the updateReplacePolicy attribute to retain or (in some cases) backup the existing physical instance of a resource when it is replaced during a stack update operation.
	UpdateReplacePolicy pulumi.StringPtrInput
}

func (TagOptionAssociationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*tagOptionAssociationArgs)(nil)).Elem()
}

type TagOptionAssociationInput interface {
	pulumi.Input

	ToTagOptionAssociationOutput() TagOptionAssociationOutput
	ToTagOptionAssociationOutputWithContext(ctx context.Context) TagOptionAssociationOutput
}

func (*TagOptionAssociation) ElementType() reflect.Type {
	return reflect.TypeOf((*TagOptionAssociation)(nil))
}

func (i *TagOptionAssociation) ToTagOptionAssociationOutput() TagOptionAssociationOutput {
	return i.ToTagOptionAssociationOutputWithContext(context.Background())
}

func (i *TagOptionAssociation) ToTagOptionAssociationOutputWithContext(ctx context.Context) TagOptionAssociationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TagOptionAssociationOutput)
}

type TagOptionAssociationOutput struct {
	*pulumi.OutputState
}

func (TagOptionAssociationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*TagOptionAssociation)(nil))
}

func (o TagOptionAssociationOutput) ToTagOptionAssociationOutput() TagOptionAssociationOutput {
	return o
}

func (o TagOptionAssociationOutput) ToTagOptionAssociationOutputWithContext(ctx context.Context) TagOptionAssociationOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(TagOptionAssociationOutput{})
}