// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package pinpointemail

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-dedicatedippool.html
type DedicatedIpPool struct {
	pulumi.CustomResourceState

	// The attributes associated with the resource
	Attributes DedicatedIpPoolAttributesOutput `pulumi:"attributes"`
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrOutput `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata pulumi.AnyOutput `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties DedicatedIpPoolPropertiesOutput `pulumi:"properties"`
}

// NewDedicatedIpPool registers a new resource with the given unique name, arguments, and options.
func NewDedicatedIpPool(ctx *pulumi.Context,
	name string, args *DedicatedIpPoolArgs, opts ...pulumi.ResourceOption) (*DedicatedIpPool, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Properties == nil {
		return nil, errors.New("invalid value for required argument 'Properties'")
	}
	var resource DedicatedIpPool
	err := ctx.RegisterResource("cloudformation:PinpointEmail:DedicatedIpPool", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDedicatedIpPool gets an existing DedicatedIpPool resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDedicatedIpPool(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DedicatedIpPoolState, opts ...pulumi.ResourceOption) (*DedicatedIpPool, error) {
	var resource DedicatedIpPool
	err := ctx.ReadResource("cloudformation:PinpointEmail:DedicatedIpPool", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DedicatedIpPool resources.
type dedicatedIpPoolState struct {
	// The attributes associated with the resource
	Attributes *DedicatedIpPoolAttributes `pulumi:"attributes"`
	// An explicit logical ID for the resource
	LogicalId *string `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata interface{} `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties *DedicatedIpPoolProperties `pulumi:"properties"`
}

type DedicatedIpPoolState struct {
	// The attributes associated with the resource
	Attributes DedicatedIpPoolAttributesPtrInput
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrInput
	// Arbitrary structured data associated with the resource
	Metadata pulumi.Input
	// The input properties associated with the resource
	Properties DedicatedIpPoolPropertiesPtrInput
}

func (DedicatedIpPoolState) ElementType() reflect.Type {
	return reflect.TypeOf((*dedicatedIpPoolState)(nil)).Elem()
}

type dedicatedIpPoolArgs struct {
	// With the deletionPolicy attribute you can preserve or (in some cases) backup a resource when its stack is deleted. You can specify a deletionPolicy attribute for each resource that you want to control. If a resource has no deletionPolicy attribute, AWS CloudFormation deletes the resource by default.
	DeletionPolicy *string `pulumi:"deletionPolicy"`
	// An explicit logical ID for the resource
	LogicalId *string `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata interface{} `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties DedicatedIpPoolProperties `pulumi:"properties"`
	// Use the updateReplacePolicy attribute to retain or (in some cases) backup the existing physical instance of a resource when it is replaced during a stack update operation.
	UpdateReplacePolicy *string `pulumi:"updateReplacePolicy"`
}

// The set of arguments for constructing a DedicatedIpPool resource.
type DedicatedIpPoolArgs struct {
	// With the deletionPolicy attribute you can preserve or (in some cases) backup a resource when its stack is deleted. You can specify a deletionPolicy attribute for each resource that you want to control. If a resource has no deletionPolicy attribute, AWS CloudFormation deletes the resource by default.
	DeletionPolicy pulumi.StringPtrInput
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrInput
	// Arbitrary structured data associated with the resource
	Metadata pulumi.Input
	// The input properties associated with the resource
	Properties DedicatedIpPoolPropertiesInput
	// Use the updateReplacePolicy attribute to retain or (in some cases) backup the existing physical instance of a resource when it is replaced during a stack update operation.
	UpdateReplacePolicy pulumi.StringPtrInput
}

func (DedicatedIpPoolArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*dedicatedIpPoolArgs)(nil)).Elem()
}

type DedicatedIpPoolInput interface {
	pulumi.Input

	ToDedicatedIpPoolOutput() DedicatedIpPoolOutput
	ToDedicatedIpPoolOutputWithContext(ctx context.Context) DedicatedIpPoolOutput
}

func (*DedicatedIpPool) ElementType() reflect.Type {
	return reflect.TypeOf((*DedicatedIpPool)(nil))
}

func (i *DedicatedIpPool) ToDedicatedIpPoolOutput() DedicatedIpPoolOutput {
	return i.ToDedicatedIpPoolOutputWithContext(context.Background())
}

func (i *DedicatedIpPool) ToDedicatedIpPoolOutputWithContext(ctx context.Context) DedicatedIpPoolOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DedicatedIpPoolOutput)
}

type DedicatedIpPoolOutput struct {
	*pulumi.OutputState
}

func (DedicatedIpPoolOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*DedicatedIpPool)(nil))
}

func (o DedicatedIpPoolOutput) ToDedicatedIpPoolOutput() DedicatedIpPoolOutput {
	return o
}

func (o DedicatedIpPoolOutput) ToDedicatedIpPoolOutputWithContext(ctx context.Context) DedicatedIpPoolOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(DedicatedIpPoolOutput{})
}