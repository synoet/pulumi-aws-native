// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package medialive

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-inputsecuritygroup.html
type InputSecurityGroup struct {
	pulumi.CustomResourceState

	// The attributes associated with the resource
	Attributes InputSecurityGroupAttributesOutput `pulumi:"attributes"`
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrOutput `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata pulumi.AnyOutput `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties InputSecurityGroupPropertiesOutput `pulumi:"properties"`
}

// NewInputSecurityGroup registers a new resource with the given unique name, arguments, and options.
func NewInputSecurityGroup(ctx *pulumi.Context,
	name string, args *InputSecurityGroupArgs, opts ...pulumi.ResourceOption) (*InputSecurityGroup, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Properties == nil {
		return nil, errors.New("invalid value for required argument 'Properties'")
	}
	var resource InputSecurityGroup
	err := ctx.RegisterResource("cloudformation:MediaLive:InputSecurityGroup", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetInputSecurityGroup gets an existing InputSecurityGroup resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetInputSecurityGroup(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *InputSecurityGroupState, opts ...pulumi.ResourceOption) (*InputSecurityGroup, error) {
	var resource InputSecurityGroup
	err := ctx.ReadResource("cloudformation:MediaLive:InputSecurityGroup", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering InputSecurityGroup resources.
type inputSecurityGroupState struct {
	// The attributes associated with the resource
	Attributes *InputSecurityGroupAttributes `pulumi:"attributes"`
	// An explicit logical ID for the resource
	LogicalId *string `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata interface{} `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties *InputSecurityGroupProperties `pulumi:"properties"`
}

type InputSecurityGroupState struct {
	// The attributes associated with the resource
	Attributes InputSecurityGroupAttributesPtrInput
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrInput
	// Arbitrary structured data associated with the resource
	Metadata pulumi.Input
	// The input properties associated with the resource
	Properties InputSecurityGroupPropertiesPtrInput
}

func (InputSecurityGroupState) ElementType() reflect.Type {
	return reflect.TypeOf((*inputSecurityGroupState)(nil)).Elem()
}

type inputSecurityGroupArgs struct {
	// With the deletionPolicy attribute you can preserve or (in some cases) backup a resource when its stack is deleted. You can specify a deletionPolicy attribute for each resource that you want to control. If a resource has no deletionPolicy attribute, AWS CloudFormation deletes the resource by default.
	DeletionPolicy *string `pulumi:"deletionPolicy"`
	// An explicit logical ID for the resource
	LogicalId *string `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata interface{} `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties InputSecurityGroupProperties `pulumi:"properties"`
	// Use the updateReplacePolicy attribute to retain or (in some cases) backup the existing physical instance of a resource when it is replaced during a stack update operation.
	UpdateReplacePolicy *string `pulumi:"updateReplacePolicy"`
}

// The set of arguments for constructing a InputSecurityGroup resource.
type InputSecurityGroupArgs struct {
	// With the deletionPolicy attribute you can preserve or (in some cases) backup a resource when its stack is deleted. You can specify a deletionPolicy attribute for each resource that you want to control. If a resource has no deletionPolicy attribute, AWS CloudFormation deletes the resource by default.
	DeletionPolicy pulumi.StringPtrInput
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrInput
	// Arbitrary structured data associated with the resource
	Metadata pulumi.Input
	// The input properties associated with the resource
	Properties InputSecurityGroupPropertiesInput
	// Use the updateReplacePolicy attribute to retain or (in some cases) backup the existing physical instance of a resource when it is replaced during a stack update operation.
	UpdateReplacePolicy pulumi.StringPtrInput
}

func (InputSecurityGroupArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*inputSecurityGroupArgs)(nil)).Elem()
}

type InputSecurityGroupInput interface {
	pulumi.Input

	ToInputSecurityGroupOutput() InputSecurityGroupOutput
	ToInputSecurityGroupOutputWithContext(ctx context.Context) InputSecurityGroupOutput
}

func (*InputSecurityGroup) ElementType() reflect.Type {
	return reflect.TypeOf((*InputSecurityGroup)(nil))
}

func (i *InputSecurityGroup) ToInputSecurityGroupOutput() InputSecurityGroupOutput {
	return i.ToInputSecurityGroupOutputWithContext(context.Background())
}

func (i *InputSecurityGroup) ToInputSecurityGroupOutputWithContext(ctx context.Context) InputSecurityGroupOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InputSecurityGroupOutput)
}

type InputSecurityGroupOutput struct {
	*pulumi.OutputState
}

func (InputSecurityGroupOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*InputSecurityGroup)(nil))
}

func (o InputSecurityGroupOutput) ToInputSecurityGroupOutput() InputSecurityGroupOutput {
	return o
}

func (o InputSecurityGroupOutput) ToInputSecurityGroupOutputWithContext(ctx context.Context) InputSecurityGroupOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(InputSecurityGroupOutput{})
}