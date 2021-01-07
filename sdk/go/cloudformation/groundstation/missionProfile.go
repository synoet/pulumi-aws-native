// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package groundstation

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html
type MissionProfile struct {
	pulumi.CustomResourceState

	// The attributes associated with the resource
	Attributes MissionProfileAttributesOutput `pulumi:"attributes"`
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrOutput `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata pulumi.AnyOutput `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties MissionProfilePropertiesOutput `pulumi:"properties"`
}

// NewMissionProfile registers a new resource with the given unique name, arguments, and options.
func NewMissionProfile(ctx *pulumi.Context,
	name string, args *MissionProfileArgs, opts ...pulumi.ResourceOption) (*MissionProfile, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Properties == nil {
		return nil, errors.New("invalid value for required argument 'Properties'")
	}
	var resource MissionProfile
	err := ctx.RegisterResource("cloudformation:GroundStation:MissionProfile", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetMissionProfile gets an existing MissionProfile resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetMissionProfile(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *MissionProfileState, opts ...pulumi.ResourceOption) (*MissionProfile, error) {
	var resource MissionProfile
	err := ctx.ReadResource("cloudformation:GroundStation:MissionProfile", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering MissionProfile resources.
type missionProfileState struct {
	// The attributes associated with the resource
	Attributes *MissionProfileAttributes `pulumi:"attributes"`
	// An explicit logical ID for the resource
	LogicalId *string `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata interface{} `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties *MissionProfileProperties `pulumi:"properties"`
}

type MissionProfileState struct {
	// The attributes associated with the resource
	Attributes MissionProfileAttributesPtrInput
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrInput
	// Arbitrary structured data associated with the resource
	Metadata pulumi.Input
	// The input properties associated with the resource
	Properties MissionProfilePropertiesPtrInput
}

func (MissionProfileState) ElementType() reflect.Type {
	return reflect.TypeOf((*missionProfileState)(nil)).Elem()
}

type missionProfileArgs struct {
	// With the deletionPolicy attribute you can preserve or (in some cases) backup a resource when its stack is deleted. You can specify a deletionPolicy attribute for each resource that you want to control. If a resource has no deletionPolicy attribute, AWS CloudFormation deletes the resource by default.
	DeletionPolicy *string `pulumi:"deletionPolicy"`
	// An explicit logical ID for the resource
	LogicalId *string `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata interface{} `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties MissionProfileProperties `pulumi:"properties"`
	// Use the updateReplacePolicy attribute to retain or (in some cases) backup the existing physical instance of a resource when it is replaced during a stack update operation.
	UpdateReplacePolicy *string `pulumi:"updateReplacePolicy"`
}

// The set of arguments for constructing a MissionProfile resource.
type MissionProfileArgs struct {
	// With the deletionPolicy attribute you can preserve or (in some cases) backup a resource when its stack is deleted. You can specify a deletionPolicy attribute for each resource that you want to control. If a resource has no deletionPolicy attribute, AWS CloudFormation deletes the resource by default.
	DeletionPolicy pulumi.StringPtrInput
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrInput
	// Arbitrary structured data associated with the resource
	Metadata pulumi.Input
	// The input properties associated with the resource
	Properties MissionProfilePropertiesInput
	// Use the updateReplacePolicy attribute to retain or (in some cases) backup the existing physical instance of a resource when it is replaced during a stack update operation.
	UpdateReplacePolicy pulumi.StringPtrInput
}

func (MissionProfileArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*missionProfileArgs)(nil)).Elem()
}

type MissionProfileInput interface {
	pulumi.Input

	ToMissionProfileOutput() MissionProfileOutput
	ToMissionProfileOutputWithContext(ctx context.Context) MissionProfileOutput
}

func (*MissionProfile) ElementType() reflect.Type {
	return reflect.TypeOf((*MissionProfile)(nil))
}

func (i *MissionProfile) ToMissionProfileOutput() MissionProfileOutput {
	return i.ToMissionProfileOutputWithContext(context.Background())
}

func (i *MissionProfile) ToMissionProfileOutputWithContext(ctx context.Context) MissionProfileOutput {
	return pulumi.ToOutputWithContext(ctx, i).(MissionProfileOutput)
}

type MissionProfileOutput struct {
	*pulumi.OutputState
}

func (MissionProfileOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*MissionProfile)(nil))
}

func (o MissionProfileOutput) ToMissionProfileOutput() MissionProfileOutput {
	return o
}

func (o MissionProfileOutput) ToMissionProfileOutputWithContext(ctx context.Context) MissionProfileOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(MissionProfileOutput{})
}