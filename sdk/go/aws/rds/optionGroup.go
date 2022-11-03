// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package rds

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The AWS::RDS::OptionGroup resource creates an option group, to enable and configure features that are specific to a particular DB engine.
type OptionGroup struct {
	pulumi.CustomResourceState

	// Indicates the name of the engine that this option group can be applied to.
	EngineName pulumi.StringOutput `pulumi:"engineName"`
	// Indicates the major engine version associated with this option group.
	MajorEngineVersion pulumi.StringOutput `pulumi:"majorEngineVersion"`
	// Indicates what options are available in the option group.
	OptionConfigurations OptionGroupOptionConfigurationArrayOutput `pulumi:"optionConfigurations"`
	// Provides a description of the option group.
	OptionGroupDescription pulumi.StringOutput `pulumi:"optionGroupDescription"`
	// Specifies the name of the option group.
	OptionGroupName pulumi.StringPtrOutput `pulumi:"optionGroupName"`
	// An array of key-value pairs to apply to this resource.
	Tags OptionGroupTagArrayOutput `pulumi:"tags"`
}

// NewOptionGroup registers a new resource with the given unique name, arguments, and options.
func NewOptionGroup(ctx *pulumi.Context,
	name string, args *OptionGroupArgs, opts ...pulumi.ResourceOption) (*OptionGroup, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.EngineName == nil {
		return nil, errors.New("invalid value for required argument 'EngineName'")
	}
	if args.MajorEngineVersion == nil {
		return nil, errors.New("invalid value for required argument 'MajorEngineVersion'")
	}
	if args.OptionGroupDescription == nil {
		return nil, errors.New("invalid value for required argument 'OptionGroupDescription'")
	}
	var resource OptionGroup
	err := ctx.RegisterResource("aws-native:rds:OptionGroup", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetOptionGroup gets an existing OptionGroup resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetOptionGroup(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *OptionGroupState, opts ...pulumi.ResourceOption) (*OptionGroup, error) {
	var resource OptionGroup
	err := ctx.ReadResource("aws-native:rds:OptionGroup", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering OptionGroup resources.
type optionGroupState struct {
}

type OptionGroupState struct {
}

func (OptionGroupState) ElementType() reflect.Type {
	return reflect.TypeOf((*optionGroupState)(nil)).Elem()
}

type optionGroupArgs struct {
	// Indicates the name of the engine that this option group can be applied to.
	EngineName string `pulumi:"engineName"`
	// Indicates the major engine version associated with this option group.
	MajorEngineVersion string `pulumi:"majorEngineVersion"`
	// Indicates what options are available in the option group.
	OptionConfigurations []OptionGroupOptionConfiguration `pulumi:"optionConfigurations"`
	// Provides a description of the option group.
	OptionGroupDescription string `pulumi:"optionGroupDescription"`
	// Specifies the name of the option group.
	OptionGroupName *string `pulumi:"optionGroupName"`
	// An array of key-value pairs to apply to this resource.
	Tags []OptionGroupTag `pulumi:"tags"`
}

// The set of arguments for constructing a OptionGroup resource.
type OptionGroupArgs struct {
	// Indicates the name of the engine that this option group can be applied to.
	EngineName pulumi.StringInput
	// Indicates the major engine version associated with this option group.
	MajorEngineVersion pulumi.StringInput
	// Indicates what options are available in the option group.
	OptionConfigurations OptionGroupOptionConfigurationArrayInput
	// Provides a description of the option group.
	OptionGroupDescription pulumi.StringInput
	// Specifies the name of the option group.
	OptionGroupName pulumi.StringPtrInput
	// An array of key-value pairs to apply to this resource.
	Tags OptionGroupTagArrayInput
}

func (OptionGroupArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*optionGroupArgs)(nil)).Elem()
}

type OptionGroupInput interface {
	pulumi.Input

	ToOptionGroupOutput() OptionGroupOutput
	ToOptionGroupOutputWithContext(ctx context.Context) OptionGroupOutput
}

func (*OptionGroup) ElementType() reflect.Type {
	return reflect.TypeOf((**OptionGroup)(nil)).Elem()
}

func (i *OptionGroup) ToOptionGroupOutput() OptionGroupOutput {
	return i.ToOptionGroupOutputWithContext(context.Background())
}

func (i *OptionGroup) ToOptionGroupOutputWithContext(ctx context.Context) OptionGroupOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OptionGroupOutput)
}

type OptionGroupOutput struct{ *pulumi.OutputState }

func (OptionGroupOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**OptionGroup)(nil)).Elem()
}

func (o OptionGroupOutput) ToOptionGroupOutput() OptionGroupOutput {
	return o
}

func (o OptionGroupOutput) ToOptionGroupOutputWithContext(ctx context.Context) OptionGroupOutput {
	return o
}

// Indicates the name of the engine that this option group can be applied to.
func (o OptionGroupOutput) EngineName() pulumi.StringOutput {
	return o.ApplyT(func(v *OptionGroup) pulumi.StringOutput { return v.EngineName }).(pulumi.StringOutput)
}

// Indicates the major engine version associated with this option group.
func (o OptionGroupOutput) MajorEngineVersion() pulumi.StringOutput {
	return o.ApplyT(func(v *OptionGroup) pulumi.StringOutput { return v.MajorEngineVersion }).(pulumi.StringOutput)
}

// Indicates what options are available in the option group.
func (o OptionGroupOutput) OptionConfigurations() OptionGroupOptionConfigurationArrayOutput {
	return o.ApplyT(func(v *OptionGroup) OptionGroupOptionConfigurationArrayOutput { return v.OptionConfigurations }).(OptionGroupOptionConfigurationArrayOutput)
}

// Provides a description of the option group.
func (o OptionGroupOutput) OptionGroupDescription() pulumi.StringOutput {
	return o.ApplyT(func(v *OptionGroup) pulumi.StringOutput { return v.OptionGroupDescription }).(pulumi.StringOutput)
}

// Specifies the name of the option group.
func (o OptionGroupOutput) OptionGroupName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *OptionGroup) pulumi.StringPtrOutput { return v.OptionGroupName }).(pulumi.StringPtrOutput)
}

// An array of key-value pairs to apply to this resource.
func (o OptionGroupOutput) Tags() OptionGroupTagArrayOutput {
	return o.ApplyT(func(v *OptionGroup) OptionGroupTagArrayOutput { return v.Tags }).(OptionGroupTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*OptionGroupInput)(nil)).Elem(), &OptionGroup{})
	pulumi.RegisterOutputType(OptionGroupOutput{})
}
