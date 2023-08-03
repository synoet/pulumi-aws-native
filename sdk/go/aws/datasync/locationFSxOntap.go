// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package datasync

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for AWS::DataSync::LocationFSxONTAP.
type LocationFSxOntap struct {
	pulumi.CustomResourceState

	// The Amazon Resource Name (ARN) for the FSx ONAP file system.
	FsxFilesystemArn pulumi.StringOutput `pulumi:"fsxFilesystemArn"`
	// The Amazon Resource Name (ARN) of the Amazon FSx ONTAP file system location that is created.
	LocationArn pulumi.StringOutput `pulumi:"locationArn"`
	// The URL of the FSx ONTAP file system that was described.
	LocationUri pulumi.StringOutput               `pulumi:"locationUri"`
	Protocol    LocationFSxOntapProtocolPtrOutput `pulumi:"protocol"`
	// The ARNs of the security groups that are to use to configure the FSx ONTAP file system.
	SecurityGroupArns pulumi.StringArrayOutput `pulumi:"securityGroupArns"`
	// The Amazon Resource Name (ARN) for the FSx ONTAP SVM.
	StorageVirtualMachineArn pulumi.StringOutput `pulumi:"storageVirtualMachineArn"`
	// A subdirectory in the location's path.
	Subdirectory pulumi.StringPtrOutput `pulumi:"subdirectory"`
	// An array of key-value pairs to apply to this resource.
	Tags LocationFSxOntapTagArrayOutput `pulumi:"tags"`
}

// NewLocationFSxOntap registers a new resource with the given unique name, arguments, and options.
func NewLocationFSxOntap(ctx *pulumi.Context,
	name string, args *LocationFSxOntapArgs, opts ...pulumi.ResourceOption) (*LocationFSxOntap, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.SecurityGroupArns == nil {
		return nil, errors.New("invalid value for required argument 'SecurityGroupArns'")
	}
	if args.StorageVirtualMachineArn == nil {
		return nil, errors.New("invalid value for required argument 'StorageVirtualMachineArn'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource LocationFSxOntap
	err := ctx.RegisterResource("aws-native:datasync:LocationFSxOntap", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetLocationFSxOntap gets an existing LocationFSxOntap resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetLocationFSxOntap(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *LocationFSxOntapState, opts ...pulumi.ResourceOption) (*LocationFSxOntap, error) {
	var resource LocationFSxOntap
	err := ctx.ReadResource("aws-native:datasync:LocationFSxOntap", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering LocationFSxOntap resources.
type locationFSxOntapState struct {
}

type LocationFSxOntapState struct {
}

func (LocationFSxOntapState) ElementType() reflect.Type {
	return reflect.TypeOf((*locationFSxOntapState)(nil)).Elem()
}

type locationFSxOntapArgs struct {
	Protocol *LocationFSxOntapProtocol `pulumi:"protocol"`
	// The ARNs of the security groups that are to use to configure the FSx ONTAP file system.
	SecurityGroupArns []string `pulumi:"securityGroupArns"`
	// The Amazon Resource Name (ARN) for the FSx ONTAP SVM.
	StorageVirtualMachineArn string `pulumi:"storageVirtualMachineArn"`
	// A subdirectory in the location's path.
	Subdirectory *string `pulumi:"subdirectory"`
	// An array of key-value pairs to apply to this resource.
	Tags []LocationFSxOntapTag `pulumi:"tags"`
}

// The set of arguments for constructing a LocationFSxOntap resource.
type LocationFSxOntapArgs struct {
	Protocol LocationFSxOntapProtocolPtrInput
	// The ARNs of the security groups that are to use to configure the FSx ONTAP file system.
	SecurityGroupArns pulumi.StringArrayInput
	// The Amazon Resource Name (ARN) for the FSx ONTAP SVM.
	StorageVirtualMachineArn pulumi.StringInput
	// A subdirectory in the location's path.
	Subdirectory pulumi.StringPtrInput
	// An array of key-value pairs to apply to this resource.
	Tags LocationFSxOntapTagArrayInput
}

func (LocationFSxOntapArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*locationFSxOntapArgs)(nil)).Elem()
}

type LocationFSxOntapInput interface {
	pulumi.Input

	ToLocationFSxOntapOutput() LocationFSxOntapOutput
	ToLocationFSxOntapOutputWithContext(ctx context.Context) LocationFSxOntapOutput
}

func (*LocationFSxOntap) ElementType() reflect.Type {
	return reflect.TypeOf((**LocationFSxOntap)(nil)).Elem()
}

func (i *LocationFSxOntap) ToLocationFSxOntapOutput() LocationFSxOntapOutput {
	return i.ToLocationFSxOntapOutputWithContext(context.Background())
}

func (i *LocationFSxOntap) ToLocationFSxOntapOutputWithContext(ctx context.Context) LocationFSxOntapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(LocationFSxOntapOutput)
}

type LocationFSxOntapOutput struct{ *pulumi.OutputState }

func (LocationFSxOntapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**LocationFSxOntap)(nil)).Elem()
}

func (o LocationFSxOntapOutput) ToLocationFSxOntapOutput() LocationFSxOntapOutput {
	return o
}

func (o LocationFSxOntapOutput) ToLocationFSxOntapOutputWithContext(ctx context.Context) LocationFSxOntapOutput {
	return o
}

// The Amazon Resource Name (ARN) for the FSx ONAP file system.
func (o LocationFSxOntapOutput) FsxFilesystemArn() pulumi.StringOutput {
	return o.ApplyT(func(v *LocationFSxOntap) pulumi.StringOutput { return v.FsxFilesystemArn }).(pulumi.StringOutput)
}

// The Amazon Resource Name (ARN) of the Amazon FSx ONTAP file system location that is created.
func (o LocationFSxOntapOutput) LocationArn() pulumi.StringOutput {
	return o.ApplyT(func(v *LocationFSxOntap) pulumi.StringOutput { return v.LocationArn }).(pulumi.StringOutput)
}

// The URL of the FSx ONTAP file system that was described.
func (o LocationFSxOntapOutput) LocationUri() pulumi.StringOutput {
	return o.ApplyT(func(v *LocationFSxOntap) pulumi.StringOutput { return v.LocationUri }).(pulumi.StringOutput)
}

func (o LocationFSxOntapOutput) Protocol() LocationFSxOntapProtocolPtrOutput {
	return o.ApplyT(func(v *LocationFSxOntap) LocationFSxOntapProtocolPtrOutput { return v.Protocol }).(LocationFSxOntapProtocolPtrOutput)
}

// The ARNs of the security groups that are to use to configure the FSx ONTAP file system.
func (o LocationFSxOntapOutput) SecurityGroupArns() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *LocationFSxOntap) pulumi.StringArrayOutput { return v.SecurityGroupArns }).(pulumi.StringArrayOutput)
}

// The Amazon Resource Name (ARN) for the FSx ONTAP SVM.
func (o LocationFSxOntapOutput) StorageVirtualMachineArn() pulumi.StringOutput {
	return o.ApplyT(func(v *LocationFSxOntap) pulumi.StringOutput { return v.StorageVirtualMachineArn }).(pulumi.StringOutput)
}

// A subdirectory in the location's path.
func (o LocationFSxOntapOutput) Subdirectory() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *LocationFSxOntap) pulumi.StringPtrOutput { return v.Subdirectory }).(pulumi.StringPtrOutput)
}

// An array of key-value pairs to apply to this resource.
func (o LocationFSxOntapOutput) Tags() LocationFSxOntapTagArrayOutput {
	return o.ApplyT(func(v *LocationFSxOntap) LocationFSxOntapTagArrayOutput { return v.Tags }).(LocationFSxOntapTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*LocationFSxOntapInput)(nil)).Elem(), &LocationFSxOntap{})
	pulumi.RegisterOutputType(LocationFSxOntapOutput{})
}
