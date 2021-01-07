// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package apigateway

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-usageplan.html
type UsagePlan struct {
	pulumi.CustomResourceState

	// The attributes associated with the resource
	Attributes UsagePlanAttributesOutput `pulumi:"attributes"`
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrOutput `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata pulumi.AnyOutput `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties UsagePlanPropertiesOutput `pulumi:"properties"`
}

// NewUsagePlan registers a new resource with the given unique name, arguments, and options.
func NewUsagePlan(ctx *pulumi.Context,
	name string, args *UsagePlanArgs, opts ...pulumi.ResourceOption) (*UsagePlan, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Properties == nil {
		return nil, errors.New("invalid value for required argument 'Properties'")
	}
	var resource UsagePlan
	err := ctx.RegisterResource("cloudformation:ApiGateway:UsagePlan", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetUsagePlan gets an existing UsagePlan resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetUsagePlan(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *UsagePlanState, opts ...pulumi.ResourceOption) (*UsagePlan, error) {
	var resource UsagePlan
	err := ctx.ReadResource("cloudformation:ApiGateway:UsagePlan", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering UsagePlan resources.
type usagePlanState struct {
	// The attributes associated with the resource
	Attributes *UsagePlanAttributes `pulumi:"attributes"`
	// An explicit logical ID for the resource
	LogicalId *string `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata interface{} `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties *UsagePlanProperties `pulumi:"properties"`
}

type UsagePlanState struct {
	// The attributes associated with the resource
	Attributes UsagePlanAttributesPtrInput
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrInput
	// Arbitrary structured data associated with the resource
	Metadata pulumi.Input
	// The input properties associated with the resource
	Properties UsagePlanPropertiesPtrInput
}

func (UsagePlanState) ElementType() reflect.Type {
	return reflect.TypeOf((*usagePlanState)(nil)).Elem()
}

type usagePlanArgs struct {
	// With the deletionPolicy attribute you can preserve or (in some cases) backup a resource when its stack is deleted. You can specify a deletionPolicy attribute for each resource that you want to control. If a resource has no deletionPolicy attribute, AWS CloudFormation deletes the resource by default.
	DeletionPolicy *string `pulumi:"deletionPolicy"`
	// An explicit logical ID for the resource
	LogicalId *string `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata interface{} `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties UsagePlanProperties `pulumi:"properties"`
	// Use the updateReplacePolicy attribute to retain or (in some cases) backup the existing physical instance of a resource when it is replaced during a stack update operation.
	UpdateReplacePolicy *string `pulumi:"updateReplacePolicy"`
}

// The set of arguments for constructing a UsagePlan resource.
type UsagePlanArgs struct {
	// With the deletionPolicy attribute you can preserve or (in some cases) backup a resource when its stack is deleted. You can specify a deletionPolicy attribute for each resource that you want to control. If a resource has no deletionPolicy attribute, AWS CloudFormation deletes the resource by default.
	DeletionPolicy pulumi.StringPtrInput
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrInput
	// Arbitrary structured data associated with the resource
	Metadata pulumi.Input
	// The input properties associated with the resource
	Properties UsagePlanPropertiesInput
	// Use the updateReplacePolicy attribute to retain or (in some cases) backup the existing physical instance of a resource when it is replaced during a stack update operation.
	UpdateReplacePolicy pulumi.StringPtrInput
}

func (UsagePlanArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*usagePlanArgs)(nil)).Elem()
}

type UsagePlanInput interface {
	pulumi.Input

	ToUsagePlanOutput() UsagePlanOutput
	ToUsagePlanOutputWithContext(ctx context.Context) UsagePlanOutput
}

func (*UsagePlan) ElementType() reflect.Type {
	return reflect.TypeOf((*UsagePlan)(nil))
}

func (i *UsagePlan) ToUsagePlanOutput() UsagePlanOutput {
	return i.ToUsagePlanOutputWithContext(context.Background())
}

func (i *UsagePlan) ToUsagePlanOutputWithContext(ctx context.Context) UsagePlanOutput {
	return pulumi.ToOutputWithContext(ctx, i).(UsagePlanOutput)
}

type UsagePlanOutput struct {
	*pulumi.OutputState
}

func (UsagePlanOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*UsagePlan)(nil))
}

func (o UsagePlanOutput) ToUsagePlanOutput() UsagePlanOutput {
	return o
}

func (o UsagePlanOutput) ToUsagePlanOutputWithContext(ctx context.Context) UsagePlanOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(UsagePlanOutput{})
}