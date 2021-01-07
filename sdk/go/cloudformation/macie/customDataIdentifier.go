// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package macie

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html
type CustomDataIdentifier struct {
	pulumi.CustomResourceState

	// The attributes associated with the resource
	Attributes CustomDataIdentifierAttributesOutput `pulumi:"attributes"`
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrOutput `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata pulumi.AnyOutput `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties CustomDataIdentifierPropertiesOutput `pulumi:"properties"`
}

// NewCustomDataIdentifier registers a new resource with the given unique name, arguments, and options.
func NewCustomDataIdentifier(ctx *pulumi.Context,
	name string, args *CustomDataIdentifierArgs, opts ...pulumi.ResourceOption) (*CustomDataIdentifier, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Properties == nil {
		return nil, errors.New("invalid value for required argument 'Properties'")
	}
	var resource CustomDataIdentifier
	err := ctx.RegisterResource("cloudformation:Macie:CustomDataIdentifier", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCustomDataIdentifier gets an existing CustomDataIdentifier resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCustomDataIdentifier(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *CustomDataIdentifierState, opts ...pulumi.ResourceOption) (*CustomDataIdentifier, error) {
	var resource CustomDataIdentifier
	err := ctx.ReadResource("cloudformation:Macie:CustomDataIdentifier", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering CustomDataIdentifier resources.
type customDataIdentifierState struct {
	// The attributes associated with the resource
	Attributes *CustomDataIdentifierAttributes `pulumi:"attributes"`
	// An explicit logical ID for the resource
	LogicalId *string `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata interface{} `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties *CustomDataIdentifierProperties `pulumi:"properties"`
}

type CustomDataIdentifierState struct {
	// The attributes associated with the resource
	Attributes CustomDataIdentifierAttributesPtrInput
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrInput
	// Arbitrary structured data associated with the resource
	Metadata pulumi.Input
	// The input properties associated with the resource
	Properties CustomDataIdentifierPropertiesPtrInput
}

func (CustomDataIdentifierState) ElementType() reflect.Type {
	return reflect.TypeOf((*customDataIdentifierState)(nil)).Elem()
}

type customDataIdentifierArgs struct {
	// With the deletionPolicy attribute you can preserve or (in some cases) backup a resource when its stack is deleted. You can specify a deletionPolicy attribute for each resource that you want to control. If a resource has no deletionPolicy attribute, AWS CloudFormation deletes the resource by default.
	DeletionPolicy *string `pulumi:"deletionPolicy"`
	// An explicit logical ID for the resource
	LogicalId *string `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata interface{} `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties CustomDataIdentifierProperties `pulumi:"properties"`
	// Use the updateReplacePolicy attribute to retain or (in some cases) backup the existing physical instance of a resource when it is replaced during a stack update operation.
	UpdateReplacePolicy *string `pulumi:"updateReplacePolicy"`
}

// The set of arguments for constructing a CustomDataIdentifier resource.
type CustomDataIdentifierArgs struct {
	// With the deletionPolicy attribute you can preserve or (in some cases) backup a resource when its stack is deleted. You can specify a deletionPolicy attribute for each resource that you want to control. If a resource has no deletionPolicy attribute, AWS CloudFormation deletes the resource by default.
	DeletionPolicy pulumi.StringPtrInput
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrInput
	// Arbitrary structured data associated with the resource
	Metadata pulumi.Input
	// The input properties associated with the resource
	Properties CustomDataIdentifierPropertiesInput
	// Use the updateReplacePolicy attribute to retain or (in some cases) backup the existing physical instance of a resource when it is replaced during a stack update operation.
	UpdateReplacePolicy pulumi.StringPtrInput
}

func (CustomDataIdentifierArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*customDataIdentifierArgs)(nil)).Elem()
}

type CustomDataIdentifierInput interface {
	pulumi.Input

	ToCustomDataIdentifierOutput() CustomDataIdentifierOutput
	ToCustomDataIdentifierOutputWithContext(ctx context.Context) CustomDataIdentifierOutput
}

func (*CustomDataIdentifier) ElementType() reflect.Type {
	return reflect.TypeOf((*CustomDataIdentifier)(nil))
}

func (i *CustomDataIdentifier) ToCustomDataIdentifierOutput() CustomDataIdentifierOutput {
	return i.ToCustomDataIdentifierOutputWithContext(context.Background())
}

func (i *CustomDataIdentifier) ToCustomDataIdentifierOutputWithContext(ctx context.Context) CustomDataIdentifierOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CustomDataIdentifierOutput)
}

type CustomDataIdentifierOutput struct {
	*pulumi.OutputState
}

func (CustomDataIdentifierOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*CustomDataIdentifier)(nil))
}

func (o CustomDataIdentifierOutput) ToCustomDataIdentifierOutput() CustomDataIdentifierOutput {
	return o
}

func (o CustomDataIdentifierOutput) ToCustomDataIdentifierOutputWithContext(ctx context.Context) CustomDataIdentifierOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(CustomDataIdentifierOutput{})
}