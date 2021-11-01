// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package panorama

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Schema for PackageVersion Resource Type
type PackageVersion struct {
	pulumi.CustomResourceState

	IsLatestPatch             pulumi.BoolOutput          `pulumi:"isLatestPatch"`
	MarkLatest                pulumi.BoolPtrOutput       `pulumi:"markLatest"`
	OwnerAccount              pulumi.StringPtrOutput     `pulumi:"ownerAccount"`
	PackageArn                pulumi.StringOutput        `pulumi:"packageArn"`
	PackageId                 pulumi.StringOutput        `pulumi:"packageId"`
	PackageName               pulumi.StringOutput        `pulumi:"packageName"`
	PackageVersion            pulumi.StringOutput        `pulumi:"packageVersion"`
	PatchVersion              pulumi.StringOutput        `pulumi:"patchVersion"`
	RegisteredTime            pulumi.IntOutput           `pulumi:"registeredTime"`
	Status                    PackageVersionStatusOutput `pulumi:"status"`
	StatusDescription         pulumi.StringOutput        `pulumi:"statusDescription"`
	UpdatedLatestPatchVersion pulumi.StringPtrOutput     `pulumi:"updatedLatestPatchVersion"`
}

// NewPackageVersion registers a new resource with the given unique name, arguments, and options.
func NewPackageVersion(ctx *pulumi.Context,
	name string, args *PackageVersionArgs, opts ...pulumi.ResourceOption) (*PackageVersion, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.PackageId == nil {
		return nil, errors.New("invalid value for required argument 'PackageId'")
	}
	if args.PackageVersion == nil {
		return nil, errors.New("invalid value for required argument 'PackageVersion'")
	}
	if args.PatchVersion == nil {
		return nil, errors.New("invalid value for required argument 'PatchVersion'")
	}
	var resource PackageVersion
	err := ctx.RegisterResource("aws-native:panorama:PackageVersion", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetPackageVersion gets an existing PackageVersion resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetPackageVersion(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *PackageVersionState, opts ...pulumi.ResourceOption) (*PackageVersion, error) {
	var resource PackageVersion
	err := ctx.ReadResource("aws-native:panorama:PackageVersion", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering PackageVersion resources.
type packageVersionState struct {
}

type PackageVersionState struct {
}

func (PackageVersionState) ElementType() reflect.Type {
	return reflect.TypeOf((*packageVersionState)(nil)).Elem()
}

type packageVersionArgs struct {
	MarkLatest                *bool   `pulumi:"markLatest"`
	OwnerAccount              *string `pulumi:"ownerAccount"`
	PackageId                 string  `pulumi:"packageId"`
	PackageVersion            string  `pulumi:"packageVersion"`
	PatchVersion              string  `pulumi:"patchVersion"`
	UpdatedLatestPatchVersion *string `pulumi:"updatedLatestPatchVersion"`
}

// The set of arguments for constructing a PackageVersion resource.
type PackageVersionArgs struct {
	MarkLatest                pulumi.BoolPtrInput
	OwnerAccount              pulumi.StringPtrInput
	PackageId                 pulumi.StringInput
	PackageVersion            pulumi.StringInput
	PatchVersion              pulumi.StringInput
	UpdatedLatestPatchVersion pulumi.StringPtrInput
}

func (PackageVersionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*packageVersionArgs)(nil)).Elem()
}

type PackageVersionInput interface {
	pulumi.Input

	ToPackageVersionOutput() PackageVersionOutput
	ToPackageVersionOutputWithContext(ctx context.Context) PackageVersionOutput
}

func (*PackageVersion) ElementType() reflect.Type {
	return reflect.TypeOf((*PackageVersion)(nil))
}

func (i *PackageVersion) ToPackageVersionOutput() PackageVersionOutput {
	return i.ToPackageVersionOutputWithContext(context.Background())
}

func (i *PackageVersion) ToPackageVersionOutputWithContext(ctx context.Context) PackageVersionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PackageVersionOutput)
}

type PackageVersionOutput struct{ *pulumi.OutputState }

func (PackageVersionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*PackageVersion)(nil))
}

func (o PackageVersionOutput) ToPackageVersionOutput() PackageVersionOutput {
	return o
}

func (o PackageVersionOutput) ToPackageVersionOutputWithContext(ctx context.Context) PackageVersionOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(PackageVersionOutput{})
}
