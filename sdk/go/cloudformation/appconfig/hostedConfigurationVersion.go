// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package appconfig

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-hostedconfigurationversion.html
type HostedConfigurationVersion struct {
	pulumi.CustomResourceState

	// The attributes associated with the resource
	Attributes HostedConfigurationVersionAttributesOutput `pulumi:"attributes"`
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrOutput `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata pulumi.AnyOutput `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties HostedConfigurationVersionPropertiesOutput `pulumi:"properties"`
}

// NewHostedConfigurationVersion registers a new resource with the given unique name, arguments, and options.
func NewHostedConfigurationVersion(ctx *pulumi.Context,
	name string, args *HostedConfigurationVersionArgs, opts ...pulumi.ResourceOption) (*HostedConfigurationVersion, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Properties == nil {
		return nil, errors.New("invalid value for required argument 'Properties'")
	}
	var resource HostedConfigurationVersion
	err := ctx.RegisterResource("cloudformation:AppConfig:HostedConfigurationVersion", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetHostedConfigurationVersion gets an existing HostedConfigurationVersion resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetHostedConfigurationVersion(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *HostedConfigurationVersionState, opts ...pulumi.ResourceOption) (*HostedConfigurationVersion, error) {
	var resource HostedConfigurationVersion
	err := ctx.ReadResource("cloudformation:AppConfig:HostedConfigurationVersion", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering HostedConfigurationVersion resources.
type hostedConfigurationVersionState struct {
	// The attributes associated with the resource
	Attributes *HostedConfigurationVersionAttributes `pulumi:"attributes"`
	// An explicit logical ID for the resource
	LogicalId *string `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata interface{} `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties *HostedConfigurationVersionProperties `pulumi:"properties"`
}

type HostedConfigurationVersionState struct {
	// The attributes associated with the resource
	Attributes HostedConfigurationVersionAttributesPtrInput
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrInput
	// Arbitrary structured data associated with the resource
	Metadata pulumi.Input
	// The input properties associated with the resource
	Properties HostedConfigurationVersionPropertiesPtrInput
}

func (HostedConfigurationVersionState) ElementType() reflect.Type {
	return reflect.TypeOf((*hostedConfigurationVersionState)(nil)).Elem()
}

type hostedConfigurationVersionArgs struct {
	// With the deletionPolicy attribute you can preserve or (in some cases) backup a resource when its stack is deleted. You can specify a deletionPolicy attribute for each resource that you want to control. If a resource has no deletionPolicy attribute, AWS CloudFormation deletes the resource by default.
	DeletionPolicy *string `pulumi:"deletionPolicy"`
	// An explicit logical ID for the resource
	LogicalId *string `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata interface{} `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties HostedConfigurationVersionProperties `pulumi:"properties"`
	// Use the updateReplacePolicy attribute to retain or (in some cases) backup the existing physical instance of a resource when it is replaced during a stack update operation.
	UpdateReplacePolicy *string `pulumi:"updateReplacePolicy"`
}

// The set of arguments for constructing a HostedConfigurationVersion resource.
type HostedConfigurationVersionArgs struct {
	// With the deletionPolicy attribute you can preserve or (in some cases) backup a resource when its stack is deleted. You can specify a deletionPolicy attribute for each resource that you want to control. If a resource has no deletionPolicy attribute, AWS CloudFormation deletes the resource by default.
	DeletionPolicy pulumi.StringPtrInput
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrInput
	// Arbitrary structured data associated with the resource
	Metadata pulumi.Input
	// The input properties associated with the resource
	Properties HostedConfigurationVersionPropertiesInput
	// Use the updateReplacePolicy attribute to retain or (in some cases) backup the existing physical instance of a resource when it is replaced during a stack update operation.
	UpdateReplacePolicy pulumi.StringPtrInput
}

func (HostedConfigurationVersionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*hostedConfigurationVersionArgs)(nil)).Elem()
}

type HostedConfigurationVersionInput interface {
	pulumi.Input

	ToHostedConfigurationVersionOutput() HostedConfigurationVersionOutput
	ToHostedConfigurationVersionOutputWithContext(ctx context.Context) HostedConfigurationVersionOutput
}

func (*HostedConfigurationVersion) ElementType() reflect.Type {
	return reflect.TypeOf((*HostedConfigurationVersion)(nil))
}

func (i *HostedConfigurationVersion) ToHostedConfigurationVersionOutput() HostedConfigurationVersionOutput {
	return i.ToHostedConfigurationVersionOutputWithContext(context.Background())
}

func (i *HostedConfigurationVersion) ToHostedConfigurationVersionOutputWithContext(ctx context.Context) HostedConfigurationVersionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(HostedConfigurationVersionOutput)
}

type HostedConfigurationVersionOutput struct {
	*pulumi.OutputState
}

func (HostedConfigurationVersionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*HostedConfigurationVersion)(nil))
}

func (o HostedConfigurationVersionOutput) ToHostedConfigurationVersionOutput() HostedConfigurationVersionOutput {
	return o
}

func (o HostedConfigurationVersionOutput) ToHostedConfigurationVersionOutputWithContext(ctx context.Context) HostedConfigurationVersionOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(HostedConfigurationVersionOutput{})
}