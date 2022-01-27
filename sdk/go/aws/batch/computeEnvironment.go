// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package batch

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::Batch::ComputeEnvironment
//
// Deprecated: ComputeEnvironment is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type ComputeEnvironment struct {
	pulumi.CustomResourceState

	ComputeEnvironmentName pulumi.StringPtrOutput                      `pulumi:"computeEnvironmentName"`
	ComputeResources       ComputeEnvironmentComputeResourcesPtrOutput `pulumi:"computeResources"`
	ServiceRole            pulumi.StringPtrOutput                      `pulumi:"serviceRole"`
	State                  pulumi.StringPtrOutput                      `pulumi:"state"`
	Tags                   pulumi.AnyOutput                            `pulumi:"tags"`
	Type                   pulumi.StringOutput                         `pulumi:"type"`
	UnmanagedvCpus         pulumi.IntPtrOutput                         `pulumi:"unmanagedvCpus"`
}

// NewComputeEnvironment registers a new resource with the given unique name, arguments, and options.
func NewComputeEnvironment(ctx *pulumi.Context,
	name string, args *ComputeEnvironmentArgs, opts ...pulumi.ResourceOption) (*ComputeEnvironment, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Type == nil {
		return nil, errors.New("invalid value for required argument 'Type'")
	}
	var resource ComputeEnvironment
	err := ctx.RegisterResource("aws-native:batch:ComputeEnvironment", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetComputeEnvironment gets an existing ComputeEnvironment resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetComputeEnvironment(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ComputeEnvironmentState, opts ...pulumi.ResourceOption) (*ComputeEnvironment, error) {
	var resource ComputeEnvironment
	err := ctx.ReadResource("aws-native:batch:ComputeEnvironment", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ComputeEnvironment resources.
type computeEnvironmentState struct {
}

type ComputeEnvironmentState struct {
}

func (ComputeEnvironmentState) ElementType() reflect.Type {
	return reflect.TypeOf((*computeEnvironmentState)(nil)).Elem()
}

type computeEnvironmentArgs struct {
	ComputeEnvironmentName *string                             `pulumi:"computeEnvironmentName"`
	ComputeResources       *ComputeEnvironmentComputeResources `pulumi:"computeResources"`
	ServiceRole            *string                             `pulumi:"serviceRole"`
	State                  *string                             `pulumi:"state"`
	Tags                   interface{}                         `pulumi:"tags"`
	Type                   string                              `pulumi:"type"`
	UnmanagedvCpus         *int                                `pulumi:"unmanagedvCpus"`
}

// The set of arguments for constructing a ComputeEnvironment resource.
type ComputeEnvironmentArgs struct {
	ComputeEnvironmentName pulumi.StringPtrInput
	ComputeResources       ComputeEnvironmentComputeResourcesPtrInput
	ServiceRole            pulumi.StringPtrInput
	State                  pulumi.StringPtrInput
	Tags                   pulumi.Input
	Type                   pulumi.StringInput
	UnmanagedvCpus         pulumi.IntPtrInput
}

func (ComputeEnvironmentArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*computeEnvironmentArgs)(nil)).Elem()
}

type ComputeEnvironmentInput interface {
	pulumi.Input

	ToComputeEnvironmentOutput() ComputeEnvironmentOutput
	ToComputeEnvironmentOutputWithContext(ctx context.Context) ComputeEnvironmentOutput
}

func (*ComputeEnvironment) ElementType() reflect.Type {
	return reflect.TypeOf((**ComputeEnvironment)(nil)).Elem()
}

func (i *ComputeEnvironment) ToComputeEnvironmentOutput() ComputeEnvironmentOutput {
	return i.ToComputeEnvironmentOutputWithContext(context.Background())
}

func (i *ComputeEnvironment) ToComputeEnvironmentOutputWithContext(ctx context.Context) ComputeEnvironmentOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ComputeEnvironmentOutput)
}

type ComputeEnvironmentOutput struct{ *pulumi.OutputState }

func (ComputeEnvironmentOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ComputeEnvironment)(nil)).Elem()
}

func (o ComputeEnvironmentOutput) ToComputeEnvironmentOutput() ComputeEnvironmentOutput {
	return o
}

func (o ComputeEnvironmentOutput) ToComputeEnvironmentOutputWithContext(ctx context.Context) ComputeEnvironmentOutput {
	return o
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ComputeEnvironmentInput)(nil)).Elem(), &ComputeEnvironment{})
	pulumi.RegisterOutputType(ComputeEnvironmentOutput{})
}
