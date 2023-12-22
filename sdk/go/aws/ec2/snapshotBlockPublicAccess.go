// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::EC2::SnapshotBlockPublicAccess
type SnapshotBlockPublicAccess struct {
	pulumi.CustomResourceState

	// The identifier for the specified AWS account.
	AccountId pulumi.StringOutput `pulumi:"accountId"`
	// The state of EBS Snapshot Block Public Access.
	State SnapshotBlockPublicAccessStateEnumOutput `pulumi:"state"`
}

// NewSnapshotBlockPublicAccess registers a new resource with the given unique name, arguments, and options.
func NewSnapshotBlockPublicAccess(ctx *pulumi.Context,
	name string, args *SnapshotBlockPublicAccessArgs, opts ...pulumi.ResourceOption) (*SnapshotBlockPublicAccess, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.State == nil {
		return nil, errors.New("invalid value for required argument 'State'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource SnapshotBlockPublicAccess
	err := ctx.RegisterResource("aws-native:ec2:SnapshotBlockPublicAccess", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSnapshotBlockPublicAccess gets an existing SnapshotBlockPublicAccess resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSnapshotBlockPublicAccess(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SnapshotBlockPublicAccessState, opts ...pulumi.ResourceOption) (*SnapshotBlockPublicAccess, error) {
	var resource SnapshotBlockPublicAccess
	err := ctx.ReadResource("aws-native:ec2:SnapshotBlockPublicAccess", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SnapshotBlockPublicAccess resources.
type snapshotBlockPublicAccessState struct {
}

type SnapshotBlockPublicAccessState struct {
}

func (SnapshotBlockPublicAccessState) ElementType() reflect.Type {
	return reflect.TypeOf((*snapshotBlockPublicAccessState)(nil)).Elem()
}

type snapshotBlockPublicAccessArgs struct {
	// The state of EBS Snapshot Block Public Access.
	State SnapshotBlockPublicAccessStateEnum `pulumi:"state"`
}

// The set of arguments for constructing a SnapshotBlockPublicAccess resource.
type SnapshotBlockPublicAccessArgs struct {
	// The state of EBS Snapshot Block Public Access.
	State SnapshotBlockPublicAccessStateEnumInput
}

func (SnapshotBlockPublicAccessArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*snapshotBlockPublicAccessArgs)(nil)).Elem()
}

type SnapshotBlockPublicAccessInput interface {
	pulumi.Input

	ToSnapshotBlockPublicAccessOutput() SnapshotBlockPublicAccessOutput
	ToSnapshotBlockPublicAccessOutputWithContext(ctx context.Context) SnapshotBlockPublicAccessOutput
}

func (*SnapshotBlockPublicAccess) ElementType() reflect.Type {
	return reflect.TypeOf((**SnapshotBlockPublicAccess)(nil)).Elem()
}

func (i *SnapshotBlockPublicAccess) ToSnapshotBlockPublicAccessOutput() SnapshotBlockPublicAccessOutput {
	return i.ToSnapshotBlockPublicAccessOutputWithContext(context.Background())
}

func (i *SnapshotBlockPublicAccess) ToSnapshotBlockPublicAccessOutputWithContext(ctx context.Context) SnapshotBlockPublicAccessOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SnapshotBlockPublicAccessOutput)
}

func (i *SnapshotBlockPublicAccess) ToOutput(ctx context.Context) pulumix.Output[*SnapshotBlockPublicAccess] {
	return pulumix.Output[*SnapshotBlockPublicAccess]{
		OutputState: i.ToSnapshotBlockPublicAccessOutputWithContext(ctx).OutputState,
	}
}

type SnapshotBlockPublicAccessOutput struct{ *pulumi.OutputState }

func (SnapshotBlockPublicAccessOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**SnapshotBlockPublicAccess)(nil)).Elem()
}

func (o SnapshotBlockPublicAccessOutput) ToSnapshotBlockPublicAccessOutput() SnapshotBlockPublicAccessOutput {
	return o
}

func (o SnapshotBlockPublicAccessOutput) ToSnapshotBlockPublicAccessOutputWithContext(ctx context.Context) SnapshotBlockPublicAccessOutput {
	return o
}

func (o SnapshotBlockPublicAccessOutput) ToOutput(ctx context.Context) pulumix.Output[*SnapshotBlockPublicAccess] {
	return pulumix.Output[*SnapshotBlockPublicAccess]{
		OutputState: o.OutputState,
	}
}

// The identifier for the specified AWS account.
func (o SnapshotBlockPublicAccessOutput) AccountId() pulumi.StringOutput {
	return o.ApplyT(func(v *SnapshotBlockPublicAccess) pulumi.StringOutput { return v.AccountId }).(pulumi.StringOutput)
}

// The state of EBS Snapshot Block Public Access.
func (o SnapshotBlockPublicAccessOutput) State() SnapshotBlockPublicAccessStateEnumOutput {
	return o.ApplyT(func(v *SnapshotBlockPublicAccess) SnapshotBlockPublicAccessStateEnumOutput { return v.State }).(SnapshotBlockPublicAccessStateEnumOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*SnapshotBlockPublicAccessInput)(nil)).Elem(), &SnapshotBlockPublicAccess{})
	pulumi.RegisterOutputType(SnapshotBlockPublicAccessOutput{})
}
