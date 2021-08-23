// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package s3

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-storagelens.html
type StorageLens struct {
	pulumi.CustomResourceState

	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-storagelens.html#cfn-s3-storagelens-storagelensconfiguration
	StorageLensConfiguration               StorageLensStorageLensConfigurationOutput `pulumi:"storageLensConfiguration"`
	StorageLensConfigurationStorageLensArn pulumi.StringOutput                       `pulumi:"storageLensConfigurationStorageLensArn"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-storagelens.html#cfn-s3-storagelens-tags
	Tags aws.TagArrayOutput `pulumi:"tags"`
}

// NewStorageLens registers a new resource with the given unique name, arguments, and options.
func NewStorageLens(ctx *pulumi.Context,
	name string, args *StorageLensArgs, opts ...pulumi.ResourceOption) (*StorageLens, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.StorageLensConfiguration == nil {
		return nil, errors.New("invalid value for required argument 'StorageLensConfiguration'")
	}
	var resource StorageLens
	err := ctx.RegisterResource("aws-native:s3:StorageLens", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetStorageLens gets an existing StorageLens resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetStorageLens(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *StorageLensState, opts ...pulumi.ResourceOption) (*StorageLens, error) {
	var resource StorageLens
	err := ctx.ReadResource("aws-native:s3:StorageLens", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering StorageLens resources.
type storageLensState struct {
}

type StorageLensState struct {
}

func (StorageLensState) ElementType() reflect.Type {
	return reflect.TypeOf((*storageLensState)(nil)).Elem()
}

type storageLensArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-storagelens.html#cfn-s3-storagelens-storagelensconfiguration
	StorageLensConfiguration StorageLensStorageLensConfiguration `pulumi:"storageLensConfiguration"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-storagelens.html#cfn-s3-storagelens-tags
	Tags []aws.Tag `pulumi:"tags"`
}

// The set of arguments for constructing a StorageLens resource.
type StorageLensArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-storagelens.html#cfn-s3-storagelens-storagelensconfiguration
	StorageLensConfiguration StorageLensStorageLensConfigurationInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-storagelens.html#cfn-s3-storagelens-tags
	Tags aws.TagArrayInput
}

func (StorageLensArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*storageLensArgs)(nil)).Elem()
}

type StorageLensInput interface {
	pulumi.Input

	ToStorageLensOutput() StorageLensOutput
	ToStorageLensOutputWithContext(ctx context.Context) StorageLensOutput
}

func (*StorageLens) ElementType() reflect.Type {
	return reflect.TypeOf((*StorageLens)(nil))
}

func (i *StorageLens) ToStorageLensOutput() StorageLensOutput {
	return i.ToStorageLensOutputWithContext(context.Background())
}

func (i *StorageLens) ToStorageLensOutputWithContext(ctx context.Context) StorageLensOutput {
	return pulumi.ToOutputWithContext(ctx, i).(StorageLensOutput)
}

type StorageLensOutput struct{ *pulumi.OutputState }

func (StorageLensOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*StorageLens)(nil))
}

func (o StorageLensOutput) ToStorageLensOutput() StorageLensOutput {
	return o
}

func (o StorageLensOutput) ToStorageLensOutputWithContext(ctx context.Context) StorageLensOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(StorageLensOutput{})
}
