// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package greengrass

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinition.html
type ConnectorDefinition struct {
	pulumi.CustomResourceState

	// The attributes associated with the resource
	Attributes ConnectorDefinitionAttributesOutput `pulumi:"attributes"`
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrOutput `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata pulumi.AnyOutput `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties ConnectorDefinitionPropertiesOutput `pulumi:"properties"`
}

// NewConnectorDefinition registers a new resource with the given unique name, arguments, and options.
func NewConnectorDefinition(ctx *pulumi.Context,
	name string, args *ConnectorDefinitionArgs, opts ...pulumi.ResourceOption) (*ConnectorDefinition, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Properties == nil {
		return nil, errors.New("invalid value for required argument 'Properties'")
	}
	var resource ConnectorDefinition
	err := ctx.RegisterResource("cloudformation:Greengrass:ConnectorDefinition", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetConnectorDefinition gets an existing ConnectorDefinition resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetConnectorDefinition(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ConnectorDefinitionState, opts ...pulumi.ResourceOption) (*ConnectorDefinition, error) {
	var resource ConnectorDefinition
	err := ctx.ReadResource("cloudformation:Greengrass:ConnectorDefinition", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ConnectorDefinition resources.
type connectorDefinitionState struct {
	// The attributes associated with the resource
	Attributes *ConnectorDefinitionAttributes `pulumi:"attributes"`
	// An explicit logical ID for the resource
	LogicalId *string `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata interface{} `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties *ConnectorDefinitionProperties `pulumi:"properties"`
}

type ConnectorDefinitionState struct {
	// The attributes associated with the resource
	Attributes ConnectorDefinitionAttributesPtrInput
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrInput
	// Arbitrary structured data associated with the resource
	Metadata pulumi.Input
	// The input properties associated with the resource
	Properties ConnectorDefinitionPropertiesPtrInput
}

func (ConnectorDefinitionState) ElementType() reflect.Type {
	return reflect.TypeOf((*connectorDefinitionState)(nil)).Elem()
}

type connectorDefinitionArgs struct {
	// With the deletionPolicy attribute you can preserve or (in some cases) backup a resource when its stack is deleted. You can specify a deletionPolicy attribute for each resource that you want to control. If a resource has no deletionPolicy attribute, AWS CloudFormation deletes the resource by default.
	DeletionPolicy *string `pulumi:"deletionPolicy"`
	// An explicit logical ID for the resource
	LogicalId *string `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata interface{} `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties ConnectorDefinitionProperties `pulumi:"properties"`
	// Use the updateReplacePolicy attribute to retain or (in some cases) backup the existing physical instance of a resource when it is replaced during a stack update operation.
	UpdateReplacePolicy *string `pulumi:"updateReplacePolicy"`
}

// The set of arguments for constructing a ConnectorDefinition resource.
type ConnectorDefinitionArgs struct {
	// With the deletionPolicy attribute you can preserve or (in some cases) backup a resource when its stack is deleted. You can specify a deletionPolicy attribute for each resource that you want to control. If a resource has no deletionPolicy attribute, AWS CloudFormation deletes the resource by default.
	DeletionPolicy pulumi.StringPtrInput
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrInput
	// Arbitrary structured data associated with the resource
	Metadata pulumi.Input
	// The input properties associated with the resource
	Properties ConnectorDefinitionPropertiesInput
	// Use the updateReplacePolicy attribute to retain or (in some cases) backup the existing physical instance of a resource when it is replaced during a stack update operation.
	UpdateReplacePolicy pulumi.StringPtrInput
}

func (ConnectorDefinitionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*connectorDefinitionArgs)(nil)).Elem()
}

type ConnectorDefinitionInput interface {
	pulumi.Input

	ToConnectorDefinitionOutput() ConnectorDefinitionOutput
	ToConnectorDefinitionOutputWithContext(ctx context.Context) ConnectorDefinitionOutput
}

func (*ConnectorDefinition) ElementType() reflect.Type {
	return reflect.TypeOf((*ConnectorDefinition)(nil))
}

func (i *ConnectorDefinition) ToConnectorDefinitionOutput() ConnectorDefinitionOutput {
	return i.ToConnectorDefinitionOutputWithContext(context.Background())
}

func (i *ConnectorDefinition) ToConnectorDefinitionOutputWithContext(ctx context.Context) ConnectorDefinitionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConnectorDefinitionOutput)
}

type ConnectorDefinitionOutput struct {
	*pulumi.OutputState
}

func (ConnectorDefinitionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ConnectorDefinition)(nil))
}

func (o ConnectorDefinitionOutput) ToConnectorDefinitionOutput() ConnectorDefinitionOutput {
	return o
}

func (o ConnectorDefinitionOutput) ToConnectorDefinitionOutputWithContext(ctx context.Context) ConnectorDefinitionOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(ConnectorDefinitionOutput{})
}