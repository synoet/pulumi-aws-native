// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnendpoint.html
type ClientVpnEndpoint struct {
	pulumi.CustomResourceState

	// The attributes associated with the resource
	Attributes ClientVpnEndpointAttributesOutput `pulumi:"attributes"`
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrOutput `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata pulumi.AnyOutput `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties ClientVpnEndpointPropertiesOutput `pulumi:"properties"`
}

// NewClientVpnEndpoint registers a new resource with the given unique name, arguments, and options.
func NewClientVpnEndpoint(ctx *pulumi.Context,
	name string, args *ClientVpnEndpointArgs, opts ...pulumi.ResourceOption) (*ClientVpnEndpoint, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Properties == nil {
		return nil, errors.New("invalid value for required argument 'Properties'")
	}
	var resource ClientVpnEndpoint
	err := ctx.RegisterResource("cloudformation:EC2:ClientVpnEndpoint", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetClientVpnEndpoint gets an existing ClientVpnEndpoint resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetClientVpnEndpoint(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ClientVpnEndpointState, opts ...pulumi.ResourceOption) (*ClientVpnEndpoint, error) {
	var resource ClientVpnEndpoint
	err := ctx.ReadResource("cloudformation:EC2:ClientVpnEndpoint", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ClientVpnEndpoint resources.
type clientVpnEndpointState struct {
	// The attributes associated with the resource
	Attributes *ClientVpnEndpointAttributes `pulumi:"attributes"`
	// An explicit logical ID for the resource
	LogicalId *string `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata interface{} `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties *ClientVpnEndpointProperties `pulumi:"properties"`
}

type ClientVpnEndpointState struct {
	// The attributes associated with the resource
	Attributes ClientVpnEndpointAttributesPtrInput
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrInput
	// Arbitrary structured data associated with the resource
	Metadata pulumi.Input
	// The input properties associated with the resource
	Properties ClientVpnEndpointPropertiesPtrInput
}

func (ClientVpnEndpointState) ElementType() reflect.Type {
	return reflect.TypeOf((*clientVpnEndpointState)(nil)).Elem()
}

type clientVpnEndpointArgs struct {
	// With the deletionPolicy attribute you can preserve or (in some cases) backup a resource when its stack is deleted. You can specify a deletionPolicy attribute for each resource that you want to control. If a resource has no deletionPolicy attribute, AWS CloudFormation deletes the resource by default.
	DeletionPolicy *string `pulumi:"deletionPolicy"`
	// An explicit logical ID for the resource
	LogicalId *string `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata interface{} `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties ClientVpnEndpointProperties `pulumi:"properties"`
	// Use the updateReplacePolicy attribute to retain or (in some cases) backup the existing physical instance of a resource when it is replaced during a stack update operation.
	UpdateReplacePolicy *string `pulumi:"updateReplacePolicy"`
}

// The set of arguments for constructing a ClientVpnEndpoint resource.
type ClientVpnEndpointArgs struct {
	// With the deletionPolicy attribute you can preserve or (in some cases) backup a resource when its stack is deleted. You can specify a deletionPolicy attribute for each resource that you want to control. If a resource has no deletionPolicy attribute, AWS CloudFormation deletes the resource by default.
	DeletionPolicy pulumi.StringPtrInput
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrInput
	// Arbitrary structured data associated with the resource
	Metadata pulumi.Input
	// The input properties associated with the resource
	Properties ClientVpnEndpointPropertiesInput
	// Use the updateReplacePolicy attribute to retain or (in some cases) backup the existing physical instance of a resource when it is replaced during a stack update operation.
	UpdateReplacePolicy pulumi.StringPtrInput
}

func (ClientVpnEndpointArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*clientVpnEndpointArgs)(nil)).Elem()
}

type ClientVpnEndpointInput interface {
	pulumi.Input

	ToClientVpnEndpointOutput() ClientVpnEndpointOutput
	ToClientVpnEndpointOutputWithContext(ctx context.Context) ClientVpnEndpointOutput
}

func (*ClientVpnEndpoint) ElementType() reflect.Type {
	return reflect.TypeOf((*ClientVpnEndpoint)(nil))
}

func (i *ClientVpnEndpoint) ToClientVpnEndpointOutput() ClientVpnEndpointOutput {
	return i.ToClientVpnEndpointOutputWithContext(context.Background())
}

func (i *ClientVpnEndpoint) ToClientVpnEndpointOutputWithContext(ctx context.Context) ClientVpnEndpointOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ClientVpnEndpointOutput)
}

type ClientVpnEndpointOutput struct {
	*pulumi.OutputState
}

func (ClientVpnEndpointOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ClientVpnEndpoint)(nil))
}

func (o ClientVpnEndpointOutput) ToClientVpnEndpointOutput() ClientVpnEndpointOutput {
	return o
}

func (o ClientVpnEndpointOutput) ToClientVpnEndpointOutputWithContext(ctx context.Context) ClientVpnEndpointOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(ClientVpnEndpointOutput{})
}