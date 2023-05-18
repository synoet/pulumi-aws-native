// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ssmcontacts

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::SSMContacts::Rotation.
type Rotation struct {
	pulumi.CustomResourceState

	// The Amazon Resource Name (ARN) of the rotation.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// Members of the rotation
	ContactIds pulumi.StringArrayOutput `pulumi:"contactIds"`
	// Name of the Rotation
	Name       pulumi.StringOutput              `pulumi:"name"`
	Recurrence RotationRecurrenceSettingsOutput `pulumi:"recurrence"`
	// Start time of the first shift of Oncall Schedule
	StartTime pulumi.StringOutput    `pulumi:"startTime"`
	Tags      RotationTagArrayOutput `pulumi:"tags"`
	// TimeZone Identifier for the Oncall Schedule
	TimeZoneId pulumi.StringOutput `pulumi:"timeZoneId"`
}

// NewRotation registers a new resource with the given unique name, arguments, and options.
func NewRotation(ctx *pulumi.Context,
	name string, args *RotationArgs, opts ...pulumi.ResourceOption) (*Rotation, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ContactIds == nil {
		return nil, errors.New("invalid value for required argument 'ContactIds'")
	}
	if args.Recurrence == nil {
		return nil, errors.New("invalid value for required argument 'Recurrence'")
	}
	if args.StartTime == nil {
		return nil, errors.New("invalid value for required argument 'StartTime'")
	}
	if args.TimeZoneId == nil {
		return nil, errors.New("invalid value for required argument 'TimeZoneId'")
	}
	var resource Rotation
	err := ctx.RegisterResource("aws-native:ssmcontacts:Rotation", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetRotation gets an existing Rotation resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRotation(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *RotationState, opts ...pulumi.ResourceOption) (*Rotation, error) {
	var resource Rotation
	err := ctx.ReadResource("aws-native:ssmcontacts:Rotation", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Rotation resources.
type rotationState struct {
}

type RotationState struct {
}

func (RotationState) ElementType() reflect.Type {
	return reflect.TypeOf((*rotationState)(nil)).Elem()
}

type rotationArgs struct {
	// Members of the rotation
	ContactIds []string `pulumi:"contactIds"`
	// Name of the Rotation
	Name       *string                    `pulumi:"name"`
	Recurrence RotationRecurrenceSettings `pulumi:"recurrence"`
	// Start time of the first shift of Oncall Schedule
	StartTime string        `pulumi:"startTime"`
	Tags      []RotationTag `pulumi:"tags"`
	// TimeZone Identifier for the Oncall Schedule
	TimeZoneId string `pulumi:"timeZoneId"`
}

// The set of arguments for constructing a Rotation resource.
type RotationArgs struct {
	// Members of the rotation
	ContactIds pulumi.StringArrayInput
	// Name of the Rotation
	Name       pulumi.StringPtrInput
	Recurrence RotationRecurrenceSettingsInput
	// Start time of the first shift of Oncall Schedule
	StartTime pulumi.StringInput
	Tags      RotationTagArrayInput
	// TimeZone Identifier for the Oncall Schedule
	TimeZoneId pulumi.StringInput
}

func (RotationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*rotationArgs)(nil)).Elem()
}

type RotationInput interface {
	pulumi.Input

	ToRotationOutput() RotationOutput
	ToRotationOutputWithContext(ctx context.Context) RotationOutput
}

func (*Rotation) ElementType() reflect.Type {
	return reflect.TypeOf((**Rotation)(nil)).Elem()
}

func (i *Rotation) ToRotationOutput() RotationOutput {
	return i.ToRotationOutputWithContext(context.Background())
}

func (i *Rotation) ToRotationOutputWithContext(ctx context.Context) RotationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RotationOutput)
}

type RotationOutput struct{ *pulumi.OutputState }

func (RotationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Rotation)(nil)).Elem()
}

func (o RotationOutput) ToRotationOutput() RotationOutput {
	return o
}

func (o RotationOutput) ToRotationOutputWithContext(ctx context.Context) RotationOutput {
	return o
}

// The Amazon Resource Name (ARN) of the rotation.
func (o RotationOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *Rotation) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

// Members of the rotation
func (o RotationOutput) ContactIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Rotation) pulumi.StringArrayOutput { return v.ContactIds }).(pulumi.StringArrayOutput)
}

// Name of the Rotation
func (o RotationOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Rotation) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o RotationOutput) Recurrence() RotationRecurrenceSettingsOutput {
	return o.ApplyT(func(v *Rotation) RotationRecurrenceSettingsOutput { return v.Recurrence }).(RotationRecurrenceSettingsOutput)
}

// Start time of the first shift of Oncall Schedule
func (o RotationOutput) StartTime() pulumi.StringOutput {
	return o.ApplyT(func(v *Rotation) pulumi.StringOutput { return v.StartTime }).(pulumi.StringOutput)
}

func (o RotationOutput) Tags() RotationTagArrayOutput {
	return o.ApplyT(func(v *Rotation) RotationTagArrayOutput { return v.Tags }).(RotationTagArrayOutput)
}

// TimeZone Identifier for the Oncall Schedule
func (o RotationOutput) TimeZoneId() pulumi.StringOutput {
	return o.ApplyT(func(v *Rotation) pulumi.StringOutput { return v.TimeZoneId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*RotationInput)(nil)).Elem(), &Rotation{})
	pulumi.RegisterOutputType(RotationOutput{})
}
