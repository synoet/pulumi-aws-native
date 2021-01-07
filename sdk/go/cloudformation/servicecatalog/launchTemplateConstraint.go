// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package servicecatalog

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html
type LaunchTemplateConstraint struct {
	pulumi.CustomResourceState

	// The attributes associated with the resource
	Attributes LaunchTemplateConstraintAttributesOutput `pulumi:"attributes"`
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrOutput `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata pulumi.AnyOutput `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties LaunchTemplateConstraintPropertiesOutput `pulumi:"properties"`
}

// NewLaunchTemplateConstraint registers a new resource with the given unique name, arguments, and options.
func NewLaunchTemplateConstraint(ctx *pulumi.Context,
	name string, args *LaunchTemplateConstraintArgs, opts ...pulumi.ResourceOption) (*LaunchTemplateConstraint, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Properties == nil {
		return nil, errors.New("invalid value for required argument 'Properties'")
	}
	var resource LaunchTemplateConstraint
	err := ctx.RegisterResource("cloudformation:ServiceCatalog:LaunchTemplateConstraint", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetLaunchTemplateConstraint gets an existing LaunchTemplateConstraint resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetLaunchTemplateConstraint(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *LaunchTemplateConstraintState, opts ...pulumi.ResourceOption) (*LaunchTemplateConstraint, error) {
	var resource LaunchTemplateConstraint
	err := ctx.ReadResource("cloudformation:ServiceCatalog:LaunchTemplateConstraint", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering LaunchTemplateConstraint resources.
type launchTemplateConstraintState struct {
	// The attributes associated with the resource
	Attributes *LaunchTemplateConstraintAttributes `pulumi:"attributes"`
	// An explicit logical ID for the resource
	LogicalId *string `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata interface{} `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties *LaunchTemplateConstraintProperties `pulumi:"properties"`
}

type LaunchTemplateConstraintState struct {
	// The attributes associated with the resource
	Attributes LaunchTemplateConstraintAttributesPtrInput
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrInput
	// Arbitrary structured data associated with the resource
	Metadata pulumi.Input
	// The input properties associated with the resource
	Properties LaunchTemplateConstraintPropertiesPtrInput
}

func (LaunchTemplateConstraintState) ElementType() reflect.Type {
	return reflect.TypeOf((*launchTemplateConstraintState)(nil)).Elem()
}

type launchTemplateConstraintArgs struct {
	// With the deletionPolicy attribute you can preserve or (in some cases) backup a resource when its stack is deleted. You can specify a deletionPolicy attribute for each resource that you want to control. If a resource has no deletionPolicy attribute, AWS CloudFormation deletes the resource by default.
	DeletionPolicy *string `pulumi:"deletionPolicy"`
	// An explicit logical ID for the resource
	LogicalId *string `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata interface{} `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties LaunchTemplateConstraintProperties `pulumi:"properties"`
	// Use the updateReplacePolicy attribute to retain or (in some cases) backup the existing physical instance of a resource when it is replaced during a stack update operation.
	UpdateReplacePolicy *string `pulumi:"updateReplacePolicy"`
}

// The set of arguments for constructing a LaunchTemplateConstraint resource.
type LaunchTemplateConstraintArgs struct {
	// With the deletionPolicy attribute you can preserve or (in some cases) backup a resource when its stack is deleted. You can specify a deletionPolicy attribute for each resource that you want to control. If a resource has no deletionPolicy attribute, AWS CloudFormation deletes the resource by default.
	DeletionPolicy pulumi.StringPtrInput
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrInput
	// Arbitrary structured data associated with the resource
	Metadata pulumi.Input
	// The input properties associated with the resource
	Properties LaunchTemplateConstraintPropertiesInput
	// Use the updateReplacePolicy attribute to retain or (in some cases) backup the existing physical instance of a resource when it is replaced during a stack update operation.
	UpdateReplacePolicy pulumi.StringPtrInput
}

func (LaunchTemplateConstraintArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*launchTemplateConstraintArgs)(nil)).Elem()
}

type LaunchTemplateConstraintInput interface {
	pulumi.Input

	ToLaunchTemplateConstraintOutput() LaunchTemplateConstraintOutput
	ToLaunchTemplateConstraintOutputWithContext(ctx context.Context) LaunchTemplateConstraintOutput
}

func (*LaunchTemplateConstraint) ElementType() reflect.Type {
	return reflect.TypeOf((*LaunchTemplateConstraint)(nil))
}

func (i *LaunchTemplateConstraint) ToLaunchTemplateConstraintOutput() LaunchTemplateConstraintOutput {
	return i.ToLaunchTemplateConstraintOutputWithContext(context.Background())
}

func (i *LaunchTemplateConstraint) ToLaunchTemplateConstraintOutputWithContext(ctx context.Context) LaunchTemplateConstraintOutput {
	return pulumi.ToOutputWithContext(ctx, i).(LaunchTemplateConstraintOutput)
}

type LaunchTemplateConstraintOutput struct {
	*pulumi.OutputState
}

func (LaunchTemplateConstraintOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LaunchTemplateConstraint)(nil))
}

func (o LaunchTemplateConstraintOutput) ToLaunchTemplateConstraintOutput() LaunchTemplateConstraintOutput {
	return o
}

func (o LaunchTemplateConstraintOutput) ToLaunchTemplateConstraintOutputWithContext(ctx context.Context) LaunchTemplateConstraintOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(LaunchTemplateConstraintOutput{})
}