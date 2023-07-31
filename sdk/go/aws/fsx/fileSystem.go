// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package fsx

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::FSx::FileSystem
//
// Deprecated: FileSystem is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type FileSystem struct {
	pulumi.CustomResourceState

	BackupId              pulumi.StringPtrOutput                  `pulumi:"backupId"`
	DnsName               pulumi.StringOutput                     `pulumi:"dnsName"`
	FileSystemType        pulumi.StringOutput                     `pulumi:"fileSystemType"`
	FileSystemTypeVersion pulumi.StringPtrOutput                  `pulumi:"fileSystemTypeVersion"`
	KmsKeyId              pulumi.StringPtrOutput                  `pulumi:"kmsKeyId"`
	LustreConfiguration   FileSystemLustreConfigurationPtrOutput  `pulumi:"lustreConfiguration"`
	LustreMountName       pulumi.StringOutput                     `pulumi:"lustreMountName"`
	OntapConfiguration    FileSystemOntapConfigurationPtrOutput   `pulumi:"ontapConfiguration"`
	OpenZfsConfiguration  FileSystemOpenZFSConfigurationPtrOutput `pulumi:"openZfsConfiguration"`
	ResourceArn           pulumi.StringOutput                     `pulumi:"resourceArn"`
	RootVolumeId          pulumi.StringOutput                     `pulumi:"rootVolumeId"`
	SecurityGroupIds      pulumi.StringArrayOutput                `pulumi:"securityGroupIds"`
	StorageCapacity       pulumi.IntPtrOutput                     `pulumi:"storageCapacity"`
	StorageType           pulumi.StringPtrOutput                  `pulumi:"storageType"`
	SubnetIds             pulumi.StringArrayOutput                `pulumi:"subnetIds"`
	Tags                  FileSystemTagArrayOutput                `pulumi:"tags"`
	WindowsConfiguration  FileSystemWindowsConfigurationPtrOutput `pulumi:"windowsConfiguration"`
}

// NewFileSystem registers a new resource with the given unique name, arguments, and options.
func NewFileSystem(ctx *pulumi.Context,
	name string, args *FileSystemArgs, opts ...pulumi.ResourceOption) (*FileSystem, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.FileSystemType == nil {
		return nil, errors.New("invalid value for required argument 'FileSystemType'")
	}
	if args.SubnetIds == nil {
		return nil, errors.New("invalid value for required argument 'SubnetIds'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource FileSystem
	err := ctx.RegisterResource("aws-native:fsx:FileSystem", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetFileSystem gets an existing FileSystem resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetFileSystem(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *FileSystemState, opts ...pulumi.ResourceOption) (*FileSystem, error) {
	var resource FileSystem
	err := ctx.ReadResource("aws-native:fsx:FileSystem", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering FileSystem resources.
type fileSystemState struct {
}

type FileSystemState struct {
}

func (FileSystemState) ElementType() reflect.Type {
	return reflect.TypeOf((*fileSystemState)(nil)).Elem()
}

type fileSystemArgs struct {
	BackupId              *string                         `pulumi:"backupId"`
	FileSystemType        string                          `pulumi:"fileSystemType"`
	FileSystemTypeVersion *string                         `pulumi:"fileSystemTypeVersion"`
	KmsKeyId              *string                         `pulumi:"kmsKeyId"`
	LustreConfiguration   *FileSystemLustreConfiguration  `pulumi:"lustreConfiguration"`
	OntapConfiguration    *FileSystemOntapConfiguration   `pulumi:"ontapConfiguration"`
	OpenZfsConfiguration  *FileSystemOpenZFSConfiguration `pulumi:"openZfsConfiguration"`
	SecurityGroupIds      []string                        `pulumi:"securityGroupIds"`
	StorageCapacity       *int                            `pulumi:"storageCapacity"`
	StorageType           *string                         `pulumi:"storageType"`
	SubnetIds             []string                        `pulumi:"subnetIds"`
	Tags                  []FileSystemTag                 `pulumi:"tags"`
	WindowsConfiguration  *FileSystemWindowsConfiguration `pulumi:"windowsConfiguration"`
}

// The set of arguments for constructing a FileSystem resource.
type FileSystemArgs struct {
	BackupId              pulumi.StringPtrInput
	FileSystemType        pulumi.StringInput
	FileSystemTypeVersion pulumi.StringPtrInput
	KmsKeyId              pulumi.StringPtrInput
	LustreConfiguration   FileSystemLustreConfigurationPtrInput
	OntapConfiguration    FileSystemOntapConfigurationPtrInput
	OpenZfsConfiguration  FileSystemOpenZFSConfigurationPtrInput
	SecurityGroupIds      pulumi.StringArrayInput
	StorageCapacity       pulumi.IntPtrInput
	StorageType           pulumi.StringPtrInput
	SubnetIds             pulumi.StringArrayInput
	Tags                  FileSystemTagArrayInput
	WindowsConfiguration  FileSystemWindowsConfigurationPtrInput
}

func (FileSystemArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*fileSystemArgs)(nil)).Elem()
}

type FileSystemInput interface {
	pulumi.Input

	ToFileSystemOutput() FileSystemOutput
	ToFileSystemOutputWithContext(ctx context.Context) FileSystemOutput
}

func (*FileSystem) ElementType() reflect.Type {
	return reflect.TypeOf((**FileSystem)(nil)).Elem()
}

func (i *FileSystem) ToFileSystemOutput() FileSystemOutput {
	return i.ToFileSystemOutputWithContext(context.Background())
}

func (i *FileSystem) ToFileSystemOutputWithContext(ctx context.Context) FileSystemOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FileSystemOutput)
}

type FileSystemOutput struct{ *pulumi.OutputState }

func (FileSystemOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**FileSystem)(nil)).Elem()
}

func (o FileSystemOutput) ToFileSystemOutput() FileSystemOutput {
	return o
}

func (o FileSystemOutput) ToFileSystemOutputWithContext(ctx context.Context) FileSystemOutput {
	return o
}

func (o FileSystemOutput) BackupId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *FileSystem) pulumi.StringPtrOutput { return v.BackupId }).(pulumi.StringPtrOutput)
}

func (o FileSystemOutput) DnsName() pulumi.StringOutput {
	return o.ApplyT(func(v *FileSystem) pulumi.StringOutput { return v.DnsName }).(pulumi.StringOutput)
}

func (o FileSystemOutput) FileSystemType() pulumi.StringOutput {
	return o.ApplyT(func(v *FileSystem) pulumi.StringOutput { return v.FileSystemType }).(pulumi.StringOutput)
}

func (o FileSystemOutput) FileSystemTypeVersion() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *FileSystem) pulumi.StringPtrOutput { return v.FileSystemTypeVersion }).(pulumi.StringPtrOutput)
}

func (o FileSystemOutput) KmsKeyId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *FileSystem) pulumi.StringPtrOutput { return v.KmsKeyId }).(pulumi.StringPtrOutput)
}

func (o FileSystemOutput) LustreConfiguration() FileSystemLustreConfigurationPtrOutput {
	return o.ApplyT(func(v *FileSystem) FileSystemLustreConfigurationPtrOutput { return v.LustreConfiguration }).(FileSystemLustreConfigurationPtrOutput)
}

func (o FileSystemOutput) LustreMountName() pulumi.StringOutput {
	return o.ApplyT(func(v *FileSystem) pulumi.StringOutput { return v.LustreMountName }).(pulumi.StringOutput)
}

func (o FileSystemOutput) OntapConfiguration() FileSystemOntapConfigurationPtrOutput {
	return o.ApplyT(func(v *FileSystem) FileSystemOntapConfigurationPtrOutput { return v.OntapConfiguration }).(FileSystemOntapConfigurationPtrOutput)
}

func (o FileSystemOutput) OpenZfsConfiguration() FileSystemOpenZFSConfigurationPtrOutput {
	return o.ApplyT(func(v *FileSystem) FileSystemOpenZFSConfigurationPtrOutput { return v.OpenZfsConfiguration }).(FileSystemOpenZFSConfigurationPtrOutput)
}

func (o FileSystemOutput) ResourceArn() pulumi.StringOutput {
	return o.ApplyT(func(v *FileSystem) pulumi.StringOutput { return v.ResourceArn }).(pulumi.StringOutput)
}

func (o FileSystemOutput) RootVolumeId() pulumi.StringOutput {
	return o.ApplyT(func(v *FileSystem) pulumi.StringOutput { return v.RootVolumeId }).(pulumi.StringOutput)
}

func (o FileSystemOutput) SecurityGroupIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *FileSystem) pulumi.StringArrayOutput { return v.SecurityGroupIds }).(pulumi.StringArrayOutput)
}

func (o FileSystemOutput) StorageCapacity() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *FileSystem) pulumi.IntPtrOutput { return v.StorageCapacity }).(pulumi.IntPtrOutput)
}

func (o FileSystemOutput) StorageType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *FileSystem) pulumi.StringPtrOutput { return v.StorageType }).(pulumi.StringPtrOutput)
}

func (o FileSystemOutput) SubnetIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *FileSystem) pulumi.StringArrayOutput { return v.SubnetIds }).(pulumi.StringArrayOutput)
}

func (o FileSystemOutput) Tags() FileSystemTagArrayOutput {
	return o.ApplyT(func(v *FileSystem) FileSystemTagArrayOutput { return v.Tags }).(FileSystemTagArrayOutput)
}

func (o FileSystemOutput) WindowsConfiguration() FileSystemWindowsConfigurationPtrOutput {
	return o.ApplyT(func(v *FileSystem) FileSystemWindowsConfigurationPtrOutput { return v.WindowsConfiguration }).(FileSystemWindowsConfigurationPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*FileSystemInput)(nil)).Elem(), &FileSystem{})
	pulumi.RegisterOutputType(FileSystemOutput{})
}
