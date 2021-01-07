// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package appconfig

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html
type ConfigurationProfile struct {
	pulumi.CustomResourceState

	// The attributes associated with the resource
	Attributes ConfigurationProfileAttributesOutput `pulumi:"attributes"`
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrOutput `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata pulumi.AnyOutput `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties ConfigurationProfilePropertiesOutput `pulumi:"properties"`
}

// NewConfigurationProfile registers a new resource with the given unique name, arguments, and options.
func NewConfigurationProfile(ctx *pulumi.Context,
	name string, args *ConfigurationProfileArgs, opts ...pulumi.ResourceOption) (*ConfigurationProfile, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Properties == nil {
		return nil, errors.New("invalid value for required argument 'Properties'")
	}
	var resource ConfigurationProfile
	err := ctx.RegisterResource("cloudformation:AppConfig:ConfigurationProfile", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetConfigurationProfile gets an existing ConfigurationProfile resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetConfigurationProfile(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ConfigurationProfileState, opts ...pulumi.ResourceOption) (*ConfigurationProfile, error) {
	var resource ConfigurationProfile
	err := ctx.ReadResource("cloudformation:AppConfig:ConfigurationProfile", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ConfigurationProfile resources.
type configurationProfileState struct {
	// The attributes associated with the resource
	Attributes *ConfigurationProfileAttributes `pulumi:"attributes"`
	// An explicit logical ID for the resource
	LogicalId *string `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata interface{} `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties *ConfigurationProfileProperties `pulumi:"properties"`
}

type ConfigurationProfileState struct {
	// The attributes associated with the resource
	Attributes ConfigurationProfileAttributesPtrInput
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrInput
	// Arbitrary structured data associated with the resource
	Metadata pulumi.Input
	// The input properties associated with the resource
	Properties ConfigurationProfilePropertiesPtrInput
}

func (ConfigurationProfileState) ElementType() reflect.Type {
	return reflect.TypeOf((*configurationProfileState)(nil)).Elem()
}

type configurationProfileArgs struct {
	// With the deletionPolicy attribute you can preserve or (in some cases) backup a resource when its stack is deleted. You can specify a deletionPolicy attribute for each resource that you want to control. If a resource has no deletionPolicy attribute, AWS CloudFormation deletes the resource by default.
	DeletionPolicy *string `pulumi:"deletionPolicy"`
	// An explicit logical ID for the resource
	LogicalId *string `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata interface{} `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties ConfigurationProfileProperties `pulumi:"properties"`
	// Use the updateReplacePolicy attribute to retain or (in some cases) backup the existing physical instance of a resource when it is replaced during a stack update operation.
	UpdateReplacePolicy *string `pulumi:"updateReplacePolicy"`
}

// The set of arguments for constructing a ConfigurationProfile resource.
type ConfigurationProfileArgs struct {
	// With the deletionPolicy attribute you can preserve or (in some cases) backup a resource when its stack is deleted. You can specify a deletionPolicy attribute for each resource that you want to control. If a resource has no deletionPolicy attribute, AWS CloudFormation deletes the resource by default.
	DeletionPolicy pulumi.StringPtrInput
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrInput
	// Arbitrary structured data associated with the resource
	Metadata pulumi.Input
	// The input properties associated with the resource
	Properties ConfigurationProfilePropertiesInput
	// Use the updateReplacePolicy attribute to retain or (in some cases) backup the existing physical instance of a resource when it is replaced during a stack update operation.
	UpdateReplacePolicy pulumi.StringPtrInput
}

func (ConfigurationProfileArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*configurationProfileArgs)(nil)).Elem()
}

type ConfigurationProfileInput interface {
	pulumi.Input

	ToConfigurationProfileOutput() ConfigurationProfileOutput
	ToConfigurationProfileOutputWithContext(ctx context.Context) ConfigurationProfileOutput
}

func (*ConfigurationProfile) ElementType() reflect.Type {
	return reflect.TypeOf((*ConfigurationProfile)(nil))
}

func (i *ConfigurationProfile) ToConfigurationProfileOutput() ConfigurationProfileOutput {
	return i.ToConfigurationProfileOutputWithContext(context.Background())
}

func (i *ConfigurationProfile) ToConfigurationProfileOutputWithContext(ctx context.Context) ConfigurationProfileOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConfigurationProfileOutput)
}

type ConfigurationProfileOutput struct {
	*pulumi.OutputState
}

func (ConfigurationProfileOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ConfigurationProfile)(nil))
}

func (o ConfigurationProfileOutput) ToConfigurationProfileOutput() ConfigurationProfileOutput {
	return o
}

func (o ConfigurationProfileOutput) ToConfigurationProfileOutputWithContext(ctx context.Context) ConfigurationProfileOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(ConfigurationProfileOutput{})
}