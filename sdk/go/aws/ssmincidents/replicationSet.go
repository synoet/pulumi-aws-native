// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ssmincidents

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-replicationset.html
type ReplicationSet struct {
	pulumi.CustomResourceState

	Arn pulumi.StringOutput `pulumi:"arn"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-replicationset.html#cfn-ssmincidents-replicationset-deletionprotected
	DeletionProtected pulumi.BoolPtrOutput `pulumi:"deletionProtected"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-replicationset.html#cfn-ssmincidents-replicationset-regions
	Regions ReplicationSetReplicationRegionArrayOutput `pulumi:"regions"`
}

// NewReplicationSet registers a new resource with the given unique name, arguments, and options.
func NewReplicationSet(ctx *pulumi.Context,
	name string, args *ReplicationSetArgs, opts ...pulumi.ResourceOption) (*ReplicationSet, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Regions == nil {
		return nil, errors.New("invalid value for required argument 'Regions'")
	}
	var resource ReplicationSet
	err := ctx.RegisterResource("aws-native:ssmincidents:ReplicationSet", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetReplicationSet gets an existing ReplicationSet resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetReplicationSet(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ReplicationSetState, opts ...pulumi.ResourceOption) (*ReplicationSet, error) {
	var resource ReplicationSet
	err := ctx.ReadResource("aws-native:ssmincidents:ReplicationSet", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ReplicationSet resources.
type replicationSetState struct {
}

type ReplicationSetState struct {
}

func (ReplicationSetState) ElementType() reflect.Type {
	return reflect.TypeOf((*replicationSetState)(nil)).Elem()
}

type replicationSetArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-replicationset.html#cfn-ssmincidents-replicationset-deletionprotected
	DeletionProtected *bool `pulumi:"deletionProtected"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-replicationset.html#cfn-ssmincidents-replicationset-regions
	Regions []ReplicationSetReplicationRegion `pulumi:"regions"`
}

// The set of arguments for constructing a ReplicationSet resource.
type ReplicationSetArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-replicationset.html#cfn-ssmincidents-replicationset-deletionprotected
	DeletionProtected pulumi.BoolPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-replicationset.html#cfn-ssmincidents-replicationset-regions
	Regions ReplicationSetReplicationRegionArrayInput
}

func (ReplicationSetArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*replicationSetArgs)(nil)).Elem()
}

type ReplicationSetInput interface {
	pulumi.Input

	ToReplicationSetOutput() ReplicationSetOutput
	ToReplicationSetOutputWithContext(ctx context.Context) ReplicationSetOutput
}

func (*ReplicationSet) ElementType() reflect.Type {
	return reflect.TypeOf((*ReplicationSet)(nil))
}

func (i *ReplicationSet) ToReplicationSetOutput() ReplicationSetOutput {
	return i.ToReplicationSetOutputWithContext(context.Background())
}

func (i *ReplicationSet) ToReplicationSetOutputWithContext(ctx context.Context) ReplicationSetOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ReplicationSetOutput)
}

type ReplicationSetOutput struct{ *pulumi.OutputState }

func (ReplicationSetOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ReplicationSet)(nil))
}

func (o ReplicationSetOutput) ToReplicationSetOutput() ReplicationSetOutput {
	return o
}

func (o ReplicationSetOutput) ToReplicationSetOutputWithContext(ctx context.Context) ReplicationSetOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(ReplicationSetOutput{})
}
