// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointservicepermissions.html
type VPCEndpointServicePermissions struct {
	pulumi.CustomResourceState

	// The attributes associated with the resource
	Attributes VPCEndpointServicePermissionsAttributesOutput `pulumi:"attributes"`
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrOutput `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata pulumi.AnyOutput `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties VPCEndpointServicePermissionsPropertiesOutput `pulumi:"properties"`
}

// NewVPCEndpointServicePermissions registers a new resource with the given unique name, arguments, and options.
func NewVPCEndpointServicePermissions(ctx *pulumi.Context,
	name string, args *VPCEndpointServicePermissionsArgs, opts ...pulumi.ResourceOption) (*VPCEndpointServicePermissions, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Properties == nil {
		return nil, errors.New("invalid value for required argument 'Properties'")
	}
	var resource VPCEndpointServicePermissions
	err := ctx.RegisterResource("cloudformation:EC2:VPCEndpointServicePermissions", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetVPCEndpointServicePermissions gets an existing VPCEndpointServicePermissions resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetVPCEndpointServicePermissions(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *VPCEndpointServicePermissionsState, opts ...pulumi.ResourceOption) (*VPCEndpointServicePermissions, error) {
	var resource VPCEndpointServicePermissions
	err := ctx.ReadResource("cloudformation:EC2:VPCEndpointServicePermissions", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering VPCEndpointServicePermissions resources.
type vpcendpointServicePermissionsState struct {
	// The attributes associated with the resource
	Attributes *VPCEndpointServicePermissionsAttributes `pulumi:"attributes"`
	// An explicit logical ID for the resource
	LogicalId *string `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata interface{} `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties *VPCEndpointServicePermissionsProperties `pulumi:"properties"`
}

type VPCEndpointServicePermissionsState struct {
	// The attributes associated with the resource
	Attributes VPCEndpointServicePermissionsAttributesPtrInput
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrInput
	// Arbitrary structured data associated with the resource
	Metadata pulumi.Input
	// The input properties associated with the resource
	Properties VPCEndpointServicePermissionsPropertiesPtrInput
}

func (VPCEndpointServicePermissionsState) ElementType() reflect.Type {
	return reflect.TypeOf((*vpcendpointServicePermissionsState)(nil)).Elem()
}

type vpcendpointServicePermissionsArgs struct {
	// With the deletionPolicy attribute you can preserve or (in some cases) backup a resource when its stack is deleted. You can specify a deletionPolicy attribute for each resource that you want to control. If a resource has no deletionPolicy attribute, AWS CloudFormation deletes the resource by default.
	DeletionPolicy *string `pulumi:"deletionPolicy"`
	// An explicit logical ID for the resource
	LogicalId *string `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata interface{} `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties VPCEndpointServicePermissionsProperties `pulumi:"properties"`
	// Use the updateReplacePolicy attribute to retain or (in some cases) backup the existing physical instance of a resource when it is replaced during a stack update operation.
	UpdateReplacePolicy *string `pulumi:"updateReplacePolicy"`
}

// The set of arguments for constructing a VPCEndpointServicePermissions resource.
type VPCEndpointServicePermissionsArgs struct {
	// With the deletionPolicy attribute you can preserve or (in some cases) backup a resource when its stack is deleted. You can specify a deletionPolicy attribute for each resource that you want to control. If a resource has no deletionPolicy attribute, AWS CloudFormation deletes the resource by default.
	DeletionPolicy pulumi.StringPtrInput
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrInput
	// Arbitrary structured data associated with the resource
	Metadata pulumi.Input
	// The input properties associated with the resource
	Properties VPCEndpointServicePermissionsPropertiesInput
	// Use the updateReplacePolicy attribute to retain or (in some cases) backup the existing physical instance of a resource when it is replaced during a stack update operation.
	UpdateReplacePolicy pulumi.StringPtrInput
}

func (VPCEndpointServicePermissionsArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*vpcendpointServicePermissionsArgs)(nil)).Elem()
}

type VPCEndpointServicePermissionsInput interface {
	pulumi.Input

	ToVPCEndpointServicePermissionsOutput() VPCEndpointServicePermissionsOutput
	ToVPCEndpointServicePermissionsOutputWithContext(ctx context.Context) VPCEndpointServicePermissionsOutput
}

func (*VPCEndpointServicePermissions) ElementType() reflect.Type {
	return reflect.TypeOf((*VPCEndpointServicePermissions)(nil))
}

func (i *VPCEndpointServicePermissions) ToVPCEndpointServicePermissionsOutput() VPCEndpointServicePermissionsOutput {
	return i.ToVPCEndpointServicePermissionsOutputWithContext(context.Background())
}

func (i *VPCEndpointServicePermissions) ToVPCEndpointServicePermissionsOutputWithContext(ctx context.Context) VPCEndpointServicePermissionsOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VPCEndpointServicePermissionsOutput)
}

type VPCEndpointServicePermissionsOutput struct {
	*pulumi.OutputState
}

func (VPCEndpointServicePermissionsOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*VPCEndpointServicePermissions)(nil))
}

func (o VPCEndpointServicePermissionsOutput) ToVPCEndpointServicePermissionsOutput() VPCEndpointServicePermissionsOutput {
	return o
}

func (o VPCEndpointServicePermissionsOutput) ToVPCEndpointServicePermissionsOutputWithContext(ctx context.Context) VPCEndpointServicePermissionsOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(VPCEndpointServicePermissionsOutput{})
}