// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package lightsail

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::Lightsail::Disk
type Disk struct {
	pulumi.CustomResourceState

	// An array of objects representing the add-ons to enable for the new instance.
	AddOns DiskAddOnArrayOutput `pulumi:"addOns"`
	// Name of the attached Lightsail Instance
	AttachedTo pulumi.StringOutput `pulumi:"attachedTo"`
	// Attachment State of the Lightsail disk
	AttachmentState pulumi.StringOutput `pulumi:"attachmentState"`
	// The Availability Zone in which to create your instance. Use the following format: us-east-2a (case sensitive). Be sure to add the include Availability Zones parameter to your request.
	AvailabilityZone pulumi.StringPtrOutput `pulumi:"availabilityZone"`
	DiskArn          pulumi.StringOutput    `pulumi:"diskArn"`
	// The names to use for your new Lightsail disk.
	DiskName pulumi.StringOutput `pulumi:"diskName"`
	// Iops of the Lightsail disk
	Iops pulumi.IntOutput `pulumi:"iops"`
	// Check is Disk is attached state
	IsAttached pulumi.BoolOutput     `pulumi:"isAttached"`
	Location   DiskLocationPtrOutput `pulumi:"location"`
	// Path of the  attached Disk
	Path pulumi.StringOutput `pulumi:"path"`
	// Resource type of Lightsail instance.
	ResourceType pulumi.StringOutput `pulumi:"resourceType"`
	// Size of the Lightsail disk
	SizeInGb pulumi.IntOutput `pulumi:"sizeInGb"`
	// State of the Lightsail disk
	State pulumi.StringOutput `pulumi:"state"`
	// Support code to help identify any issues
	SupportCode pulumi.StringOutput `pulumi:"supportCode"`
	// An array of key-value pairs to apply to this resource.
	Tags DiskTagArrayOutput `pulumi:"tags"`
}

// NewDisk registers a new resource with the given unique name, arguments, and options.
func NewDisk(ctx *pulumi.Context,
	name string, args *DiskArgs, opts ...pulumi.ResourceOption) (*Disk, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.SizeInGb == nil {
		return nil, errors.New("invalid value for required argument 'SizeInGb'")
	}
	var resource Disk
	err := ctx.RegisterResource("aws-native:lightsail:Disk", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDisk gets an existing Disk resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDisk(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DiskState, opts ...pulumi.ResourceOption) (*Disk, error) {
	var resource Disk
	err := ctx.ReadResource("aws-native:lightsail:Disk", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Disk resources.
type diskState struct {
}

type DiskState struct {
}

func (DiskState) ElementType() reflect.Type {
	return reflect.TypeOf((*diskState)(nil)).Elem()
}

type diskArgs struct {
	// An array of objects representing the add-ons to enable for the new instance.
	AddOns []DiskAddOn `pulumi:"addOns"`
	// The Availability Zone in which to create your instance. Use the following format: us-east-2a (case sensitive). Be sure to add the include Availability Zones parameter to your request.
	AvailabilityZone *string `pulumi:"availabilityZone"`
	// The names to use for your new Lightsail disk.
	DiskName *string       `pulumi:"diskName"`
	Location *DiskLocation `pulumi:"location"`
	// Size of the Lightsail disk
	SizeInGb int `pulumi:"sizeInGb"`
	// An array of key-value pairs to apply to this resource.
	Tags []DiskTag `pulumi:"tags"`
}

// The set of arguments for constructing a Disk resource.
type DiskArgs struct {
	// An array of objects representing the add-ons to enable for the new instance.
	AddOns DiskAddOnArrayInput
	// The Availability Zone in which to create your instance. Use the following format: us-east-2a (case sensitive). Be sure to add the include Availability Zones parameter to your request.
	AvailabilityZone pulumi.StringPtrInput
	// The names to use for your new Lightsail disk.
	DiskName pulumi.StringPtrInput
	Location DiskLocationPtrInput
	// Size of the Lightsail disk
	SizeInGb pulumi.IntInput
	// An array of key-value pairs to apply to this resource.
	Tags DiskTagArrayInput
}

func (DiskArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*diskArgs)(nil)).Elem()
}

type DiskInput interface {
	pulumi.Input

	ToDiskOutput() DiskOutput
	ToDiskOutputWithContext(ctx context.Context) DiskOutput
}

func (*Disk) ElementType() reflect.Type {
	return reflect.TypeOf((**Disk)(nil)).Elem()
}

func (i *Disk) ToDiskOutput() DiskOutput {
	return i.ToDiskOutputWithContext(context.Background())
}

func (i *Disk) ToDiskOutputWithContext(ctx context.Context) DiskOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DiskOutput)
}

type DiskOutput struct{ *pulumi.OutputState }

func (DiskOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Disk)(nil)).Elem()
}

func (o DiskOutput) ToDiskOutput() DiskOutput {
	return o
}

func (o DiskOutput) ToDiskOutputWithContext(ctx context.Context) DiskOutput {
	return o
}

// An array of objects representing the add-ons to enable for the new instance.
func (o DiskOutput) AddOns() DiskAddOnArrayOutput {
	return o.ApplyT(func(v *Disk) DiskAddOnArrayOutput { return v.AddOns }).(DiskAddOnArrayOutput)
}

// Name of the attached Lightsail Instance
func (o DiskOutput) AttachedTo() pulumi.StringOutput {
	return o.ApplyT(func(v *Disk) pulumi.StringOutput { return v.AttachedTo }).(pulumi.StringOutput)
}

// Attachment State of the Lightsail disk
func (o DiskOutput) AttachmentState() pulumi.StringOutput {
	return o.ApplyT(func(v *Disk) pulumi.StringOutput { return v.AttachmentState }).(pulumi.StringOutput)
}

// The Availability Zone in which to create your instance. Use the following format: us-east-2a (case sensitive). Be sure to add the include Availability Zones parameter to your request.
func (o DiskOutput) AvailabilityZone() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Disk) pulumi.StringPtrOutput { return v.AvailabilityZone }).(pulumi.StringPtrOutput)
}

func (o DiskOutput) DiskArn() pulumi.StringOutput {
	return o.ApplyT(func(v *Disk) pulumi.StringOutput { return v.DiskArn }).(pulumi.StringOutput)
}

// The names to use for your new Lightsail disk.
func (o DiskOutput) DiskName() pulumi.StringOutput {
	return o.ApplyT(func(v *Disk) pulumi.StringOutput { return v.DiskName }).(pulumi.StringOutput)
}

// Iops of the Lightsail disk
func (o DiskOutput) Iops() pulumi.IntOutput {
	return o.ApplyT(func(v *Disk) pulumi.IntOutput { return v.Iops }).(pulumi.IntOutput)
}

// Check is Disk is attached state
func (o DiskOutput) IsAttached() pulumi.BoolOutput {
	return o.ApplyT(func(v *Disk) pulumi.BoolOutput { return v.IsAttached }).(pulumi.BoolOutput)
}

func (o DiskOutput) Location() DiskLocationPtrOutput {
	return o.ApplyT(func(v *Disk) DiskLocationPtrOutput { return v.Location }).(DiskLocationPtrOutput)
}

// Path of the  attached Disk
func (o DiskOutput) Path() pulumi.StringOutput {
	return o.ApplyT(func(v *Disk) pulumi.StringOutput { return v.Path }).(pulumi.StringOutput)
}

// Resource type of Lightsail instance.
func (o DiskOutput) ResourceType() pulumi.StringOutput {
	return o.ApplyT(func(v *Disk) pulumi.StringOutput { return v.ResourceType }).(pulumi.StringOutput)
}

// Size of the Lightsail disk
func (o DiskOutput) SizeInGb() pulumi.IntOutput {
	return o.ApplyT(func(v *Disk) pulumi.IntOutput { return v.SizeInGb }).(pulumi.IntOutput)
}

// State of the Lightsail disk
func (o DiskOutput) State() pulumi.StringOutput {
	return o.ApplyT(func(v *Disk) pulumi.StringOutput { return v.State }).(pulumi.StringOutput)
}

// Support code to help identify any issues
func (o DiskOutput) SupportCode() pulumi.StringOutput {
	return o.ApplyT(func(v *Disk) pulumi.StringOutput { return v.SupportCode }).(pulumi.StringOutput)
}

// An array of key-value pairs to apply to this resource.
func (o DiskOutput) Tags() DiskTagArrayOutput {
	return o.ApplyT(func(v *Disk) DiskTagArrayOutput { return v.Tags }).(DiskTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DiskInput)(nil)).Elem(), &Disk{})
	pulumi.RegisterOutputType(DiskOutput{})
}
