// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package iotsitewise

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html
type Portal struct {
	pulumi.CustomResourceState

	// The attributes associated with the resource
	Attributes PortalAttributesOutput `pulumi:"attributes"`
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrOutput `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata pulumi.AnyOutput `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties PortalPropertiesOutput `pulumi:"properties"`
}

// NewPortal registers a new resource with the given unique name, arguments, and options.
func NewPortal(ctx *pulumi.Context,
	name string, args *PortalArgs, opts ...pulumi.ResourceOption) (*Portal, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Properties == nil {
		return nil, errors.New("invalid value for required argument 'Properties'")
	}
	var resource Portal
	err := ctx.RegisterResource("cloudformation:IoTSiteWise:Portal", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetPortal gets an existing Portal resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetPortal(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *PortalState, opts ...pulumi.ResourceOption) (*Portal, error) {
	var resource Portal
	err := ctx.ReadResource("cloudformation:IoTSiteWise:Portal", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Portal resources.
type portalState struct {
	// The attributes associated with the resource
	Attributes *PortalAttributes `pulumi:"attributes"`
	// An explicit logical ID for the resource
	LogicalId *string `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata interface{} `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties *PortalProperties `pulumi:"properties"`
}

type PortalState struct {
	// The attributes associated with the resource
	Attributes PortalAttributesPtrInput
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrInput
	// Arbitrary structured data associated with the resource
	Metadata pulumi.Input
	// The input properties associated with the resource
	Properties PortalPropertiesPtrInput
}

func (PortalState) ElementType() reflect.Type {
	return reflect.TypeOf((*portalState)(nil)).Elem()
}

type portalArgs struct {
	// With the deletionPolicy attribute you can preserve or (in some cases) backup a resource when its stack is deleted. You can specify a deletionPolicy attribute for each resource that you want to control. If a resource has no deletionPolicy attribute, AWS CloudFormation deletes the resource by default.
	DeletionPolicy *string `pulumi:"deletionPolicy"`
	// An explicit logical ID for the resource
	LogicalId *string `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata interface{} `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties PortalProperties `pulumi:"properties"`
	// Use the updateReplacePolicy attribute to retain or (in some cases) backup the existing physical instance of a resource when it is replaced during a stack update operation.
	UpdateReplacePolicy *string `pulumi:"updateReplacePolicy"`
}

// The set of arguments for constructing a Portal resource.
type PortalArgs struct {
	// With the deletionPolicy attribute you can preserve or (in some cases) backup a resource when its stack is deleted. You can specify a deletionPolicy attribute for each resource that you want to control. If a resource has no deletionPolicy attribute, AWS CloudFormation deletes the resource by default.
	DeletionPolicy pulumi.StringPtrInput
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrInput
	// Arbitrary structured data associated with the resource
	Metadata pulumi.Input
	// The input properties associated with the resource
	Properties PortalPropertiesInput
	// Use the updateReplacePolicy attribute to retain or (in some cases) backup the existing physical instance of a resource when it is replaced during a stack update operation.
	UpdateReplacePolicy pulumi.StringPtrInput
}

func (PortalArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*portalArgs)(nil)).Elem()
}

type PortalInput interface {
	pulumi.Input

	ToPortalOutput() PortalOutput
	ToPortalOutputWithContext(ctx context.Context) PortalOutput
}

func (*Portal) ElementType() reflect.Type {
	return reflect.TypeOf((*Portal)(nil))
}

func (i *Portal) ToPortalOutput() PortalOutput {
	return i.ToPortalOutputWithContext(context.Background())
}

func (i *Portal) ToPortalOutputWithContext(ctx context.Context) PortalOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PortalOutput)
}

type PortalOutput struct {
	*pulumi.OutputState
}

func (PortalOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Portal)(nil))
}

func (o PortalOutput) ToPortalOutput() PortalOutput {
	return o
}

func (o PortalOutput) ToPortalOutputWithContext(ctx context.Context) PortalOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(PortalOutput{})
}